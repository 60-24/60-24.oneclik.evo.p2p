import threading


def test_two_nodes_exchange_message_through_public_api():
    from src.p2p import P2PNode

    server = P2PNode("B")
    client = P2PNode("A")
    received = {}

    def serve():
        received["response"] = server.listen_once()

    thread = threading.Thread(target=serve)
    thread.start()

    client.send("127.0.0.1", server.bound_port, "ping-from-A")
    thread.join(timeout=5)

    assert received["response"] == "pong-from-B"
    server.close()
    client.close()
