"""SES-025 minimal integration of the established runtime boundaries."""

from sessions.SES_023.runtime_entrypoint import start_runtime
from sessions.SES_024.runtime_observation import observe_runtime


def run_runtime_flow(runtime_input):
    """Run explicit input through the existing start and observation boundaries."""
    started = start_runtime(runtime_input)
    runtime_state = {
        "runtime_id": started["runtime_id"],
        "runtime_status": started["status"],
    }
    return observe_runtime(runtime_state)
