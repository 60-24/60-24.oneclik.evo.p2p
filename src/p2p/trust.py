"""Trusted introductions (web-of-trust vouchers) for the P2P 60-24 node.

A voucher is a signed introduction: a sponsor signs the subject's public key
with the sponsor's own identity key. A listening node configured with a set of
trusted public keys accepts a connecting peer only when:

- the peer's public key is itself in the trusted set (direct trust), or
- the peer presents a voucher whose sponsor is in the trusted set and whose
  signature over the peer's public key verifies (introduced trust).

This implements "trust as a value" with nothing but the Ed25519 identities the
runtime already has: no server, no database, no consensus.
"""

from __future__ import annotations

import base64
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)

VOUCHER_PREFIX = "VOUCHER1"
VOUCH = "VOUCH"
VOUCHER_CONTEXT = b"P2P60-24-VOUCHER-V1"

_PUBLIC_KEY_SIZE = 32
_SIGNATURE_SIZE = 64


def _b64(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def _unb64(value: str) -> bytes:
    try:
        return base64.b64decode(value.encode("ascii"), validate=True)
    except Exception as exc:
        raise ValueError("invalid base64 field") from exc


def voucher_payload(sponsor_public_key: bytes, subject_public_key: bytes) -> bytes:
    if len(sponsor_public_key) != _PUBLIC_KEY_SIZE:
        raise ValueError("invalid sponsor public key")
    if len(subject_public_key) != _PUBLIC_KEY_SIZE:
        raise ValueError("invalid subject public key")
    return VOUCHER_CONTEXT + sponsor_public_key + subject_public_key


class Voucher:
    """A signed introduction of ``subject_public_key`` by ``sponsor_public_key``."""

    __slots__ = ("sponsor_public_key", "subject_public_key", "signature")

    def __init__(
        self,
        sponsor_public_key: bytes,
        subject_public_key: bytes,
        signature: bytes,
    ) -> None:
        if len(sponsor_public_key) != _PUBLIC_KEY_SIZE:
            raise ValueError("invalid sponsor public key")
        if len(subject_public_key) != _PUBLIC_KEY_SIZE:
            raise ValueError("invalid subject public key")
        if len(signature) != _SIGNATURE_SIZE:
            raise ValueError("invalid voucher signature")
        self.sponsor_public_key = sponsor_public_key
        self.subject_public_key = subject_public_key
        self.signature = signature

    def to_line(self) -> str:
        return (
            f"{VOUCHER_PREFIX} {_b64(self.sponsor_public_key)} "
            f"{_b64(self.subject_public_key)} {_b64(self.signature)}"
        )

    @classmethod
    def from_line(cls, line: str) -> "Voucher":
        parts = line.strip().split(" ")
        if len(parts) != 4 or parts[0] != VOUCHER_PREFIX:
            raise ValueError("invalid voucher")
        return cls(_unb64(parts[1]), _unb64(parts[2]), _unb64(parts[3]))

    def verify(self) -> None:
        """Raise ValueError when the sponsor's signature does not verify."""
        payload = voucher_payload(self.sponsor_public_key, self.subject_public_key)
        try:
            Ed25519PublicKey.from_public_bytes(self.sponsor_public_key).verify(
                self.signature, payload
            )
        except (ValueError, InvalidSignature) as exc:
            raise ValueError("voucher signature verification failed") from exc


def issue_voucher(
    sponsor_private_key: Ed25519PrivateKey, subject_public_key: bytes
) -> Voucher:
    """Sponsor signs the subject's public key, producing a portable voucher."""
    from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

    sponsor_public_key = sponsor_private_key.public_key().public_bytes(
        Encoding.Raw, PublicFormat.Raw
    )
    signature = sponsor_private_key.sign(
        voucher_payload(sponsor_public_key, subject_public_key)
    )
    return Voucher(sponsor_public_key, subject_public_key, signature)


def vouch_line(voucher: Voucher) -> str:
    """Protocol line the connecting peer sends after AUTH."""
    return f"{VOUCH} {_b64(voucher.sponsor_public_key)} {_b64(voucher.signature)}"


def parse_vouch(line: str, subject_public_key: bytes) -> Voucher:
    """Parse a VOUCH protocol line presented by ``subject_public_key``."""
    parts = line.split(" ")
    if len(parts) != 3 or parts[0] != VOUCH:
        raise ValueError("invalid VOUCH")
    return Voucher(_unb64(parts[1]), subject_public_key, _unb64(parts[2]))


def is_authorized(
    peer_public_key: bytes,
    trusted_keys: frozenset[bytes],
    voucher: Voucher | None,
) -> bool:
    """Decide whether a fully authenticated peer may deliver a message.

    Direct trust: the peer's key is in the trusted set.
    Introduced trust: a verifying voucher for the peer's key, signed by a
    sponsor whose key is in the trusted set.
    """
    if peer_public_key in trusted_keys:
        return True
    if voucher is None:
        return False
    if voucher.subject_public_key != peer_public_key:
        return False
    if voucher.sponsor_public_key not in trusted_keys:
        return False
    try:
        voucher.verify()
    except ValueError:
        return False
    return True


def load_trusted_keys(path: str | Path) -> frozenset[bytes]:
    """Read a trusted-keys file: one base64 Ed25519 public key per line.

    Blank lines and lines starting with ``#`` are ignored.
    """
    keys: set[bytes] = set()
    for raw_line in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        key = _unb64(line)
        if len(key) != _PUBLIC_KEY_SIZE:
            raise ValueError(f"invalid trusted key in {path}: {line!r}")
        keys.add(key)
    if not keys:
        raise ValueError(f"trusted keys file {path} contains no keys")
    return frozenset(keys)
