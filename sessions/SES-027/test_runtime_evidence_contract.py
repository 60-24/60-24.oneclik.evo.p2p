import importlib


def test_runtime_flow_produces_deterministic_evidence_ready_record():
    module = importlib.import_module("src.runtime.flow")

    runtime_input = {"runtime_id": "runtime-027-001"}

    first = module.run_runtime_flow(runtime_input)
    second = module.run_runtime_flow(runtime_input)

    assert first == {
        "status": "OBSERVED",
        "runtime_id": "runtime-027-001",
        "runtime_status": "STARTED",
        "source": "RUNTIME_STATE",
    }
    assert second == first
