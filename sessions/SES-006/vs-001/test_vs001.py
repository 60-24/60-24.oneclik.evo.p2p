import json
import tempfile
import unittest
from pathlib import Path

from run_vs001 import EXAMPLE_INTENT, build, canonical_json, normalize, render_markdown


class VS001Tests(unittest.TestCase):
    def test_t001_valid_intent(self):
        spec = normalize(EXAMPLE_INTENT)
        self.assertEqual(spec["intent"], EXAMPLE_INTENT["statement"])
        self.assertEqual(spec["status"], "VERIFIED")

    def test_t002_ambiguous_intent_is_explicitly_representable(self):
        ambiguous = dict(EXAMPLE_INTENT)
        ambiguous["acceptance_criteria"] = []
        spec = normalize(ambiguous)
        self.assertIn("open_questions", spec)
        self.assertIsInstance(spec["open_questions"], list)

    def test_t003_constraint_preservation(self):
        spec = normalize(EXAMPLE_INTENT)
        self.assertEqual(spec["constraints"], EXAMPLE_INTENT["constraints"])

    def test_t004_deterministic_representation(self):
        spec = normalize(EXAMPLE_INTENT)
        self.assertEqual(canonical_json(spec), canonical_json(spec))
        self.assertEqual(render_markdown(spec), render_markdown(spec))

    def test_t005_delivery_requires_verification_artifact(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = build(Path(tmp))
            self.assertEqual(result["result"], "PASS")
            self.assertTrue((Path(tmp) / "verification.json").exists())
            self.assertTrue((Path(tmp) / "delivery-manifest.json").exists())
            verification = json.loads((Path(tmp) / "verification.json").read_text(encoding="utf-8"))
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
