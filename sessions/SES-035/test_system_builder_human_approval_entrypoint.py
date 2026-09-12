"""SES-035: prove explicit human approval through the production entrypoint."""
from __future__ import annotations

import importlib.util
from copy import deepcopy
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


def _proposed_specification() -> dict[str, object]:
    specification = _load("ses008", "sessions/SES-008/specification.py")
    intent = _load("ses007", "sessions/SES-007/intent_envelope.py")
    validated = intent.validate(_valid_raw_intent())
    proposed = deepcopy(specification.build_specification(validated))
    proposed["requirements"][0]["origin"] = "PROPOSED"
    proposed["provenance"][0]["origin"] = "PROPOSED"
    return proposed


def test_production_entrypoint_preserves_explicit_human_approval_boundary(tmp_path: Path):
    entrypoint = _load("system_builder_entrypoint", "src/system_builder/entrypoint.py")
    proposed = _proposed_specification()

    original_builder = entrypoint.specification.build_specification
    entrypoint.specification.build_specification = lambda _: deepcopy(proposed)
    try:
        with pytest.raises(PermissionError, match="Explicit human approval is required"):
            entrypoint.run_system_builder(
                _valid_raw_intent(), human_approval=None, output_dir=tmp_path / "rejected"
            )
        assert not (tmp_path / "rejected").exists()

        result = entrypoint.run_system_builder(
            _valid_raw_intent(),
            human_approval={
                "approved": True,
                "build_plan_id": _load(
                    "ses011", "sessions/SES-011/build_plan.py"
                ).transform_specification_to_build_plan(proposed)["build_plan_id"],
                "authority_scope": "human-approved",
            },
            output_dir=tmp_path / "approved",
        )
    finally:
        entrypoint.specification.build_specification = original_builder

    assert result["status"] == "DELIVERED"
    assert result["source"] == "VERIFICATION"
    assert result["artifact_ids"]
    assert (tmp_path / "approved").exists()


def test_production_entrypoint_does_not_accept_mismatched_human_approval(tmp_path: Path):
    entrypoint = _load("system_builder_entrypoint_mismatch", "src/system_builder/entrypoint.py")
    proposed = _proposed_specification()
    original_builder = entrypoint.specification.build_specification
    entrypoint.specification.build_specification = lambda _: deepcopy(proposed)
    try:
        with pytest.raises(PermissionError, match="does not match the BuildPlan"):
            entrypoint.run_system_builder(
                _valid_raw_intent(),
                human_approval={
                    "approved": True,
                    "build_plan_id": "BUILD-NOT-THE-PLAN",
                    "authority_scope": "human-approved",
                },
                output_dir=tmp_path,
            )
    finally:
        entrypoint.specification.build_specification = original_builder
    assert not tmp_path.exists()
