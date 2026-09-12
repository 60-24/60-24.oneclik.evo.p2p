"""SES-034 proof: one production entrypoint composes the verified chain."""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


def _load(name: str, relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


def test_system_builder_entrypoint_composes_validated_chain_without_approval(tmp_path: Path):
    intent = _load("ses007", "sessions/SES-007/intent_envelope.py")
    specification = _load("ses008", "sessions/SES-008/specification.py")
    build_plan = _load("ses011", "sessions/SES-011/build_plan.py")
    entrypoint = _load("system_builder_entrypoint", "src/system_builder/entrypoint.py")

    validated = intent.validate(_valid_raw_intent())
    spec = specification.build_specification(validated)
    plan = build_plan.transform_specification_to_build_plan(spec)
    assert plan["status"] == "VALIDATED"
    assert plan["approval"]["required"] is False
    assert plan["approval"]["status"] == "NOT_REQUIRED"

    result = entrypoint.run_system_builder(
        _valid_raw_intent(),
        human_approval=None,
        output_dir=tmp_path,
    )

    assert result["status"] == "DELIVERED"
    assert result["source"] == "VERIFICATION"
    assert result["artifact_ids"]
    assert result["build_plan_id"] == plan["build_plan_id"]


def test_validated_authorization_rejects_a_plan_that_requires_approval():
    authorization = _load(
        "validated_execution_authorization",
        "src/system_builder/validated_execution_authorization.py",
    )
    with pytest.raises(PermissionError, match="requires human approval"):
        authorization.authorize_validated_build_plan(
            {
                "status": "READY_FOR_APPROVAL",
                "approval": {"required": True, "status": "PENDING"},
                "blockers": [],
            }
        )
