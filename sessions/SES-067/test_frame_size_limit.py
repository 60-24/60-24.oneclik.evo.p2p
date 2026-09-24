import pytest

from src.p2p import P2PNode


MAX_FRAME_SIZE = 64 * 1024


def test_listener_rejects_message_larger_than_max_frame_size():
    server = P2PNode("B")
    result = {}
    oversized_message = "X" * (MAX_FRAME_SIZE + 1)

    def serve():
        try:
            result["response"] = server.listen_once()
        except Exception as exc:
            result["error"] = exc

    thread = __import__("threading").Thread(target=serve)
    thread.start()

    client = P2PNode("A")
    try:
        client.send("127.0.0.1", server.bound_port, oversized_message)

        thread.join(timeout=3)

        assert "error" in result
        assert server.last_message is None
    finally:
        client.close()
        server.close()
        if thread.is_alive():
            thread.join(timeout=1)
