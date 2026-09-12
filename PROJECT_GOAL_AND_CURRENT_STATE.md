# System Builder — Aktualny stan, cel pośredni i cel ostateczny

**Data:** 2026-09-12  
**Status:** ACTIVE / SOURCE OF TRUTH  
**Repozytorium:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`

## 1. Po co powstał ten dokument

Ten plik zapisuje aktualny stan projektu, najbliższy cel, cel ostateczny oraz zasady autonomicznej pracy.

Repozytorium jest Source of Truth. Chat dostarcza kontekstu, ale stan projektu, dowody i decyzje mają być zapisane w repozytorium.

## 2. Aktualny stan po pełnym audycie i E2E

Projekt ma zweryfikowane kolejne granice od budowania planu do dostarczenia wewnętrznego manifestu:

`INTENT → UNDERSTAND → SPECIFICATION → BUILD PLAN → HUMAN APPROVAL → EXECUTION AUTHORIZATION → EXECUTION REQUEST → EXECUTION → RESULT → EFFECT → VERIFICATION → DELIVERY`

SES-030 ustanowił `EXECUTION_EFFECT → VERIFICATION`. `VERIFIED` oznacza wyłącznie weryfikację kontraktu/proweniencji; nie jest dowodem wystąpienia efektu w świecie zewnętrznym.

SES-031 ustanowił `VERIFICATION → DELIVERY`, gdzie `DELIVERY` oznacza obecnie **wewnętrzny, odtwarzalny manifest dostarczenia**, a nie transmisję do systemu zewnętrznego.

SES-032 ustanowił rzeczywisty test end-to-end łączący istniejące elementy w jeden spójny przepływ od Intent do Delivery Manifest. Test obejmuje rzeczywistą granicę Human Approval oraz propagację `authorization_source` do `EXECUTION_EFFECT`.

Następnie zamknięto konkretną lukę wykonawczą: lokalny executor wykonuje rzeczywistą operację `create` w systemie plików. SES-032 został rozszerzony o obserwację rzeczywiście utworzonego artefaktu i dowód `EVIDENCE_READY` powiązany z `EXECUTION_EFFECT`.

### Dowód C0 / SES-033

Commit: `72347125ff5e59973353a735f057ca6b42b79b9e`  
CI: **6/6 check-runs SUCCESS**  
Kluczowe runy: `34660091139` (`e2e`), `34660091254` (`local-execution`).

Potwierdzony przepływ:

`APPROVED BUILD PLAN → REAL LOCAL EXECUTION → REAL ARTIFACT → OBSERVATION → EVIDENCE → EXECUTION RESULT → EFFECT → VERIFICATION → DELIVERY MANIFEST`

Weryfikacja artefaktu jest rzeczywista: E2E sprawdza istnienie pliku, identyfikator artefaktu oraz powiązanie dowodu z `EXECUTION_EFFECT`.

## 3. Stan celu pośredniego C0

C0 — Canonical Runtime Verification — jest zamknięte. Kontrakty runtime oraz regresja SES-023–028 są potwierdzone, a lokalny efekt wykonania ma teraz własną obserwację i dowód.

Nie należy ponownie otwierać C0 bez konkretnej, wykazanej luki funkcjonalnej.

Nie będziemy sztucznie rozszerzać C0 ani tworzyć kolejnych sesji tylko po to, aby je numerować.

## 4. Najbliższa rzeczywista granica Beta

Po zamknięciu C0 pozostała jedna istotna luka integracyjna: **E2E dowodzi całego przepływu, ale przepływ nadal jest składany bezpośrednio w teście z wielu modułów SES. Nie istnieje jeszcze jeden produkcyjny entrypoint/orchestrator System Buildera, który przyjmuje Intent i prowadzi cały zweryfikowany przepływ do Delivery Manifest.**

Najbliższy cel:

`INTENT → SYSTEM BUILDER ENTRYPOINT → EXISTING VERIFIED CHAIN → DELIVERY MANIFEST`

Warunek zakresu:
- wykorzystać istniejące moduły i kontrakty,
- nie tworzyć drugiego runtime obok `src/runtime/`,
- nie zmieniać semantyki authorization/execution/effect/verification,
- nie dodawać external delivery,
- nie dodawać P2P/UDP, agentów, Trust, persistence ani UI,
- najpierw RED tylko wtedy, gdy brak testu dla jednego produkcyjnego entrypointu jest rzeczywistą luką,
- minimalna implementacja i jeden E2E dowód uruchamiający ten entrypoint.

To jest obecnie najbardziej bezpośrednia granica prowadząca do funkcjonalnej Beta System Buildera.

## 5. Najważniejsze błędy, których nie powtarzamy

1. **Nie mnożymy sesji i kontraktów dla samego postępu.** Sesja musi mieć rzeczywisty cel funkcjonalny, dowód lub konieczne zamknięcie.
2. **Nie tworzymy sztucznego RED.** Jeżeli kod już spełnia wymaganie, brak jest w testach/dowodzie, a nie w implementacji.
3. **Nie deklarujemy GREEN bez rzeczywistego testu/CI odnoszącego się do aktualnego kodu.**
4. **Każdą sesję kontrolujemy jako część całego projektu.** Lokalnie poprawna zmiana może być globalnie błędna.
5. **Minimalistyczna maksymalizacja:** najmniejsza ilość kodu, testów i dokumentacji potrzebna do zamknięcia rzeczywistej luki.
6. **Nie wzmacniamy semantyki bez decyzji:** `AUTHORIZED ≠ REQUESTED ≠ EXECUTION_ATTEMPT ≠ EXECUTED ≠ RESULT ≠ EFFECT`; `VERIFIED ≠ real-world effect`; `DELIVERY MANIFEST ≠ external transmission`.
7. **Nie dokładamy P2P/UDP, agentów, Trust, persistence, płatności, integracji zewnętrznych ani nowych znaczeń Constitution/Ontology/protocol bez dowodu, że są potrzebne dla najbliższego celu.**
8. **Nie tworzymy duplikatów runtime.** `src/runtime/` pozostaje canonical runtime; `sessions/` to kontrakty, testy, dowody i historia.
9. **Dokumentacja stanu musi być aktualizowana po istotnym przejściu.** Nie wolno pozostawiać starego numeru sesji jako aktualnego stanu.
10. **Celem jest zakończenie działającego Beta, nie nieskończony ciąg sesji.** Przy każdym kroku pytanie kontrolne brzmi: „Czy to materialnie przybliża nas do działającej Beta?”

## 6. Zasada pracy

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST (tylko gdy luka jest rzeczywista) → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CLOSE`

