"""SES-023 RED test: minimal bounded runtime entry point."""

import importlib
import pytest


def test_runtime_entrypoint_contract_exists_and_is_callable():
    module = importlib.import_module("sessions.SES_023.runtime_entrypoint")
    assert callable(module.start_runtime)


def test_valid_input_returns_bounded_started_record():
    module = importlib.import_module("sessions.SES_023.runtime_entrypoint")
    result = module.start_runtime({"runtime_id": "runtime-023-001"})
    assert result["status"] == "STARTED"
    assert result["runtime_id"] == "runtime-023-001"
    assert result["source"] == "EXPLICIT_INPUT"
    assert "executed" not in result
    assert "result" not in result


def test_invalid_input_fails_closed():
    module = importlib.import_module("sessions.SES_023.runtime_entrypoint")
    with pytest.raises(ValueError):
        module.start_runtime({})


def test_identical_input_is_deterministic():
    module = importlib.import_module("sessions.SES_023.runtime_entrypoint")
    first = module.start_runtime({"runtime_id": "runtime-023-001"})
    second = module.start_runtime({"runtime_id": "runtime-023-001"})
    assert first == second
