import pytest

from src.p2p import P2PNode


def test_identity_persists_across_restart(tmp_path):
    identity_path = tmp_path / "node-a.key"

    first = P2PNode("A", identity_path=identity_path)
    first_id = first.node_id
    first_public_key = first.public_key
    first.close()

    second = P2PNode("A", identity_path=identity_path)
    try:
        assert second.node_id == first_id
        assert second.public_key == first_public_key
    finally:
        second.close()


def test_corrupt_identity_store_is_rejected(tmp_path):
    identity_path = tmp_path / "node-a.key"
    identity_path.write_bytes(b"not-a-valid-ed25519-key")

    with pytest.raises(ValueError, match="invalid identity key"):
        P2PNode("A", identity_path=identity_path)
