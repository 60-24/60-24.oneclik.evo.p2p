"""SES-032 E2E: prove the existing System Builder chain can be composed."""
from __future__ import annotations

import importlib.util
from copy import deepcopy
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


intent = load_module("ses007", ROOT / "sessions/SES-007/intent_envelope.py")
specification = load_module("ses008", ROOT / "sessions/SES-008/specification.py")
build_plan = load_module("ses011", ROOT / "sessions/SES-011/build_plan.py")
authorization = load_module(
    "ses014", ROOT / "sessions/SES-014/execution_authorization.py"
)


def _valid_raw_intent() -> dict[str, object]:
    return {
        "version": 1,
        "objective": "Create a minimal reproducible system artifact",
        "requirements": ["create the artifact"],
        "constraints": ["local only"],
        "assumptions": [],
        "optional_information": [],
        "open_questions": [],
        "protected_decisions": [],
        "authority": "human",
    }


def _proposed_specification() -> dict[str, object]:
    validated = intent.validate(_valid_raw_intent())
    spec = specification.build_specification(validated)
    proposed = deepcopy(spec)
    proposed["requirements"][0]["origin"] = "PROPOSED"
    proposed["provenance"][0]["origin"] = "PROPOSED"
    return proposed


def test_existing_chain_reaches_build_plan_without_adapter_code():
    validated = intent.validate(_valid_raw_intent())
    assert validated["status"] == "VALID"

    spec = specification.build_specification(validated)
    assert spec["status"] == "VALID"
    assert spec["source_intent_id"] == validated["intent_id"]

    plan = build_plan.transform_specification_to_build_plan(spec)
    assert plan["build_plan_id"]
    assert plan["source_specification_id"] == spec["specification_id"]
    assert plan["steps"]
    assert plan["status"] == "VALIDATED"
    assert "execution_authorization" not in plan


def test_proposed_build_plan_requires_and_accepts_explicit_human_approval():
    spec = _proposed_specification()
    assert spec["status"] == "VALID"
    assert spec["requirements"][0]["origin"] == "PROPOSED"

    plan = build_plan.transform_specification_to_build_plan(spec)
    assert plan["steps"][0]["origin"] == "PROPOSED"
    assert plan["status"] == "READY_FOR_APPROVAL"
    assert plan["approval"]["required"] is True
    assert plan["approval"]["status"] == "PENDING"
    assert "execution_authorization" not in plan

    with pytest.raises(PermissionError):
        authorization.authorize_build_plan(plan, human_approval=None)

    approved = authorization.authorize_build_plan(
        plan,
        human_approval={
            "approved": True,
            "build_plan_id": plan["build_plan_id"],
            "authority_scope": "human-approved",
        },
    )

    assert approved["approval"]["status"] == "APPROVED"
    assert approved["execution_authorization"]["status"] == "AUTHORIZED"
    assert approved["execution_authorization"]["source"] == "EXPLICIT_HUMAN_APPROVAL"
    assert approved["status"] == "READY_FOR_APPROVAL"
    assert "execution_request" not in approved
    assert "execution_attempt" not in approved
    assert "execution_result" not in approved
    assert "execution_effect" not in approved
