"""Deterministic regression coverage for coalesced TCP line frames."""

from src.p2p.node import _receive_line


class ChunkSocket:
    """Socket stub that returns the supplied chunk boundaries exactly."""

    def __init__(self, chunks: list[bytes]) -> None:
        self.chunks = list(chunks)
        self.recv_calls = 0

    def recv(self, size: int) -> bytes:
        self.recv_calls += 1
        if not self.chunks:
            return b""
        chunk = self.chunks.pop(0)
        assert len(chunk) <= size
        return chunk


def test_receive_line_preserves_second_frame_from_same_recv():
    conn = ChunkSocket([b"AUTH signature\napplication-message\n"])
    buffer = bytearray()

    assert _receive_line(conn, buffer) == "AUTH signature"
    assert _receive_line(conn, buffer) == "application-message"
    assert conn.recv_calls == 1
    assert not buffer
