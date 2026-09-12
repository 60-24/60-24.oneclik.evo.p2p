# SES-035 — Istotny dokument projektowy

**Data:** 2026-09-12  
**Status:** zapisane w Source of Truth  
**Sesja:** SES-035 — Human Approval Production EntryPoint Proof

## Dlaczego ten dokument jest wartościowy

SES-035 zamyka ważną lukę w dowodzie działania System Buildera: pokazuje, że granica **jawnej decyzji człowieka** jest zachowana również wtedy, gdy przepływ przechodzi przez rzeczywisty produkcyjny EntryPoint.

Nie wystarcza dowód, że poszczególne kontrakty działają osobno. Wartość SES-035 polega na sprawdzeniu ich połączenia w realnym wejściu systemowym, przy zachowaniu rozdzielenia:

`PROPOSED INTENT → READY_FOR_APPROVAL → HUMAN APPROVAL → PRODUCTION ENTRYPOINT → REAL EXECUTION → RESULT → EFFECT → VERIFICATION → DELIVERY`

## Najważniejsze ustalenia

### 1. Human Approval jest rzeczywistą granicą

Dla planu wymagającego zatwierdzenia produkcyjny EntryPoint nie może wykonać działania bez jawnej zgody człowieka.

Brak zgody musi zakończyć przepływ błędem i bez utworzenia efektu wykonania.

### 2. Zgoda musi być związana z konkretnym BuildPlan

Samo `approved=true` nie wystarcza. Zgoda musi wskazywać dokładnie ten `build_plan_id`, który ma zostać wykonany.

Niezgodny identyfikator jest odrzucany fail-closed i nie może wywołać efektu wykonania.

### 3. Authorization ≠ Approval

Nadal obowiązuje fundamentalna zasada:

`AUTHORIZATION ≠ APPROVAL`

Human Approval jest źródłem autoryzacji w ścieżce wymagającej decyzji człowieka, ale nie jest z nią utożsamiane.

### 4. Provenance autoryzacji jest istotna

Dla ścieżki jawnej decyzji człowieka wymagane jest źródło:

`EXPLICIT_HUMAN_APPROVAL`

Nie można zastąpić go `VALIDATED_NO_APPROVAL_REQUIRED`.

### 5. Ścieżka bez zgody człowieka pozostaje odrębna

Jeżeli BuildPlan ma:

`VALIDATED + approval.required=false + approval.status=NOT_REQUIRED`

może legalnie przejść przez:

`AUTHORIZED / VALIDATED_NO_APPROVAL_REQUIRED`

bez sztucznego wymagania Human Approval.

## Granica dowodu

SES-035 **nie wprowadza nowego mechanizmu Proposal do produkcji**. Test izoluje granicę produkcyjnego EntryPoint, przekazując mu już poprawną reprezentację `PROPOSED` Specification.

Jest to świadome ograniczenie zakresu: celem jest dowód zachowania EntryPoint, a nie rozszerzanie architektury.

## Zasada projektowa

> System może zaproponować. System może przygotować plan. System nie może sam dopisać zgody człowieka.

Dla każdego przepływu należy utrzymywać rozróżnienie:

`PROPOSAL → APPROVAL → AUTHORIZATION → REQUEST → ATTEMPT → RESULT → EFFECT`

Żaden etap nie może być traktowany jako dowód wykonania następnego.

## Wniosek dla dalszego projektu

Nie należy dodawać kolejnej warstwy architektury tylko dlatego, że poprzednie kontrakty są już poprawne. Następny krok powinien wynikać z **najmniejszej rzeczywistej luki funkcjonalnej**, potwierdzonej przez repozytorium i CI.

SES-035 jest więc kamieniem kontrolnym dla zasady:

**najpierw rzeczywisty przepływ → potem dowód → dopiero potem kolejna funkcja.**

---

**Source of Truth:** repozytorium `60-24/60-24.oneclik.evo.p2p`  
**Sesja referencyjna:** `sessions/SES-035/`  
**Zasada:** brak fałszywego PASS; stan projektu musi wynikać z kodu, testów i CI.
