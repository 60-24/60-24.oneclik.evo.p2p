"""SES-024 minimal deterministic runtime observation."""


def observe_runtime(runtime_state):
    if not isinstance(runtime_state, dict):
        raise ValueError("runtime_state must be a dict")

    runtime_id = runtime_state.get("runtime_id")
    runtime_status = runtime_state.get("runtime_status")

    if not isinstance(runtime_id, str) or not runtime_id:
        raise ValueError("runtime_id must be a non-empty string")
    if runtime_status != "STARTED":
        raise ValueError("runtime_status must be STARTED")

    return {
        "status": "OBSERVED",
        "runtime_id": runtime_id,
        "runtime_status": "STARTED",
        "source": "RUNTIME_STATE",
    }
