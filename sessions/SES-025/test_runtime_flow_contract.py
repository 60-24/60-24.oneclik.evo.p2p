import importlib


def test_runtime_flow_integrates_canonical_boundaries():
    module = importlib.import_module("src.runtime.flow")

    result = module.run_runtime_flow({"runtime_id": "runtime-025-001"})

    assert result["status"] == "OBSERVED"
    assert result["runtime_id"] == "runtime-025-001"
    assert result["runtime_status"] == "STARTED"
    assert result["source"] == "RUNTIME_STATE"
