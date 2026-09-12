"""Minimal real local executor for the System Builder Beta boundary."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


_ALLOWED_ACTIONS = {"create"}


def _is_execution_authorized(build_plan: dict[str, Any]) -> bool:
    authorization = build_plan.get("execution_authorization")
    if not isinstance(authorization, dict) or authorization.get("status") != "AUTHORIZED":
        return False

    status = build_plan.get("status")
    approval = build_plan.get("approval")
    if not isinstance(approval, dict):
        return False

    # Existing SES-014 path: explicit human approval remains mandatory when required.
    if status == "READY_FOR_APPROVAL":
        return approval.get("status") == "APPROVED"

    # New SES-034 path: validated plans may execute only when approval is explicitly
    # not required. This is authorization, not approval.
    if status == "VALIDATED":
        return (
            approval.get("required") is False
            and approval.get("status") == "NOT_REQUIRED"
            and authorization.get("source") == "VALIDATED_NO_APPROVAL_REQUIRED"
        )

    return False


def execute_build_plan(build_plan: dict[str, Any], output_dir: Path) -> dict[str, Any]:
    """Execute an authorized BuildPlan as deterministic local artifacts.

    Authorization is checked independently from planning and approval. This is
    deliberately local-only and performs a real filesystem side effect.
    """
    if not isinstance(build_plan, dict):
        raise TypeError("BuildPlan must be a mapping")
    if not _is_execution_authorized(build_plan):
        raise PermissionError("execution-authorized BuildPlan required")

    steps = build_plan.get("steps")
    if not isinstance(steps, list) or not steps:
        raise PermissionError("BuildPlan must contain executable steps")

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    artifacts: list[dict[str, str]] = []

    for step in steps:
        if not isinstance(step, dict) or step.get("action") not in _ALLOWED_ACTIONS:
            raise PermissionError("unsupported execution action")
        target = step.get("target")
        step_id = step.get("id")
        if not isinstance(target, str) or not target:
            raise PermissionError("executable step target required")
        if not isinstance(step_id, str) or not step_id:
            raise PermissionError("executable step id required")

        artifact_id = "ARTIFACT-" + hashlib.sha256(
            json.dumps(
                {"build_plan_id": build_plan["build_plan_id"], "step_id": step_id, "target": target},
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()[:16]
        path = output_dir / f"{artifact_id}.txt"
        path.write_text(target + "\n", encoding="utf-8")
        artifacts.append({"artifact_id": artifact_id, "path": str(path), "step_id": step_id})

    return {
        "status": "EXECUTED",
        "build_plan_id": build_plan["build_plan_id"],
        "artifacts": artifacts,
    }
