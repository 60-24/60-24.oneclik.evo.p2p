# SES-009 — SYSTEM BUILDER / CI EVIDENCE
## Dokument przeniesienia i inicjacji nowej sesji

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repozytorium:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Sesja:** SES-009  
**Poprzednia sesja:** SES-008  
**Status:** OPENING  
**Data:** 2026-09-08

---

## 1. Punkt startowy

SES-008 została zamknięta jako:

**CLOSED — CONDITIONAL / EVIDENCE GAP**

Specification została zdefiniowana i zaimplementowana jako deterministyczna transformacja zwalidowanego Intent Envelope.

W repozytorium istnieją:

- `sessions/SES-008/specification.py`
- `sessions/SES-008/test_specification.py`
- `sessions/SES-008/SES-008_SPECIFICATION_CONTRACT.md`
- `sessions/SES-008/SES-008_CLOSEOUT.md`

Ostatni commit SES-008 przed closeout:

`35e64321554f37666d39771656b62cece262feb9`

Commit zamykający dokumentację SES-008:

`c08ba89b97170888ae6ace9d49659109e0e38030`

---

## 2. Cel SES-009

SES-009 NIE rozpoczyna przebudowy Specification.

Pierwszym zadaniem jest uzyskanie rzeczywistego, obserwowalnego dowodu CI dla aktualnego stanu `main` oraz ustalenie, dlaczego wcześniejszy odczyt nie dostarczył wyniku dla SES-008.

**Evidence gap ≠ implementation failure.**

---

## 3. Zakres pracy

1. Ustalić aktualny HEAD `main`.
2. Zidentyfikować właściwy workflow GitHub Actions.
3. Sprawdzić jego trigger, joby i warunki uruchomienia.
4. Odnaleźć workflow run odpowiadający aktualnemu stanowi `main`.
5. Jeżeli run istnieje — pobrać rzeczywisty status, conclusion i wyniki jobów.
6. Jeżeli run nie istnieje — ustalić konkretną przyczynę.
7. Jeżeli CI FAIL — diagnozować wyłącznie rzeczywisty błąd i wykonać minimalną korektę.
8. Jeżeli CI PASS — zachować run ID jako evidence i domknąć evidence gap SES-008.

---

## 4. Twarde zasady

### Nie robimy

- spekulacyjnej zmiany `specification.py`,
- przebudowy SES-007 bez konkretnego dowodu defektu,
- rozszerzania Specification bez uzasadnienia,
- oznaczania CI jako PASS bez rzeczywistego wyniku,
- przyjmowania zewnętrznej analizy AI jako źródła prawdy sprzecznego z repozytorium.

### Robimy

- repozytorium traktujemy jako techniczne źródło prawdy,
- CI traktujemy jako źródło dowodu wykonania,
- diagnozujemy na podstawie obserwowalnych faktów,
- każdą zmianę wykonujemy minimalnie i śledzalnie.

---

## 5. Granica decyzyjna

Obowiązuje:

> **System suggests. Human decides.**

Zmiany konstytucyjne, ontologiczne, trust, governance, security oraz inne decyzje chronione wymagają jawnej decyzji człowieka.

SES-009 jest sesją **verification / evidence**, a nie redesignu architektury.

---

## 6. Kryterium wyjścia

SES-009 może zostać zamknięta po osiągnięciu jednego z trzech jednoznacznych stanów:

### A. CI PASS

Rzeczywisty run dla aktualnego stanu `main` został znaleziony i zakończył się sukcesem.

### B. CI INFRASTRUCTURE ISSUE

Brak runu został wyjaśniony konkretnym problemem konfiguracji lub infrastruktury CI, który został zapisany jako evidence i zadanie.

### C. CI FAIL → FIX → PASS

Istnieje rzeczywisty, odtwarzalny błąd, został naprawiony, a poprawka została ponownie zweryfikowana przez CI.

Nie zamykamy sesji na podstawie przypuszczeń.

---

## 7. Następny etap

Po zamknięciu evidence gap można przejść do:

`Specification → Execution / Build Plan`

Nie należy omijać weryfikacji obecnej warstwy.

---

## 8. Stan wejściowy

**SES-009 — OPENING**

Pierwsze zadanie:

> **Odnaleźć i zweryfikować rzeczywisty CI workflow/run dla aktualnego `main`.**

Nie przebudowywać. Nie zgadywać. Najpierw dowód.

---

## 9. Kamień wejściowy

> **SES-008 zamknięta. Specification pozostaje nienaruszona. SES-009 rozpoczyna się od zamknięcia evidence gap poprzez rzeczywistą obserwację CI.**
