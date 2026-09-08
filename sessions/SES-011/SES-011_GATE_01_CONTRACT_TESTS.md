# SES-011 — GATE 01 — CONTRACT TESTS

**Projekt:** P2P 60-24 OneClick Evo Positiv
**Sesja:** SES-011
**Status:** OPEN — TDD GATE
**Źródło:** `sessions/SES-010/SES-010_BUILD_PLAN_CONTRACT.md`

## 1. Cel

Gate 01 weryfikuje zgodność testów kontraktowych z kontraktem BuildPlan ustanowionym w SES-010.

Przed implementacją transformatora:

`Specification → BuildPlan`

testy MUSZĄ definiować rzeczywiste wymagania kontraktu.

## 2. Zasada

**Contract → Tests → RED → Implementation → GREEN**

Transformer nie może zmieniać znaczenia kontraktu.

## 3. Zakres weryfikacji

Testy MUSZĄ zabezpieczać:

- strukturę BuildPlan;
- `contract_version`;
- status planowania;
- objective;
- steps;
- origin semantics;
- `DERIVED`;
- `PROPOSED`;
- `UNRESOLVED`;
- provenance;
- blockers;
- human approval;
- protected decisions;
- determinism;
- stabilne identity;
- stabilne ordering;
- odrzucenie nieważnej Specification;
- brak skutków ubocznych;
- brak możliwości syntetycznego approval.

## 4. Reguły krytyczne

### UNRESOLVED

`UNRESOLVED` MUSI pozostać nierozstrzygnięte.

MUSI powodować blokadę planu i nie może prowadzić do wykonania.

### PROPOSED

`PROPOSED` MUSI zachować swoje pochodzenie.

MUSI wymagać decyzji człowieka.

Transformer NIE MOŻE automatycznie zamienić `PROPOSED` w `DERIVED` ani wygenerować zatwierdzenia.

### Provenance

Każdy element związany z wykonaniem MUSI posiadać wymagane pochodzenie.

Minimalna relacja:

`Specification Element → BuildPlan Element → provenance`

### Determinism

Dla identycznej kanonicznej Specification i identycznej wersji kontraktu wynik pochodny MUSI być stabilny.

Nie wolno uzależniać semantyki od:

- czasu;
- losowości;
- próbkowania modelu;
- środowiska wykonawczego.

## 5. Gate PASS

Gate 01 może zostać oznaczony jako PASS wyłącznie wtedy, gdy:

1. testy odpowiadają kontraktowi SES-010;
2. wszystkie wymagania krytyczne mają test;
3. testy nie wprowadzają nowych decyzji architektonicznych;
4. brak implementacji transformatora nie narusza TDD;
5. RED wynika z braku implementacji, a nie z błędnego modelu testowego.

## 6. Gate FAIL

Gate 01 pozostaje FAIL, jeżeli:

- testy wymagają pól nieistniejących w kontrakcie;
- kontraktowe pola nie są testowane;
- `UNRESOLVED` nie blokuje planu;
- `PROPOSED` może zostać potraktowane jako `DERIVED`;
- approval może zostać syntetycznie wygenerowany;
- provenance może zostać pominięte;
- determinism nie jest zabezpieczony.

## 7. Kolejność

```text
SES-010 Contract
       ↓
Gate 01
       ↓
test_build_plan_contract.py v2
       ↓
RED
       ↓
Transformer
       ↓
GREEN
```

**Decyzja SES-011:**

> Nie implementować transformatora przed zamknięciem Gate 01.
