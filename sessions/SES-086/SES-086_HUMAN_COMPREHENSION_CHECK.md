# SES-086 — Human comprehension check

**Status:** evaluation protocol proposal; no participants/results claimed.
**Question:** does the H/S approach make requests clearer, or merely replace familiar words with unfamiliar labels?

## Method

Give reviewers each scenario in two forms, in randomized order:
1. Original natural-language request.
2. Human-readable summary generated from a typed S statement, including explicit unknowns.

Do not teach reviewers the intended answer first. Ask the same questions after each version. Record correct answers, unresolved items, and time. Compare versions within the same reviewer; do not count a confident guess as correct.

## Scenario A — underspecified resource

**Natural request:** “Udostępnij mi raport.”

**Structured summary:** “Requester: principal:requester-7. Resource: resource:report-17. Requested operation: read. Copying: not allowed. Expiry: 2026-12-01 00:00 UTC. Authorization: not yet decided.”

Expected understanding: the resource and requested operation are explicit in the structured version; the request itself does not grant access. In the original sentence, the report, recipient, operation, duration, and copying rules are unknown.

## Scenario B — identity versus authorization

**Natural request:** “To zaufany użytkownik, pozwól mu wejść.”

**Structured summary:** “Requester identity: authenticated. Authorization decision: absent. Local trust assessment: not supplied by this statement. Result: access not authorized by this message.”

Expected understanding: authentication and trust do not, by themselves, establish permission.

## Scenario C — ambiguous mapping

**Natural request:** “Daj mu dostęp tylko do odczytu.”

**Structured summary:** “Requested operation: read. Copying, retention, and onward sharing: unspecified unless separately constrained. Mapping from the human phrase is partial/context-bound.”

Expected understanding: “read” does not silently grant or deny copying, retention, or onward sharing.

## Questions after each version

1. Who is making the request, if known?
2. Which resource and operation are specified?
3. What restrictions are explicit?
4. What remains unknown or ambiguous?
5. Does this message itself authorize the operation? Why?

## Scoring

- Score each answer 0 (wrong/guess), 1 (partly correct), or 2 (correct and identifies uncertainty).
- Record completion time and whether the reviewer incorrectly inferred authorization.
- Primary measure: average score per scenario/version.
- Safety measure: number of false claims that access is authorized.
- Use a small pilot (at least 5 reviewers if available) to find confusing wording, not to claim statistical proof.

## Decision rule for the pilot

Keep the approach only if the structured summary improves identification of explicit fields and unknowns without increasing false authorization assumptions. If terminology adds burden without improving comprehension, simplify H labels and summaries before adding concepts.

## Limitations

This is a test protocol, not evidence of improvement. Results depend on reviewer familiarity, translation quality, scenario selection, and presentation order. S validation success cannot substitute for human comprehension results.