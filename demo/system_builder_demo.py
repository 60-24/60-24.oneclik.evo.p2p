"""Small real System Builder demonstration program.

It exercises the production System Builder entrypoint with one deterministic
example and prints the resulting delivery manifest and artifact contents.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_entrypoint():
    path = ROOT / "src" / "system_builder" / "entrypoint.py"
    spec = importlib.util.spec_from_file_location("system_builder_entrypoint", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description="System Builder — real minimal demo")
    parser.add_argument(
        "--text",
        default="Hello Beta Extension",
        help="text to request in the generated artifact",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("demo-output"),
        help="directory for the generated artifact",
    )
    args = parser.parse_args()

    print("System Builder — Demo")
    print("=" * 24)
    print("Example request:")
    print(f'  Create one text artifact containing: {args.text!r}')
    print()
    print("Real flow:")
    print("  INTENT → SPECIFICATION → BUILD PLAN → AUTHORIZATION")
    print("  → REQUEST → ATTEMPT → EXECUTION → RESULT → EFFECT")
    print("  → OBSERVATION → VERIFICATION → DELIVERY")
    print()

    raw_intent = {
        "version": 1,
        "objective": "Create one text artifact containing the requested text",
        "requirements": [args.text],
        "constraints": ["local only"],
        "assumptions": [],
        "optional_information": [],
        "open_questions": [],
        "protected_decisions": [],
        "authority": "human",
    }

    entrypoint = _load_entrypoint()
    result = entrypoint.run_system_builder(
        raw_intent,
        human_approval=None,
        output_dir=args.output,
    )

    artifact_id = result["artifact_ids"][0]
    artifact = next(args.output.glob(f"{artifact_id}.txt"))

    print("RESULT")
    print(f"  status: {result['status']}")
    print(f"  verification: {result['verification_id']}")
    print(f"  build_plan: {result['build_plan_id']}")
    print(f"  artifact: {artifact}")
    print()
    print("ARTIFACT CONTENT")
    print(artifact.read_text(encoding="utf-8"), end="")
    print()
    print("Demo completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
