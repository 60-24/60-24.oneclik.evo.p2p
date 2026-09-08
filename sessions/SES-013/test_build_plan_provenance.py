"""SES-013 TDD test: mandatory provenance must fail closed."""

from sessions.SES_011.build_plan import transform_specification_to_build_plan


def _specification_without_provenance():
    return {
        "specification_id": "spec-013-provenance-gap",
        "status": "VALID",
        "objective": {"statement": "Build the requested system", "origin": "DERIVED"},
        "requirements": [{"id": "req-001", "statement": "Create the requested component", "origin": "DERIVED"}],
        "constraints": [], "inputs": [], "outputs": [], "acceptance_criteria": [],
        "assumptions": [], "unresolved_decisions": [], "provenance": [],
        "authority": {"scope": "human-approved"},
    }


def test_missing_mandatory_provenance_blocks_plan():
    """SES-010 §5/§7: missing mandatory provenance must fail closed."""
    plan = transform_specification_to_build_plan(_specification_without_provenance())
    assert plan["status"] == "BLOCKED"
    assert any(blocker.get("type") == "MISSING_PROVENANCE" for blocker in plan["blockers"])
    assert plan["approval"]["status"] != "APPROVED"
