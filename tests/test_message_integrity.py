"""SES-090: authenticated message integrity after the HELLO/WELCOME/AUTH handshake.

Specification under test (approved design, SES-090):

* The handshake context is ``P2P60-24-IDENTITY-V2``; V1 and V2 peers reject each
  other during the handshake, before any application message is sent.
* The application line after AUTH (and the optional VOUCH) is a signed frame::

      MSG <seq> <signature_b64> <text>

* The signed bytes are built field by field, with fixed widths and a byte length::

      "P2P60-24-MSG-V1" || session_id(32) || sender_id(32) || recipient_id(32)
                        || seq(8, big-endian) || len(text_utf8)(4, big-endian)
                        || text_utf8

* ``session_id = SHA-256("P2P60-24-SESSION-V1" || client_id || server_id
  || client_challenge || server_challenge)``.
* One message per connection: ``seq`` is 1. The response is NOT authenticated
  (separate task, outside SES-090).

The payload and session builders below are written independently of ``src`` on
purpose: they act as the known-answer reference for the implementation.
"""

from __future__ import annotations

import base64
import hashlib
import secrets
import socket
import string
import threading

import pytest
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)

from src.p2p import P2PNode, protocol
from src.p2p.node import _receive_line
from src.p2p.protocol import auth, auth_payload, hello, parse_hello, parse_welcome
from src.p2p.protocol import verify_signature, welcome

IO_TIMEOUT = 5

MSG_CONTEXT = b"P2P60-24-MSG-V1"
SESSION_CONTEXT = b"P2P60-24-SESSION-V1"
LEGACY_IDENTITY_CONTEXT = b"P2P60-24-IDENTITY-V1"

BAD_SIGNATURE = "message signature verification failed"
BAD_FRAME = "invalid message frame"
BAD_SEQUENCE = "unexpected message sequence"
EXTRA_DATA = "unexpected data after message"


# --- independent reference builders (do not import these from src) -----------------


def _session_id(client_id, server_id, client_challenge, server_challenge):
    return hashlib.sha256(
        SESSION_CONTEXT
        + bytes.fromhex(client_id)
        + bytes.fromhex(server_id)
        + client_challenge
        + server_challenge
    ).digest()


def _payload(sid, sender_id, recipient_id, seq, text):
    data = text.encode("utf-8")
    return (
        MSG_CONTEXT
        + sid
        + bytes.fromhex(sender_id)
        + bytes.fromhex(recipient_id)
        + seq.to_bytes(8, "big")
        + len(data).to_bytes(4, "big")
        + data
    )


def _legacy_auth_payload(client_id, server_id, challenge):
    return LEGACY_IDENTITY_CONTEXT + bytes.fromhex(client_id) + bytes.fromhex(server_id) + challenge


def _b64(data):
    return base64.b64encode(data).decode("ascii")


# --- harness ----------------------------------------------------------------------


@pytest.fixture
def pair():
    server = P2PNode("B")
    client = P2PNode("A")
    server._server.settimeout(IO_TIMEOUT)
    try:
        yield server, client
    finally:
        server.close()
        client.close()


def _start_listener(server):
    result = {}

    def run():
        try:
            result["response"] = server.listen_once()
        except Exception as exc:  # captured for assertions
            result["error"] = exc

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    return thread, result


def _join(thread):
    thread.join(timeout=IO_TIMEOUT + 3)
    assert not thread.is_alive(), "listener did not terminate"


class _Session:
    """Client side of an authenticated session driven by hand."""

    def __init__(self, conn, buffer, client, server_id, client_challenge, server_challenge):
        self.conn = conn
        self.buffer = buffer
        self.client = client
        self.client_id = client.node_id
        self.server_id = server_id
        self.client_challenge = client_challenge
        self.server_challenge = server_challenge
        self.sid = _session_id(self.client_id, server_id, client_challenge, server_challenge)


def _open_session(client, server):
    conn = socket.create_connection((server.bound_host, server.bound_port), timeout=IO_TIMEOUT)
    buffer = bytearray()
    client_challenge = secrets.token_bytes(32)
    conn.sendall(
        (hello(client.node_id, client.public_key, client_challenge, client.label) + "\n").encode()
    )
    server_id, server_pk, server_challenge, server_sig = parse_welcome(_receive_line(conn, buffer))
    verify_signature(
        server_pk, server_sig, auth_payload(client.node_id, server_id, client_challenge)
    )
    signature = client._identity_key.sign(auth_payload(client.node_id, server_id, server_challenge))
    conn.sendall((auth(signature) + "\n").encode())
    return _Session(conn, buffer, client, server_id, client_challenge, server_challenge)


