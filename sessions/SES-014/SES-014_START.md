# SES-014 — SYSTEM BUILDER / INTENT
## Dokument inicjacji nowej sesji

**Status:** OPEN — sesja inicjująca
**Branch:** `main`
**Poprzedni kamień:** SES-013 — GREEN / PASSED

## 1. Punkt startowy

SES-013 zakończono po uzyskaniu rzeczywistego dowodu CI dla granicy pochodzenia Specification → BuildPlan.

GREEN evidence:

- GitHub Actions run: `34296825708`
- Commit workflow: `672a8e4e8d4ef5d245884cb509a968d45288e651`
- `Run SES-011 contract tests` — PASS
- `Run SES-013 provenance boundary test` — PASS

## 2. Obowiązująca granica

`VALID Specification → BuildPlan → Human Approval → Execution`

**BuildPlan jest propozycją. Nie jest autoryzacją wykonania.**

Zasada nadrzędna:

> **System suggests. Human decides.**

## 3. Źródła prawdy

Przed rozpoczęciem prac należy sprawdzić w repozytorium:

1. SES-010 — BuildPlan Contract
2. SES-011 — kontraktowe testy BuildPlan
3. SES-012 — Gate 01 GREEN / PASSED
4. SES-013 — START, DECISIONS, SUMMARY i CLOSEOUT
5. `sessions/SES_011/build_plan.py`
6. aktualny workflow `.github/workflows/ses011-build-plan-contract.yml`

## 4. Cel SES-014

Wykonać **następną kontrolowaną weryfikację granicy BuildPlan**, bez rozszerzania zakresu i bez wprowadzania autonomicznego wykonania.

Pierwszym krokiem jest inspekcja aktualnego kontraktu i identyfikacja najwyższej wartości następnego testu granicznego.

## 5. Metoda pracy

Obowiązuje TDD:

`CONTRACT → TEST → RED → MINIMAL IMPLEMENTATION → GREEN → CI EVIDENCE`

Nie uznajemy GREEN bez rzeczywistego, wykonywalnego dowodu.

## 6. Stop conditions

Prace należy zatrzymać przy:

- brakującym provenance,
- nierozstrzygniętej decyzji wykonawczej,
- niedeterministycznym zachowaniu,
- skutkach ubocznych,
- próbie autonomicznego autoryzowania wykonania,
- sprzeczności z wcześniejszym kontraktem,
- scope creep.

## 7. Reguła zakończenia

Po uzyskaniu PASS:

1. zapisać rzeczywisty dowód,
2. udokumentować decyzje,
3. postawić kamień sesji,
4. zamknąć SES-014,
5. wygenerować handoff dla kolejnej sesji.

Bez dowodu wykonawczego — brak kamienia i brak zamknięcia.

## 8. Pierwsza czynność SES-014

**Inspekcja → wybór jednego najwyżej wartościowego testu granicznego → test przed implementacją.**
