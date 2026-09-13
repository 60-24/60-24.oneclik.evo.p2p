# SES-036 — Beta Boundary Audit / Next Real Gap

**Data:** 2026-09-13  
**Status:** START  
**Previous:** SES-035 GREEN / CLOSED  
**Repository:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`

## PURPOSE

Nie zakładać z góry kolejnego kontraktu ani numerowanej funkcji. Ustalić na podstawie aktualnego repozytorium, kodu, testów, workflow i kryterium Beta **najmniejszą rzeczywistą lukę funkcjonalną**.

## SOURCE OF TRUTH

Repozytorium jest Source of Truth. Chat jest wyłącznie kontekstem.

Stan wejściowy: SES-035 dowiodła jawnej Human Approval przez produkcyjny EntryPoint, fail-closed, poprawne `build_plan_id`, provenance `EXPLICIT_HUMAN_APPROVAL`, rzeczywistą egzekucję, RESULT/EFFECT/OBSERVATION/VERIFICATION oraz DELIVERY MANIFEST.

## CURRENT BOUNDARY

Canonical flow:

`INTENT → SPECIFICATION → BUILD PLAN → HUMAN APPROVAL / AUTHORIZATION → REQUEST → ATTEMPT → REAL EXECUTION → RESULT → EFFECT → OBSERVATION/EVIDENCE → VERIFICATION → DELIVERY MANIFEST`

Twarde rozróżnienia:

`AUTHORIZATION ≠ APPROVAL`

`AUTHORIZED ≠ REQUESTED ≠ EXECUTION_ATTEMPT ≠ EXECUTED ≠ RESULT ≠ EFFECT`

`VERIFIED ≠ real-world effect`

`DELIVERY MANIFEST ≠ EXTERNAL DELIVERY`

## WORK METHOD

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST (only if real gap) → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CLOSE → CONTINUE`

Autonomiczne działania rutynowe w delegowanym zakresie wykonuj bez ponownego pytania o zgodę.

## FIRST AUDIT

Sprawdź przed zmianą kodu:

1. `PROJECT_GOAL_AND_CURRENT_STATE.md` i ostatnie dokumenty SES-035.
2. Produkcyjny `src/system_builder/` oraz canonical runtime `src/runtime/`.
3. Istniejące testy E2E/unit i wszystkie workflow CI dotyczące Beta/System Builder.
4. Rzeczywisty stan `PROPOSED`/Proposal oraz `DELIVERY MANIFEST`.
5. Kryterium Beta: czy istnieje brak bezpośrednio uniemożliwiający funkcjonalny przepływ Beta.

## DECISION RULE

Po audycie wybierz tylko jedną ścieżkę:

**A — Proposal flow**, jeżeli istniejące kryterium Beta wymaga produkcyjnego przejścia do `PROPOSED`, a repozytorium rzeczywiście nie potrafi tego wykonać.

**B — External Delivery**, tylko jeżeli kryterium Beta wymaga faktycznego dostarczenia poza wewnętrzny `DELIVERY MANIFEST`.

**C — No implementation**, jeżeli żadna z powyższych granic nie jest rzeczywistą luką Beta. Wtedy udokumentuj dowód i wyznacz następny najmniejszy brak.

Nie budować P2P/UDP, Trust, swarm, persistence, UI ani nowych warstw bez bezpośredniego wymagania Beta.

## CHECKPOINT FORMAT

`STATE → EVIDENCE → GAP → DECISION → ACTION → NEXT`

Maksymalnie 5 istotnych działań na checkpoint.

## SUCCESS CONDITION

SES-036 ma zakończyć się konkretną decyzją opartą na dowodzie repozytorium. Żadnego PASS na podstawie deklaracji ani samej liczby sesji.
