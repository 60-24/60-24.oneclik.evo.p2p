"""SES-014 — TDD RED test for the Human Approval -> Execution boundary.

The authorization seam is intentionally absent at this stage.  This test
must therefore fail because no execution authorization may be granted merely
from BuildPlan generation or pending approval metadata.
"""

from __future__ import annotations

import importlib
from typing import Any

import pytest


BUILD_PLAN_MODULE = "sessions.SES_011.build_plan"
AUTHORIZATION_MODULE = "sessions.SES_014.execution_authorization"
AUTHORIZER_NAME = "authorize_build_plan"


def _valid_specification() -> dict[str, Any]:
    return {
        "specification_id": "spec-014-001",
        "source_intent_id": "intent-014-001",
        "version": 1,
        "status": "VALID",
        "objective": {
            "statement": "Build the requested component",
            "source_intent_id": "intent-014-001",
            "source_field": "objective",
            "origin": "DERIVED",
        },
        "requirements": [
            {
                "id": "req-014-001",
                "statement": "Create the requested component",
                "source_element_id": "intent-element-014-001",
                "origin": "DERIVED",
            },
            {
                "id": "req-014-002",
                "statement": "Use a builder-selected implementation alternative",
                "source_element_id": "intent-element-014-002",
                "origin": "PROPOSED",
            },
        ],
        "constraints": [],
        "inputs": [],
        "outputs": [],
        "acceptance_criteria": [],
        "assumptions": [],
        "unresolved_decisions": [],
        "provenance": [
            {
                "source_intent_id": "intent-014-001",
                "source_element_id": "intent-element-014-001",
                "specification_element_id": "req-014-001",
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
    try:
        module = importlib.import_module(AUTHORIZATION_MODULE)
    except ModuleNotFoundError:
        pytest.fail(
            "RED: SES-014 execution authorization seam is intentionally absent; "
            f"expected {AUTHORIZATION_MODULE}.{AUTHORIZER_NAME}"
        )
    authorize = getattr(module, AUTHORIZER_NAME, None)
    if not callable(authorize):
        pytest.fail(
            f"RED: expected callable {AUTHORIZATION_MODULE}.{AUTHORIZER_NAME}"
        )
    return authorize


def test_pending_human_approval_cannot_authorize_execution():
    plan = _transformer()(_valid_specification())

    assert plan["status"] == "READY_FOR_APPROVAL"
    assert plan["approval"]["required"] is True
    assert plan["approval"]["status"] == "PENDING"

    authorize = _authorizer()

    with pytest.raises((PermissionError, ValueError)):
        authorize(plan, human_approval=None)
