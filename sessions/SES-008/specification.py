"""Deterministic SES-008 Specification builder.

Transforms a validated SES-007 Intent Envelope into a machine-representable
Specification without inventing unresolved or protected decisions.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any

from pathlib import Path
import importlib.util


CONTRACT_VERSION = 1
ORIGINS = ("DERIVED", "PROPOSED", "UNRESOLVED")


def _load_intent_validator():
    path = Path(__file__).resolve().parent.parent / "SES-007" / "intent_envelope.py"
    spec = importlib.util.spec_from_file_location("ses007_intent_envelope", path)
    if spec is None or spec.loader is None:
        raise ImportError("cannot load SES-007 intent validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def stable_id(prefix: str, value: Any) -> str:
    digest = hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()[:16]
    return f"{prefix}-{digest}"


def _source_element(envelope: dict[str, Any], field: str, statement: str) -> str:
    for item in envelope.get("element_ids", []):
        if item["field"] == field and item["content"] == statement:
            return item["element_id"]
    raise ValueError(f"missing source element id for {field}: {statement}")


def _derived_item(prefix: str, statement: str, source_element_id: str) -> dict[str, str]:
    item_id = stable_id(prefix, {"statement": statement, "source_element_id": source_element_id})
    return {
        "id": item_id,
        "statement": statement,
        "source_element_id": source_element_id,
        "origin": "DERIVED",
    }


def build_specification(raw_intent: dict[str, Any]) -> dict[str, Any]:
    intent_module = _load_intent_validator()
    envelope = intent_module.validate(raw_intent)

    if envelope["status"] != "VALID":
        raise ValueError(
            f"cannot build Specification from Intent status {envelope['status']}: "
            + "; ".join(envelope["validation"]["reasons"])
        )

    source_intent_id = envelope["intent_id"]
    requirements = [
        _derived_item("SPEC-REQ", value, _source_element(envelope, "requirements", value))
        for value in envelope["requirements"]
    ]
    constraints = [
        _derived_item("SPEC-CON", value, _source_element(envelope, "constraints", value))
        for value in envelope["constraints"]
    ]
    assumptions = [
        _derived_item("SPEC-ASM", value, _source_element(envelope, "assumptions", value))
        for value in envelope["assumptions"]
    ]

    specification = {
        "specification_id": "",
        "source_intent_id": source_intent_id,
        "version": CONTRACT_VERSION,
        "status": "VALID",
        "objective": {
            "statement": envelope["objective"],
            "source_intent_id": source_intent_id,
            "source_field": "objective",
            "origin": "DERIVED",
        },
        "requirements": requirements,
        "constraints": constraints,
        "inputs": [],
        "outputs": [],
        "acceptance_criteria": [],
        "assumptions": assumptions,
        "unresolved_decisions": [],
        "provenance": [],
        "authority": envelope["authority"],
    }

    provenance: list[dict[str, str]] = []
    for item in requirements + constraints + assumptions:
        provenance.append({
            "source_intent_id": source_intent_id,
            "source_element_id": item["source_element_id"],
            "specification_element_id": item["id"],
            "origin": item["origin"],
        })
    specification["provenance"] = sorted(
        provenance,
        key=lambda item: (item["source_element_id"], item["specification_element_id"]),
    )

    identity_payload = dict(specification)
    identity_payload.pop("specification_id")
    specification["specification_id"] = stable_id("SPEC", identity_payload)
    return specification
