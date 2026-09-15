"""Minimal reusable P2P node plus the SES CLI compatibility entrypoint."""

from __future__ import annotations

import argparse
import socket

BUFFER_SIZE = 4096
RESPONSE = "pong-from-B"
CONNECT_TIMEOUT_SECONDS = 5


def _parse_address(value: str) -> tuple[str, int]:
    host, separator, port_text = value.rpartition(":")
    if not separator or not host or not port_text:
        raise ValueError(f"invalid address: {value!r}")
    port = int(port_text)
    if not 0 < port < 65536:
        raise ValueError(f"invalid port: {port}")
    return host, port


def _receive_line(conn: socket.socket) -> str:
    data = bytearray()
    while b"\n" not in data:
        chunk = conn.recv(BUFFER_SIZE)
        if not chunk:
            break
        data.extend(chunk)
    return bytes(data).split(b"\n", 1)[0].decode("utf-8")


class P2PNode:
    """Small dependency-free node boundary for the concrete P2P system."""

    def __init__(self, node_id: str, host: str = "127.0.0.1", port: int = 0) -> None:
        if not node_id:
            raise ValueError("node_id must not be empty")
        self.node_id = node_id
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server.bind((host, port))
        self._server.listen(1)
        self.bound_host, self.bound_port = self._server.getsockname()

    def listen_once(self) -> str:
        conn, _peer = self._server.accept()
        with conn:
            _receive_line(conn)
            conn.sendall(f"{RESPONSE}\n".encode("utf-8"))
        return RESPONSE

    def send(self, host: str, port: int, message: str) -> str:
        with socket.create_connection(
            (host, port), timeout=CONNECT_TIMEOUT_SECONDS
        ) as conn:
            conn.sendall(f"{message}\n".encode("utf-8"))
            return _receive_line(conn)

    def close(self) -> None:
        self._server.close()


def _listen(address: str, node_id: str) -> int:
    host, port = _parse_address(address)
    node = P2PNode(node_id, host, port)
    try:
        node.listen_once()
    finally:
        node.close()
    return 0


def _connect(address: str, node_id: str, message: str) -> int:
    host, port = _parse_address(address)
    client = P2PNode(node_id)
    try:
        print(client.send(host, port, message))
    finally:
        client.close()
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Minimal P2P node")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--listen")
    mode.add_argument("--connect")
    parser.add_argument("--node-id", required=True)
    parser.add_argument("--message")
    args = parser.parse_args()

    if args.connect and args.message is None:
        parser.error("--message is required with --connect")
    if args.listen:
        return _listen(args.listen, args.node_id)
    return _connect(args.connect, args.node_id, args.message)


if __name__ == "__main__":
    raise SystemExit(main())
