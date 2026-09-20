import socket
import subprocess
import sys
import time


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "src.p2p.node", *args],
        capture_output=True,
        text=True,
    )


def test_invalid_address_returns_actionable_error():
    result = run_cli("--connect", "192.168.1.10", "--node-id", "A", "--message", "hello")
    assert result.returncode == 1
    assert "Use the format IP:PORT" in result.stderr
    assert "Traceback" not in result.stderr


def test_connection_refused_returns_actionable_error():
    result = run_cli("--connect", "127.0.0.1:1", "--node-id", "A", "--message", "hello")
    assert result.returncode == 1
    assert "Connection refused" in result.stderr
    assert "Node B" in result.stderr
    assert "Traceback" not in result.stderr


def test_help_exposes_basic_cli_usage():
    result = run_cli("--help")
    assert result.returncode == 0
    assert "--listen" in result.stdout
    assert "--connect" in result.stdout
    assert "--node-id" in result.stdout


def test_malformed_handshake_on_listener_is_actionable():
    port = 39011
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
            conn.sendall(b"NOT-A-HANDSHAKE\n")
        stdout, stderr = listener.communicate(timeout=3)
        assert listener.returncode == 1
        assert "ERROR:" in stderr
        assert "Traceback" not in stderr
        assert stdout == ""
    finally:
        if listener.poll() is None:
            listener.kill()
            listener.wait()


def test_malformed_welcome_on_connect_is_actionable():
    port = 39012
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", port))
    server.listen(1)
    try:
        listener = subprocess.Popen(
            [
                sys.executable,
                "-m",
                "src.p2p.node",
                "--connect",
                f"127.0.0.1:{port}",
                "--node-id",
                "A",
                "--message",
                "hello",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        conn, _ = server.accept()
        with conn:
            conn.recv(4096)
            conn.sendall(b"NOT-A-WELCOME\n")
        stdout, stderr = listener.communicate(timeout=3)
        assert listener.returncode == 1
        assert "ERROR:" in stderr
        assert "Traceback" not in stderr
        assert stdout == ""
    finally:
        server.close()