def _sign(
    session,
    text="hello-from-A",
    *,
    seq=1,
    sender=None,
    recipient=None,
    sid=None,
    signer=None,
):
    payload = _payload(
        sid if sid is not None else session.sid,
        sender or session.client_id,
        recipient or session.server_id,
        seq,
        text,
    )
    return (signer or session.client._identity_key).sign(payload)


def _good(session, text="hello-from-A", *, seq=1, **kwargs):
    return f"MSG {seq} {_b64(_sign(session, text, seq=seq, **kwargs))} {text}"


def _deliver(server, client, build, tail_build=None):
    """Open a session, send ``build(session)`` as the application line, collect the outcome."""
    thread, result = _start_listener(server)
    session = _open_session(client, server)
    try:
        data = build(session) + "\n"
        if tail_build is not None:
            data += tail_build(session) + "\n"
        session.conn.sendall(data.encode("utf-8"))
        try:
            reply = _receive_line(session.conn, session.buffer)
        except (ValueError, OSError):
            reply = None
    finally:
        session.conn.close()
    _join(thread)
    return result, reply


def _run_relay(server, mutate):
    """Active relay: forwards the handshake untouched and mutates the application line."""
    relay = socket.socket()
    relay.bind(("127.0.0.1", 0))
    relay.listen(1)
    relay.settimeout(IO_TIMEOUT)
    record = {}

    def run():
        client_conn = server_conn = None
        try:
            client_conn, _ = relay.accept()
            client_conn.settimeout(IO_TIMEOUT)
            server_conn = socket.create_connection(
                (server.bound_host, server.bound_port), timeout=IO_TIMEOUT
            )
            cf = client_conn.makefile("rwb")
            sf = server_conn.makefile("rwb")
            record["hello"] = cf.readline()
            sf.write(record["hello"])
            sf.flush()
            record["welcome"] = sf.readline()
            cf.write(record["welcome"])
            cf.flush()
            sf.write(cf.readline())  # AUTH
            sf.flush()
            record["original"] = cf.readline()
            sf.write(mutate(record["original"]))
            sf.flush()
            cf.write(sf.readline())  # response, if the server sends one
            cf.flush()
        except Exception as exc:  # noqa: BLE001 - recorded for debugging
            record["relay_error"] = repr(exc)
        finally:
            for item in (client_conn, server_conn, relay):
                if item is not None:
                    try:
                        item.close()
                    except OSError:
                        pass

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    return relay.getsockname()[1], thread, record


# --- 5. a correct message passes ----------------------------------------------------


def test_valid_message_passes_through_node_api(pair):
    server, client = pair
    thread, result = _start_listener(server)
    assert client.send(server.bound_host, server.bound_port, "hello-from-A") == "pong-from-B"
    _join(thread)
    assert "error" not in result
    assert server.last_message == "hello-from-A"
    assert server.last_peer_id == client.node_id


def test_valid_hand_crafted_frame_passes_and_text_may_contain_spaces_and_utf8(pair):
    server, client = pair
    text = "hand crafted zażółć gęślą jaźń"
    result, reply = _deliver(server, client, lambda s: _good(s, text))
    assert result == {"response": "pong-from-B"}
    assert reply == "pong-from-B"
    assert server.last_message == text
    assert server.last_peer_id == client.node_id


def test_empty_message_keeps_working(pair):
    server, client = pair
    thread, result = _start_listener(server)
    assert client.send(server.bound_host, server.bound_port, "") == "pong-from-B"
    _join(thread)
    assert "error" not in result
    assert server.last_message == ""


# --- 1. a modified message is rejected ----------------------------------------------


def test_message_modified_by_relay_is_rejected(pair):
    server, client = pair
    thread, result = _start_listener(server)
    port, relay_thread, record = _run_relay(
        server, lambda line: line.replace(b"hello-from-A", b"hello-from-X")
    )
    try:
        response = client.send("127.0.0.1", port, "hello-from-A")
    except (ValueError, OSError):
        response = None
    _join(thread)
    relay_thread.join(timeout=IO_TIMEOUT)
    assert b"hello-from-A" in record["original"]
    assert response is None, "client must not receive an acknowledgement for a tampered message"
    assert isinstance(result.get("error"), ValueError)
    assert str(result["error"]) == BAD_SIGNATURE
    assert server.last_message is None


