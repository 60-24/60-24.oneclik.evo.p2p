"""SES-018 — TDD contract for Execution Request -> Execution Attempt.

The implementation is loaded from the canonical SES-018 session folder.
This contract defines the dispatch seam without performing execution.
"""

import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("execution_dispatch.py")
FACTORY = "create_execution_attempt"


def _factory():
    spec = importlib.util.spec_from_file_location("ses018_execution_dispatch", MODULE_PATH)
    assert spec is not None and spec.loader is not None, "RED: execution-dispatch seam is unavailable"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    factory = getattr(module, FACTORY, None)
    assert callable(factory), "RED: execution-dispatch seam is unavailable"
    return factory


def _request():
    return {
        "status": "REQUESTED",
        "source": "EXECUTION_AUTHORIZATION",
        "build_plan_id": "plan-018-001",
        "execution_authorization_status": "AUTHORIZED",
        "plan": {
            "build_plan_id": "plan-018-001",
            "status": "READY_FOR_APPROVAL",
            "approval": {"required": True, "status": "APPROVED"},
            "execution_authorization": {
                "status": "AUTHORIZED",
                "source": "EXPLICIT_HUMAN_APPROVAL",
            },
            "steps": [
                {"id": "step-018-001", "action": "NO_SIDE_EFFECT"},
            ],
        },
    }


def test_execution_dispatch_seam_exists_and_exposes_attempt_factory():
    """A requested execution must have an explicit dispatch/attempt seam."""
    _factory()


def test_execution_request_becomes_attempt_without_becoming_executed():
    """Dispatch creates an attempt record, not an execution result or side effect."""
    create_execution_attempt = _factory()

    attempt = create_execution_attempt(_request())

    assert attempt["status"] == "EXECUTION_ATTEMPT"
    assert attempt["source"] == "EXECUTION_REQUEST"
    assert attempt["build_plan_id"] == "plan-018-001"
    assert attempt["request_status"] == "REQUESTED"
    assert "executed" not in attempt
    assert "result" not in attempt


def test_dispatch_does_not_bypass_authorization_or_plan_identity():
    """Dispatch must reject malformed requests instead of authorizing implicitly."""
    create_execution_attempt = _factory()

    unauthorized = _request()
    unauthorized["execution_authorization_status"] = "NOT_AUTHORIZED"

    mismatched_plan = _request()
    mismatched_plan["plan"]["build_plan_id"] = "plan-018-DIFFERENT"

    import pytest

    with pytest.raises(PermissionError):
        create_execution_attempt(unauthorized)

    with pytest.raises(PermissionError):
        create_execution_attempt(mismatched_plan)
