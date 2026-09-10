"""SES-021 — TDD RED contract for effect-authorization plan binding."""

import importlib.util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).with_name("execution_effect.py")

VALID_RESULT = {
    "status": "EXECUTION_RESULT",
    "source": "EXECUTION_ATTEMPT",
    "execution_attempt_id": "attempt-021-001",
    "build_plan_id": "plan-021-001",
    "outcome": "SUCCEEDED",
}


def _factory():
    spec = importlib.util.spec_from_file_location("ses021_execution_effect", MODULE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.create_execution_effect


def test_effect_authorization_must_bind_to_same_build_plan():
    with pytest.raises(PermissionError):
        _factory()(
            VALID_RESULT,
            execution_effect_id="effect-021-001",
            effect_authorization={
                "status": "AUTHORIZED",
                "build_plan_id": "different-plan",
            },
        )


def test_effect_authorization_with_matching_build_plan_is_accepted():
    effect = _factory()(
        VALID_RESULT,
        execution_effect_id="effect-021-002",
        effect_authorization={
            "status": "AUTHORIZED",
            "build_plan_id": "plan-021-001",
        },
    )

    assert effect["build_plan_id"] == VALID_RESULT["build_plan_id"]
