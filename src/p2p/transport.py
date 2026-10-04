"""Transport adapters for the P2P node boundary."""

from __future__ import annotations

import socket
from typing import Protocol

class Transport(Protocol):
    """Internal transport contract; identity and protocol remain transport-neutral."""
    def listen(self, host: str, port: int) -> socket.socket: ...
    def connect(self, host: str, port: int, timeout: float) -> socket.socket: ...

class TCPTransport:
    """TCP implementation of the internal transport contract."""
    def listen(self, host: str, port: int) -> socket.socket:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(1)
        return server

    def connect(self, host: str, port: int, timeout: float) -> socket.socket:
        return socket.create_connection((host, port), timeout=timeout)