import threading

def test_client_records_peer_identity_after_handshake():
    from src.p2p import P2PNode

    server = P2PNode("B")
    client = P2PNode("A")
    result = {}

    def serve():
        result["response"] = server.listen_once()

    thread = threading.Thread(target=serve)
    thread.start()

    try:
        assert client.send("127.0.0.1", server.bound_port, "identity-check") == "pong-from-B"
        thread.join(timeout=5)
        assert not thread.is_alive()
        assert result["response"] == "pong-from-B"
        assert client.last_peer_id == server.node_id
    finally:
        server.close()
        client.close()
