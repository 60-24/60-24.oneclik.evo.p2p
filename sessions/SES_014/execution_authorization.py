"""SES-014 — explicit Human Approval -> Execution authorization boundary.

This module authorizes a BuildPlan only from an explicit human approval
record. It does not execute any step or perform external side effects.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any


def authorize_build_plan(
    plan: dict[str, Any], human_approval: dict[str, Any] | None
) -> dict[str, Any]:
    """Return an execution-authorized plan only after explicit human approval."""
    if not isinstance(plan, dict):
        raise TypeError("BuildPlan must be a mapping")
    if plan.get("status") != "READY_FOR_APPROVAL":
        raise ValueError("BuildPlan is not awaiting human approval")

    approval = plan.get("approval")
    if not isinstance(approval, dict) or approval.get("required") is not True:
        raise ValueError("BuildPlan does not require human approval")
    if human_approval is None:
        raise PermissionError("Explicit human approval is required")
    if not isinstance(human_approval, dict) or human_approval.get("approved") is not True:
        raise PermissionError("Explicit human approval was not granted")

    authorized = deepcopy(plan)
    authorized["approval"] = {
        **approval,
        "status": "APPROVED",
        "authority_scope": human_approval.get(
            "authority_scope", approval.get("authority_scope")
        ),
    }
    authorized["execution_authorization"] = {
        "status": "AUTHORIZED",
        "source": "EXPLICIT_HUMAN_APPROVAL",
    }
    return authorized
