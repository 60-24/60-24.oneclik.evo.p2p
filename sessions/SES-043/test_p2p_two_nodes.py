"""SES-043 RED contract: two independent local P2P nodes exchange a message.

This test intentionally precedes the implementation.  The transport remains an
implementation detail; the observable contract is two independently started
processes, a connection, request delivery, and a response.
"""

from __future__ import annotations

import socket
import subprocess
import sys
import time


NODE_MODULE = "src.p2p.node"


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def test_two_independent_nodes_exchange_message() -> None:
    """A and B must communicate as separate OS processes."""
    port = _free_port()
    address = f"127.0.0.1:{port}"

    node_b = subprocess.Popen(
        [
            sys.executable,
            "-m",
            NODE_MODULE,
            "--listen",
            address,
            "--node-id",
            "B",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    node_a = None
    try:
        time.sleep(0.1)
        node_a = subprocess.run(
            [
                sys.executable,
                "-m",
                NODE_MODULE,
                "--connect",
                address,
                "--node-id",
                "A",
                "--message",
                "ping-from-A",
            ],
            capture_output=True,
            text=True,
            timeout=5,
            check=True,
        )

        assert "pong-from-B" in node_a.stdout
    finally:
        if node_a is not None:
            node_a.kill() if node_a.returncode is None else None
        node_b.terminate()
        try:
            node_b.wait(timeout=2)
        except subprocess.TimeoutExpired:
            node_b.kill()
            node_b.wait(timeout=2)
