import unittest

from specification import build_specification


class SpecificationContractTests(unittest.TestCase):
    def base_intent(self):
        return {
            "version": 1,
            "objective": "Build the target system from explicit intent.",
            "requirements": ["produce a reproducible build"],
            "constraints": ["bounded execution"],
            "assumptions": ["runtime is available"],
            "optional_information": ["future deployment context"],
            "open_questions": [],
            "protected_decisions": [],
            "authority": "human",
        }

    def test_minimum_machine_representable_contract(self):
        spec = build_specification(self.base_intent())
        for field in (
            "specification_id", "source_intent_id", "version", "status",
            "objective", "requirements", "constraints", "inputs", "outputs",
            "acceptance_criteria", "assumptions", "unresolved_decisions",
            "provenance", "authority",
        ):
            self.assertIn(field, spec)
        self.assertEqual(spec["status"], "VALID")

    def test_requirement_and_constraint_provenance(self):
        spec = build_specification(self.base_intent())
        self.assertEqual(len(spec["requirements"]), 1)
        self.assertEqual(spec["requirements"][0]["origin"], "DERIVED")
        self.assertTrue(spec["requirements"][0]["source_element_id"])
        self.assertEqual(len(spec["constraints"]), 1)
        self.assertEqual(spec["constraints"][0]["origin"], "DERIVED")
        self.assertTrue(spec["constraints"][0]["source_element_id"])

    def test_origins_are_explicit(self):
        spec = build_specification(self.base_intent())
        self.assertIn(spec["requirements"][0]["origin"], {"DERIVED", "PROPOSED", "UNRESOLVED"})
        self.assertIn(spec["constraints"][0]["origin"], {"DERIVED", "PROPOSED", "UNRESOLVED"})
        for item in spec["assumptions"]:
            self.assertEqual(item["origin"], "DERIVED")

    def test_incomplete_intent_is_blocked(self):
        intent = self.base_intent()
        intent["requirements"] = []
        with self.assertRaises(ValueError):
            build_specification(intent)

    def test_ambiguous_intent_is_blocked(self):
        intent = self.base_intent()
        intent["open_questions"] = ["Choose either local or remote execution interpretation."]
        with self.assertRaises(ValueError):
            build_specification(intent)

    def test_protected_intent_is_blocked(self):
        intent = self.base_intent()
        intent["protected_decisions"] = ["Change foundational governance rule"]
        with self.assertRaises(ValueError):
            build_specification(intent)

    def test_deterministic_transformation(self):
        first = build_specification(self.base_intent())
        second = build_specification(dict(reversed(list(self.base_intent().items()))))
        self.assertEqual(first, second)

    def test_assumptions_do_not_become_requirements(self):
        spec = build_specification(self.base_intent())
        requirement_statements = {item["statement"] for item in spec["requirements"]}
        assumption_statements = {item["statement"] for item in spec["assumptions"]}
        self.assertTrue(assumption_statements.isdisjoint(requirement_statements))

    def test_provenance_links_back_to_source_intent(self):
        spec = build_specification(self.base_intent())
        self.assertEqual(spec["source_intent_id"], spec["provenance"][0]["source_intent_id"])
        for entry in spec["provenance"]:
            self.assertTrue(entry["source_element_id"])
            self.assertTrue(entry["specification_element_id"])

    def test_unresolved_decisions_remain_unresolved(self):
        intent = self.base_intent()
        intent["open_questions"] = ["Which deployment region should be used?"]
        # An unresolved decision is never silently converted into an executable choice.
        with self.assertRaises(ValueError):
            build_specification(intent)


if __name__ == "__main__":
    unittest.main()
