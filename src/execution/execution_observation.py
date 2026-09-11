"""Minimal observation of a real local execution artifact."""

from pathlib import Path
from typing import Any


def observe_execution_artifact(execution_artifact: dict[str, Any]) -> dict[str, Any]:
    """Observe a locally executed artifact and emit an evidence-ready record."""
    if not isinstance(execution_artifact, dict):
        raise ValueError("execution_artifact must be a dict")

    required = (
        "execution_effect_id",
        "execution_attempt_id",
        "build_plan_id",
        "artifact_id",
        "path",
    )
    for field in required:
        value = execution_artifact.get(field)
        if not isinstance(value, str) or not value:
            raise ValueError(f"{field} must be a non-empty string")

    path = Path(execution_artifact["path"])
    exists = path.is_file()

    return {
        "status": "OBSERVED",
        "source": "LOCAL_EXECUTION_ARTIFACT",
        "execution_effect_id": execution_artifact["execution_effect_id"],
        "execution_attempt_id": execution_artifact["execution_attempt_id"],
        "build_plan_id": execution_artifact["build_plan_id"],
        "artifact_id": execution_artifact["artifact_id"],
        "path": str(path),
        "exists": exists,
        "evidence": {
            "status": "EVIDENCE_READY" if exists else "EVIDENCE_NOT_READY",
            "artifact_id": execution_artifact["artifact_id"],
            "execution_effect_id": execution_artifact["execution_effect_id"],
            "path": str(path),
        },
    }
