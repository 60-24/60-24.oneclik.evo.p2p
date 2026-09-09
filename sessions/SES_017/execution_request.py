"""SES-017 — explicit Execution Authorization -> Execution Request seam.

This module creates an execution request only. It does not execute any
BuildPlan step and performs no external side effects.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any


def create_execution_request(authorized_plan: dict[str, Any]) -> dict[str, Any]:
    """Create an explicit request from an authorized BuildPlan without execution."""
    if not isinstance(authorized_plan, dict):
        raise TypeError("Authorized BuildPlan must be a mapping")

    authorization = authorized_plan.get("execution_authorization")
    if not isinstance(authorization, dict):
        raise PermissionError("Execution authorization is required")
    if authorization.get("status") != "AUTHORIZED":
        raise PermissionError("BuildPlan is not execution-authorized")

    build_plan_id = authorized_plan.get("build_plan_id")
    if not build_plan_id:
        raise ValueError("BuildPlan must have a build_plan_id")

    return {
        "status": "REQUESTED",
        "source": "EXECUTION_AUTHORIZATION",
        "build_plan_id": build_plan_id,
        "execution_authorization_status": authorization["status"],
        "plan": deepcopy(authorized_plan),
    }
