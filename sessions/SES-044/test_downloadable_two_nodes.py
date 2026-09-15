"""RED contract for the standalone downloadable two-node P2P program."""

from __future__ import annotations

import socket
import subprocess
import sys
import time
from pathlib import Path


NODE = Path("p2p_node.py")


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def test_downloadable_program_connects_two_independent_nodes() -> None:
    port = _free_port()
    address = f"127.0.0.1:{port}"

    node_b = subprocess.Popen(
        [sys.executable, str(NODE), "--listen", address, "--node-id", "B"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        time.sleep(0.1)
        node_a = subprocess.run(
            [
                sys.executable,
                str(NODE),
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
        node_b.terminate()
        try:
            node_b.wait(timeout=2)
        except subprocess.TimeoutExpired:
            node_b.kill()
            node_b.wait(timeout=2)
