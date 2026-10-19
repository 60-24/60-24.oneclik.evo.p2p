"""Contract tests for the experimental Tagologia S validator.

Run from the repository root:
    python -m unittest discover -s experiments/tagologia_s -p 'test_*.py' -v
"""
import copy
import unittest

from validator import ContractError, canonical_json, validate_statement


def valid_statement():
    return {
        "schema": "urn:60-24:tagologia-s:resource-request",
        "version": "0.1",
        "kind": "resource.request",
        "statement_id": "urn:example:statement:001",
        "subject": {"type": "principal", "id": "principal:requester-7"},
        "resource": {"type": "resource", "id": "resource:report-17"},
        "requested_operations": ["read"],
        "constraints": {"copy": False},
        "references": [],
    }


class TagologiaSContractTests(unittest.TestCase):
    def test_valid_request_is_accepted_but_not_authorized(self):
        result = validate_statement(valid_statement())
        self.assertEqual(result["requested_operations"], ["read"])
        # Contract validation returns no authorization grant.
        self.assertNotIn("authorized", result)

    def test_canonical_json_is_deterministic_across_key_order(self):
        original = valid_statement()
        reversed_order = dict(reversed(list(original.items())))
        self.assertEqual(canonical_json(original), canonical_json(reversed_order))

    def test_missing_resource_id_is_rejected(self):
        item = valid_statement()
        item["resource"].pop("id")
        with self.assertRaisesRegex(ContractError, "missing_reference_id:resource"):
            validate_statement(item)

    def test_unsupported_version_is_rejected_without_guessing(self):
        item = valid_statement()
        item["version"] = "99.0"
        with self.assertRaisesRegex(ContractError, "unsupported_version"):
            validate_statement(item)

    def test_unknown_operation_is_rejected(self):
        item = valid_statement()
        item["requested_operations"] = ["read", "delete"]
        with self.assertRaisesRegex(ContractError, "unsupported_operation"):
            validate_statement(item)

    def test_unknown_top_level_field_is_rejected(self):
        item = valid_statement()
        item["trust_score"] = 100
        with self.assertRaisesRegex(ContractError, "unknown_fields:trust_score"):
            validate_statement(item)

    def test_wrong_top_level_type_is_rejected(self):
        with self.assertRaisesRegex(ContractError, "invalid_type:statement"):
            validate_statement(["not", "an", "object"])

    def test_missing_required_field_is_rejected(self):
        item = valid_statement()
        item.pop("resource")
        with self.assertRaisesRegex(ContractError, "missing_fields:resource"):
            validate_statement(item)

    def test_schema_mismatch_is_rejected(self):
        item = valid_statement()
        item["schema"] = "urn:unknown:schema"
        with self.assertRaisesRegex(ContractError, "unsupported_schema"):
            validate_statement(item)



    def test_explicit_bridge_mapping_is_accepted(self):
        from bridge import validate_mapping
        mapping = {
            "h_concept_id": "h:read-only",
            "h_revision": "3",
            "s_term_id": "s:operation.read",
            "s_schema_version": "0.1",
            "direction": "H_TO_S",
            "scope": "resource-request",
            "mapping_kind": "lossy",
            "status": "mapped",
        }
        self.assertEqual(validate_mapping(mapping)["mapping_kind"], "lossy")

    def test_unmapped_h_concept_does_not_invent_s_target(self):
        from bridge import MappingError, validate_mapping
        mapping = {
            "h_concept_id": "h:trust",
            "h_revision": "1",
            "s_term_id": None,
            "s_schema_version": None,
            "direction": "H_TO_S",
            "scope": "resource-request",
            "mapping_kind": "lossy",
            "status": "unmapped",
        }
        self.assertIsNone(validate_mapping(mapping)["s_term_id"])
        mapping["s_term_id"] = "s:authorization"
        with self.assertRaisesRegex(MappingError, "unmapped_target_must_be_null"):
            validate_mapping(mapping)

    def test_ambiguous_mapping_cannot_claim_exactness(self):
        from bridge import MappingError, validate_mapping
        mapping = {
            "h_concept_id": "h:share",
            "h_revision": "2",
            "s_term_id": None,
            "s_schema_version": None,
            "direction": "H_TO_S",
            "scope": "unspecified",
            "mapping_kind": "exact",
            "status": "ambiguous",
        }
        with self.assertRaisesRegex(MappingError, "ambiguous_cannot_be_exact"):
            validate_mapping(mapping)

    def test_bridge_requires_scope(self):
        from bridge import MappingError, validate_mapping
        mapping = {
            "h_concept_id": "h:read-only",
            "h_revision": "3",
            "s_term_id": "s:operation.read",
            "s_schema_version": "0.1",
            "direction": "H_TO_S",
            "mapping_kind": "lossy",
            "status": "mapped",
        }
        with self.assertRaisesRegex(MappingError, "missing_fields:scope"):
            validate_mapping(mapping)

if __name__ == "__main__":
    unittest.main()
