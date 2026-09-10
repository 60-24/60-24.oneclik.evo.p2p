"""SES-022 — RED contract for execution-effect authorization provenance."""

import importlib.util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).with_name("execution_effect.py")

VALID_RESULT = {
    "status": "EXECUTION_RESULT",
    "source": "EXECUTION_ATTEMPT",
    "execution_attempt_id": "attempt-022-001",
    "build_plan_id": "plan-022-001",
    "outcome": "SUCCEEDED",
}

VALID_EXECUTION_AUTHORIZATION = {
    "status": "AUTHORIZED",
    "source": "EXPLICIT_HUMAN_APPROVAL",
    "build_plan_id": "plan-022-001",
}


def _factory():
    spec = importlib.util.spec_from_file_location("ses022_execution_effect", MODULE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.create_execution_effect


def test_effect_authorization_must_have_execution_authorization_provenance():
    with pytest.raises(PermissionError):
        _factory()(
            VALID_RESULT,
            execution_effect_id="effect-022-001",
            effect_authorization={
                "status": "AUTHORIZED",
                "build_plan_id": "plan-022-001",
            },
            execution_authorization=None,
        )


def test_effect_authorization_must_preserve_explicit_human_authorization():
    effect = _factory()(
        VALID_RESULT,
        execution_effect_id="effect-022-002",
        effect_authorization={
            "status": "AUTHORIZED",
            "build_plan_id": "plan-022-001",
        },
        execution_authorization=VALID_EXECUTION_AUTHORIZATION,
    )

    assert effect["authorization_source"] == "EXPLICIT_HUMAN_APPROVAL"
