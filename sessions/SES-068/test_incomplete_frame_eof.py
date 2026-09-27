import socket
import threading

import pytest

from src.p2p import P2PNode


def test_listener_rejects_eof_before_frame_delimiter():
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
            conn.sendall(b"HELLO")
        thread.join(timeout=3)

        assert "error" in result
        assert isinstance(result["error"], ValueError)
        assert "incomplete frame" in str(result["error"])
        assert server.last_peer_id is None
    finally:
        server.close()
        if thread.is_alive():
            thread.join(timeout=1)
