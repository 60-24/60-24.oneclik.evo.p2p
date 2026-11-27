"""Regression test (Issue #24): a signed message cannot be replayed into another session.

A frame ``MSG <seq> <signature_b64> <text>`` is signed over the session id, which is
``SHA-256(context || client_id || server_id || client_challenge || server_challenge)``.
Both sides contribute a fresh challenge, so a frame captured in one session must not verify
in a session that differs in either challenge, even though sender, recipient, sequence
number and text are identical.

Everything here is deterministic: fixed identity seeds, fixed challenges, and Ed25519
(deterministic signatures). Nothing depends on randomness or timing.

Scope: session binding only. Sequence/window semantics are not exercised or changed.
"""

from __future__ import annotations

import hashlib
import socket
import threading

import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    NoEncryption,
    PrivateFormat,
    PublicFormat,
)

from src.p2p import P2PNode, node as node_module, protocol
from src.p2p.node import RESPONSE, _receive_line
from src.p2p.protocol import (
    MessageReceiver,
    auth,
    auth_payload,
    hello,
    message_payload,
    msg,
    node_id_from_public_key,
    parse_msg,
    parse_welcome,
    session_id,
    verify_signature,
)

IO_TIMEOUT = 5
TEXT = "replayed-from-session-1"

# Fixed identities and challenges (32 bytes each).
CLIENT_SEED = bytes(range(0, 32))
SERVER_SEED = bytes(range(32, 64))
CLIENT_CHALLENGE_1 = bytes([0x11]) * 32
CLIENT_CHALLENGE_2 = bytes([0x12]) * 32
SERVER_CHALLENGE_1 = bytes([0x21]) * 32
SERVER_CHALLENGE_2 = bytes([0x22]) * 32

# Which handshake challenges differ in the second session.
# Each case changes the session identifier; sender, recipient, seq and text stay identical.
SECOND_SESSION_CASES = [
    pytest.param(CLIENT_CHALLENGE_1, SERVER_CHALLENGE_2, id="only_server_challenge_differs"),
    pytest.param(CLIENT_CHALLENGE_2, SERVER_CHALLENGE_1, id="only_client_challenge_differs"),
    pytest.param(CLIENT_CHALLENGE_2, SERVER_CHALLENGE_2, id="both_challenges_differ"),
]


def _public_key(private_key: Ed25519PrivateKey) -> bytes:
    return private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)


CLIENT_KEY = Ed25519PrivateKey.from_private_bytes(CLIENT_SEED)
SERVER_KEY = Ed25519PrivateKey.from_private_bytes(SERVER_SEED)
CLIENT_PUBLIC_KEY = _public_key(CLIENT_KEY)
SERVER_PUBLIC_KEY = _public_key(SERVER_KEY)
CLIENT_ID = node_id_from_public_key(CLIENT_PUBLIC_KEY)
SERVER_ID = node_id_from_public_key(SERVER_PUBLIC_KEY)


def _session(client_challenge: bytes, server_challenge: bytes) -> bytes:
    return session_id(CLIENT_ID, SERVER_ID, client_challenge, server_challenge)


def _signed_frame(session: bytes, *, seq: int = 1, text: str = TEXT) -> str:
    """A correctly signed frame from the client to the server, bound to ``session``."""
    signature = CLIENT_KEY.sign(message_payload(session, CLIENT_ID, SERVER_ID, seq, text))
    return msg(seq, signature, text)


def _server_receiver(session: bytes) -> MessageReceiver:
    """The server side of one session; a fresh receiver always expects sequence 1."""
    return MessageReceiver(session, CLIENT_ID, CLIENT_PUBLIC_KEY, SERVER_ID)


# --- unit level: the session identifier and the receiver ----------------------------------


def test_session_id_matches_independent_known_answer_and_differs_per_challenge():
    expected = hashlib.sha256(
        b"P2P60-24-SESSION-V1"
        + bytes.fromhex(CLIENT_ID)
        + bytes.fromhex(SERVER_ID)
        + CLIENT_CHALLENGE_1
        + SERVER_CHALLENGE_1
    ).digest()
    original = _session(CLIENT_CHALLENGE_1, SERVER_CHALLENGE_1)
    assert original == expected

    others = [
        _session(CLIENT_CHALLENGE_1, SERVER_CHALLENGE_2),
        _session(CLIENT_CHALLENGE_2, SERVER_CHALLENGE_1),
        _session(CLIENT_CHALLENGE_2, SERVER_CHALLENGE_2),
    ]
    assert len({original, *others}) == 4, "every challenge change must change the session id"


def test_frame_is_accepted_in_the_session_it_was_signed_for():
    """Positive control: the frame used by the replay tests is valid in its own session."""
    frame = _signed_frame(_session(CLIENT_CHALLENGE_1, SERVER_CHALLENGE_1))
    assert _server_receiver(_session(CLIENT_CHALLENGE_1, SERVER_CHALLENGE_1)).accept(frame) == TEXT


