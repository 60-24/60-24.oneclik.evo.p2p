"""SES-030 — minimal EXECUTION_EFFECT -> VERIFICATION contract."""

import importlib.util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).with_name("execution_effect_verification.py")

VALID_EFFECT = {
    "status": "EXECUTION_EFFECT",
    "source": "EXECUTION_RESULT",
    "execution_effect_id": "effect-030-001",
    "execution_attempt_id": "attempt-030-001",
    "build_plan_id": "plan-030-001",
    "outcome": "SUCCEEDED",
    "authorization_source": "EXPLICIT_HUMAN_APPROVAL",
}


def _verifier():
    spec = importlib.util.spec_from_file_location("ses030_execution_effect_verification", MODULE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.verify_execution_effect


def test_verification_accepts_only_a_provenanced_succeeded_effect():
    verification = _verifier()(VALID_EFFECT)

    assert verification == {
        "status": "VERIFIED",
        "source": "EXECUTION_EFFECT",
        "execution_effect_id": "effect-030-001",
        "execution_attempt_id": "attempt-030-001",
        "build_plan_id": "plan-030-001",
        "verification_basis": "CONTRACT_PROVENANCE",
    }


def test_verification_fails_closed_for_missing_provenance():
    effect = dict(VALID_EFFECT)
    effect.pop("authorization_source")

    with pytest.raises(PermissionError):
        _verifier()(effect)


def test_verification_fails_closed_for_failed_effect():
    effect = dict(VALID_EFFECT)
    effect["outcome"] = "FAILED"

    with pytest.raises(PermissionError):
        _verifier()(effect)
