"""Trusted introductions: a listening node only accepts trusted or vouched peers.

Direct trust: the peer's public key is listed in the listener's trusted keys.
Introduced trust: the peer presents a voucher for its own key signed by a
sponsor the listener trusts.
Everything else is rejected before the message is accepted.
"""

import threading

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from src.p2p import P2PNode, Voucher, issue_voucher, load_trusted_keys
from src.p2p.trust import vouch_line


def _public_bytes(private_key: Ed25519PrivateKey) -> bytes:
    return private_key.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)


def _run_listener(server: P2PNode) -> tuple[threading.Thread, list[Exception]]:
    errors: list[Exception] = []

    def run() -> None:
        try:
            server.listen_once()
        except Exception as exc:  # captured for assertions
            errors.append(exc)

    thread = threading.Thread(target=run)
    thread.start()
    return thread, errors


def test_directly_trusted_peer_is_accepted():
    client = P2PNode("A")
    server = P2PNode("B", trusted_keys=frozenset({client.public_key}))
    thread, errors = _run_listener(server)
    try:
        assert client.send("127.0.0.1", server.bound_port, "direct") == "pong-from-B"
        thread.join(timeout=5)
        assert errors == []
        assert server.last_message == "direct"
        assert server.last_peer_id == client.node_id
    finally:
        server.close()
        client.close()


def test_vouched_peer_is_accepted():
    sponsor = Ed25519PrivateKey.generate()
    client = P2PNode("A")
    client._voucher = issue_voucher(sponsor, client.public_key)
    server = P2PNode("B", trusted_keys=frozenset({_public_bytes(sponsor)}))
    thread, errors = _run_listener(server)
    try:
        assert (
            client.send("127.0.0.1", server.bound_port, "introduced")
            == "pong-from-B"
        )
        thread.join(timeout=5)
        assert errors == []
        assert server.last_message == "introduced"
    finally:
        server.close()
        client.close()


def test_unknown_peer_without_voucher_is_rejected():
    trusted_stranger = Ed25519PrivateKey.generate()
    server = P2PNode(
        "B", trusted_keys=frozenset({_public_bytes(trusted_stranger)})
    )
    client = P2PNode("A")
    thread, errors = _run_listener(server)
    try:
        try:
            client.send("127.0.0.1", server.bound_port, "sneak")
        except (ValueError, OSError):
            pass  # connection is torn down by the listener
        thread.join(timeout=5)
        assert len(errors) == 1
        assert "not authorized" in str(errors[0])
        # the peer did authenticate (its identity is recorded), but no
        # message was accepted from it
        assert server.last_peer_id == client.node_id
        assert server.last_message is None
    finally:
        server.close()
        client.close()


def test_voucher_from_untrusted_sponsor_is_rejected():
    trusted = Ed25519PrivateKey.generate()
    untrusted_sponsor = Ed25519PrivateKey.generate()
    client = P2PNode("A")
    client._voucher = issue_voucher(untrusted_sponsor, client.public_key)
    server = P2PNode("B", trusted_keys=frozenset({_public_bytes(trusted)}))
    thread, errors = _run_listener(server)
    try:
        try:
            client.send("127.0.0.1", server.bound_port, "forged-sponsor")
        except (ValueError, OSError):
            pass
        thread.join(timeout=5)
        assert len(errors) == 1
        assert "not authorized" in str(errors[0])
        assert server.last_message is None
    finally:
        server.close()
        client.close()


def test_tampered_voucher_signature_is_rejected():
    sponsor = Ed25519PrivateKey.generate()
    client = P2PNode("A")
    voucher = issue_voucher(sponsor, client.public_key)
    tampered = Voucher(
        voucher.sponsor_public_key,
        voucher.subject_public_key,
        bytes(64),
    )
    client._voucher = tampered
    server = P2PNode("B", trusted_keys=frozenset({_public_bytes(sponsor)}))
    thread, errors = _run_listener(server)
    try:
        try:
            client.send("127.0.0.1", server.bound_port, "forged-signature")
        except (ValueError, OSError):
            pass
        thread.join(timeout=5)
        assert len(errors) == 1
        assert "not authorized" in str(errors[0])
        assert server.last_message is None
    finally:
        server.close()
        client.close()


def test_stolen_voucher_for_someone_else_is_rejected():
    """A voucher issued for a different key must not admit the connecting peer."""
    sponsor = Ed25519PrivateKey.generate()
    someone_else = Ed25519PrivateKey.generate()
    client = P2PNode("A")
    # bypass the client-side subject check to simulate a stolen voucher
    client._voucher = issue_voucher(sponsor, _public_bytes(someone_else))
    server = P2PNode("B", trusted_keys=frozenset({_public_bytes(sponsor)}))
    thread, errors = _run_listener(server)
    try:
        try:
            client.send("127.0.0.1", server.bound_port, "stolen")
        except (ValueError, OSError):
            pass
        thread.join(timeout=5)
        assert len(errors) == 1
        assert "not authorized" in str(errors[0])
        assert server.last_message is None
    finally:
        server.close()
        client.close()


def test_node_rejects_voucher_for_foreign_subject_at_construction():
    sponsor = Ed25519PrivateKey.generate()
    someone_else = Ed25519PrivateKey.generate()
    foreign = issue_voucher(sponsor, _public_bytes(someone_else))
    try:
        P2PNode("A", voucher=foreign)
    except ValueError as exc:
        assert "voucher subject" in str(exc)
    else:
        raise AssertionError("expected ValueError for foreign voucher subject")


def test_trusted_keys_file_roundtrip(tmp_path):
    import base64

    key_a = _public_bytes(Ed25519PrivateKey.generate())
    key_b = _public_bytes(Ed25519PrivateKey.generate())
    path = tmp_path / "trusted_keys"
    path.write_text(
        "# trusted sponsors\n"
        f"{base64.b64encode(key_a).decode()}\n"
        "\n"
        f"{base64.b64encode(key_b).decode()}\n",
        encoding="utf-8",
    )
    assert load_trusted_keys(path) == frozenset({key_a, key_b})


def test_node_without_trusted_keys_accepts_anyone():
    server = P2PNode("B")
    client = P2PNode("A")
    thread, errors = _run_listener(server)
    try:
        assert client.send("127.0.0.1", server.bound_port, "open") == "pong-from-B"
        thread.join(timeout=5)
        assert errors == []
        assert server.last_message == "open"
    finally:
        server.close()
        client.close()
