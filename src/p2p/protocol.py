"""Minimal line protocol for the concrete two-node P2P boundary."""

from __future__ import annotations

HELLO = "HELLO"
WELCOME = "WELCOME"


def hello(node_id: str) -> str:
    if not node_id:
        raise ValueError("node_id must not be empty")
    return f"{HELLO} {node_id}"


def parse_hello(message: str) -> str:
    prefix = f"{HELLO} "
    if not message.startswith(prefix):
        raise ValueError("invalid handshake")
    node_id = message[len(prefix) :]
    if not node_id or "\n" in node_id or "\r" in node_id:
        raise ValueError("invalid peer identity")
    return node_id


def welcome(node_id: str) -> str:
    if not node_id:
        raise ValueError("node_id must not be empty")
    return f"{WELCOME} {node_id}"


def parse_welcome(message: str) -> str:
    prefix = f"{WELCOME} "
    if not message.startswith(prefix):
        raise ValueError("handshake failed")
    node_id = message[len(prefix) :]
    if not node_id or "\n" in node_id or "\r" in node_id:
        raise ValueError("invalid peer identity")
    return node_id
