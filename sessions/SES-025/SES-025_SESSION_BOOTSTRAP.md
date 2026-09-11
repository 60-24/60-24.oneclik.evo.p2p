# SES-025 — SESSION BOOTSTRAP

**Date:** 2026-09-11  
**Status:** OPEN  
**Project:** P2P 60-24 OneClick Evo Positiv

## 1. PURPOSE
Kontynuacja po zamkniętej SES-024. Celem SES-025 jest najpierw wykonanie audytu repozytorium i na jego podstawie wyznaczenie **najmniejszej, rzeczywiście uzasadnionej granicy semantycznej** dla kolejnego kroku System Buildera.

Nie zakładamy z góry, jaki ma być kolejny kontrakt. Najpierw dowód, potem decyzja.

## 2. VERIFIED STATE AT HANDOFF
- SES-023: **CLOSED — GREEN / PASSED**.
- SES-024: **CLOSED — GREEN / PASSED**.
- SES-024 udowodniła granicę: `STARTED → OBSERVATION → EVIDENCE-READY RECORD`.
- SES-024 closeout: `sessions/SES-024/SES-024_CLOSEOUT.md`.
- Implementacja SES-024: `sessions/SES_024/runtime_observation.py`.
- Repozytorium jest technicznym źródłem prawdy; historia rozmów jest tylko kontekstem.
- Aktualny kierunek System Buildera pozostaje: minimalny, weryfikowalny runtime/builder proof przed rozszerzaniem P2P.
- Nie wolno automatycznie zakładać potrzeby UDP/P2P/Node/Agent/Peer/Trust/TrustGraph.

## 3. CURRENT SYSTEM BUILDER POSITION
Dotychczas potwierdzono:

`INPUT → RUNTIME ENTRYPOINT → STARTED → OBSERVATION → EVIDENCE-READY RECORD`

SES-025 ma ustalić **następną granicę na podstawie audytu**, a nie rozszerzać architekturę dla samego rozszerzania.

## 4. FIRST OBJECTIVE — REPOSITORY AUDIT
Audyt ma sprawdzić co najmniej:

1. istniejące kontrakty i ich kolejność,
2. istniejące testy i rzeczywiste dowody CI,
3. runtime/build/entrypoint/observation artifacts,
4. workflowy GitHub Actions i ewentualne nakładanie się triggerów,
5. istniejące wzorce możliwe do REUSE,
6. luki między aktualnym stanem a pipeline System Buildera,
7. artefakty częściowe, historyczne, eksperymentalne lub niecanonicalne,
8. czy kolejny krok jest GREEN, YELLOW, RED lub BLACK.

## 5. DECISION RULE
Po audycie wybierz tylko jeden najlepszy następny krok:

`REUSE → INTEGRATE → IMPROVE → INVENT → REJECT / ESCALATE`

Jeżeli brak wystarczających dowodów — **nie implementuj**; zapisz GAP i wykonaj dalszy audit.

Jeżeli proponowany krok dotyka Constitution, foundational Ontology, Trust, fundamental security/governance, API/protocol/data-model lub cross-layer contract, zatrzymaj się na odpowiedniej granicy autonomii.

## 6. ENGINEERING METHOD
Pracuj według:

`SEE → THINK → DECIDE → ACT → TEST → VERIFY → RECORD → CONTINUE`

TDD, gdy powstaje nowy kontrakt:

`SPECIFICATION → RED TEST → CI RED → MINIMAL IMPLEMENTATION → CI GREEN → EVIDENCE`

Maksymalnie 5 znaczących akcji na checkpoint.

## 7. HARD BOUNDARIES
Nie:
- zmieniaj zamkniętych historycznych sesji,
- nie rozszerzaj architektury bez dowodu,
- nie wprowadzaj UDP/P2P/Trust/Node/Agent tylko dlatego, że są częścią docelowej wizji,
- nie wykonuj rzeczywistych efektów zewnętrznych,
- nie wprowadzaj płatności, tokenów, walletów ani transferu wartości,
- nie umieszczaj sekretów w Git,
- nie deklaruj RED/GREEN bez rzeczywistego dowodu,
- nie zmieniaj cicho Constitution/Ontology/Trust.

## 8. SUCCESS CRITERIA
SES-025 ma zakończyć się jednym z dwóch poprawnych stanów:

**A. GAP FOUND:** audyt wskazuje konkretną lukę i powstaje minimalny, evidence-backed następny kontrakt/krok.

**B. NO SAFE NEXT STEP:** brak wystarczającego dowodu lub wejście w YELLOW/RED/BLACK; zapisujemy stan i zatrzymujemy implementację.

Nie ma obowiązku tworzenia kodu.

## 9. FIRST ACTION
**Wykonaj pełny audit repozytorium od stanu po SES-024. Następnie przedstaw checkpoint w formacie:**

`STATE → EVIDENCE → GAP → DECISION → NEXT`

Nie rozpoczynaj implementacji SES-025 przed zakończeniem tego audytu.

---
**Handoff:** SES-024 CLOSED → SES-025 OPEN  
**Project Lead mode:** ACTIVE
