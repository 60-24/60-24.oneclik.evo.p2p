"""SES-024 RED test: minimal runtime observation contract."""

import importlib


def test_runtime_observation_contract_exists_and_is_callable():
    module = importlib.import_module("sessions.SES_024.runtime_observation")
    assert callable(module.observe_runtime)


def test_started_runtime_produces_evidence_ready_observation():
    module = importlib.import_module("sessions.SES_024.runtime_observation")
    result = module.observe_runtime({"runtime_id": "runtime-023-001", "status": "STARTED"})
    assert result == {
        "status": "OBSERVED",
        "runtime_id": "runtime-023-001",
        "runtime_status": "STARTED",
        "source": "RUNTIME_STATE",
    }


def test_observation_contains_no_execution_or_real_result():
    module = importlib.import_module("sessions.SES_024.runtime_observation")
    result = module.observe_runtime({"runtime_id": "runtime-023-001", "status": "STARTED"})
    assert "executed" not in result
    assert "result" not in result


def test_identical_runtime_state_is_deterministic():
    module = importlib.import_module("sessions.SES_024.runtime_observation")
    state = {"runtime_id": "runtime-023-001", "status": "STARTED"}
    assert module.observe_runtime(state) == module.observe_runtime(state)
