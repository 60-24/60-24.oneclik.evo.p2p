# SES-024 — SESSION BOOTSTRAP

**Date:** 2026-09-11  
**Status:** OPEN  
**Project:** P2P 60-24 OneClick Evo Positiv

## 1. PURPOSE
Kontynuacja po zamkniętej SES-023. Celem jest wykonanie najmniejszego kolejnego, weryfikowalnego kroku System Buildera: **Runtime Observation Contract**.

## 2. VERIFIED STATE AT HANDOFF
- SES-023: **CLOSED — GREEN / PASSED**.
- SES-023 udowodniła granicę: `INPUT → RUNTIME ENTRYPOINT → STARTED`.
- Główny HEAD po SES-023: `5e661ea20f2d21e3dadbad5f1382f956aa388602`.
- Runtime target `src/` nadal nie posiada właściwej implementacji P2P; istnieje tylko `src/README.md`.
- Implementacja SES-023 znajduje się w importowalnym pakiecie `sessions/SES_023/`.
- Nie ma podstaw do dokładania teraz UDP/P2P/Node/Trust/TrustGraph.
- Repozytorium jest źródłem prawdy; historia rozmów jest kontekstem.

## 3. CURRENT SYSTEM BUILDER POSITION
`... → IMPLEMENTATION → RUNTIME → OBSERVATION → EVIDENCE → VALIDATION ...`

SES-023 pokrywa:
`INPUT → RUNTIME ENTRYPOINT → STARTED`

SES-024 ma pokryć minimalnie:
`STARTED → OBSERVATION → EVIDENCE-READY RECORD`

## 4. NEXT STEP — SES-024
### Runtime Observation Contract
Minimalny kontrakt powinien dowodzić, że runtime może lokalnie i deterministycznie opisać własny stan, bez wykonywania działania zewnętrznego.

Proponowany minimalny rekord:
- `status: OBSERVED`
- `runtime_id`
- `runtime_status: STARTED`
- `source: RUNTIME_STATE`

Zakazane w tym kroku:
- `executed`
- realny `result`
- UDP/P2P transport
- Node / Agent / Peer
- Trust / TrustGraph
- persistence
- zależność od zegara systemowego
- subprocess/process execution
- mutacja zewnętrznego filesystemu
- network
- autonomous external effects

## 5. EXECUTION ORDER
1. AUDIT — sprawdzić, czy SES-024 nie istnieje już częściowo.
2. Zdefiniować `SES-024_RUNTIME_OBSERVATION_CONTRACT.md`.
3. RED test.
4. CI RED — rzeczywiste niepowodzenie przed implementacją.
5. Minimalna implementacja.
6. CI GREEN — rzeczywiste pytest + dowód checkout commit.
7. Evidence.
8. `SES-024_CLOSEOUT.md`.
9. Ponowny audit przed wyznaczeniem SES-025.

## 6. ENGINEERING RULES
Pracuj według:
`SEE → THINK → DECIDE → ACT → TEST → VERIFY → RECORD → CONTINUE`

TDD:
`SPECIFICATION → RED TEST → CI RED → MINIMAL IMPLEMENTATION → CI GREEN → EVIDENCE`

Maksymalnie 5 znaczących akcji na checkpoint.

Nie pytaj o zgodę na zwykłe działania GREEN. Przy zmianach YELLOW/RED zatrzymaj się na granicy i przedstaw decyzję do akceptacji. Nie wykonuj rzeczywistych efektów zewnętrznych.

## 7. SUCCESS CRITERIA
SES-024 może zostać zamknięta tylko po rzeczywistym dowodzie CI GREEN, zgodności testów z kontraktem i zapisaniu closeout. Nie wolno deklarować GREEN bez dowodu.

## 8. FIRST ACTION FOR NEW SESSION
**Najpierw wykonaj audit repo dla SES-024. Nie zakładaj, że SES-024 jest pusta. Następnie zastosuj najmniejszą zmianę zgodną z powyższym stanem.**

---
**Handoff:** SES-023 CLOSED → SES-024 OPEN  
**Project Lead mode:** ACTIVE
