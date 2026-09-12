# System Builder — Aktualny stan, cel pośredni i cel ostateczny

**Data:** 2026-09-12  
**Status:** ACTIVE / SOURCE OF TRUTH  
**Repozytorium:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`

## 1. Zasada Source of Truth

Repozytorium jest Source of Truth. Chat dostarcza kontekstu, ale stan projektu, decyzje, dowody i checkpointy mają być zapisane w repozytorium.

## 2. Stan po SES-034

Zweryfikowany jest spójny szkielet procesu:

`INTENT → SPECIFICATION → BUILD PLAN → APPROVAL/AUTHORIZATION → REQUEST → ATTEMPT → REAL EXECUTION → RESULT → EFFECT → OBSERVATION/EVIDENCE → VERIFICATION → DELIVERY MANIFEST`

SES-032 dowodzi bezpośredniego pełnego happy path z wymaganym human approval. SES-033 zamknął C0: rzeczywista lokalna egzekucja, artefakt, obserwacja i evidence.

SES-034 dodał i zweryfikował **produkcyjny entrypoint System Buildera**. Aktualny `src/system_builder/entrypoint.py` prowadzi Intent przez istniejące kontrakty aż do Delivery Manifest. Aktywny CI run `34673329445` jest GREEN i wykonał zarówno SES-032, jak i test produkcyjnego entrypointu SES-034.

### Dowód SES-034

- commit: `aee8c372693220522768e7bb1813b039a6c3d316`
- CI run: `34673329445`
- job: `103498677715`
- conclusion: `success`
- SES-032 integration test: `success`
- SES-034 production entrypoint test: `success`

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

Po SES-034 nie ma podstaw do tworzenia nowego kontraktu. Pozostała jedna mała luka integracyjna:

> Produkcyjny entrypoint został dowiedziony dla ścieżki `VALIDATED + NOT_REQUIRED`, natomiast ścieżka wymagająca jawnej zgody człowieka nie ma jeszcze własnego E2E dowodu przechodzącego przez produkcyjny entrypoint.

To jest zakres SES-035.

Cel:

`PROPOSED INTENT → READY_FOR_APPROVAL → HUMAN APPROVAL → PRODUCTION ENTRYPOINT → REAL EXECUTION → RESULT → EFFECT → VERIFICATION → DELIVERY MANIFEST`

## 6. Czego teraz NIE robimy

Nie dodajemy:

- P2P/UDP,
- Trust/LocalTrust,
- agent swarm,
- persistence,
- UI,
- external delivery,
- nowych źródeł authorization,
- nowych warstw runtime,
- kolejnych kontraktów bez wykazanej luki.

Nie tworzymy sesji dla samej numeracji.

## 7. Zasada pracy

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST (tylko gdy luka jest rzeczywista) → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CLOSE`

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

Najbliższy cel jest celowo mały: **SES-035 — explicit human approval przez production entrypoint + GREEN CI.**
