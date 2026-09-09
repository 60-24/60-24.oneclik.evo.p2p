"""SES-017 — TDD contract for Authorization -> Execution Request.

The implementation is intentionally absent at the RED stage.
This test defines the boundary without executing any step or side effect.
"""

import importlib


MODULE = "sessions.SES_017.execution_request"
FACTORY = "create_execution_request"


def test_execution_request_seam_exists_and_exposes_factory():
    """An authorized plan must have an explicit, importable request seam."""
    module = importlib.import_module(MODULE)
    assert callable(getattr(module, FACTORY, None))


def test_execution_request_preserves_authorization_without_execution():
    """The request contract must represent intent to execute, not execution itself."""
    module = importlib.import_module(MODULE)
    create_execution_request = getattr(module, FACTORY)

    authorized_plan = {
        "build_plan_id": "plan-017-001",
        "status": "READY_FOR_APPROVAL",
        "approval": {"required": True},
        "execution_authorization": {
            "status": "AUTHORIZED",
            "source": "EXPLICIT_HUMAN_APPROVAL",
        },
        "steps": [
            {"id": "step-017-001", "action": "NO_SIDE_EFFECT"},
        ],
    }

    request = create_execution_request(authorized_plan)

    assert request["status"] == "REQUESTED"
    assert request["source"] == "EXECUTION_AUTHORIZATION"
    assert request["build_plan_id"] == "plan-017-001"
    assert request["execution_authorization_status"] == "AUTHORIZED"
    assert "executed" not in request
    assert "result" not in request
