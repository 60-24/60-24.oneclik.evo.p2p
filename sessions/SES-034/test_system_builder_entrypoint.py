"""SES-034 RED test: one production entrypoint must compose the verified chain."""
from __future__ import annotations

from pathlib import Path


def _valid_raw_intent() -> dict[str, object]:
    return {
        "version": 1,
        "objective": "Create a minimal reproducible system artifact",
        "requirements": ["create the artifact"],
        "constraints": ["local only"],
        "assumptions": [],
        "optional_information": [],
        "open_questions": [],
        "protected_decisions": [],
        "authority": "human",
    }


def test_system_builder_entrypoint_composes_existing_verified_chain(tmp_path: Path):
    from src.system_builder.entrypoint import run_system_builder

    result = run_system_builder(
        _valid_raw_intent(),
        human_approval={
            "approved": True,
            "authority_scope": "human-approved",
        },
        output_dir=tmp_path,
    )

    assert result["status"] == "DELIVERED"
    assert result["source"] == "VERIFICATION"
    assert result["artifact_ids"]
    assert result["build_plan_id"]
