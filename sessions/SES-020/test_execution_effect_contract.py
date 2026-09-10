"""SES-020 — TDD contract for Execution Result -> Execution Effect.

The contract defines the smallest explicit effect seam.
No real effect or side effect is permitted.
"""

import importlib.util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).with_name("execution_effect.py")
FACTORY = "create_execution_effect"


VALID_RESULT = {
    "status": "EXECUTION_RESULT",
    "source": "EXECUTION_ATTEMPT",
    "execution_attempt_id": "attempt-020-001",
    "build_plan_id": "plan-020-001",
    "outcome": "SUCCEEDED",
}

VALID_AUTHORIZATION = {"status": "AUTHORIZED"}


def _factory():
    spec = importlib.util.spec_from_file_location("ses020_execution_effect", MODULE_PATH)
    assert spec is not None and spec.loader is not None, "RED: execution-effect seam is unavailable"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    factory = getattr(module, FACTORY, None)
    assert callable(factory), "RED: execution-effect seam is unavailable"
    return factory


def test_execution_effect_seam_exists_and_is_callable():
    assert callable(_factory())


def test_succeeded_result_with_effect_authorization_creates_effect_record():
    effect = _factory()(
        VALID_RESULT,
        execution_effect_id="effect-020-001",
        effect_authorization=VALID_AUTHORIZATION,
    )

    assert effect["status"] == "EXECUTION_EFFECT"
    assert effect["source"] == "EXECUTION_RESULT"
    assert effect["execution_effect_id"] == "effect-020-001"
    assert effect["execution_attempt_id"] == "attempt-020-001"
    assert effect["build_plan_id"] == "plan-020-001"
    assert effect["outcome"] == "SUCCEEDED"


def test_result_without_effect_authorization_is_rejected():
    with pytest.raises(PermissionError):
        _factory()(
            VALID_RESULT,
            execution_effect_id="effect-020-002",
            effect_authorization={},
        )


def test_failed_result_cannot_become_execution_effect():
    failed_result = {**VALID_RESULT, "outcome": "FAILED"}

    with pytest.raises(PermissionError):
        _factory()(
            failed_result,
            execution_effect_id="effect-020-003",
            effect_authorization=VALID_AUTHORIZATION,
        )


def test_invalid_result_is_rejected():
    with pytest.raises(PermissionError):
        _factory()(
            {},
            execution_effect_id="effect-020-004",
            effect_authorization=VALID_AUTHORIZATION,
        )


def test_build_plan_identity_is_preserved():
    effect = _factory()(
        VALID_RESULT,
        execution_effect_id="effect-020-005",
        effect_authorization=VALID_AUTHORIZATION,
    )

    assert effect["build_plan_id"] == VALID_RESULT["build_plan_id"]


def test_empty_effect_id_is_rejected():
    with pytest.raises(PermissionError):
        _factory()(
            VALID_RESULT,
            execution_effect_id="",
            effect_authorization=VALID_AUTHORIZATION,
        )
