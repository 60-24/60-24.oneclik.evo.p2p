"""Experimental, local-only Tagologia S validator.

This module is a contract experiment, not a P2P protocol or authorization engine.
It deliberately does not infer identity, truth, trust, or permission.
"""
from __future__ import annotations

import json
from typing import Any

SUPPORTED_SCHEMA = "urn:60-24:tagologia-s:resource-request"
SUPPORTED_VERSION = "0.1"
ALLOWED_OPERATIONS = {"read"}
REQUIRED_TOP_LEVEL = {
    "schema",
    "version",
    "kind",
    "statement_id",
    "subject",
    "resource",
    "requested_operations",
    "constraints",
    "references",
}


class ContractError(ValueError):
    """Raised when a statement cannot be accepted by this experimental contract."""


def validate_statement(statement: Any) -> dict[str, Any]:
    """Validate the small resource-request contract; return a shallow copy.

    Acceptance means only 'valid under this experimental schema'. It does not
    authorize the requested operation or prove any claim.
    """
    if not isinstance(statement, dict):
        raise ContractError("invalid_type:statement")

    missing = REQUIRED_TOP_LEVEL - statement.keys()
    if missing:
        raise ContractError("missing_fields:" + ",".join(sorted(missing)))

    if statement["schema"] != SUPPORTED_SCHEMA:
        raise ContractError("unsupported_schema")
    if statement["version"] != SUPPORTED_VERSION:
        raise ContractError("unsupported_version")
    if statement["kind"] != "resource.request":
        raise ContractError("unsupported_kind")

    for field in ("statement_id",):
        if not isinstance(statement[field], str) or not statement[field].strip():
            raise ContractError("invalid_field:" + field)

    for field, expected_type in (("subject", dict), ("resource", dict)):
        value = statement[field]
        if not isinstance(value, expected_type):
            raise ContractError("invalid_type:" + field)
        if not isinstance(value.get("type"), str) or not value["type"]:
            raise ContractError("invalid_reference_type:" + field)
        if not isinstance(value.get("id"), str) or not value["id"]:
            raise ContractError("missing_reference_id:" + field)

    operations = statement["requested_operations"]
    if not isinstance(operations, list) or not operations:
        raise ContractError("invalid_operations")
    if any(not isinstance(op, str) or op not in ALLOWED_OPERATIONS for op in operations):
        raise ContractError("unsupported_operation")

    if not isinstance(statement["constraints"], dict):
        raise ContractError("invalid_type:constraints")
    if not isinstance(statement["references"], list):
        raise ContractError("invalid_type:references")

    # This prototype rejects unknown top-level fields rather than guessing.
    unknown = statement.keys() - REQUIRED_TOP_LEVEL
    if unknown:
        raise ContractError("unknown_fields:" + ",".join(sorted(unknown)))

    return dict(statement)


def canonical_json(statement: Any) -> str:
    """Return deterministic JSON only after contract validation."""
    validated = validate_statement(statement)
    return json.dumps(
        validated,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    )
