"""SES-010 TDD contract tests for Specification -> Build Plan.

These tests define the execution boundary before a transformer is implemented.
The implementation is intentionally absent at this stage.
"""

import pytest


REQUIRED_FIELDS = {
    "build_plan_id",
    "source_specification_id",
    "version",
    "status",
    "steps",
    "provenance",
    "unresolved_decisions",
    "authority",
}

ALLOWED_ORIGINS = {"DERIVED", "PROPOSED", "UNRESOLVED"}
BLOCKING_STATUSES = {"INCOMPLETE", "AMBIGUOUS", "PROTECTED"}


def validate_build_plan_contract(plan):
    """Contract-level validator expected to be implemented by the transformer layer."""
    raise NotImplementedError


def test_build_plan_has_minimum_contract_fields():
    plan = {
        "build_plan_id": "bp-1",
        "source_specification_id": "spec-1",
        "version": 1,
        "status": "DRAFT",
        "steps": [],
        "provenance": [],
        "unresolved_decisions": [],
        "authority": "HUMAN_CONTROLLED",
    }
    assert REQUIRED_FIELDS <= set(plan)


def test_origin_semantics_are_closed_set():
    assert ALLOWED_ORIGINS == {"DERIVED", "PROPOSED", "UNRESOLVED"}


def test_unresolved_cannot_be_executable():
    step = {"id": "step-1", "origin": "UNRESOLVED"}
    assert step["origin"] == "UNRESOLVED"
    assert step.get("executable", False) is False


def test_proposed_requires_human_decision():
    step = {"id": "step-1", "origin": "PROPOSED", "human_approved": False}
    assert step["origin"] == "PROPOSED"
    assert step["human_approved"] is False


def test_blocking_specification_states_are_not_executable():
    for status in BLOCKING_STATUSES:
        specification = {"status": status}
        assert specification["status"] in BLOCKING_STATUSES


def test_provenance_is_required_for_every_step():
    step = {"id": "step-1", "provenance": {"source_specification_id": "spec-1"}}
    assert step["provenance"]["source_specification_id"]


def test_transformer_is_not_implemented_yet():
    with pytest.raises(NotImplementedError):
        validate_build_plan_contract({})
