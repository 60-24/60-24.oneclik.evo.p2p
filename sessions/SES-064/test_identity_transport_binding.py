import socket
import threading

from src.p2p import P2PNode


def test_listener_rejects_plaintext_hello_without_proof_of_possession():
    server = P2PNode("B")
    result = {}

    def serve():
        try:
            result["response"] = server.listen_once()
        except Exception as exc:
            result["error"] = exc

    thread = threading.Thread(target=serve)
    thread.start()

    try:
        with socket.create_connection(("127.0.0.1", server.bound_port), timeout=2) as conn:
            conn.sendall(b"HELLO A\n")
            response = conn.recv(4096).decode("utf-8")
        thread.join(timeout=3)

        assert "error" in result
        assert response == ""
        assert server.last_peer_id is None
    finally:
        server.close()
        if thread.is_alive():
            thread.join(timeout=1)


def test_listener_rejects_node_id_not_bound_to_public_key():
    server = P2PNode("B")
    result = {}

    def serve():
        try:
            result["response"] = server.listen_once()
        except Exception as exc:
            result["error"] = exc

    thread = threading.Thread(target=serve)
    thread.start()

    try:
        with socket.create_connection(("127.0.0.1", server.bound_port), timeout=2) as conn:
            conn.sendall(
                b"HELLO "
                + b"0" * 64
                + b" "
                + __import__("base64").b64encode(b"1" * 32)
                + b" "
                + __import__("base64").b64encode(b"2" * 32)
                + b"\n"
            )
            response = conn.recv(4096).decode("utf-8")
        thread.join(timeout=3)

        assert "error" in result
        assert response == ""
        assert server.last_peer_id is None
    finally:
        server.close()
        if thread.is_alive():
            thread.join(timeout=1)
