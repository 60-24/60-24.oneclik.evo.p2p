"""Execution authorization for BuildPlans that explicitly require no human approval."""
from __future__ import annotations

from copy import deepcopy
from typing import Any


def authorize_validated_build_plan(plan: dict[str, Any]) -> dict[str, Any]:
    """Authorize execution only for a fully validated plan with no approval requirement.

    This does not approve anything and does not replace SES-014 human approval.
    Plans requiring approval must continue through the explicit human boundary.
    """
    if not isinstance(plan, dict):
        raise TypeError("BuildPlan must be a mapping")
    if plan.get("status") != "VALIDATED":
        raise ValueError("only VALIDATED BuildPlans can use no-approval authorization")

    approval = plan.get("approval")
    if not isinstance(approval, dict):
        raise ValueError("BuildPlan approval contract is missing")
    if approval.get("required") is not False:
        raise PermissionError("BuildPlan requires human approval")
    if approval.get("status") != "NOT_REQUIRED":
        raise ValueError("no-approval BuildPlan must have NOT_REQUIRED approval status")
    if plan.get("blockers"):
        raise PermissionError("blocked BuildPlan cannot be authorized")

    authorized = deepcopy(plan)
    authorized["execution_authorization"] = {
        "status": "AUTHORIZED",
        "source": "VALIDATED_NO_APPROVAL_REQUIRED",
    }
    return authorized