# --- 2/3/6 and parser strictness: invalid frames are rejected -----------------------


def _flip_signature_bit(session):
    sig = bytearray(_sign(session))
    sig[0] ^= 0x01
    return f"MSG 1 {_b64(bytes(sig))} hello-from-A"


def _non_canonical_b64(session):
    sig = _sign(session)
    canonical = _b64(sig)
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
    assert canonical.endswith("==")
    variant = canonical[:-3] + alphabet[alphabet.index(canonical[-3]) | 1] + "=="
    # Python's lenient decoder accepts this variant: that is why the parser must compare.
    assert variant != canonical
    assert base64.b64decode(variant, validate=True) == sig
    return f"MSG 1 {variant} hello-from-A"


def _with_seq(seq_text):
    return lambda session: f"MSG {seq_text} {_b64(_sign(session))} hello-from-A"


def _with_sig(sig_bytes):
    return lambda session: f"MSG 1 {_b64(sig_bytes)} hello-from-A"


REJECTED_FRAMES = [
    # cryptographic rejections
    ("bit_flipped_signature", _flip_signature_bit, BAD_SIGNATURE),
    (
        "text_changed_after_signing",
        lambda s: f"MSG 1 {_b64(_sign(s))} hello-from-X",
        BAD_SIGNATURE,
    ),
    (
        "signed_by_other_identity",
        lambda s: _good(s, signer=Ed25519PrivateKey.generate()),
        BAD_SIGNATURE,
    ),
    (
        "addressed_to_other_recipient",
        lambda s: _good(s, recipient=hashlib.sha256(b"someone-else").hexdigest()),
        BAD_SIGNATURE,
    ),
    (
        "sender_and_recipient_swapped",
        lambda s: _good(s, sender=s.server_id, recipient=s.client_id),
        BAD_SIGNATURE,
    ),
    (
        "other_session_context",
        lambda s: _good(
            s,
            sid=_session_id(
                s.client_id, s.server_id, s.client_challenge, secrets.token_bytes(32)
            ),
        ),
        BAD_SIGNATURE,
    ),
    # a correctly signed message that is not the first of the session
    ("validly_signed_but_sequence_two", lambda s: _good(s, seq=2), BAD_SEQUENCE),
    # structure and canonical encoding
    ("legacy_plain_line", lambda s: "hello-from-A", BAD_FRAME),
    ("empty_frame", lambda s: "", BAD_FRAME),
    ("lowercase_keyword", lambda s: f"msg 1 {_b64(_sign(s))} hello-from-A", BAD_FRAME),
    ("double_space_after_keyword", lambda s: f"MSG  1 {_b64(_sign(s))} hello-from-A", BAD_FRAME),
    ("missing_text_separator", lambda s: f"MSG 1 {_b64(_sign(s))}", BAD_FRAME),
    ("sequence_zero", _with_seq("0"), BAD_FRAME),
    ("sequence_leading_zero", _with_seq("01"), BAD_FRAME),
    ("sequence_plus_sign", _with_seq("+1"), BAD_FRAME),
    ("sequence_unicode_digit", _with_seq("١"), BAD_FRAME),
    ("sequence_beyond_63_bits", _with_seq(str(2**63)), BAD_FRAME),
    ("sequence_empty", _with_seq(""), BAD_FRAME),
    ("signature_63_bytes", _with_sig(b"\x01" * 63), BAD_FRAME),
    ("signature_65_bytes", _with_sig(b"\x01" * 65), BAD_FRAME),
    ("signature_not_base64", lambda s: "MSG 1 !!!not-base64!!! hello-from-A", BAD_FRAME),
    ("signature_non_canonical_base64", _non_canonical_b64, BAD_FRAME),
]


@pytest.mark.parametrize(
    "build,error",
    [(case[1], case[2]) for case in REJECTED_FRAMES],
    ids=[case[0] for case in REJECTED_FRAMES],
)
def test_invalid_frame_is_rejected_and_not_delivered(pair, build, error):
    server, client = pair
    result, reply = _deliver(server, client, build)
    assert isinstance(result.get("error"), ValueError), result
    assert str(result["error"]) == error
    assert server.last_message is None
    assert reply is None


# --- 4. replay -----------------------------------------------------------------------


