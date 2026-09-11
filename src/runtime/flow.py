"""Canonical minimal integration of the runtime boundaries."""

from src.runtime.entrypoint import start_runtime
from src.runtime.observation import observe_runtime


def run_runtime_flow(runtime_input):
    """Run explicit input through the established start and observation boundaries."""
    started = start_runtime(runtime_input)
    runtime_state = {
        "runtime_id": started["runtime_id"],
        "runtime_status": started["status"],
    }
    return observe_runtime(runtime_state)
