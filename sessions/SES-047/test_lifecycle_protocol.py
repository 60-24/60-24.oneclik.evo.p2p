import threading

import pytest


def _run_listen(node, result):
    try:
        result["value"] = node.listen_once()
    except Exception as exc:  # test harness captures protocol rejection explicitly
        result["error"] = exc


def test_node_survives_disconnect_and_reconnect():
    from src.p2p import P2PNode

    server = P2PNode("B")
    client = P2PNode("A")
    try:
        first = {}
        thread = threading.Thread(target=_run_listen, args=(server, first))
        thread.start()
        assert client.send("127.0.0.1", server.bound_port, "first") == "pong-from-B"
        thread.join(timeout=5)
        assert not thread.is_alive()
        assert first == {"value": "pong-from-B"}
        assert server.last_peer_id == client.node_id

        second = {}
        thread = threading.Thread(target=_run_listen, args=(server, second))
        thread.start()
        assert client.send("127.0.0.1", server.bound_port, "second") == "pong-from-B"
        thread.join(timeout=5)
        assert not thread.is_alive()
        assert second == {"value": "pong-from-B"}
    finally:
        server.close()
        client.close()


def test_malformed_handshake_is_rejected_and_node_can_continue():
    from src.p2p import P2PNode

    server = P2PNode("B")
    try:
        malformed = {}

        import socket

        def send_malformed():
            with socket.create_connection(("127.0.0.1", server.bound_port), timeout=5) as conn:
                conn.sendall(b"NOT-A-HANDSHAKE\n")

        thread = threading.Thread(target=send_malformed)
        listener = threading.Thread(target=_run_listen, args=(server, malformed))
        listener.start()
        thread.start()
        thread.join(timeout=5)
        listener.join(timeout=5)

        assert not thread.is_alive()
        assert not listener.is_alive()
        assert isinstance(malformed.get("error"), ValueError)
        assert "handshake" in str(malformed["error"]).lower()

        valid = {}
        client = P2PNode("A")
        try:
            listener = threading.Thread(target=_run_listen, args=(server, valid))
            listener.start()
            assert client.send("127.0.0.1", server.bound_port, "after-malformed") == "pong-from-B"
            listener.join(timeout=5)
            assert not listener.is_alive()
            assert valid == {"value": "pong-from-B"}
        finally:
            client.close()
    finally:
        server.close()
