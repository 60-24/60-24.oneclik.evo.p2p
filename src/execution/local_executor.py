"""Minimal real local executor for the System Builder Beta boundary."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


_ALLOWED_ACTIONS = {"create"}


def execute_build_plan(build_plan: dict[str, Any], output_dir: Path) -> dict[str, Any]:
    """Execute authorized BuildPlan steps as deterministic local artifacts.

    This is deliberately local-only. It performs a real filesystem side effect,
    while leaving remote execution and external transmission outside this boundary.
    """
    if not isinstance(build_plan, dict):
        raise TypeError("BuildPlan must be a mapping")
    if build_plan.get("approval", {}).get("status") != "APPROVED":
        raise PermissionError("approved BuildPlan required")
    if build_plan.get("status") != "READY_FOR_APPROVAL":
        raise PermissionError("BuildPlan must be READY_FOR_APPROVAL")

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
