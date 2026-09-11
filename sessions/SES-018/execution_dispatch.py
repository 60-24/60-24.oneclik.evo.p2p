"""SES-018 — Execution Request -> Execution Attempt seam.

Dispatch creates an attempt record only. It does not execute any operation,
produce a result, or perform external side effects.
"""
from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from typing import Any


def _stable_attempt_id(execution_request: dict[str, Any]) -> str:
    payload = {
        "build_plan_id": execution_request["build_plan_id"],
        "source": execution_request["source"],
        "execution_authorization_status": execution_request["execution_authorization_status"],
    }
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]
    return f"ATTEMPT-{digest}"


def create_execution_attempt(execution_request: dict[str, Any]) -> dict[str, Any]:
    """Convert an authorized REQUESTED request into an execution attempt."""
    if not isinstance(execution_request, dict):
        raise TypeError("Execution request must be a mapping")

    if execution_request.get("status") != "REQUESTED":
        raise PermissionError("Execution request must be REQUESTED")

    if execution_request.get("source") != "EXECUTION_AUTHORIZATION":
        raise PermissionError("Execution request must originate from authorization")

    if execution_request.get("execution_authorization_status") != "AUTHORIZED":
        raise PermissionError("Execution request is not authorized")

    build_plan_id = execution_request.get("build_plan_id")
    plan = execution_request.get("plan")
    if not isinstance(plan, dict):
        raise PermissionError("Execution request must contain its BuildPlan")

    if not build_plan_id or plan.get("build_plan_id") != build_plan_id:
        raise PermissionError("Execution request and BuildPlan identity must match")

    return {
        "status": "EXECUTION_ATTEMPT",
        "source": "EXECUTION_REQUEST",
        "execution_attempt_id": _stable_attempt_id(execution_request),
        "build_plan_id": build_plan_id,
        "request_status": execution_request["status"],
        "request": deepcopy(execution_request),
    }
