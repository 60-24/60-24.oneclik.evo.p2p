"""SES-007 — ambiguity token boundaries in the Intent Envelope validator."""

import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("intent_envelope.py")


def _validate():
    spec = importlib.util.spec_from_file_location("ses007_intent_envelope_boundaries", MODULE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate


def _intent(**overrides):
    intent = {
        "version": 1,
        "objective": "Build the target system from explicit intent.",
        "requirements": ["produce a reproducible build"],
        "constraints": ["bounded execution"],
        "assumptions": ["runtime is available"],
        "optional_information": [],
        "open_questions": [],
        "protected_decisions": [],
        "authority": "human",
    }
    intent.update(overrides)
    return intent


def test_substring_matches_do_not_raise_ambiguity():
    """"or" inside storage, report or work order is not a disjunction."""
    validate = _validate()
    for question in (
        "Need more storage?",
        "Who writes the report?",
        "What is the work order?",
    ):
        status = validate(_intent(open_questions=[question]))["status"]
        assert status != "AMBIGUOUS", question
        assert status == "INCOMPLETE", question


def test_english_disjunction_is_ambiguous():
    validate = _validate()
    result = validate(_intent(open_questions=["Should execution be local or remote?"]))
    assert result["status"] == "AMBIGUOUS"


def test_polish_disjunction_is_ambiguous():
    validate = _validate()
    result = validate(_intent(open_questions=["Zapisywać wynik lokalnie albo zdalnie?"]))
    assert result["status"] == "AMBIGUOUS"


def test_polish_inflected_ambiguity_term_is_detected():
    validate = _validate()
    result = validate(_intent(open_questions=["Wymaganie jest niejednoznaczne."]))
    assert result["status"] == "AMBIGUOUS"


def test_other_statuses_are_unchanged():
    validate = _validate()
    assert validate(_intent())["status"] == "VALID"
    assert validate(_intent(requirements=[]))["status"] == "INCOMPLETE"
    assert validate(_intent(protected_decisions=["Change governance rule"]))["status"] == "PROTECTED"


def test_result_shape_is_unchanged():
    validate = _validate()
    result = validate(_intent(open_questions=["Should execution be local or remote?"]))
    assert set(result) == {
        "intent_id", "version", "objective", "requirements", "constraints",
        "assumptions", "optional_information", "open_questions",
        "protected_decisions", "authority", "status", "element_ids", "validation",
    }
