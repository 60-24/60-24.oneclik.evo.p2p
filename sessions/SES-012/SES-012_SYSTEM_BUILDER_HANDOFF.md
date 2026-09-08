# SES-012 — SYSTEM BUILDER / NEXT CONTRACT
## Dokument przeniesienia i inicjacji nowej sesji

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repozytorium:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Poprzednia sesja:** SES-011  
**Bieżąca sesja:** SES-012  
**Status:** OPEN  
**Data:** 2026-09-08

---

## 1. Stan przekazania

SES-011 została przerwana z powodu długości sesji.

**WAŻNE:** nie oznaczać SES-011 jako PASS ani nie stawiać kamienia na podstawie samego przygotowania testów.

Ostatni znany stan techniczny:

- SES-010 Build Plan Contract pozostaje źródłem prawdy.
- SES-011 zawiera poprawiony zestaw testów kontraktowych.
- Ostatni commit SES-011: `1c299629e7d623a9429b57346a54c4536c51e6e1`.
- Transformer `Specification → BuildPlan` nadal NIE został zaimplementowany.
- Zmiany performance w SES-006 / SES-007 / SES-008 pozostają wstrzymane.
- Nie wykonywać żadnych zmian poza zakresem SES-012 bez osobnej decyzji.

---

## 2. Łańcuch obowiązujący

`Human Intent → Intent Envelope → Specification → Build Plan → Human Approval → Execution`

Granica SES-010:

`VALID Specification → BuildPlan → Human Approval → Execution`

Zasada nadrzędna:

> **System suggests. Human decides.**

---

## 3. Twarda metoda TDD

Obowiązuje bez wyjątków:

`CONTRACT → TEST → RED → IMPLEMENTATION → GREEN`

Nie implementować transformera przed potwierdzeniem poprawnego RED.

Nie deklarować PASS bez rzeczywistego evidence.

Nie stawiać kamienia przed PASS.

---

## 4. Pierwsze zadanie SES-012

### Gate 01 / kontynuacja SES-011

Najpierw:

1. zweryfikować aktualny stan repozytorium;
2. przejrzeć poprawione testy SES-011;
3. uruchomić testy;
4. potwierdzić, że RED wynika wyłącznie z braku implementacji transformera, a nie z błędnego testu;
5. dopiero wtedy formalnie zamknąć Gate 01;
6. następnie przejść do minimalnej implementacji transformera.

**Nie rozpoczynać implementacji przed wykonaniem punktów 1–5.**

---

## 5. Zakres SES-012

W zakresie:

- weryfikacja i domknięcie Gate 01;
- minimalny transformer `VALID Specification → BuildPlan`;
- zachowanie `DERIVED / PROPOSED / UNRESOLVED`;
- provenance;
- blocking rules;
- determinism;
- brak execution side effects;
- testy GREEN;
- rzeczywisty CI evidence;
- closeout dopiero po dowodzie.

Poza zakresem:

- deployment produkcyjny;
- remote execution;
- runtime orchestration;
- credentials / secrets;
- TrustGraph / governance / constitution;
- token / blockchain / mining;
- autonomiczna autoryzacja;
- niezwiązane optymalizacje wcześniejszych sesji.

---

## 6. Kryterium STOP

Jeżeli wystąpi:

- niejasny kontrakt,
- brak provenance,
- nierozstrzygnięta decyzja,
- sprzeczność,
- nieuprawniona zmiana zakresu,
- brak wiarygodnego evidence,

**STOP. Nie zgadywać.**

---

## 7. Zasada prowadzenia sesji

Pracujemy krótko i etapami.

Po każdym istotnym kroku raportujemy:

**STATUS → DOWÓD → DECYZJA → NASTĘPNY KROK**

Nie rozwijamy sesji poza konieczny zakres.

---

## 8. Oczekiwany rezultat SES-012

Końcowo ma istnieć:

`Specification → BuildPlan`

jako minimalna, przetestowana, deterministyczna granica planowania — bez autonomicznego wykonania.

Dopiero po rzeczywistym PASS:

**DOWÓD → KAMIEŃ → ZAMKNIĘCIE → kolejna sesja.**
