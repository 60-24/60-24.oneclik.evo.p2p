"""RED test for observing a real local execution artifact."""
from pathlib import Path

from src.execution.execution_observation import observe_execution_artifact


def test_observe_execution_artifact_produces_evidence_linked_to_effect(tmp_path):
    artifact = tmp_path / "ARTIFACT-demo.txt"
    artifact.write_text("target: create the artifact\n", encoding="utf-8")

    observed = observe_execution_artifact(
        {
            "execution_effect_id": "effect-1",
            "execution_attempt_id": "attempt-1",
            "build_plan_id": "plan-1",
            "artifact_id": "artifact-1",
            "path": str(artifact),
        }
    )

    assert observed == {
        "status": "OBSERVED",
        "source": "LOCAL_EXECUTION_ARTIFACT",
        "execution_effect_id": "effect-1",
        "execution_attempt_id": "attempt-1",
        "build_plan_id": "plan-1",
        "artifact_id": "artifact-1",
        "path": str(artifact),
        "exists": True,
        "evidence": {
            "status": "EVIDENCE_READY",
            "artifact_id": "artifact-1",
            "execution_effect_id": "effect-1",
            "path": str(artifact),
        },
    }
