"""Deterministic SES-010 Specification -> BuildPlan transformer.

This module implements only the planning boundary. It never executes a step,
grants approval, resolves unresolved decisions, or widens authority.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any


CONTRACT_VERSION = 1
ALLOWED_ORIGINS = {"DERIVED", "PROPOSED", "UNRESOLVED"}


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def stable_id(prefix: str, value: Any) -> str:
    digest = hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()[:16]
    return f"{prefix}-{digest}"


def _validate_specification(specification: Any) -> None:
    if not isinstance(specification, dict):
        raise TypeError("Specification must be a mapping")

    required = {
        "specification_id", "status", "objective", "requirements", "constraints",
        "inputs", "outputs", "acceptance_criteria", "assumptions",
        "unresolved_decisions", "provenance", "authority",
    }
    missing = sorted(required - set(specification))
    if missing:
        raise ValueError(f"incomplete Specification: missing {', '.join(missing)}")
    if specification["status"] != "VALID":
        raise ValueError("BuildPlan transformation requires a VALID Specification")
    if not isinstance(specification["specification_id"], str) or not specification["specification_id"]:
        raise ValueError("Specification must have a non-empty specification_id")
    if not isinstance(specification["objective"], dict):
        raise TypeError("Specification objective must be a mapping")
    for field in ("requirements", "constraints", "inputs", "outputs", "acceptance_criteria", "assumptions", "unresolved_decisions", "provenance"):
        if not isinstance(specification[field], list):
            raise TypeError(f"Specification field {field} must be a list")

    for collection_name in ("requirements", "constraints", "inputs", "outputs", "acceptance_criteria", "assumptions"):
        for item in specification[collection_name]:
            if not isinstance(item, dict):
                raise TypeError(f"Specification {collection_name} entries must be mappings")
            if item.get("origin") not in ALLOWED_ORIGINS:
                raise ValueError(f"unsupported origin in {collection_name}: {item.get('origin')!r}")


def _step_for_requirement(specification: dict[str, Any], requirement: dict[str, Any], sequence: int) -> dict[str, Any]:
    source_id = requirement["id"]
    origin = requirement["origin"]
    step_id = stable_id(
        "STEP",
        {"source_specification_id": specification["specification_id"], "source_specification_element_id": source_id},
    )
    provenance = [{
        "source_specification_id": specification["specification_id"],
        "source_specification_element_id": source_id,
        "build_plan_element_id": step_id,
        "origin": origin,
    }]

    return {
        "id": step_id,
        "sequence": sequence,
        "action": "create",
        "target": requirement["statement"],
        "preconditions": [],
        "inputs": [],
        "expected_outputs": [],
        "acceptance_criteria": [],
        "provenance": provenance,
        "origin": origin,
        "execution_state": "PLANNED",
    }


def transform_specification_to_build_plan(specification: dict[str, Any]) -> dict[str, Any]:
    """Transform a VALID Specification into a deterministic, non-executing BuildPlan."""
    _validate_specification(specification)

    spec_id = specification["specification_id"]
    requirements = list(specification["requirements"])
    steps = [
        _step_for_requirement(specification, requirement, sequence)
        for sequence, requirement in enumerate(requirements, start=1)
    ]

    unresolved = list(specification["unresolved_decisions"])
    proposed_present = any(step["origin"] == "PROPOSED" for step in steps)
    protected_unresolved = any(decision.get("protected") for decision in unresolved)
    authority = specification.get("authority")
    authority_scope = authority.get("scope") if isinstance(authority, dict) else authority

    blockers: list[dict[str, Any]] = []
    if not specification["provenance"]:
        blockers.append({
            "type": "MISSING_PROVENANCE",
            "reason": "mandatory Specification provenance is empty",
        })
    if unresolved:
        blockers.append({
            "type": "UNRESOLVED_DECISION",
            "source_ids": [decision.get("id") for decision in unresolved],
            "reason": "execution-relevant decision remains unresolved",
        })
    if protected_unresolved and authority_scope in (None, "", "none"):
        blockers.append({
            "type": "PROTECTED_DECISION_WITHOUT_AUTHORITY",
            "reason": "protected decision has no explicit authority scope",
        })

    approval_required = proposed_present or protected_unresolved
    approval_status = "PENDING" if approval_required or blockers else "NOT_REQUIRED"

    plan_provenance: list[dict[str, Any]] = []
    for item in specification["provenance"]:
        if not isinstance(item, dict):
            continue
        element_id = item.get("specification_element_id")
        if element_id is None:
            continue
        matching_steps = [step for step in steps if step["origin"] != "UNRESOLVED" and step["id"]]
        for step in matching_steps:
            if any(p["source_specification_element_id"] == element_id for p in step["provenance"]):
                plan_provenance.append({
                    "source_specification_id": spec_id,
                    "source_specification_element_id": element_id,
                    "build_plan_element_id": step["id"],
                    "origin": step["origin"],
                })

    plan_provenance.sort(key=lambda item: (item["source_specification_element_id"], item["build_plan_element_id"]))

    status = "BLOCKED" if blockers else ("READY_FOR_APPROVAL" if approval_required else "VALIDATED")

    identity_payload = {
        "source_specification_id": spec_id,
        "contract_version": CONTRACT_VERSION,
        "objective": specification["objective"],
        "steps": steps,
        "dependencies": [],
        "constraints": specification["constraints"],
        "assumptions": specification["assumptions"],
        "unresolved_decisions": unresolved,
        "approval": {"required": approval_required, "status": approval_status, "authority_scope": authority_scope},
        "blockers": blockers,
        "provenance": plan_provenance,
    }
    build_plan_id = stable_id("BUILD", identity_payload)

    return {
        "build_plan_id": build_plan_id,
        "source_specification_id": spec_id,
        "contract_version": CONTRACT_VERSION,
        "status": status,
        "objective": {
            "statement": specification["objective"].get("statement"),
            "origin": specification["objective"].get("origin", "DERIVED"),
        },
        "steps": steps,
        "dependencies": [],
        "constraints": list(specification["constraints"]),
        "assumptions": list(specification["assumptions"]),
        "unresolved_decisions": unresolved,
        "approval": {
            "required": approval_required,
            "status": approval_status,
            "authority_scope": authority_scope,
        },
        "blockers": blockers,
        "provenance": plan_provenance,
        "determinism": {
            "canonicalization": "JSON sort_keys=true separators=(',', ':') ensure_ascii=false",
            "ordering": "source requirement order; provenance sorted by source element and build-plan element",
            "identity_rule": "SHA-256 canonical JSON truncated to 16 hex characters",
        },
    }
