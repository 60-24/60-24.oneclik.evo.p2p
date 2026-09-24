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
PROTOCOL_CONTEXT = b"P2P60-24-IDENTITY-V1"
NODE_ID_PATTERN = re.compile(r"^[0-9a-f]{64}$")


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


def hello(node_id: str, public_key: bytes, challenge: bytes) -> str:
    node_id = _validate_node_id(node_id)
    if len(public_key) != 32 or len(challenge) != 32:
        raise ValueError("invalid HELLO fields")
    return f"{HELLO} {node_id} {_b64(public_key)} {_b64(challenge)}"


def parse_hello(message: str) -> tuple[str, bytes, bytes]:
    parts = message.split(" ")
    if len(parts) != 4 or parts[0] != HELLO:
        raise ValueError("invalid handshake")
    node_id = _validate_node_id(parts[1])
    public_key = _unb64(parts[2])
    challenge = _unb64(parts[3])
    if len(public_key) != 32 or len(challenge) != 32:
        raise ValueError("invalid HELLO fields")
    if node_id_from_public_key(public_key) != node_id:
        raise ValueError("node identity does not match public key")
    return node_id, public_key, challenge


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