Po zamknięciu krótkiego celu ponownie kontrolujemy cały projekt i dopiero wtedy wybieramy następny.

Rutynowa inspekcja, testy, dokumentacja i commity są autonomiczne w już delegowanym zakresie.

Każdy checkpoint:

`STATE → EVIDENCE → GAP → DECISION → ACTION → NEXT`

Maksymalnie 5 istotnych działań na checkpoint.

## 7. Cel ostateczny

Funkcjonalny Beta System Builder / P2P 60-24 OneClick Evo Positiv:

`INTENT → UNDERSTAND → SPECIFICATION → BUILD PLAN → HUMAN APPROVAL → EXECUTION AUTHORIZATION → EXECUTION REQUEST → EXECUTION → RESULT → EFFECT → VERIFICATION → DELIVERY`

System ma rozumieć, projektować, budować, testować i dostarczać, przy zachowaniu ludzkiej kontroli nad decyzjami wymagającymi człowieka.

## 8. Kryterium zakończenia

Nie uznajemy celu za osiągnięty na podstawie deklaracji. Potrzebny jest aktualny, odtwarzalny dowód w repozytorium.

**Kierunek nadrzędny: nie budować więcej kodu niż potrzeba. Najpierw udowodnić istniejące elementy, potem naprawić tylko rzeczywiste luki, a następnie zakończyć Beta.**
