"""Standalone, dependency-free two-node P2P communication demo.

Run one process with --listen and a second with --connect.
The program uses only Python's standard library and is intentionally limited
 to a small local communication proof; it is not a production P2P protocol.
"""

from __future__ import annotations

import argparse
import socket

BUFFER_SIZE = 4096
DEFAULT_RESPONSE = "pong-from-B"
CONNECT_TIMEOUT_SECONDS = 5


def parse_address(value: str) -> tuple[str, int]:
    host, separator, port_text = value.rpartition(":")
    if not separator or not host or not port_text:
        raise ValueError(f"invalid address: {value!r}; expected HOST:PORT")
    try:
        port = int(port_text)
    except ValueError as exc:
        raise ValueError(f"invalid port: {port_text!r}") from exc
    if not 0 < port < 65536:
        raise ValueError(f"invalid port: {port}")
    return host, port


def receive_line(conn: socket.socket) -> str:
    data = bytearray()
    while b"\n" not in data:
        chunk = conn.recv(BUFFER_SIZE)
        if not chunk:
            break
        data.extend(chunk)
    return bytes(data).split(b"\n", 1)[0].decode("utf-8")


def listen(address: str, node_id: str) -> int:
    host, port = parse_address(address)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(1)
        print(f"node {node_id} listening on {host}:{port}", flush=True)
        conn, peer = server.accept()
        with conn:
            message = receive_line(conn)
            print(f"node {node_id} received from {peer[0]}: {message}", flush=True)
            conn.sendall(f"{DEFAULT_RESPONSE}\n".encode("utf-8"))
    return 0


def connect(address: str, node_id: str, message: str) -> int:
    host, port = parse_address(address)
    with socket.create_connection(
        (host, port), timeout=CONNECT_TIMEOUT_SECONDS
    ) as conn:
        print(f"node {node_id} connected to {host}:{port}", flush=True)
        conn.sendall(f"{message}\n".encode("utf-8"))
        response = receive_line(conn)
    print(response)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Standalone dependency-free two-node P2P communication demo"
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--listen", metavar="HOST:PORT")
    mode.add_argument("--connect", metavar="HOST:PORT")
    parser.add_argument("--node-id", required=True, help="human-readable node ID")
    parser.add_argument("--message", help="message sent by a connecting node")
    args = parser.parse_args()

    try:
        if args.listen:
            return listen(args.listen, args.node_id)
        if args.message is None:
            parser.error("--message is required with --connect")
        return connect(args.connect, args.node_id, args.message)
    except (OSError, ValueError, UnicodeError) as exc:
        parser.error(str(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