def test_frame_captured_in_one_session_is_rejected_in_another(pair):
    server, client = pair
    captured = {}

    def first(session):
        captured["frame"] = _good(session, "replayed")
        return captured["frame"]

    first_result, first_reply = _deliver(server, client, first)
    assert first_result == {"response": "pong-from-B"}
    assert first_reply == "pong-from-B"

    server.last_message = None
    second_result, second_reply = _deliver(server, client, lambda session: captured["frame"])
    assert isinstance(second_result.get("error"), ValueError), second_result
    assert str(second_result["error"]) == BAD_SIGNATURE
    assert server.last_message is None
    assert second_reply is None


def test_second_frame_coalesced_after_the_message_is_rejected(pair):
    server, client = pair
    result, reply = _deliver(
        server,
        client,
        lambda s: _good(s, "first"),
        tail_build=lambda s: _good(s, "second", seq=2),
    )
    assert isinstance(result.get("error"), ValueError), result
    assert str(result["error"]) == EXTRA_DATA
    assert server.last_message is None
    assert reply is None


# --- decision 1: PROTOCOL_CONTEXT V2 fails during the handshake ------------------------


def test_legacy_v1_client_is_rejected_by_v2_server_during_handshake(pair):
    server, client = pair
    thread, result = _start_listener(server)
    with socket.create_connection((server.bound_host, server.bound_port), timeout=IO_TIMEOUT) as conn:
        buffer = bytearray()
        client_challenge = secrets.token_bytes(32)
        conn.sendall(
            (hello(client.node_id, client.public_key, client_challenge, client.label) + "\n").encode()
        )
        server_id, server_pk, server_challenge, server_sig = parse_welcome(
            _receive_line(conn, buffer)
        )
        # The server's WELCOME proof is V2: a V1-only client cannot verify it.
        with pytest.raises(InvalidSignature):
            Ed25519PublicKey.from_public_bytes(server_pk).verify(
                server_sig, _legacy_auth_payload(client.node_id, server_id, client_challenge)
            )
        # A V1 client that skipped that check and sent a V1 AUTH is rejected by the server.
        legacy_sig = client._identity_key.sign(
            _legacy_auth_payload(client.node_id, server.node_id, server_challenge)
        )
        conn.sendall((auth(legacy_sig) + "\nmessage-from-legacy-client\n").encode())
    _join(thread)
    assert isinstance(result.get("error"), ValueError)
    assert str(result["error"]) == "proof of possession failed"
    assert server.last_message is None


def test_v2_client_refuses_legacy_v1_server_and_sends_nothing_more(pair):
    _, client = pair
    legacy_key = Ed25519PrivateKey.generate()
    legacy_pub = legacy_key.public_key().public_bytes_raw()
    legacy_id = hashlib.sha256(legacy_pub).hexdigest()
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    listener.settimeout(IO_TIMEOUT)
    seen = {"after_welcome": []}

    def legacy_server():
        try:
            conn, _ = listener.accept()
            conn.settimeout(IO_TIMEOUT + 3)
            with conn:
                buffer = bytearray()
                peer_id, _pk, client_challenge, _label = parse_hello(_receive_line(conn, buffer))
                signature = legacy_key.sign(
                    _legacy_auth_payload(peer_id, legacy_id, client_challenge)
                )
                conn.sendall(
                    (welcome(legacy_id, legacy_pub, secrets.token_bytes(32), signature) + "\n").encode()
                )
                while True:
                    chunk = conn.recv(4096)
                    if not chunk:
                        break
                    seen["after_welcome"].append(chunk)
        except Exception as exc:  # noqa: BLE001 - recorded for debugging
            seen["error"] = repr(exc)
        finally:
            listener.close()

    thread = threading.Thread(target=legacy_server, daemon=True)
    thread.start()
    with pytest.raises(ValueError, match="proof of possession failed"):
        client.send("127.0.0.1", listener.getsockname()[1], "secret-text")
    thread.join(timeout=IO_TIMEOUT + 4)
    assert not thread.is_alive()
    assert seen["after_welcome"] == [], "client must not send AUTH or a message to a V1 server"


# --- handshake challenges: size and freshness -------------------------------------------


