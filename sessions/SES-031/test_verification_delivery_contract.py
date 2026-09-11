"""SES-031 — minimal VERIFICATION -> DELIVERY boundary tests."""

import pytest

from delivery import create_delivery_manifest


VALID_VERIFICATION = {
    "status": "VERIFIED",
    "source": "EXECUTION_EFFECT",
    "execution_effect_id": "effect-1",
    "execution_attempt_id": "attempt-1",
    "build_plan_id": "plan-1",
    "verification_basis": "CONTRACT_PROVENANCE",
}


def test_verified_execution_can_be_delivered_as_internal_manifest():
    delivery = create_delivery_manifest(VALID_VERIFICATION, ["artifact-1"])

    assert delivery["status"] == "DELIVERED"
    assert delivery["source"] == "VERIFICATION"
    assert delivery["verification_id"] == "effect-1"
    assert delivery["execution_attempt_id"] == "attempt-1"
    assert delivery["build_plan_id"] == "plan-1"
    assert delivery["artifact_ids"] == ["artifact-1"]
    assert delivery["delivery_basis"] == "VERIFICATION"


def test_delivery_fails_closed_without_verified_status():
    invalid = dict(VALID_VERIFICATION, status="PENDING")

    with pytest.raises(PermissionError):
        create_delivery_manifest(invalid, ["artifact-1"])


def test_delivery_fails_closed_without_verification_provenance():
    invalid = dict(VALID_VERIFICATION)
    invalid.pop("verification_basis")

    with pytest.raises(PermissionError):
        create_delivery_manifest(invalid, ["artifact-1"])


def test_delivery_requires_at_least_one_artifact():
    with pytest.raises(PermissionError):
        create_delivery_manifest(VALID_VERIFICATION, [])
