"""Experimental validator for explicit Tagologia H↔S mapping records.

This validates mapping metadata only; it does not translate statements.
"""
from typing import Any

REQUIRED_FIELDS = {
    "h_concept_id",
    "h_revision",
    "s_term_id",
    "s_schema_version",
    "direction",
    "scope",
    "mapping_kind",
    "status",
}
ALLOWED_DIRECTIONS = {"H_TO_S", "S_TO_H", "BIDIRECTIONAL"}
ALLOWED_KINDS = {"exact", "narrower", "broader", "lossy"}
ALLOWED_STATUSES = {"mapped", "unmapped", "ambiguous"}


class MappingError(ValueError):
    """Raised when mapping metadata is incomplete or internally inconsistent."""


def validate_mapping(mapping: Any) -> dict[str, Any]:
    if not isinstance(mapping, dict):
        raise MappingError("invalid_type:mapping")
    missing = REQUIRED_FIELDS - mapping.keys()
    if missing:
        raise MappingError("missing_fields:" + ",".join(sorted(missing)))

    for field in ("h_concept_id", "h_revision", "direction", "scope", "mapping_kind", "status"):
        if not isinstance(mapping[field], str) or not mapping[field].strip():
            raise MappingError("invalid_field:" + field)

    if mapping["direction"] not in ALLOWED_DIRECTIONS:
        raise MappingError("invalid_direction")
    if mapping["mapping_kind"] not in ALLOWED_KINDS:
        raise MappingError("invalid_mapping_kind")
    if mapping["status"] not in ALLOWED_STATUSES:
        raise MappingError("invalid_status")

    target_id = mapping["s_term_id"]
    target_version = mapping["s_schema_version"]
    if mapping["status"] == "mapped":
        if not isinstance(target_id, str) or not target_id.strip():
            raise MappingError("mapped_target_required")
        if not isinstance(target_version, str) or not target_version.strip():
            raise MappingError("mapped_version_required")
    elif target_id is not None or target_version is not None:
        raise MappingError("unmapped_target_must_be_null")

    if mapping["status"] == "ambiguous" and mapping["mapping_kind"] == "exact":
        raise MappingError("ambiguous_cannot_be_exact")

    unknown = mapping.keys() - REQUIRED_FIELDS
    if unknown:
        raise MappingError("unknown_fields:" + ",".join(sorted(unknown)))

    return dict(mapping)
