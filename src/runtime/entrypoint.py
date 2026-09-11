"""Canonical minimal bounded runtime entry point."""


def start_runtime(runtime_input):
    """Validate explicit input and return a deterministic runtime-start record."""
    if not isinstance(runtime_input, dict):
        raise ValueError("runtime_input must be a dict")

    runtime_id = runtime_input.get("runtime_id")
    if not isinstance(runtime_id, str) or not runtime_id:
        raise ValueError("runtime_id must be a non-empty string")

    return {
        "status": "STARTED",
        "runtime_id": runtime_id,
        "source": "EXPLICIT_INPUT",
    }
