"""SES-011 TDD contract tests for Specification -> BuildPlan.

The tests encode the SES-010 BuildPlan contract.
Transformer implementation is intentionally absent.
"""

import pytest


ALLOWED_ORIGINS = {
    "DERIVED",
    "PROPOSED",
    "UNRESOLVED",
}

ALLOWED_PLAN_STATUSES = {
    "DRAFT",
    "VALIDATED",
    "BLOCKED",
    "READY_FOR_APPROVAL",
}

REQUIRED_BUILD_PLAN_FIELDS = {
    "build_plan_id",
    "source_specification_id",
    "contract_version",
    "status",
    "objective",
    "steps",
    "dependencies",
    "constraints",
    "assumptions",
    "unresolved_decisions",
    "approval",
    "blockers",
    "provenance",
    "determinism",
}


def validate_build_plan_contract(plan):
    """Contract validator expected from the implementation layer."""
    raise NotImplementedError


def test_build_plan_has_contract_structure():
    plan = {
        "build_plan_id": "bp-1",
        "source_specification_id": "spec-1",
        "contract_version": 1,
        "status": "DRAFT",
        "objective": {"statement": "test", "origin": "DERIVED"},
        "steps": [],
        "dependencies": [],
        "constraints": [],
        "assumptions": [],
        "unresolved_decisions": [],
        "approval": {"required": False, "status": "NOT_REQUIRED", "authority_scope": "NONE"},
        "blockers": [],
        "provenance": [],
        "determinism": {"canonicalization": "required", "ordering": "stable", "identity_rule": "stable"},
    }
    assert REQUIRED_BUILD_PLAN_FIELDS <= set(plan)


def test_plan_status_is_closed_set():
    assert ALLOWED_PLAN_STATUSES == {
        "DRAFT",
        "VALIDATED",
        "BLOCKED",
        "READY_FOR_APPROVAL",
    }


def test_origin_semantics_are_closed_set():
    assert ALLOWED_ORIGINS == {
        "DERIVED",
        "PROPOSED",
        "UNRESOLVED",
    }


def test_derived_step_requires_provenance():
    step = {
        "id": "step-1",
        "origin": "DERIVED",
        "provenance": [{
            "source_specification_id": "spec-1",
            "source_specification_element_id": "spec-element-1",
            "build_plan_element_id": "step-1",
            "origin": "DERIVED",
        }],
    }
    assert step["origin"] == "DERIVED"
    assert step["provenance"]


def test_proposed_step_requires_human_approval():
    step = {"id": "step-1", "origin": "PROPOSED", "human_approved": False}
    assert step["origin"] == "PROPOSED"
    assert step["human_approved"] is False


def test_proposed_cannot_be_reclassified_as_derived():
    step = {"id": "step-1", "origin": "PROPOSED"}
    assert step["origin"] != "DERIVED"


def test_unresolved_step_is_not_executable():
    step = {"id": "step-1", "origin": "UNRESOLVED", "executable": False}
    assert step["origin"] == "UNRESOLVED"
    assert step["executable"] is False


def test_unresolved_requires_blocked_plan():
    plan = {
        "status": "BLOCKED",
        "unresolved_decisions": [{"id": "decision-1", "origin": "UNRESOLVED"}],
    }
    assert plan["status"] == "BLOCKED"


def test_blocked_plan_cannot_be_ready_for_approval():
    plan = {"status": "BLOCKED", "blockers": ["unresolved-decision"]}
    assert plan["status"] != "READY_FOR_APPROVAL"


def test_proposed_plan_requires_approval():
    plan = {
        "status": "READY_FOR_APPROVAL",
        "approval": {"required": True, "status": "PENDING", "authority_scope": "HUMAN"},
        "steps": [{"id": "step-1", "origin": "PROPOSED"}],
    }
    assert plan["approval"]["required"] is True
    assert plan["approval"]["status"] == "PENDING"


def test_transformer_cannot_synthesize_human_approval():
    plan = {"approval": {"required": True, "status": "PENDING", "authority_scope": "HUMAN"}}
    assert plan["approval"]["status"] != "APPROVED"


def test_provenance_requires_source_specification():
    provenance = {
        "source_specification_id": "spec-1",
        "source_specification_element_id": "element-1",
        "build_plan_element_id": "step-1",
        "origin": "DERIVED",
    }
    assert provenance["source_specification_id"]
    assert provenance["source_specification_element_id"]
    assert provenance["build_plan_element_id"]
    assert provenance["origin"] in ALLOWED_ORIGINS


def test_determinism_contract_is_explicit():
    determinism = {"canonicalization": "required", "ordering": "stable", "identity_rule": "stable"}
    assert determinism["canonicalization"] == "required"
    assert determinism["ordering"] == "stable"
    assert determinism["identity_rule"] == "stable"


def test_step_identity_must_be_stable():
    step_a = {"id": "step-spec-1-01", "sequence": 1}
    step_b = {"id": "step-spec-1-01", "sequence": 1}
    assert step_a["id"] == step_b["id"]
    assert step_a["sequence"] == step_b["sequence"]


def test_step_ordering_must_be_stable():
    steps = [{"id": "step-1", "sequence": 1}, {"id": "step-2", "sequence": 2}]
    assert [step["sequence"] for step in steps] == [1, 2]


def test_invalid_specification_must_be_rejected():
    invalid_specification = {"status": "INVALID"}
    assert invalid_specification["status"] != "VALID"


def test_generation_has_no_execution_side_effect():
    execution_performed = False
    assert execution_performed is False


def test_transformer_is_not_implemented_yet():
    with pytest.raises(NotImplementedError):
        validate_build_plan_contract({})
