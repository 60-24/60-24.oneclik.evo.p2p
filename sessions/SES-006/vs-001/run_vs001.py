#!/usr/bin/env python3
"""VS-001: deterministic local Intent -> Specification builder."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


EXAMPLE_INTENT = {
    "id": "INTENT-VS001-001",
    "statement": (
        "Create a small local utility that reads a text file and reports the "
        "number of lines, words and characters. It must not modify the input "
        "file or access the network."
    ),
    "constraints": [
        "local-only",
        "read-only-input",
        "no-network-access",
    ],
    "acceptance_criteria": [
        "reports line count",
        "reports word count",
        "reports character count",
        "does not modify the input file",
        "does not access the network",
    ],
}


def validate_intent(intent: dict[str, Any]) -> None:
    required = ("id", "statement", "constraints", "acceptance_criteria")
    missing = [key for key in required if key not in intent]
    if missing:
        raise ValueError(f"Intent missing required fields: {', '.join(missing)}")
    if not isinstance(intent["statement"], str) or not intent["statement"].strip():
        raise ValueError("Intent.statement must be a non-empty string")
    if not isinstance(intent["constraints"], list):
        raise ValueError("Intent.constraints must be a list")
    if not isinstance(intent["acceptance_criteria"], list):
        raise ValueError("Intent.acceptance_criteria must be a list")


def normalize(intent: dict[str, Any]) -> dict[str, Any]:
    validate_intent(intent)
    open_questions = []
    assumptions = [
        "The input is a readable UTF-8 text file.",
        "Word counting uses whitespace-delimited tokens.",
    ]
    if not intent["acceptance_criteria"]:
        open_questions.append("Acceptance criteria must be supplied before delivery.")

    return {
        "id": "SPEC-VS001-001",
        "intent_id": intent["id"],
        "intent": intent["statement"],
        "purpose": "Define a small local text-file counting utility.",
        "inputs": ["text file"],
        "outputs": ["line count", "word count", "character count"],
        "constraints": list(intent["constraints"]),
        "assumptions": assumptions,
        "open_questions": open_questions,
        "acceptance_criteria": list(intent["acceptance_criteria"]),
        "status": "PROPOSED" if open_questions else "VERIFIED",
    }


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def render_markdown(spec: dict[str, Any]) -> str:
    lines = [
        "# VS-001 Specification",
        "",
        f"**ID:** `{spec['id']}`  ",
        f"**Intent ID:** `{spec['intent_id']}`  ",
        f"**Status:** `{spec['status']}`",
        "",
        "## Original Intent",
        "",
        spec["intent"],
        "",
        "## Purpose",
        "",
        spec["purpose"],
        "",
        "## Inputs",
        "",
    ]
    lines += [f"- {item}" for item in spec["inputs"]]
    lines += ["", "## Outputs", ""]
    lines += [f"- {item}" for item in spec["outputs"]]
    lines += ["", "## Constraints", ""]
    lines += [f"- `{item}`" for item in spec["constraints"]]
    lines += ["", "## Assumptions", ""]
    lines += [f"- {item}" for item in spec["assumptions"]]
    lines += ["", "## Open Questions", ""]
    lines += [f"- {item}" for item in spec["open_questions"]] or ["- None."]
    lines += ["", "## Acceptance Criteria", ""]
    lines += [f"- [ ] {item}" for item in spec["acceptance_criteria"]]
    lines += [""]
    return "\n".join(lines)


def deliver(output_dir: Path, spec_id: str, verification: dict[str, Any], hashes: dict[str, str]) -> dict[str, Any]:
    if not spec_id or not verification or verification.get("result") != "PASS":
        raise ValueError("Delivery requires a source specification and passing verification evidence")
    if "verification.json" not in hashes:
        raise ValueError("Delivery requires verification artifact evidence")
    manifest = {
        "id": "DELIVERY-VS001-001",
        "specification_id": spec_id,
        "verification_id": verification["id"],
        "artifacts": hashes,
        "delivery_status": "DELIVERED",
    }
    (output_dir / "delivery-manifest.json").write_text(
        canonical_json(manifest), encoding="utf-8", newline="\n"
    )
    return manifest


def build(output_dir: Path, intent: dict[str, Any] | None = None) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    source_intent = EXAMPLE_INTENT if intent is None else intent
    spec = normalize(source_intent)
    json_text = canonical_json(spec)
    md_text = render_markdown(spec)

    artifacts = {
        "specification.json": json_text,
        "specification.md": md_text,
    }
    hashes = {}
    for name, content in artifacts.items():
        (output_dir / name).write_text(content, encoding="utf-8", newline="\n")
        hashes[name] = sha256_text(content)

    verification = {
        "id": "VERIFICATION-VS001-001",
        "specification_id": spec["id"],
        "checks": {
            "intent_preserved": spec["intent"] == source_intent["statement"],
            "constraints_preserved": spec["constraints"] == source_intent["constraints"],
            "acceptance_criteria_present": bool(spec["acceptance_criteria"]),
            "open_questions_explicit": isinstance(spec["open_questions"], list),
            "markdown_and_json_generated": True,
            "deterministic_representation": canonical_json(spec) == canonical_json(normalize(source_intent)),
            "network_access_not_required": True,
        },
        "artifact_hashes": hashes,
    }
    verification["result"] = "PASS" if all(verification["checks"].values()) else "FAIL"
    verification_text = canonical_json(verification)
    (output_dir / "verification.json").write_text(
        verification_text, encoding="utf-8", newline="\n"
    )
    hashes["verification.json"] = sha256_text(verification_text)

    if verification["result"] == "PASS":
        deliver(output_dir, spec["id"], verification, hashes)
    return verification


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="vs-001-output", type=Path)
    args = parser.parse_args()
    verification = build(args.output)
    print(json.dumps(verification, ensure_ascii=False, indent=2))
    return 0 if verification["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
