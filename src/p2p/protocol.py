"""Authenticated line protocol for the concrete two-node P2P boundary."""

from __future__ import annotations

import base64
import hashlib
import re

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

HELLO = "HELLO"
WELCOME = "WELCOME"
AUTH = "AUTH"
MSG = "MSG"
# V2 (SES-090): V1 and V2 peers fail the proof-of-possession check during the
# handshake, so a V2 client never sends an unprotected message to a V1 server.
PROTOCOL_CONTEXT = b"P2P60-24-IDENTITY-V2"
SESSION_CONTEXT = b"P2P60-24-SESSION-V1"
MESSAGE_CONTEXT = b"P2P60-24-MSG-V1"
NODE_ID_PATTERN = re.compile(r"^[0-9a-f]{64}$")
_SEQUENCE_PATTERN = re.compile(r"[1-9][0-9]{0,18}")
_MAX_SEQUENCE = 2**63 - 1
_CHALLENGE_SIZE = 32
_SIGNATURE_SIZE = 64

INVALID_FRAME = "invalid message frame"
BAD_SIGNATURE = "message signature verification failed"
BAD_SEQUENCE = "unexpected message sequence"


def _b64(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def _unb64(value: str) -> bytes:
    try:
        return base64.b64decode(value.encode("ascii"), validate=True)
    except Exception as exc:
        raise ValueError("invalid base64 field") from exc


def node_id_from_public_key(public_key: bytes) -> str:
    if len(public_key) != 32:
        raise ValueError("invalid Ed25519 public key")
    return hashlib.sha256(public_key).hexdigest()


def _validate_node_id(node_id: str) -> str:
    if not NODE_ID_PATTERN.fullmatch(node_id):
        raise ValueError("invalid node identity")
    return node_id


def auth_payload(client_id: str, server_id: str, challenge: bytes) -> bytes:
    _validate_node_id(client_id)
    _validate_node_id(server_id)
    return PROTOCOL_CONTEXT + bytes.fromhex(client_id) + bytes.fromhex(server_id) + challenge


def hello(node_id: str, public_key: bytes, challenge: bytes, label: str) -> str:
    node_id = _validate_node_id(node_id)
    if len(public_key) != 32 or len(challenge) != 32:
        raise ValueError("invalid HELLO fields")
    if not label or " " in label or "\n" in label or "\r" in label:
        raise ValueError("invalid node label")
    return f"{HELLO} {node_id} {_b64(public_key)} {_b64(challenge)} {label}"


def parse_hello(message: str) -> tuple[str, bytes, bytes, str]:
    parts = message.split(" ")
    if len(parts) != 5 or parts[0] != HELLO:
        raise ValueError("invalid handshake")
    node_id = _validate_node_id(parts[1])
    public_key = _unb64(parts[2])
    challenge = _unb64(parts[3])
    label = parts[4]
    if not label or " " in label or "\n" in label or "\r" in label:
        raise ValueError("invalid node label")
    if len(public_key) != 32 or len(challenge) != 32:
        raise ValueError("invalid HELLO fields")
    if node_id_from_public_key(public_key) != node_id:
        raise ValueError("node identity does not match public key")
    return node_id, public_key, challenge, label


def welcome(
    node_id: str,
    public_key: bytes,
    challenge: bytes,
    signature: bytes,
) -> str:
    node_id = _validate_node_id(node_id)
    if len(public_key) != 32 or len(challenge) != 32 or len(signature) != 64:
        raise ValueError("invalid WELCOME fields")
    return f"{WELCOME} {node_id} {_b64(public_key)} {_b64(challenge)} {_b64(signature)}"


def parse_welcome(message: str) -> tuple[str, bytes, bytes, bytes]:
    parts = message.split(" ")
    if len(parts) != 5 or parts[0] != WELCOME:
        raise ValueError("handshake failed")
    node_id = _validate_node_id(parts[1])
    public_key = _unb64(parts[2])
    challenge = _unb64(parts[3])
    signature = _unb64(parts[4])
    if len(public_key) != 32 or len(challenge) != 32 or len(signature) != 64:
        raise ValueError("invalid WELCOME fields")
    if node_id_from_public_key(public_key) != node_id:
        raise ValueError("node identity does not match public key")
    return node_id, public_key, challenge, signature


def auth(signature: bytes) -> str:
    if len(signature) != 64:
        raise ValueError("invalid AUTH signature")
    return f"{AUTH} {_b64(signature)}"


def parse_auth(message: str) -> bytes:
    parts = message.split(" ")
    if len(parts) != 2 or parts[0] != AUTH:
        raise ValueError("invalid AUTH")
    signature = _unb64(parts[1])
    if len(signature) != 64:
        raise ValueError("invalid AUTH signature")
    return signature


def verify_signature(public_key: bytes, signature: bytes, payload: bytes) -> None:
    try:
        Ed25519PublicKey.from_public_bytes(public_key).verify(signature, payload)
    except (ValueError, InvalidSignature) as exc:
        raise ValueError("proof of possession failed") from exc


def session_id(
    client_id: str, server_id: str, client_challenge: bytes, server_challenge: bytes
) -> bytes:
    """Identify one authenticated session from both identities and both fresh challenges."""
    _validate_node_id(client_id)
    _validate_node_id(server_id)
    if len(client_challenge) != _CHALLENGE_SIZE or len(server_challenge) != _CHALLENGE_SIZE:
        raise ValueError("invalid session challenge")
    return hashlib.sha256(
        SESSION_CONTEXT
        + bytes.fromhex(client_id)
        + bytes.fromhex(server_id)
        + client_challenge
        + server_challenge
    ).digest()


def message_payload(
    session: bytes, sender_id: str, recipient_id: str, seq: int, text: str
) -> bytes:
    """Bytes signed for one message: fixed-width fields, then the length-prefixed text."""
    if len(session) != 32:
        raise ValueError("invalid session id")
    _validate_node_id(sender_id)
    _validate_node_id(recipient_id)
    if not 1 <= seq <= _MAX_SEQUENCE:
        raise ValueError("invalid message sequence")
    data = text.encode("utf-8")
    return (
        MESSAGE_CONTEXT
        + session
        + bytes.fromhex(sender_id)
        + bytes.fromhex(recipient_id)
        + seq.to_bytes(8, "big")
        + len(data).to_bytes(4, "big")
        + data
    )


def msg(seq: int, signature: bytes, text: str) -> str:
    if not 1 <= seq <= _MAX_SEQUENCE:
        raise ValueError("invalid message sequence")
    if len(signature) != _SIGNATURE_SIZE:
        raise ValueError("invalid message signature")
    return f"{MSG} {seq} {_b64(signature)} {text}"


def parse_msg(message: str) -> tuple[int, bytes, str]:
    """Strictly parse ``MSG <seq> <signature_b64> <text>``; the text is everything after."""
    parts = message.split(" ", 3)
    if len(parts) != 4 or parts[0] != MSG:
        raise ValueError(INVALID_FRAME)
    if not _SEQUENCE_PATTERN.fullmatch(parts[1]):
        raise ValueError(INVALID_FRAME)
    seq = int(parts[1])
    if seq > _MAX_SEQUENCE:
        raise ValueError(INVALID_FRAME)
    try:
        signature = base64.b64decode(parts[2].encode("ascii"), validate=True)
    except Exception as exc:
        raise ValueError(INVALID_FRAME) from exc
    # Canonical encoding only: reject non-zero padding bits and any other variant.
    if len(signature) != _SIGNATURE_SIZE or _b64(signature) != parts[2]:
        raise ValueError(INVALID_FRAME)
    return seq, signature, parts[3]


class MessageReceiver:
    """Verifies the signed application frames of exactly one authenticated session."""

    __slots__ = ("_session", "_sender_id", "_sender_public_key", "_recipient_id", "_expected_seq")

    def __init__(
        self, session: bytes, sender_id: str, sender_public_key: bytes, recipient_id: str
    ) -> None:
        if node_id_from_public_key(sender_public_key) != _validate_node_id(sender_id):
            raise ValueError("node identity does not match public key")
        _validate_node_id(recipient_id)
        if len(session) != 32:
            raise ValueError("invalid session id")
        self._session = session
        self._sender_id = sender_id
        self._sender_public_key = sender_public_key
        self._recipient_id = recipient_id
        self._expected_seq = 1

    def accept(self, line: str) -> str:
        """Return the text of a valid next message; raise ValueError otherwise."""
        seq, signature, text = parse_msg(line)
        payload = message_payload(
            self._session, self._sender_id, self._recipient_id, seq, text
        )
        try:
            Ed25519PublicKey.from_public_bytes(self._sender_public_key).verify(
                signature, payload
            )
        except (ValueError, InvalidSignature) as exc:
            raise ValueError(BAD_SIGNATURE) from exc
        if seq != self._expected_seq:
            raise ValueError(BAD_SEQUENCE)
        self._expected_seq += 1
        return text
