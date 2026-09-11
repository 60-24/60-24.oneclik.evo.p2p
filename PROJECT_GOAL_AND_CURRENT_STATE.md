# System Builder — Aktualny stan, cel pośredni i cel ostateczny

**Data:** 2026-09-11  
**Status:** ACTIVE / SOURCE OF TRUTH  
**Repozytorium:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`

## 1. Po co powstał ten dokument

Ten plik zapisuje w repozytorium wspólne ustalenie dotyczące **aktualnego stanu projektu, celu pośredniego, celu ostatecznego oraz kierunku dalszej autonomicznej pracy**.

Repozytorium jest Source of Truth. Chat dostarcza kontekstu, ale stan projektu, dowody i decyzje mają być zapisane w repozytorium.

## 2. Aktualny stan

Minimalny canonical runtime jest obecnie budowany i weryfikowany jako:

`INPUT → ENTRYPOINT → OBSERVATION → EVIDENCE`

SES-023–SES-028 ustanowiły i zweryfikowały kolejne kontrakty oraz regresje. SES-029 kontynuuje audyt całości runtime.

Najważniejsze zasady:

- canonical implementation znajduje się w `src/runtime/`,
- session directories zawierają kontrakty, testy, dowody i historię, a nie drugą implementację runtime,
- nie wolno tworzyć sztucznego RED,
- nie wolno deklarować GREEN bez rzeczywistego testu/CI,
- najpierw dowód i audyt, potem najmniejsza konieczna zmiana,
- nie rozszerzamy zakresu na P2P/UDP/Node/Agent/Trust bez uzasadnienia dowodowego.

## 3. Cel pośredni — C0

### Canonical Runtime Verification

Celem pośrednim jest doprowadzenie minimalnego runtime do stanu, w którym każdy istotny element przepływu:

`INPUT → ENTRYPOINT → OBSERVATION → EVIDENCE`

jest jednocześnie:

1. jednoznacznie zaimplementowany,
2. objęty testem/regresją,
3. wykonywany przez właściwy CI,
4. możliwy do odtworzenia,
5. posiada aktualny dowód zapisany w repozytorium,
6. pozbawiony ukrytych ścieżek i duplikatów,
7. zgodny z zasadą fail-closed tam, gdzie kontrakt tego wymaga.

**Definicja osiągnięcia C0:** nie musimy już pytać „czy runtime działa?”, ponieważ repozytorium samo pokazuje implementację, test, wykonanie CI i dowód.

## 4. Cel ostateczny

### Funkcjonalny Beta System Builder / P2P 60-24 OneClick Evo

Celem ostatecznym nie jest samo posiadanie kontraktów i testów. System ma wykonać rzeczywisty, kontrolowany cykl budowy systemu:

`INTENT → UNDERSTAND → SPECIFICATION → BUILD PLAN → HUMAN APPROVAL → EXECUTION AUTHORIZATION → EXECUTION REQUEST → EXECUTION → RESULT → EFFECT → VERIFICATION → DELIVERY`

Przy tym granice autoryzacji muszą pozostać jednoznaczne:

`AUTHORIZED ≠ REQUESTED ≠ EXECUTION_ATTEMPT ≠ EXECUTED ≠ RESULT ≠ EFFECT`

System ma **rozumieć, zaprojektować, zbudować, przetestować i dostarczyć**, ale decyzje wymagające człowieka pozostają po stronie człowieka.

## 5. Jak dochodzimy do celu

Pracujemy etapami, bez przeskakiwania warstw:

1. **SES-029:** dokończyć audyt canonical runtime i znaleźć najmniejszą rzeczywistą lukę.
2. **C0:** zamknąć pełną, odtwarzalną weryfikację minimalnego runtime.
3. **Następna granica System Builder:** przejść do kolejnego rzeczywistego elementu funkcjonalnego, dopiero gdy C0 jest dowiedzione.
4. **Execution chain:** połączyć kolejne granice bez mieszania authorization/request/attempt/result/effect.
5. **Functional beta:** wykazać działający minimalny pełny cykl od intencji do zweryfikowanego rezultatu/dostarczenia.

## 6. Zasada pracy od teraz

Dalsza praca jest autonomiczna w zakresie już delegowanym.

Standardowy cykl:

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CONTINUE`

Nie tworzyć sztucznego RED. Jeżeli implementacja jest poprawna, ale brakuje dowodu lub regresji, uzupełnić właśnie ten brak.

Każdy checkpoint ma kończyć się:

`STATE → EVIDENCE → GAP → DECISION → ACTION → NEXT`

Maksymalnie 5 istotnych działań na checkpoint.

## 7. Kryterium sukcesu

Nie uznajemy celu za osiągnięty na podstawie deklaracji. Uznajemy go dopiero wtedy, gdy repozytorium zawiera wystarczający, aktualny i możliwy do odtworzenia dowód.

**Kierunek nadrzędny:** nie budować więcej kodu niż potrzeba. Budować tylko to, co prowadzi do rzeczywiście działającego System Buildera.
