import importlib

import pytest


def test_runtime_flow_rejects_invalid_input_before_observation():
    module = importlib.import_module("src.runtime.flow")

    with pytest.raises(ValueError):
        module.run_runtime_flow({})
