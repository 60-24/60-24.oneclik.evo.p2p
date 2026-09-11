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
    assert module
    assert spec.loader
    spec.loader.exec_module(module)
    return module


intent = load_module("ses007", ROOT / "sessions/SES-007/intent_envelope.py")
specification = load_module("ses008", ROOT / "sessions/SES-008/specification.py")
build_plan = load_module("ses011", ROOT / "sessions/SES-011/build_plan.py")
authorization = load_module("ses014", ROOT / "sessions/SES-014/execution_authorization.py")
execution_request = load_module("ses017", ROOT / "sessions/SES_017/execution_request.py")
execution_dispatch = load_module("ses018", ROOT / "sessions/SES-018/execution_dispatch.py")
execution_result = load_module("ses019", ROOT / "sessions/SES-019/execution_result.py")
execution_effect = load_module("ses021", ROOT / "sessions/SES-021/execution_effect.py")
verification = load_module("ses030", ROOT / "sessions/SES-030/execution_effect_verification.py")
delivery = load_module("ses031", ROOT / "sessions/SES-031/delivery.py")
local_executor = load_module("local_executor", ROOT / "src/execution/local_executor.py")


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


def test_minimal_full_chain_reaches_delivery_manifest_with_real_local_effect(tmp_path):
    spec = _proposed_specification()
    plan = build_plan.transform_specification_to_build_plan(spec)
    approved = authorization.authorize_build_plan(
        plan,
        human_approval={
            "approved": True,
            "build_plan_id": plan["build_plan_id"],
            "authority_scope": "human-approved",
        },
    )

    request = execution_request.create_execution_request(approved)
    assert request["status"] == "REQUESTED"
    assert request["build_plan_id"] == plan["build_plan_id"]

    attempt = execution_dispatch.create_execution_attempt(request)
    assert attempt["status"] == "EXECUTION_ATTEMPT"
    assert attempt["build_plan_id"] == plan["build_plan_id"]

    execution = local_executor.execute_build_plan(approved, tmp_path)
    assert execution["status"] == "EXECUTED"
    assert execution["artifacts"]
    assert all(Path(item["path"]).exists() for item in execution["artifacts"])

    result = execution_result.create_execution_result(attempt, "SUCCEEDED")
    assert result["status"] == "EXECUTION_RESULT"
    assert result["execution_attempt_id"] == attempt["execution_attempt_id"]

    effect = execution_effect.create_execution_effect(
        result,
        execution["artifacts"][0]["artifact_id"],
        {
            "status": "AUTHORIZED",
            "build_plan_id": plan["build_plan_id"],
            "source": "EXPLICIT_HUMAN_APPROVAL",
        },
    )
    assert effect["status"] == "EXECUTION_EFFECT"
    assert effect["build_plan_id"] == plan["build_plan_id"]
    assert effect["authorization_source"] == "EXPLICIT_HUMAN_APPROVAL"

    verified = verification.verify_execution_effect(effect)
    assert verified["status"] == "VERIFIED"
    assert verified["execution_effect_id"] == effect["execution_effect_id"]

    manifest = delivery.create_delivery_manifest(
        verified, [item["artifact_id"] for item in execution["artifacts"]]
    )
    assert manifest["status"] == "DELIVERED"
    assert manifest["source"] == "VERIFICATION"
    assert manifest["build_plan_id"] == plan["build_plan_id"]
    assert manifest["artifact_ids"] == [item["artifact_id"] for item in execution["artifacts"]]
