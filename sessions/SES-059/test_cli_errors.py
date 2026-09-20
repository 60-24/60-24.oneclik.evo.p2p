import subprocess
import sys


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
