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


if __name__ == "__main__":
    unittest.main()
