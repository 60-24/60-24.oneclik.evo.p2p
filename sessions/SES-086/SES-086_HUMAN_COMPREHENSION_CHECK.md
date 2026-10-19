# SES-086 — Human comprehension check

**Status:** proposed protocol; no participant results claimed.  
**Question:** does Tagologia H/S improve comprehension, or merely add unfamiliar terminology?

## Design correction

A fair comparison must present the **same information and the same unknowns** in both forms. Do not compare an underspecified natural-language request with a structured summary that adds a resource ID, operation, expiry, or restrictions: that tests added information, not the representation.

Use paired forms below. Randomize order within each pair; do not explain the expected answer first.

## Minimal paired comparison matrix

| Case | Form A — plain language | Form B — explicit H/S-derived summary | Expected understanding |
|---|---|---|---|
| A — missing details | “Udostępnij mi raport.” | “Prośba o udostępnienie raportu. Nie podano, który raport, kto ma otrzymać dostęp, jakie operacje, na jak długo ani czy wolno kopiować. Dostęp nie został zatwierdzony.” | Same uncertainty is visible; neither form identifies the resource/recipient or authorizes access. |
| B — identity vs permission | “Użytkownik został uwierzytelniony. Nie podjęto decyzji o przyznaniu mu dostępu.” | “Tożsamość: uwierzytelniona. Decyzja autoryzacyjna: brak. Wynik: dostęp nieprzyznany.” | Authentication is not authorization; no access is granted by these statements. |
| C — read-only boundary | “Może odczytać zasób. Nie ustalono, czy wolno go kopiować, zachowywać ani dalej udostępniać.” | “Operacja: read. Kopiowanie, retencja i dalsze udostępnianie: nieokreślone.” | Read access alone does not settle copying, retention, or onward sharing. |

These are illustrative stimuli, not approved ontology or protocol text. Form B must not contain facts absent from Form A.

## Questions after each form

1. What is known about the requester/identity?
2. Which resource or operation is specified?
3. Which restrictions are explicit?
4. What remains unknown?
5. Does the statement itself authorize access? Explain.

Score each answer **0** = wrong/unsupported guess, **1** = partly correct, **2** = correct and uncertainty-aware. Record completion time and each false claim that access is authorized.

## Results sheet

Copy one row per reviewer × case × form:

| Reviewer (pseudonym) | Case | Form (A/B) | Q1 | Q2 | Q3 | Q4 | Q5 | Total / 10 | Time (sec) | False authorization? (0/1) | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| | A | | | | | | | | | | |
| | B | | | | | | | | | | |
| | C | | | | | | | | | | |

Summarize per case: mean score A vs B; median time A vs B; false-authorization count A vs B; common misunderstandings. Keep individual results separate from interpretation.

## Pilot and decision rule

A small pilot (target at least 5 reviewers if available) is for finding confusing wording, not statistical proof. Keep the approach only if the paired form improves identification of explicit facts/unknowns **without increasing false authorization assumptions**. If terminology adds burden without a clear benefit, simplify the H summary before adding concepts.

## Limitations

No empirical result is claimed until reviewers actually complete the sheet. A successful S unit-test run does not establish human comprehension. Results depend on reviewer background, wording, order, and scenario selection.