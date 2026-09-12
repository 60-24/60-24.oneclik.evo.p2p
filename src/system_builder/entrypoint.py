"""Production System Builder entrypoint over the verified contracts."""
from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]


def _load(name: str, relative_path: str):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {relative_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


intent = _load("ses007_intent", "sessions/SES-007/intent_envelope.py")
specification = _load("ses008_specification", "sessions/SES-008/specification.py")
build_plan = _load("ses011_build_plan", "sessions/SES-011/build_plan.py")
authorization = _load("ses014_authorization", "sessions/SES-014/execution_authorization.py")
validated_authorization = _load(
    "validated_execution_authorization", "src/system_builder/validated_execution_authorization.py"
)
execution_request = _load("ses017_request", "sessions/SES_017/execution_request.py")
execution_dispatch = _load("ses018_dispatch", "sessions/SES-018/execution_dispatch.py")
execution_result = _load("ses019_result", "sessions/SES-019/execution_result.py")
execution_effect = _load("ses021_effect", "sessions/SES-021/execution_effect.py")
verification = _load("ses030_verification", "sessions/SES-030/execution_effect_verification.py")
delivery = _load("ses031_delivery", "sessions/SES-031/delivery.py")
local_executor = _load("local_executor", "src/execution/local_executor.py")
execution_observation = _load("execution_observation", "src/execution/execution_observation.py")


def _authorize(plan: dict[str, Any], human_approval: dict[str, Any] | None) -> dict[str, Any]:
    if plan.get("status") == "VALIDATED":
        return validated_authorization.authorize_validated_build_plan(plan)
    return authorization.authorize_build_plan(plan, human_approval)


def run_system_builder(
    raw_intent: dict[str, Any],
    human_approval: dict[str, Any] | None,
    output_dir: Path,
) -> dict[str, Any]:
    """Run one explicit Intent through planning, authorization, execution and delivery."""
    validated = intent.validate(raw_intent)
    spec = specification.build_specification(validated)
    plan = build_plan.transform_specification_to_build_plan(spec)
    authorized = _authorize(plan, human_approval)

    request = execution_request.create_execution_request(authorized)
    attempt = execution_dispatch.create_execution_attempt(request)
    execution = local_executor.execute_build_plan(authorized, output_dir)
    result = execution_result.create_execution_result(attempt, "SUCCEEDED")

    first_artifact = execution["artifacts"][0]
    effect_id = f"EFFECT-{first_artifact['artifact_id']}"
    effect = execution_effect.create_execution_effect(
        result,
        effect_id,
        {
            "status": "AUTHORIZED",
            "build_plan_id": plan["build_plan_id"],
            "source": authorized["execution_authorization"]["source"],
        },
    )

    observed = execution_observation.observe_execution_artifact(
        {
            "execution_effect_id": effect["execution_effect_id"],
            "execution_attempt_id": attempt["execution_attempt_id"],
            "build_plan_id": plan["build_plan_id"],
            "artifact_id": first_artifact["artifact_id"],
            "path": first_artifact["path"],
        }
    )
    if observed["evidence"]["status"] != "EVIDENCE_READY":
        raise RuntimeError("execution artifact evidence is not ready")

    verified = verification.verify_execution_effect(effect)
    return delivery.create_delivery_manifest(
        verified, [item["artifact_id"] for item in execution["artifacts"]]
    )
