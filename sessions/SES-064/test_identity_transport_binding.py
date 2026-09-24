import socket
import threading

from src.p2p import P2PNode


def test_listener_rejects_hello_without_proof_of_possession():
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

        # Security property under test:
        # a peer claiming NodeID A must not be accepted without proof-of-possession.
        assert not response.startswith("WELCOME A"), (
            "Node B accepted plaintext HELLO A without proof-of-possession"
        )
        assert "error" in result or not thread.is_alive()
    finally:
        server.close()
        if thread.is_alive():
            thread.join(timeout=1)
