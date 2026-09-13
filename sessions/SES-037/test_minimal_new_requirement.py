"""SES-037 minimal post-Beta requirement proof."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _load(name: str, relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_minimal_new_requirement_creates_exact_requested_artifact(tmp_path: Path):
    entrypoint = _load("system_builder_entrypoint", "src/system_builder/entrypoint.py")

    requested_text = "Hello Beta Extension"
    raw_intent = {
        "version": 1,
        "objective": "Create one text artifact containing the requested text",
        "requirements": [requested_text],
        "constraints": ["local only"],
        "assumptions": [],
        "optional_information": [],
        "open_questions": [],
        "protected_decisions": [],
        "authority": "human",
    }

    result = entrypoint.run_system_builder(
        raw_intent,
        human_approval=None,
        output_dir=tmp_path,
    )

    assert result["status"] == "DELIVERED"
    assert len(result["artifact_ids"]) == 1
    artifact = next(tmp_path.glob("*.txt"))
    assert artifact.read_text(encoding="utf-8") == requested_text + "\n"
