# SES-019 — Minimal Execution Result

**Status:** STARTED  
**Date:** 2026-09-10  
**Previous gate:** SES-018 = GREEN / PASSED  
**Previous boundary:** `EXECUTION_REQUESTED → EXECUTION_ATTEMPT → STOP`

## 1. Cel sesji

Zdefiniować i zweryfikować minimalny, jawny kontrakt **Execution Result** jako następny etap po `EXECUTION_ATTEMPT`.

Sesja nie implementuje rzeczywistych side effects ani autonomicznego wykonania.

## 2. Zasada nadrzędna

`AUTHORIZED ≠ REQUESTED ≠ EXECUTION_ATTEMPT ≠ EXECUTED`

Wynik wykonania może powstać wyłącznie jako jawny rezultat wcześniej utworzonej próby wykonania. Nie może być utożsamiony z autoryzacją, żądaniem ani samą próbą.

## 3. Zakres

### IN
- minimalny obiekt `EXECUTION_RESULT`;
- powiązanie wyniku z `EXECUTION_ATTEMPT`;
- jawny status rezultatu;
- minimalna informacja o powodzeniu/niepowodzeniu;
- ochrona tożsamości `build_plan_id`;
- testy kontraktowe TDD;
- dowód CI.

### OUT
- rzeczywiste operacje systemowe;
- sieć, procesy, pliki lub inne side effects;
- retry/orchestration;
- autonomiczne decyzje AI;
- rozbudowany model błędów;
- płatności lub transfer wartości.

## 4. Oczekiwany minimalny kontrakt

Przewidywany przepływ:

`EXECUTION_AUTHORIZATION → EXECUTION_REQUEST → EXECUTION_ATTEMPT → EXECUTION_RESULT`

Minimalny wynik powinien jednoznacznie wskazywać:

- `status = EXECUTION_RESULT`;
- źródło = `EXECUTION_ATTEMPT`;
- `build_plan_id` zgodny z próbą;
- identyfikację/powiązanie z próbą wykonania;
- jawny stan rezultatu;
- brak możliwości udawania wyniku bez poprawnej próby.

Dokładne pola zostaną ustalone przez test kontraktowy, a nie przez implementację.

## 5. TDD — kolejność

1. Zdefiniować test RED dla minimalnego Execution Result.
2. Uruchomić CI i potwierdzić RED jako dowód brakującego kontraktu.
3. Wprowadzić minimalną implementację.
4. Uruchomić CI.
5. Oczekiwany wynik: GREEN / PASSED.
6. Zamknąć SES-019 i zapisać dowód.

## 6. Kryterium GATE

**GREEN / PASSED**, gdy CI potwierdzi kontrakt Execution Result oraz zachowanie granic:

- brak wyniku bez `EXECUTION_ATTEMPT`;
- brak zmiany autoryzacji przez wynik;
- brak utożsamienia `EXECUTION_ATTEMPT` z `EXECUTED`;
- zgodność `build_plan_id`;
- brak niejawnych side effects.

## 7. Następny krok po SES-019

Dopiero po GREEN zostanie oceniona potrzeba kolejnej granicy wykonawczej. Nie rozszerzać zakresu bez dowodu, że obecna granica jest stabilna.

---

**Project Lead Decision:** SES-019 rozpoczyna się od kontraktu i testu RED. Minimalizacja zakresu obowiązuje.
