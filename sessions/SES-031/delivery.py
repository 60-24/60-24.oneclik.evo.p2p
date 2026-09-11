"""SES-031 — minimal VERIFICATION -> DELIVERY boundary."""

from typing import Any


def create_delivery_manifest(
    verification: dict[str, Any], artifact_ids: list[str]
) -> dict[str, Any]:
    """Create an internal delivery manifest from verified evidence.

    DELIVERY here means a reproducible internal delivery package/manifest.
    It does not claim that an artifact was transmitted to an external system.
    """
    if not isinstance(verification, dict):
        raise PermissionError("verified execution evidence required")

    if verification.get("status") != "VERIFIED":
        raise PermissionError("only VERIFIED evidence may be delivered")

    if verification.get("source") != "EXECUTION_EFFECT":
        raise PermissionError("verification must originate from EXECUTION_EFFECT")

    if verification.get("verification_basis") != "CONTRACT_PROVENANCE":
        raise PermissionError("contract verification provenance required")

    if not verification.get("execution_effect_id"):
        raise PermissionError("execution effect verification identifier required")

    if not verification.get("execution_attempt_id"):
        raise PermissionError("execution attempt identifier required")

    if not verification.get("build_plan_id"):
        raise PermissionError("build plan identifier required")

    if not isinstance(artifact_ids, list) or not artifact_ids or any(
        not isinstance(item, str) or not item for item in artifact_ids
    ):
        raise PermissionError("at least one valid artifact identifier required")

    return {
        "status": "DELIVERED",
        "source": "VERIFICATION",
        "verification_id": verification["execution_effect_id"],
        "execution_attempt_id": verification["execution_attempt_id"],
        "build_plan_id": verification["build_plan_id"],
        "artifact_ids": list(artifact_ids),
        "delivery_basis": "VERIFICATION",
    }
