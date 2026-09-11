"""SES-030 — minimal EXECUTION_EFFECT -> VERIFICATION boundary."""

from typing import Any


def verify_execution_effect(execution_effect: dict[str, Any]) -> dict[str, Any]:
    """Verify the contract provenance of a succeeded execution effect.

    This records contract verification only; it does not claim that an external
    side effect occurred in the real world.
    """
    if not isinstance(execution_effect, dict):
        raise PermissionError("valid EXECUTION_EFFECT required")

    if execution_effect.get("status") != "EXECUTION_EFFECT":
        raise PermissionError("valid EXECUTION_EFFECT required")

    if execution_effect.get("source") != "EXECUTION_RESULT":
        raise PermissionError("execution effect must originate from an execution result")

    if not execution_effect.get("execution_effect_id"):
        raise PermissionError("execution_effect_id required")

    if not execution_effect.get("execution_attempt_id"):
        raise PermissionError("execution_attempt_id required")

    if not execution_effect.get("build_plan_id"):
        raise PermissionError("build_plan_id required")

    if execution_effect.get("outcome") != "SUCCEEDED":
        raise PermissionError("only a succeeded execution effect may be verified")

    if execution_effect.get("authorization_source") != "EXPLICIT_HUMAN_APPROVAL":
        raise PermissionError("explicit human authorization provenance required")

    return {
        "status": "VERIFIED",
        "source": "EXECUTION_EFFECT",
        "execution_effect_id": execution_effect["execution_effect_id"],
        "execution_attempt_id": execution_effect["execution_attempt_id"],
        "build_plan_id": execution_effect["build_plan_id"],
        "verification_basis": "CONTRACT_PROVENANCE",
    }