@pytest.mark.parametrize(("client_challenge", "server_challenge"), SECOND_SESSION_CASES)
def test_frame_replayed_into_a_different_session_is_rejected_by_signature(
    client_challenge, server_challenge
):
    original_session = _session(CLIENT_CHALLENGE_1, SERVER_CHALLENGE_1)
    second_session = _session(client_challenge, server_challenge)
    assert second_session != original_session

    captured = _signed_frame(original_session)

    # The captured frame is well-formed and carries sequence 1, which is exactly what a fresh
    # receiver expects. Only the session binding can make it fail.
    seq, _signature, text = parse_msg(captured)
    assert (seq, text) == (1, TEXT)

    receiver = _server_receiver(second_session)
    with pytest.raises(ValueError) as rejected:
        receiver.accept(captured)

    # Failure mode: the signature does not verify. Not a framing error, not a sequence error.
    assert str(rejected.value) == protocol.BAD_SIGNATURE
    assert str(rejected.value) not in (protocol.INVALID_FRAME, protocol.BAD_SEQUENCE)

    # Control: the rejected replay consumed nothing. The same receiver still accepts a frame
    # signed for its own session with the same sender, recipient, sequence and text.
    assert receiver.accept(_signed_frame(second_session)) == TEXT


# --- listener level: real sockets, fixed challenges ---------------------------------------


class _FixedSecrets:
    """Stand-in for the ``secrets`` module used by the listener; hands out fixed challenges."""

    def __init__(self, *challenges: bytes) -> None:
        self._queue = list(challenges)

    def token_bytes(self, size: int) -> bytes:
        assert size == 32, "the listener is expected to draw 32-byte challenges only"
        assert self._queue, "listener drew more challenges than the test provided"
        return self._queue.pop(0)


def _open_authenticated_client(server: P2PNode, client_challenge: bytes, expected_server_challenge: bytes):
    """Hand-driven client: HELLO with a fixed challenge, verify WELCOME, answer AUTH."""
    conn = socket.create_connection((server.bound_host, server.bound_port), timeout=IO_TIMEOUT)
    buffer = bytearray()
    conn.sendall(
        (hello(CLIENT_ID, CLIENT_PUBLIC_KEY, client_challenge, "A") + "\n").encode("utf-8")
    )
    server_id, server_public_key, server_challenge, server_signature = parse_welcome(
        _receive_line(conn, buffer)
    )
    assert server_id == SERVER_ID
    # Guards determinism: the injected server challenge really is the one on the wire.
    assert server_challenge == expected_server_challenge
    verify_signature(
        server_public_key, server_signature, auth_payload(CLIENT_ID, server_id, client_challenge)
    )
    signature = CLIENT_KEY.sign(auth_payload(CLIENT_ID, server_id, server_challenge))
    conn.sendall((auth(signature) + "\n").encode("utf-8"))
    return conn, buffer


def _listen_in_thread(server: P2PNode):
    result: dict = {}

    def run() -> None:
        try:
            result["response"] = server.listen_once()
        except Exception as exc:  # captured for assertions
            result["error"] = exc

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    return thread, result


def _deliver_frame(server, client_challenge, server_challenge, frame_for):
    """Run one authenticated session and send ``frame_for(session_id)`` as the application line."""
    thread, result = _listen_in_thread(server)
    conn, buffer = _open_authenticated_client(server, client_challenge, server_challenge)
    try:
        conn.sendall((frame_for(_session(client_challenge, server_challenge)) + "\n").encode("utf-8"))
        try:
            reply = _receive_line(conn, buffer)
        except (ValueError, OSError):
            reply = None
    finally:
        conn.close()
    thread.join(timeout=IO_TIMEOUT + 3)
    assert not thread.is_alive(), "listener did not terminate"
    return result, reply


@pytest.fixture
def server(tmp_path, monkeypatch):
    """One listener with a fixed identity, reused across both sessions of a test."""
    identity = tmp_path / "server-identity.key"
    identity.write_bytes(SERVER_KEY.private_bytes(Encoding.Raw, PrivateFormat.Raw, NoEncryption()))
    node = P2PNode("B", identity_path=identity)
    assert node.node_id == SERVER_ID
    node._server.settimeout(IO_TIMEOUT)
    try:
        yield node, monkeypatch
    finally:
        node.close()


@pytest.mark.parametrize(("client_challenge", "server_challenge"), SECOND_SESSION_CASES)
def test_listener_rejects_frame_captured_in_another_session(
    server, client_challenge, server_challenge
):
    node, monkeypatch = server
    monkeypatch.setattr(
        node_module, "secrets", _FixedSecrets(SERVER_CHALLENGE_1, server_challenge)
    )

    # Session 1: the frame is delivered and recorded.
    captured: dict = {}

    def first(session: bytes) -> str:
        captured["frame"] = _signed_frame(session)
        return captured["frame"]

    first_result, first_reply = _deliver_frame(
        node, CLIENT_CHALLENGE_1, SERVER_CHALLENGE_1, first
    )
    assert first_result == {"response": RESPONSE}, first_result
    assert first_reply == RESPONSE
    assert node.last_message == TEXT
    assert node.last_peer_id == CLIENT_ID

    # Session 2: same server, same client identity, different challenge(s); replay the capture.
    node.last_message = None
    second_result, second_reply = _deliver_frame(
        node, client_challenge, server_challenge, lambda _session: captured["frame"]
    )

    assert "response" not in second_result, second_result
    error = second_result.get("error")
    assert isinstance(error, ValueError), second_result
    assert str(error) == protocol.BAD_SIGNATURE  # failure mode: signature verification
    assert node.last_message is None  # nothing delivered
    assert second_reply is None  # no response sent for the replayed frame
