import pytest

from sessions.SES_020.execution_effect import create_execution_effect


VALID_RESULT = {
    "status": "EXECUTION_RESULT",
    "source": "EXECUTION_ATTEMPT",
    "execution_attempt_id": "attempt-020-001",
    "build_plan_id": "plan-020-001",
    "outcome": "SUCCEEDED",
}

VALID_AUTHORIZATION = {"status": "AUTHORIZED"}


def test_execution_effect_seam_exists_and_is_callable():
    assert callable(create_execution_effect)


def test_succeeded_result_with_effect_authorization_creates_effect_record():
    effect = create_execution_effect(
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
        create_execution_effect(
            VALID_RESULT,
            execution_effect_id="effect-020-002",
            effect_authorization={},
        )


def test_failed_result_cannot_become_execution_effect():
    failed_result = {**VALID_RESULT, "outcome": "FAILED"}

    with pytest.raises(PermissionError):
        create_execution_effect(
            failed_result,
            execution_effect_id="effect-020-003",
            effect_authorization=VALID_AUTHORIZATION,
        )


def test_invalid_result_is_rejected():
    with pytest.raises(PermissionError):
        create_execution_effect(
            {},
            execution_effect_id="effect-020-004",
            effect_authorization=VALID_AUTHORIZATION,
        )


def test_build_plan_identity_is_preserved():
    effect = create_execution_effect(
        VALID_RESULT,
        execution_effect_id="effect-020-005",
        effect_authorization=VALID_AUTHORIZATION,
    )

    assert effect["build_plan_id"] == VALID_RESULT["build_plan_id"]


def test_empty_effect_id_is_rejected():
    with pytest.raises(PermissionError):
        create_execution_effect(
            VALID_RESULT,
            execution_effect_id="",
            effect_authorization=VALID_AUTHORIZATION,
        )
