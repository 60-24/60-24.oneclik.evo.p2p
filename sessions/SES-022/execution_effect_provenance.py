"""SES-022 — minimal execution-effect authorization provenance boundary."""

from typing import Any


def bind_execution_effect_provenance(
    execution_effect: dict[str, Any],
    execution_authorization: dict[str, Any] | None,
) -> dict[str, Any]:
    """Bind an effect record to its explicit human authorization provenance."""
    if not isinstance(execution_effect, dict):
        raise PermissionError("valid EXECUTION_EFFECT required")

    if execution_effect.get("status") != "EXECUTION_EFFECT":
        raise PermissionError("valid EXECUTION_EFFECT required")

    if not isinstance(execution_authorization, dict):
        raise PermissionError("execution authorization provenance required")

    if execution_authorization.get("status") != "AUTHORIZED":
        raise PermissionError("execution authorization must be authorized")

    if execution_authorization.get("source") != "EXPLICIT_HUMAN_APPROVAL":
        raise PermissionError("execution authorization must originate from explicit human approval")

    if execution_authorization.get("build_plan_id") != execution_effect.get("build_plan_id"):
        raise PermissionError("authorization provenance must bind to the same build plan")

    return {
        **execution_effect,
        "authorization_source": execution_authorization["source"],
    }
