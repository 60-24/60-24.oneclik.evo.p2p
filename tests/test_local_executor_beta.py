from pathlib import Path

import importlib.util


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "src/execution/local_executor.py"
spec = importlib.util.spec_from_file_location("local_executor", MODULE)
assert spec and spec.loader
local_executor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(local_executor)


def test_local_executor_performs_real_filesystem_effect(tmp_path):
    build_plan = {
        "build_plan_id": "BUILD-BETA-001",
        "status": "READY_FOR_APPROVAL",
        "approval": {"status": "APPROVED"},
        "steps": [
            {"id": "STEP-001", "action": "create", "target": "hello beta artifact"}
        ],
    }

    result = local_executor.execute_build_plan(build_plan, tmp_path)

    assert result["status"] == "EXECUTED"
    assert result["build_plan_id"] == "BUILD-BETA-001"
    assert len(result["artifacts"]) == 1
    artifact = result["artifacts"][0]
    artifact_path = Path(artifact["path"])
    assert artifact_path.exists()
    assert artifact_path.read_text(encoding="utf-8") == "hello beta artifact\n"


def test_local_executor_rejects_unapproved_plan(tmp_path):
    build_plan = {
        "build_plan_id": "BUILD-BETA-002",
        "status": "READY_FOR_APPROVAL",
        "approval": {"status": "PENDING"},
        "steps": [{"id": "STEP-001", "action": "create", "target": "blocked"}],
    }

    try:
        local_executor.execute_build_plan(build_plan, tmp_path)
    except PermissionError:
        pass
    else:
        raise AssertionError("unapproved BuildPlan must not execute")
