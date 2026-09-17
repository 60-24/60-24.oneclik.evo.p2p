import threading


def test_node_receives_application_message():
    from src.p2p import P2PNode

    server = P2PNode("B")
    client = P2PNode("A")

    thread = threading.Thread(target=server.listen_once)
    thread.start()

    try:
        assert client.send("127.0.0.1", server.bound_port, "hello-from-A") == "pong-from-B"
        thread.join(timeout=5)
        assert not thread.is_alive()
        assert server.last_message == "hello-from-A"
    finally:
        server.close()
        client.close()
