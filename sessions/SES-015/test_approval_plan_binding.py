"""SES-015 — TDD RED test for approval-to-BuildPlan binding.

The authorization boundary must reject an approval record that refers to a
BuildPlan different from the plan being authorized.
"""

from __future__ import annotations

import importlib
from typing import Any

import pytest


BUILD_PLAN_MODULE = "sessions.SES_011.build_plan"
AUTHORIZATION_MODULE = "sessions.SES_014.execution_authorization"


def _valid_specification(spec_id: str = "spec-015-001") -> dict[str, Any]:
    return {
        "specification_id": spec_id,
        "source_intent_id": "intent-015-001",
        "version": 1,
        "status": "VALID",
        "objective": {
            "statement": "Build the requested component",
            "source_intent_id": "intent-015-001",
            "source_field": "objective",
            "origin": "DERIVED",
        },
        "requirements": [
            {
                "id": "req-015-001",
                "statement": "Create the requested component",
                "source_element_id": "intent-element-015-001",
                "origin": "DERIVED",
            }
        ],
        "constraints": [],
        "inputs": [],
        "outputs": [],
        "acceptance_criteria": [],
        "assumptions": [],
        "unresolved_decisions": [],
        "provenance": [
            {
                "source_intent_id": "intent-015-001",
                "source_element_id": "intent-element-015-001",
                "specification_element_id": "req-015-001",
                "origin": "DERIVED",
            }
        ],
        "authority": {"scope": "human-approved"},
    }


def _transformer():
    module = importlib.import_module(BUILD_PLAN_MODULE)
    transform = getattr(module, "transform_specification_to_build_plan", None)
    if not callable(transform):
        pytest.fail("RED: BuildPlan transformer is unavailable")
    return transform


def _authorizer():
    module = importlib.import_module(AUTHORIZATION_MODULE)
    authorize = getattr(module, "authorize_build_plan", None)
    if not callable(authorize):
        pytest.fail("RED: execution authorization seam is unavailable")
    return authorize


def test_approval_for_different_build_plan_cannot_authorize_execution():
    transform = _transformer()
    plan = transform(_valid_specification("spec-015-A"))
    other_plan = transform(_valid_specification("spec-015-B"))

    assert plan["build_plan_id"] != other_plan["build_plan_id"]
    assert plan["status"] == "VALIDATED"
    assert other_plan["status"] == "VALIDATED"

    # The current SES-014 seam expects explicit approval but has no contract
    # yet requiring the approval record to identify the exact BuildPlan.
    human_approval_for_other_plan = {
        "approved": True,
        "build_plan_id": other_plan["build_plan_id"],
        "authority_scope": "human-approved",
    }

    authorize = _authorizer()

    with pytest.raises((PermissionError, ValueError)):
        authorize(plan, human_approval_for_other_plan)
