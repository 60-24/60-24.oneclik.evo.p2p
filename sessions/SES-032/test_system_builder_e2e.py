"""SES-032 E2E: prove the existing System Builder chain can be composed."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


intent = load_module("ses007", ROOT / "sessions/SES-007/intent_envelope.py")
specification = load_module("ses008", ROOT / "sessions/SES-008/specification.py")
build_plan = load_module("ses011", ROOT / "sessions/SES-011/build_plan.py")


def test_existing_chain_reaches_build_plan_without_adapter_code():
    raw_intent = {
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

    validated = intent.validate(raw_intent)
    assert validated["status"] == "VALID"

    spec = specification.build_specification(validated)
    assert spec["status"] == "VALID"
    assert spec["source_intent_id"] == validated["intent_id"]

    plan = build_plan.transform_specification_to_build_plan(spec)
    assert plan["build_plan_id"]
    assert plan["source_specification_id"] == spec["specification_id"]
    assert plan["steps"]
