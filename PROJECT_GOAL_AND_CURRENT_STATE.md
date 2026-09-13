# System Builder — Aktualny stan, cel pośredni i cel ostateczny

**Data:** 2026-09-13  
**Status:** ACTIVE / SOURCE OF TRUTH  
**Repozytorium:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`

## 1. Zasada Source of Truth

Repozytorium jest Source of Truth. Chat dostarcza kontekstu, ale stan projektu, decyzje, dowody i checkpointy mają być zapisane w repozytorium.

## 2. Stan po SES-035

Zweryfikowany jest spójny szkielet procesu:

`INTENT → SPECIFICATION → BUILD PLAN → HUMAN APPROVAL / AUTHORIZATION → REQUEST → ATTEMPT → REAL EXECUTION → RESULT → EFFECT → OBSERVATION/EVIDENCE → VERIFICATION → DELIVERY MANIFEST`

SES-032 dowodzi pełny happy path. SES-033 zamknął C0: rzeczywista lokalna egzekucja, artefakt, obserwacja i evidence. SES-034 dodał i zweryfikował produkcyjny entrypoint System Buildera. SES-035 zamknął brakujący dowód jawnej zgody człowieka przez ten produkcyjny entrypoint.

### Dowód SES-035

- commit: `9b46e4d9c7222aefeaae785047c87e801c7a5f46`
- commit message: `docs(SES-035): preserve human approval boundary as project knowledge`
- CI run: `34692639456`
- job: `103550506693`
- conclusion: `success`
- Beta workflow run: `34692639495`
- Beta workflow conclusion: `success`

SES-035 dowodzi przez produkcyjny `run_system_builder(...)`:

- ścieżkę wymagającą `READY_FOR_APPROVAL + APPROVED`,
- zgodność `human_approval.build_plan_id` z rzeczywistym BuildPlan,
- provenance `EXPLICIT_HUMAN_APPROVAL`,
- rzeczywistą lokalną egzekucję,
- `RESULT → EFFECT → OBSERVATION/EVIDENCE → VERIFICATION → DELIVERY MANIFEST`,
- fail-closed dla braku zgody i niedopasowanej zgody.

SES-035 nie wprowadza produkcyjnego mechanizmu Proposal. Test dostarcza już poprawną `PROPOSED` Specification, aby izolować dowód granicy Human Approval.

## 3. Granice bezpieczeństwa

Dwa legalne tryby wykonania:

1. `READY_FOR_APPROVAL + APPROVED + AUTHORIZED/EXPLICIT_HUMAN_APPROVAL`
2. `VALIDATED + NOT_REQUIRED + AUTHORIZED/VALIDATED_NO_APPROVAL_REQUIRED`

Obowiązują twarde rozróżnienia:

`AUTHORIZATION ≠ APPROVAL`

`AUTHORIZED ≠ REQUESTED ≠ EXECUTION_ATTEMPT ≠ EXECUTED ≠ RESULT ≠ EFFECT`

`VERIFIED ≠ real-world effect`

`DELIVERY MANIFEST ≠ external delivery`

Provenance jest sprawdzana fail-closed; zatwierdzony plan z niewłaściwym źródłem authorization nie może zostać wykonany.

## 4. Canonical runtime

Canonical runtime pozostaje w `src/runtime/` dla granicy:

`INPUT → ENTRYPOINT → OBSERVATION → EVIDENCE`

System Builder entrypoint jest warstwą orkiestracji istniejących kontraktów, a nie drugim canonical runtime.

## 5. Rzeczywista pozostała luka

Po SES-035 nie ma podstaw do tworzenia nowego kontraktu ani sesji dla samej numeracji. Dalszy krok musi wynikać z rzeczywistego wymagania Beta i istniejącego kodu/dowodów.

Do sprawdzenia pozostają dwie konkretne możliwości:

1. **Naturalny Proposal flow** — produkcyjny mechanizm przejścia do `PROPOSED` nie został jeszcze dowiedziony i nie należy go implementować, dopóki kryterium Beta nie wykaże, że jest to rzeczywista luka.
2. **External Delivery** — obecny `DELIVERY MANIFEST` jest wewnętrznym, zweryfikowanym dowodem dostarczenia; nie oznacza faktycznego dostarczenia do zewnętrznego odbiorcy/systemu.

Najpierw należy ustalić, która z tych granic jest rzeczywistym wymaganiem Beta. Nie budować architektury „na zapas”.

## 6. Czego teraz NIE robimy

Nie dodajemy bez wykazanej potrzeby:

- P2P/UDP,
- Trust/LocalTrust,
- agent swarm,
- persistence,
- UI,
- external delivery,
- nowych źródeł authorization,
- nowych warstw runtime,
- kolejnych kontraktów.

Nie tworzymy SES-036 wyłącznie dla numeracji.

## 7. Zasada pracy

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST (tylko gdy luka jest rzeczywista) → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CLOSE → CONTINUE`

Autonomiczne działania rutynowe w już delegowanym zakresie są dozwolone bez ponownego pytania o zgodę.

Każdy checkpoint:

`STATE → EVIDENCE → GAP → DECISION → ACTION → NEXT`

Maksymalnie 5 istotnych działań na checkpoint.

## 8. Cel Beta

Funkcjonalny Beta System Builder / P2P 60-24 OneClick Evo Positiv:

`INTENT → UNDERSTAND → SPECIFICATION → BUILD PLAN → HUMAN APPROVAL → EXECUTION AUTHORIZATION → EXECUTION REQUEST → EXECUTION → RESULT → EFFECT → VERIFICATION → DELIVERY`

System ma rozumieć, projektować, budować, testować i dostarczać, przy zachowaniu ludzkiej kontroli nad decyzjami wymagającymi człowieka.

## 9. Kryterium zakończenia

Beta nie jest uznawana na podstawie liczby sesji ani deklaracji. Potrzebny jest aktualny, odtwarzalny dowód w repozytorium obejmujący produkcyjny entrypoint, legalne ścieżki authorization, rzeczywistą lokalną egzekucję, provenance, verification oraz delivery manifest.

SES-035 jest GREEN / CLOSED. Następny krok ma zostać wyznaczony wyłącznie po ponownym przeglądzie aktualnego repozytorium i kryteriów Beta.
