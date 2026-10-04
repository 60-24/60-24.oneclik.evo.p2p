import socket

from src.p2p import P2PNode
from src.p2p.transport import TCPTransport

def test_node_accepts_explicit_transport_adapter():
    transport = TCPTransport()
    node = P2PNode("B", transport=transport)
    try:
        assert node.transport is transport
        assert node.bound_port > 0
    finally:
        node.close()

def test_tcp_transport_provides_connectable_stream():
    transport = TCPTransport()
    listener = transport.listen("127.0.0.1", 0)
    host, port = listener.getsockname()
    accepted = {}

    def accept_once():
        conn, _ = listener.accept()
        with conn:
            accepted["data"] = conn.recv(4)

    import threading
    thread = threading.Thread(target=accept_once)
    thread.start()
    with transport.connect(host, port, 2) as conn:
        conn.sendall(b"test")
    thread.join(timeout=2)
    listener.close()
    assert accepted["data"] == b"test"