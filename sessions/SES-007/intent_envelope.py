"""Deterministic SES-007 Intent Envelope validator."""
from __future__ import annotations

import hashlib
import json
import re
from typing import Any

CONTRACT_VERSION = 1
FIELDS = (
    "intent_id", "version", "objective", "requirements", "constraints",
    "assumptions", "optional_information", "open_questions",
    "protected_decisions", "authority", "status",
)
STATUSES = ("VALID", "INCOMPLETE", "AMBIGUOUS", "PROTECTED")
LIST_FIELDS = FIELDS[3:9]


def _text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value).strip())


def _items(values: Any) -> list[str]:
    if values is None:
        return []
    if not isinstance(values, list):
        raise ValueError("semantic list fields must be lists")
    return sorted({_text(v) for v in values if _text(v)})


def _canonical_without_id(raw: dict[str, Any]) -> dict[str, Any]:
    data = {k: raw.get(k) for k in FIELDS if k != "intent_id" and k != "status"}
    data["objective"] = _text(data.get("objective", ""))
    for field in LIST_FIELDS:
        data[field] = _items(data.get(field, []))
    data["version"] = int(data.get("version", CONTRACT_VERSION))
    return data


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def stable_id(prefix: str, value: Any) -> str:
    digest = hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()[:16]
    return f"{prefix}-{digest}"


def normalize(raw: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ValueError("Intent Envelope must be an object")
    data = _canonical_without_id(raw)
    data["intent_id"] = stable_id("INTENT", data)
    data["status"] = "VALID"
    return data


def validate(raw: dict[str, Any]) -> dict[str, Any]:
    envelope = normalize(raw)
    reasons: list[str] = []

    if not envelope["objective"]:
        reasons.append("objective is missing")
    if envelope["authority"] not in ("human", "system"):
        reasons.append("authority must be human or system")
    if envelope["protected_decisions"]:
        envelope["status"] = "PROTECTED"
        reasons.append("protected decision requires human approval")
    elif envelope["open_questions"]:
        ambiguous = any(
            any(token in q.lower() for token in ("either", "or", "alternative", "interpretation", "ambiguous"))
            for q in envelope["open_questions"]
        )
        envelope["status"] = "AMBIGUOUS" if ambiguous else "INCOMPLETE"
        reasons.extend(envelope["open_questions"])
    elif not envelope["objective"] or not envelope["requirements"]:
        envelope["status"] = "INCOMPLETE"
        reasons.append("material objective and at least one requirement are required")

    elements = []
    for field in ("requirements", "constraints", "assumptions", "optional_information", "open_questions", "protected_decisions"):
        for value in envelope[field]:
            elements.append({"field": field, "element_id": stable_id(f"{field.upper()}", value), "content": value})
    envelope["element_ids"] = elements
    envelope["validation"] = {"contract_version": CONTRACT_VERSION, "reasons": reasons}
    return envelope
