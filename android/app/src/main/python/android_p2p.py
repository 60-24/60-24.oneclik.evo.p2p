"""Android adapter for the existing authenticated P2P runtime."""

import os
from pathlib import Path

from p2p.node import P2PNode


def _identity_path(label: str) -> Path:
    root = Path(os.environ["HOME"]) / ".p2p60-24"
    digest = __import__("hashlib").sha256(label.encode("utf-8")).hexdigest()[:16]
    return root / f"{digest}.key"


def connect(host: str, port: int, label: str, message: str) -> str:
    node = P2PNode(label, identity_path=_identity_path(label))
    try:
        response = node.send(host, int(port), message)
        return (
            f"OK response={response} "
            f"local_node_id={node.node_id} peer_node_id={node.last_peer_id}"
        )
    finally:
        node.close()


def listen(host: str, port: int, label: str) -> str:
    node = P2PNode(
        label,
        host=host,
        port=int(port),
        identity_path=_identity_path(label),
    )
    try:
        response = node.listen_once()
        return (
            f"OK response={response} "
            f"local_node_id={node.node_id} peer_node_id={node.last_peer_id} "
            f"message={node.last_message}"
        )
    finally:
        node.close()
