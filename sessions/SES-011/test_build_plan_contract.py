"""SES-011 executable contract tests for Specification -> BuildPlan."""

from __future__ import annotations

import importlib.util
import json
from copy import deepcopy
from pathlib import Path
from typing import Any

import pytest


ROOT = Path(__file__).resolve().parents[2]
BUILD_PLAN_PATH = ROOT / "sessions" / "SES-011" / "build_plan.py"
TRANSFORMER_NAME = "transform_specification_to_build_plan"

REQUIRED_BUILD_PLAN_FIELDS = {
    "build_plan_id", "source_specification_id", "contract_version", "status",
    "objective", "steps", "dependencies", "constraints", "assumptions",
    "unresolved_decisions", "approval", "blockers", "provenance", "determinism",
}
REQUIRED_STEP_FIELDS = {
    "id", "sequence", "action", "target", "preconditions", "inputs",
    "expected_outputs", "acceptance_criteria", "provenance", "origin", "execution_state",
}
ALLOWED_ORIGINS = {"DERIVED", "PROPOSED", "UNRESOLVED"}
ALLOWED_PLAN_STATUSES = {"DRAFT", "VALIDATED", "BLOCKED", "READY_FOR_APPROVAL"}


def _transformer():
    spec = importlib.util.spec_from_file_location("ses011_build_plan", BUILD_PLAN_PATH)
    if spec is None or spec.loader is None:
        pytest.fail(f"RED: missing SES-011 transformer at {BUILD_PLAN_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    transform = getattr(module, TRANSFORMER_NAME, None)
    if not callable(transform):
        pytest.fail(f"RED: expected callable {TRANSFORMER_NAME}")
    return transform


def _valid_specification(**overrides: Any) -> dict[str, Any]:
    specification = {
        "specification_id": "spec-001", "source_intent_id": "intent-001", "version": 1,
        "status": "VALID",
        "objective": {"statement": "Build the requested system", "source_intent_id": "intent-001",
                      "source_field": "objective", "origin": "DERIVED"},
        "requirements": [{"id": "req-001", "statement": "Create the requested component",
                          "source_element_id": "intent-element-001", "origin": "DERIVED"}],
        "constraints": [], "inputs": [], "outputs": [], "acceptance_criteria": [],
        "assumptions": [], "unresolved_decisions": [],
        "provenance": [{"source_intent_id": "intent-001", "source_element_id": "intent-element-001",
                        "specification_element_id": "req-001", "origin": "DERIVED"}],
        "authority": {"scope": "human-approved"},
    }
    specification.update(overrides)
    return specification


def _canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def test_valid_specification_produces_structurally_valid_build_plan():
    plan = _transformer()(_valid_specification())
    assert REQUIRED_BUILD_PLAN_FIELDS <= set(plan)
    assert plan["source_specification_id"] == "spec-001"
    assert plan["contract_version"] == 1
    assert plan["status"] in ALLOWED_PLAN_STATUSES
    assert isinstance(plan["steps"], list)
    assert isinstance(plan["approval"], dict)
    assert isinstance(plan["determinism"], dict)
    for step in plan["steps"]:
        assert REQUIRED_STEP_FIELDS <= set(step)
        assert step["origin"] in ALLOWED_ORIGINS


def test_every_derived_execution_relevant_step_has_provenance():
    plan = _transformer()(_valid_specification())
    derived_steps = [step for step in plan["steps"] if step["origin"] == "DERIVED"]
    assert derived_steps
    for step in derived_steps:
        assert step["provenance"]
        for provenance in step["provenance"]:
            assert provenance["source_specification_id"] == "spec-001"
            assert provenance["source_specification_element_id"]
            assert provenance["build_plan_element_id"] == step["id"]
            assert provenance["origin"] == "DERIVED"


def test_proposed_elements_remain_proposed_and_require_approval():
    specification = _valid_specification(requirements=[
        {"id": "req-001", "statement": "Create the requested component",
         "source_element_id": "intent-element-001", "origin": "DERIVED"},
        {"id": "req-002", "statement": "Implementation choice is intentionally left to the builder",
         "source_element_id": "intent-element-002", "origin": "PROPOSED"},
    ])
    plan = _transformer()(specification)
    proposed = [step for step in plan["steps"] if step["origin"] == "PROPOSED"]
    assert proposed
    assert all(step["origin"] != "DERIVED" for step in proposed)
    assert plan["approval"]["required"] is True
    assert plan["approval"]["status"] != "APPROVED"


def test_unresolved_decision_is_preserved_and_blocks_plan():
    plan = _transformer()(_valid_specification(unresolved_decisions=[
        {"id": "decision-001", "statement": "Deployment target is not decided", "origin": "UNRESOLVED"}
    ]))
    assert any(d.get("id") == "decision-001" and d.get("origin") == "UNRESOLVED"
               for d in plan["unresolved_decisions"])
    assert plan["status"] == "BLOCKED"
    assert plan["blockers"]
    assert plan["approval"]["status"] != "APPROVED"


def test_blocked_plan_cannot_be_ready_or_execution_authorized():
    plan = _transformer()(_valid_specification(unresolved_decisions=[
        {"id": "decision-001", "statement": "Unknown", "origin": "UNRESOLVED"}
    ]))
    assert plan["status"] == "BLOCKED"
    assert plan["status"] != "READY_FOR_APPROVAL"
    assert plan["approval"]["status"] != "APPROVED"
    assert all(step["execution_state"] not in {"AUTHORIZED", "EXECUTING", "EXECUTED"}
               for step in plan["steps"])


def test_invalid_specification_is_rejected_fail_closed():
    with pytest.raises((ValueError, TypeError)):
        _transformer()(_valid_specification(status="INVALID"))


def test_missing_specification_is_rejected_fail_closed():
    invalid = deepcopy(_valid_specification())
    del invalid["specification_id"]
    with pytest.raises((ValueError, TypeError, KeyError)):
        _transformer()(invalid)


def test_protected_decision_without_authority_blocks_plan():
    plan = _transformer()(_valid_specification(
        unresolved_decisions=[{"id": "decision-protected", "statement": "Protected authority decision",
                              "origin": "UNRESOLVED", "protected": True}],
        authority={"scope": "none"},
    ))
    assert plan["status"] == "BLOCKED"
    assert plan["blockers"]
    assert plan["approval"]["status"] != "APPROVED"


def test_same_canonical_input_produces_identical_plan():
    specification = _valid_specification()
    assert _canonical(_transformer()(deepcopy(specification))) == _canonical(
        _transformer()(deepcopy(specification))
    )


def test_step_ids_and_ordering_are_stable():
    specification = _valid_specification(requirements=[
        {"id": "req-001", "statement": "First requirement", "source_element_id": "intent-element-001", "origin": "DERIVED"},
        {"id": "req-002", "statement": "Second requirement", "source_element_id": "intent-element-002", "origin": "DERIVED"},
    ])
    first = _transformer()(deepcopy(specification))
    second = _transformer()(deepcopy(specification))
    first_identity = [(step["id"], step["sequence"]) for step in first["steps"]]
    second_identity = [(step["id"], step["sequence"]) for step in second["steps"]]
    assert first_identity == second_identity
    assert [sequence for _, sequence in first_identity] == sorted(sequence for _, sequence in first_identity)


def test_generation_has_no_execution_side_effects(monkeypatch):
    execution_calls: list[tuple[tuple[Any, ...], dict[str, Any]]] = []
    def forbidden_execution(*args: Any, **kwargs: Any) -> None:
        execution_calls.append((args, kwargs))
        raise AssertionError("BuildPlan generation attempted execution")
    monkeypatch.setattr("subprocess.run", forbidden_execution)
    monkeypatch.setattr("subprocess.Popen", forbidden_execution)
    _transformer()(_valid_specification())
    assert execution_calls == []


def test_string_authority_is_accepted_without_widening_scope():
    plan = _transformer()(_valid_specification(authority="human"))
    assert plan["approval"]["authority_scope"] == "human"
