import json
import tempfile
import unittest
from pathlib import Path

from run_vs001 import EXAMPLE_INTENT, build, canonical_json, deliver, normalize, render_markdown


class VS001Tests(unittest.TestCase):
    def test_t001_valid_intent(self):
        spec = normalize(EXAMPLE_INTENT)
        self.assertEqual(spec["intent"], EXAMPLE_INTENT["statement"])
        self.assertEqual(spec["status"], "VERIFIED")

    def test_t002_ambiguous_intent_is_explicitly_representable(self):
        ambiguous = dict(EXAMPLE_INTENT)
        ambiguous["acceptance_criteria"] = []
        spec = normalize(ambiguous)
        self.assertEqual(spec["status"], "PROPOSED")
        self.assertTrue(spec["open_questions"])
        self.assertIn("acceptance criteria", spec["open_questions"][0])

    def test_t003_constraint_preservation(self):
        spec = normalize(EXAMPLE_INTENT)
        self.assertEqual(spec["constraints"], EXAMPLE_INTENT["constraints"])

    def test_t004_deterministic_representation(self):
        first = normalize(EXAMPLE_INTENT)
        second = normalize(dict(EXAMPLE_INTENT))
        self.assertEqual(canonical_json(first), canonical_json(second))
        self.assertEqual(render_markdown(first), render_markdown(second))
        self.assertEqual(
            canonical_json(first),
            canonical_json(normalize(EXAMPLE_INTENT)),
        )

    def test_t005_delivery_requires_verification_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            with self.assertRaises(ValueError):
                deliver(output, "SPEC-VS001-001", {}, {})
            result = build(output)
            self.assertEqual(result["result"], "PASS")
            self.assertTrue((output / "verification.json").exists())
            self.assertTrue((output / "delivery-manifest.json").exists())
            verification = json.loads((output / "verification.json").read_text(encoding="utf-8"))
            self.assertEqual(verification["result"], "PASS")

    def test_t006_protected_scope_is_not_executed(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(Path(tmp))
            files = {p.name for p in Path(tmp).iterdir()}
            self.assertNotIn("network.log", files)
            self.assertNotIn("shell.log", files)
            self.assertNotIn("deployment.log", files)


if __name__ == "__main__":
    unittest.main()
