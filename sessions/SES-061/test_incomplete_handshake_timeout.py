import socket
import subprocess
import sys
import time


def test_listener_rejects_incomplete_handshake_instead_of_hanging():
    port = 39013
    listener = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "src.p2p.node",
            "--listen",
            f"127.0.0.1:{port}",
            "--node-id",
            "B",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        time.sleep(0.5)
        with socket.create_connection(("127.0.0.1", port), timeout=2) as conn:
            conn.sendall(b"HELLO")
        stdout, stderr = listener.communicate(timeout=3)
        assert listener.returncode == 1
        assert "ERROR:" in stderr
        assert "timed out" in stderr.lower()
        assert "Traceback" not in stderr
        assert stdout == ""
    finally:
        if listener.poll() is None:
            listener.kill()
            listener.wait()
