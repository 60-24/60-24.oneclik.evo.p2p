import pytest

import src.p2p.node as node_module
from src.p2p import P2PNode


DEFAULT_MAX_FRAME_SIZE = 64 * 1024


def test_listener_rejects_message_larger_than_max_frame_size(monkeypatch):
    assert node_module.MAX_FRAME_SIZE == DEFAULT_MAX_FRAME_SIZE
    monkeypatch.setattr(node_module, "MAX_FRAME_SIZE", 1024)

    server = P2PNode("B")
    result = {}
    oversized_message = "X" * (node_module.MAX_FRAME_SIZE + 1)

    def serve():
        try:
            result["response"] = server.listen_once()
        except Exception as exc:
            result["error"] = exc

    thread = __import__("threading").Thread(target=serve)
    thread.start()

    client = P2PNode("A")
    try:
        try:
            client.send("127.0.0.1", server.bound_port, oversized_message)
        except (ValueError, OSError):
            pass

        thread.join(timeout=3)

        assert isinstance(result.get("error"), ValueError)
        assert str(result["error"]) == "frame exceeds maximum size"
        assert server.last_message is None
    finally:
        client.close()
        server.close()
        if thread.is_alive():
            thread.join(timeout=1)
