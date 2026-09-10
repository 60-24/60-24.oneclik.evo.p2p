"""SES-022 — RED contract for preserving human authorization provenance."""

import importlib.util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).with_name("execution_effect_provenance.py")

VALID_EFFECT = {
    "status": "EXECUTION_EFFECT",
    "source": "EXECUTION_RESULT",
    "execution_effect_id": "effect-022-001",
    "execution_attempt_id": "attempt-022-001",
    "build_plan_id": "plan-022-001",
    "outcome": "SUCCEEDED",
}

VALID_EXECUTION_AUTHORIZATION = {
    "status": "AUTHORIZED",
    "source": "EXPLICIT_HUMAN_APPROVAL",
    "build_plan_id": "plan-022-001",
}


def _binder():
    spec = importlib.util.spec_from_file_location("ses022_execution_effect_provenance", MODULE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.bind_execution_effect_provenance


def test_effect_provenance_requires_execution_authorization():
    with pytest.raises(PermissionError):
        _binder()(VALID_EFFECT, None)


def test_effect_provenance_preserves_explicit_human_authorization():
    effect = _binder()(VALID_EFFECT, VALID_EXECUTION_AUTHORIZATION)

    assert effect["authorization_source"] == "EXPLICIT_HUMAN_APPROVAL"
    assert effect["build_plan_id"] == VALID_EFFECT["build_plan_id"]
