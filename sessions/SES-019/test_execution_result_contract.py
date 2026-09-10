"""SES-019 — TDD RED contract for Execution Attempt -> Execution Result.

The contract intentionally defines the smallest explicit result seam.
No real execution or side effects are permitted.
"""

import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("execution_result.py")
FACTORY = "create_execution_result"


def _factory():
    spec = importlib.util.spec_from_file_location("ses019_execution_result", MODULE_PATH)
    assert spec is not None and spec.loader is not None, "RED: execution-result seam is unavailable"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    factory = getattr(module, FACTORY, None)
    assert callable(factory), "RED: execution-result seam is unavailable"
    return factory


def _attempt():
    return {
        "status": "EXECUTION_ATTEMPT",
        "source": "EXECUTION_REQUEST",
        "execution_attempt_id": "attempt-019-001",
        "build_plan_id": "plan-019-001",
        "request_status": "REQUESTED",
    }


def test_execution_result_seam_exists_and_exposes_result_factory():
    """Execution Result must have its own explicit factory seam."""
    _factory()


def test_execution_attempt_produces_explicit_success_result():
    """A valid attempt may produce a result without being confused with execution."""
    create_execution_result = _factory()

    result = create_execution_result(_attempt(), "SUCCEEDED")

    assert result["status"] == "EXECUTION_RESULT"
    assert result["source"] == "EXECUTION_ATTEMPT"
    assert result["execution_attempt_id"] == "attempt-019-001"
    assert result["build_plan_id"] == "plan-019-001"
    assert result["outcome"] == "SUCCEEDED"


def test_execution_result_can_express_failure_explicitly():
    """Failure is a result state, not an absent or implicit result."""
    create_execution_result = _factory()

    result = create_execution_result(_attempt(), "FAILED")

    assert result["status"] == "EXECUTION_RESULT"
    assert result["source"] == "EXECUTION_ATTEMPT"
    assert result["outcome"] == "FAILED"


def test_execution_result_rejects_missing_or_invalid_attempt():
    """A result cannot be manufactured without a valid Execution Attempt."""
    create_execution_result = _factory()

    import pytest

    with pytest.raises(PermissionError):
        create_execution_result({}, "SUCCEEDED")

    invalid = _attempt()
    invalid["status"] = "EXECUTION_REQUEST"
    with pytest.raises(PermissionError):
        create_execution_result(invalid, "SUCCEEDED")


def test_execution_result_preserves_build_plan_identity():
    """The result must remain bound to the exact BuildPlan identity of the attempt."""
    create_execution_result = _factory()

    result = create_execution_result(_attempt(), "SUCCEEDED")

    assert result["build_plan_id"] == _attempt()["build_plan_id"]


def test_execution_result_rejects_unknown_outcome():
    """The minimal result contract must not accept an implicit/unknown outcome."""
    create_execution_result = _factory()

    import pytest

    with pytest.raises(ValueError):
        create_execution_result(_attempt(), "UNKNOWN")
