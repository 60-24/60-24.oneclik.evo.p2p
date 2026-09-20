import socket
import threading

import pytest


def _non_loopback_ipv4() -> str:
    probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        probe.connect(("1.1.1.1", 80))
        address = probe.getsockname()[0]
    finally:
        probe.close()
    if address.startswith("127."):
        pytest.skip("runner has no non-loopback IPv4 address")
    return address


def test_node_connects_via_non_loopback_ipv4():
    from src.p2p import P2PNode

    address = _non_loopback_ipv4()
    server = P2PNode("B", host="0.0.0.0")
    client = P2PNode("A")
    thread = threading.Thread(target=server.listen_once)
    thread.start()

    try:
        assert client.send(address, server.bound_port, "lan-check") == "pong-from-B"
        thread.join(timeout=5)
        assert not thread.is_alive()
        assert server.last_peer_id == "A"
        assert server.last_message == "lan-check"
        assert client.last_peer_id == "B"
    finally:
        server.close()
        client.close()