def test_handshake_challenges_are_32_bytes_and_fresh_per_connection(pair):
    server, client = pair
    hellos, welcomes = [], []
    for _ in range(2):
        thread, _result = _start_listener(server)
        port, relay_thread, record = _run_relay(server, lambda line: line)
        try:
            client.send("127.0.0.1", port, "probe")
        except (ValueError, OSError):
            pass
        _join(thread)
        relay_thread.join(timeout=IO_TIMEOUT)
        hellos.append(parse_hello(record["hello"].decode().rstrip("\n"))[2])
        welcomes.append(parse_welcome(record["welcome"].decode().rstrip("\n"))[2])
    assert all(len(challenge) == 32 for challenge in hellos + welcomes)
    assert hellos[0] != hellos[1]
    assert welcomes[0] != welcomes[1]


@pytest.mark.parametrize("size", [0, 31, 33])
def test_handshake_rejects_challenge_of_wrong_length(size):
    node = P2PNode("C")
    try:
        with pytest.raises(ValueError):
            hello(node.node_id, node.public_key, b"c" * size, "C")
        with pytest.raises(ValueError):
            parse_hello(
                f"HELLO {node.node_id} {_b64(node.public_key)} {_b64(b'c' * size)} C"
            )
    finally:
        node.close()


# --- protocol-level unit tests (reference builders vs implementation) ------------------


def _ids():
    return "11" * 32, "22" * 32


def test_message_payload_layout_matches_independent_reference():
    sender, recipient = _ids()
    sid = bytes(range(32))
    text = "zażółć gęślą jaźń"
    assert len(text.encode("utf-8")) != len(text)  # the byte length is what is signed
    assert protocol.message_payload(sid, sender, recipient, 7, text) == _payload(
        sid, sender, recipient, 7, text
    )


@pytest.mark.parametrize("index", [0, 1, 2, 3])
def test_session_id_binds_every_handshake_component(index):
    client_id, server_id = _ids()
    parts = [client_id, server_id, b"c" * 32, b"s" * 32]
    reference = _session_id(*parts)
    assert protocol.session_id(*parts) == reference
    changed = list(parts)
    changed[index] = "33" * 32 if index < 2 else b"x" * 32
    assert protocol.session_id(*changed) != reference


def test_message_frame_roundtrip_and_argument_validation():
    sig = b"\x07" * 64
    line = protocol.msg(1, sig, "text with spaces")
    assert line == f"MSG 1 {_b64(sig)} text with spaces"
    assert protocol.parse_msg(line) == (1, sig, "text with spaces")
    assert protocol.parse_msg(protocol.msg(1, sig, "")) == (1, sig, "")
    for bad_seq in (0, -1, 2**63):
        with pytest.raises(ValueError):
            protocol.msg(bad_seq, sig, "x")
    with pytest.raises(ValueError):
        protocol.msg(1, b"\x07" * 63, "x")


def _receiver_fixture():
    key = Ed25519PrivateKey.generate()
    public = key.public_key().public_bytes_raw()
    sender = hashlib.sha256(public).hexdigest()
    recipient = "22" * 32
    sid = _session_id(sender, recipient, b"c" * 32, b"s" * 32)
    return key, public, sender, recipient, sid


def _unit_frame(key, sid, sender, recipient, seq, text):
    return f"MSG {seq} {_b64(key.sign(_payload(sid, sender, recipient, seq, text)))} {text}"


def test_receiver_enforces_strict_sequence_within_a_session():
    key, public, sender, recipient, sid = _receiver_fixture()
    receiver = protocol.MessageReceiver(sid, sender, public, recipient)
    first = _unit_frame(key, sid, sender, recipient, 1, "one")
    assert receiver.accept(first) == "one"
    with pytest.raises(ValueError, match=BAD_SEQUENCE):
        receiver.accept(first)  # replay of the same frame
    with pytest.raises(ValueError, match=BAD_SEQUENCE):
        receiver.accept(_unit_frame(key, sid, sender, recipient, 3, "skipped"))
    assert receiver.accept(_unit_frame(key, sid, sender, recipient, 2, "two")) == "two"


def test_changing_the_session_context_invalidates_the_signature():
    key, public, sender, recipient, sid = _receiver_fixture()
    other_sid = _session_id(sender, recipient, b"c" * 32, b"t" * 32)
    frame = _unit_frame(key, sid, sender, recipient, 1, "bound to one session")
    assert protocol.MessageReceiver(sid, sender, public, recipient).accept(frame) == (
        "bound to one session"
    )
    with pytest.raises(ValueError, match=BAD_SIGNATURE):
        protocol.MessageReceiver(other_sid, sender, public, recipient).accept(frame)
