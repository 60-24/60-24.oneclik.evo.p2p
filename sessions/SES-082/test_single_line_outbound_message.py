import pytest

from src.p2p import P2PNode


@pytest.mark.parametrize("message", ["first\nsecond", "first\rsecond", "first\r\nsecond"])
def test_send_rejects_multiline_message_before_connecting(message):
    node = P2PNode("A")
    try:
        with pytest.raises(ValueError, match="message must be a single line"):
            node.send("127.0.0.1", 1, message)
    finally:
        node.close()
