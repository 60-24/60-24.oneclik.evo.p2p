"""SES-024 contract test: minimal runtime observation."""

import importlib


def test_runtime_observation_contract_exists_and_is_callable():
    module = importlib.import_module("src.runtime.observation")
    assert callable(module.observe_runtime)


def test_started_runtime_produces_evidence_ready_observation():
    module = importlib.import_module("src.runtime.observation")
    result = module.observe_runtime(
        {"runtime_id": "runtime-023-001", "runtime_status": "STARTED"}
    )
    assert result == {
        "status": "OBSERVED",
        "runtime_id": "runtime-023-001",
        "runtime_status": "STARTED",
        "source": "RUNTIME_STATE",
    }


def test_invalid_runtime_state_fails_closed():
    module = importlib.import_module("src.runtime.observation")
    with __import__("pytest").raises(ValueError):
        module.observe_runtime({"runtime_id": "runtime-023-001"})


def test_identical_runtime_state_is_deterministic():
    module = importlib.import_module("src.runtime.observation")
    state = {"runtime_id": "runtime-023-001", "runtime_status": "STARTED"}
    assert module.observe_runtime(state) == module.observe_runtime(state)
