"""Minimal TCP node used by the SES-043 two-process proof."""

from __future__ import annotations

import argparse
import socket

BUFFER_SIZE = 4096
RESPONSE = "pong-from-B"


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


def _listen(address: str, node_id: str) -> int:
    host, port = _parse_address(address)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(1)
        conn, _peer = server.accept()
        with conn:
            _receive_line(conn)
            conn.sendall(f"{RESPONSE}\n".encode("utf-8"))
    return 0


def _connect(address: str, node_id: str, message: str) -> int:
    host, port = _parse_address(address)
    with socket.create_connection((host, port), timeout=5) as conn:
        conn.sendall(f"{message}\n".encode("utf-8"))
        response = _receive_line(conn)
    print(response)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Minimal SES-043 P2P node")
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
