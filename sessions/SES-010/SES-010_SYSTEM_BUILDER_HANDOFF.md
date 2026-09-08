# SES-010 — SYSTEM BUILDER / EXECUTION BUILD PLAN
## Dokument przeniesienia i inicjacji nowej sesji

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repozytorium:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Sesja:** SES-010  
**Poprzednia sesja:** SES-009  
**Status:** OPENING  
**Data:** 2026-09-08

---

## 1. Stan wejściowy

SES-009 została zamknięta jako:

**CLOSED — PASS**

Evidence gap SES-008 został zamknięty przez rzeczywisty GitHub Actions run:

- Run ID: `34198084971`
- Workflow: `SES-008 Specification Verification`
- Head SHA: `4db7f846c555f2c7ac2e42abed6b56daf946bbdb`
- Conclusion: `success`
- Job `verify`: `success`
- Compile: `success`
- Unit tests: `success`

SES-009 closeout commit:

`eb9b3431b4bd19d92dc385392b7ad8707ed3644b`

---

## 2. Zweryfikowany łańcuch

Obowiązujący łańcuch budowy:

`Human Intent → Intent Envelope → Deterministic Validation → Specification`

SES-007 dostarczyła deterministycznie walidowany Intent Envelope.

SES-008 dostarczyła deterministyczną transformację do machine-representable Specification z provenance i blokadami stanów nierozstrzygniętych.

SES-009 dostarczyła rzeczywisty dowód CI tej warstwy.

---

## 3. Cel SES-010

Zaprojektować następną, wyraźnie oddzieloną warstwę:

`Specification → Execution / Build Plan`

Celem nie jest jeszcze uruchamianie systemu produkcyjnego.

Celem jest określenie, jak zweryfikowana Specification zostaje przekształcona w **jawny, machine-representable Build/Execution Plan**, który może zostać później wykonany przez system pod kontrolą człowieka.

---

## 4. Zakres

1. Zdefiniować granicę `Specification → Build Plan`.
2. Zdefiniować minimalny kontrakt Build Plan.
3. Zachować provenance od Specification do planowanych kroków.
4. Rozdzielić:
   - `DERIVED` — wynikające ze Specification,
   - `PROPOSED` — propozycje System Buildera,
   - `UNRESOLVED` — decyzje nadal nierozstrzygnięte.
5. Zdefiniować warunki blokujące wykonanie.
6. Zdefiniować deterministyczność transformacji tam, gdzie jest wymagana.
7. Zdefiniować acceptance criteria dla planu.
8. Napisać testy kontraktu przed implementacją transformera.
9. Dopiero po testach zaimplementować minimalny transformer.
10. Dodać CI i rzeczywisty evidence.

---

## 5. Poza zakresem

Nie wykonywać w SES-010:

- produkcyjnego deploymentu,
- autonomicznego remote execution,
- projektowania pełnego runtime,
- zmian w TrustGraph / governance / constitution,
- tokena, blockchaina, mining,
- globalnego trust score,
- redesignu Intent Envelope,
- redesignu Specification bez konkretnego defektu,
- ukrytego podejmowania decyzji chronionych.

---

## 6. Twarda granica decyzyjna

> **System suggests. Human decides.**

Build Plan nie może zamieniać braku informacji w zgodę na wykonanie.

`UNRESOLVED` pozostaje blokadą wykonania.

Decyzje konstytucyjne, ontologiczne, trust, governance i security pozostają decyzjami człowieka.

---

## 7. Metoda pracy

Obowiązuje TDD:

1. kontrakt,
2. testy,
3. provenance,
4. origin semantics,
5. blocking rules,
6. determinism,
7. minimalna implementacja,
8. CI,
9. evidence,
10. closeout.

Nie implementować przed uzgodnieniem kontraktu.

---

## 8. Kryterium wyjścia

SES-010 może zostać zamknięta, gdy istnieje:

- jawny kontrakt Build Plan,
- deterministyczna lub jawnie ograniczona transformacja Specification → Build Plan,
- pełna traceability,
- jawne origin semantics,
- blokady dla `UNRESOLVED` i niedozwolonych stanów,
- testy,
- rzeczywisty CI evidence.

---

## 9. Pierwsze zadanie

> **Najpierw zdefiniować kontrakt Build Plan i granicę między Specification a Execution. Nie implementować wykonania.**

---

## 10. Kamień wejściowy SES-010

> **SES-009 zamknięta jako PASS. Evidence gap został zamknięty rzeczywistym CI. Specification pozostaje zweryfikowaną warstwą wejściową. SES-010 rozpoczyna projektowanie jawnego Build/Execution Plan bez przechodzenia do autonomicznego wykonania.**
