import unittest

from intent_envelope import CONTRACT_VERSION, canonical_json, normalize, validate


class IntentEnvelopeTests(unittest.TestCase):
    def base(self):
        return {
            "version": CONTRACT_VERSION,
            "objective": "Build the target system from explicit intent.",
            "requirements": ["produce a reproducible build"],
            "constraints": ["bounded execution"],
            "assumptions": ["runtime is available"],
            "optional_information": ["future deployment context"],
            "open_questions": [],
            "protected_decisions": [],
            "authority": "human",
        }

    def test_valid(self):
        result = validate(self.base())
        self.assertEqual(result["status"], "VALID")

    def test_incomplete(self):
        intent = self.base()
        intent["requirements"] = []
        result = validate(intent)
        self.assertEqual(result["status"], "INCOMPLETE")

    def test_ambiguous(self):
        intent = self.base()
        intent["open_questions"] = ["Choose either local or remote execution interpretation."]
        result = validate(intent)
        self.assertEqual(result["status"], "AMBIGUOUS")

    def test_protected(self):
        intent = self.base()
        intent["protected_decisions"] = ["Change foundational governance rule"]
        result = validate(intent)
        self.assertEqual(result["status"], "PROTECTED")

    def test_deterministic_identity_ignores_field_order(self):
        first = self.base()
        second = dict(reversed(list(first.items())))
        self.assertEqual(normalize(first)["intent_id"], normalize(second)["intent_id"])
        self.assertEqual(canonical_json(validate(first)), canonical_json(validate(second)))

    def test_assumptions_are_not_requirements(self):
        result = validate(self.base())
        self.assertIn("runtime is available", result["assumptions"])
        self.assertNotIn("runtime is available", result["requirements"])

    def test_stable_element_ids(self):
        first = validate(self.base())
        second = validate(self.base())
        self.assertEqual(first["element_ids"], second["element_ids"])


if __name__ == "__main__":
    unittest.main()
