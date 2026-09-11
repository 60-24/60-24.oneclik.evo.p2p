"""SES-021 — minimal Execution Result -> Execution Effect boundary."""

from typing import Any


def create_execution_effect(
    execution_result: dict[str, Any],
    execution_effect_id: str,
    effect_authorization: dict[str, Any],
) -> dict[str, Any]:
    """Record an explicitly authorized effect without performing the effect."""
    if not isinstance(execution_result, dict):
        raise PermissionError("valid EXECUTION_RESULT required")

    if execution_result.get("status") != "EXECUTION_RESULT":
        raise PermissionError("valid EXECUTION_RESULT required")

    if execution_result.get("source") != "EXECUTION_ATTEMPT":
        raise PermissionError("execution result must originate from an attempt")

    if not execution_result.get("execution_attempt_id"):
        raise PermissionError("execution_attempt_id required")

    if not execution_result.get("build_plan_id"):
        raise PermissionError("build_plan_id required")

    if execution_result.get("outcome") != "SUCCEEDED":
        raise PermissionError("only a succeeded result may record an execution effect")

    if not execution_effect_id:
        raise PermissionError("execution_effect_id required")

    if not isinstance(effect_authorization, dict):
        raise PermissionError("effect authorization required")

    if effect_authorization.get("status") != "AUTHORIZED":
        raise PermissionError("execution effect is not authorized")

    if effect_authorization.get("build_plan_id") != execution_result.get("build_plan_id"):
        raise PermissionError("effect authorization must bind to the same build plan")

    effect = {
        "status": "EXECUTION_EFFECT",
        "source": "EXECUTION_RESULT",
        "execution_effect_id": execution_effect_id,
        "execution_attempt_id": execution_result["execution_attempt_id"],
        "build_plan_id": execution_result["build_plan_id"],
        "outcome": execution_result["outcome"],
    }

    authorization_source = effect_authorization.get("source")
    if authorization_source:
        effect["authorization_source"] = authorization_source

    return effect
