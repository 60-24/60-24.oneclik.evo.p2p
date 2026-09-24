"""Minimal reusable authenticated P2P node plus the SES CLI entrypoint."""

from __future__ import annotations

import argparse
import secrets
import socket
import sys

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from .protocol import (
    auth,
    auth_payload,
    hello,
    node_id_from_public_key,
    parse_auth,
    parse_hello,
    parse_welcome,
    verify_signature,
    welcome,
)

BUFFER_SIZE = 4096
RESPONSE = "pong-from-B"
CONNECT_TIMEOUT_SECONDS = 5
LISTEN_TIMEOUT_SECONDS = 2


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
    """Small dependency-free node boundary with authenticated peer identity."""

    def __init__(self, node_id: str, host: str = "127.0.0.1", port: int = 0) -> None:
        if not node_id:
            raise ValueError("node_id must not be empty")
        self.label = node_id
        self._identity_key = Ed25519PrivateKey.generate()
        self.public_key = self._identity_key.public_key().public_bytes(
            Encoding.Raw, PublicFormat.Raw
        )
        self.node_id = node_id_from_public_key(self.public_key)
        self.last_peer_id: str | None = None
        self.last_message: str | None = None
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server.bind((host, port))
        self._server.listen(1)
        self.bound_host, self.bound_port = self._server.getsockname()

    def listen_once(self) -> str:
        conn, _peer = self._server.accept()
        conn.settimeout(LISTEN_TIMEOUT_SECONDS)
        with conn:
            peer_id, peer_public_key, client_challenge, peer_label = parse_hello(
                _receive_line(conn)
            )
            server_challenge = secrets.token_bytes(32)
            signature = self._identity_key.sign(
                auth_payload(peer_id, self.node_id, client_challenge)
            )
            conn.sendall(
                f"{welcome(self.node_id, self.public_key, server_challenge, signature)}\n".encode(
                    "utf-8"
                )
            )
            peer_signature = parse_auth(_receive_line(conn))
            verify_signature(
                peer_public_key,
                peer_signature,
                auth_payload(peer_id, self.node_id, server_challenge),
            )
            self.last_peer_id = peer_id
            self.last_message = _receive_line(conn)
            print(
                f"node {self.label} received from {peer_label}: "
                f"{self.last_message}",
                flush=True,
            )
            conn.sendall(f"{RESPONSE}\n".encode("utf-8"))
        return RESPONSE

    def send(self, host: str, port: int, message: str) -> str:
        with socket.create_connection(
            (host, port), timeout=CONNECT_TIMEOUT_SECONDS
        ) as conn:
            client_challenge = secrets.token_bytes(32)
            conn.sendall(
                f"{hello(self.node_id, self.public_key, client_challenge, self.label)}\n".encode(
                    "utf-8"
                )
            )
            peer_id, peer_public_key, server_challenge, server_signature = parse_welcome(
                _receive_line(conn)
            )
            verify_signature(
                peer_public_key,
                server_signature,
                auth_payload(self.node_id, peer_id, client_challenge),
            )
            self.last_peer_id = peer_id
            signature = self._identity_key.sign(
                auth_payload(self.node_id, peer_id, server_challenge)
            )
            conn.sendall(f"{auth(signature)}\n".encode("utf-8"))
            conn.sendall(f"{message}\n".encode("utf-8"))
            return _receive_line(conn)

    def close(self) -> None:
        self._server.close()


def _listen(address: str, node_id: str) -> int:
    try:
        host, port = _parse_address(address)
        node = P2PNode(node_id, host, port)
    except ValueError as exc:
        print(f"ERROR: {exc}. Use the format IP:PORT (for example 0.0.0.0:9000).", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"ERROR: Cannot start listening: {exc}. Check that the port is available.", file=sys.stderr)
        return 1
    try:
        node.listen_once()
    except (ValueError, UnicodeDecodeError) as exc:
        print(f"ERROR: Invalid peer handshake: {exc}.", file=sys.stderr)
        return 1
    except (OSError, TimeoutError) as exc:
        print(f"ERROR: Listening failed: {exc}.", file=sys.stderr)
        return 1
    finally:
        node.close()
    return 0


def _connect(address: str, node_id: str, message: str) -> int:
    try:
        host, port = _parse_address(address)
    except ValueError as exc:
        print(f"ERROR: {exc}. Use the format IP:PORT (for example 192.168.1.10:9000).", file=sys.stderr)
        return 1
    client = P2PNode(node_id)
    try:
        response = client.send(host, port, message)
        print(response)
    except (ValueError, UnicodeDecodeError) as exc:
        print(f"ERROR: Invalid peer handshake: {exc}.", file=sys.stderr)
        return 1
    except socket.timeout:
        print("ERROR: Connection timed out. Check that Node B is running and the address/port are correct.", file=sys.stderr)
        return 1
    except ConnectionRefusedError:
        print("ERROR: Connection refused. Make sure Node B is listening at this address and port.", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"ERROR: Cannot connect: {exc}.", file=sys.stderr)
        return 1
    finally:
        client.close()
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Minimal authenticated P2P node")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--listen")
    mode.add_argument("--connect")
    parser.add_argument("--node-id", required=True, help="local display label; cryptographic NodeID is derived from the public key")
    parser.add_argument("--message")
    args = parser.parse_args()

    if args.connect and args.message is None:
        parser.error("--message is required with --connect")
    if args.listen:
        return _listen(args.listen, args.node_id)
    return _connect(args.connect, args.node_id, args.message)


if __name__ == "__main__":
    raise SystemExit(main())
