"""SES-019 — minimal Execution Attempt -> Execution Result seam."""

from copy import deepcopy
from typing import Any


_ALLOWED_OUTCOMES = {"SUCCEEDED", "FAILED"}


def create_execution_result(execution_attempt: dict[str, Any], outcome: str) -> dict[str, Any]:
    """Create an explicit result from a valid execution attempt.

    This function records a result only; it performs no execution or side effects.
    """
    if not isinstance(execution_attempt, dict):
        raise PermissionError("valid EXECUTION_ATTEMPT required")

    if execution_attempt.get("status") != "EXECUTION_ATTEMPT":
        raise PermissionError("valid EXECUTION_ATTEMPT required")

    if not execution_attempt.get("execution_attempt_id"):
        raise PermissionError("execution_attempt_id required")

    if not execution_attempt.get("build_plan_id"):
        raise PermissionError("build_plan_id required")

    if outcome not in _ALLOWED_OUTCOMES:
        raise ValueError("outcome must be SUCCEEDED or FAILED")

    return {
        "status": "EXECUTION_RESULT",
        "source": "EXECUTION_ATTEMPT",
        "execution_attempt_id": execution_attempt["execution_attempt_id"],
        "build_plan_id": execution_attempt["build_plan_id"],
        "outcome": outcome,
    }
