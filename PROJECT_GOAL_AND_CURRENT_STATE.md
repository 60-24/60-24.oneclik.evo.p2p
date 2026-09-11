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

Najnowszy stan `main` jest zapisany w kolejnych commitach po SES-032; ostatnia zmiana funkcjonalna dodaje **rzeczywiste lokalne wykonanie** BuildPlanu, a następnie E2E łączy ten efekt z istniejącym łańcuchem dowodowym.

Aktualna granica Beta:

`APPROVED BUILD PLAN → REAL LOCAL EXECUTION → ARTIFACT → EXECUTION RESULT → EFFECT → VERIFICATION → DELIVERY MANIFEST`

Nowy executor jest celowo lokalny i ograniczony do akcji `create`. Wykonuje rzeczywisty zapis artefaktu do systemu plików. Nie oznacza to jeszcze wykonania zdalnego ani transmisji zewnętrznej.

Minimalny canonical runtime pozostaje:

`INPUT → ENTRYPOINT → OBSERVATION → EVIDENCE`

Canonical implementation runtime znajduje się w `src/runtime/`.

## 3. Stan celu pośredniego C0

C0 — Canonical Runtime Verification — jest osiągnięte na poziomie ustanowionych kontraktów runtime i regresji SES-023–028.

Pełna integracja późniejszego cyklu System Buildera ma rzeczywisty dowód E2E w SES-032. Nie należy ponownie otwierać C0 bez konkretnej, wykazanej luki funkcjonalnej.

Nie będziemy sztucznie rozszerzać C0 ani tworzyć kolejnych sesji tylko po to, aby je numerować.

## 4. Cel najbliższy

### Domknięcie minimalnej funkcjonalnej granicy Beta

Najważniejsza wykazana luka po SES-032 była konkretna: wcześniejszy przepływ tworzył `EXECUTION_ATTEMPT` i `EXECUTION_RESULT` jako rekordy kontraktowe, ale nie wykonywał rzeczywistej operacji.

Zamknięto minimalną część tej luki przez lokalny executor:

`APPROVED BUILD PLAN → REAL LOCAL FILESYSTEM EFFECT`

Executor:
- wymaga zatwierdzonego BuildPlanu,
- wykonuje wyłącznie lokalną akcję `create`,
- tworzy rzeczywisty artefakt,
- zwraca identyfikator i ścieżkę artefaktu,
- nie wykonuje operacji zdalnych.

SES-032 został rozszerzony tak, aby E2E sprawdzał istnienie rzeczywiście utworzonego artefaktu, a jego identyfikator trafiał dalej do `EXECUTION_EFFECT` i `DELIVERY_MANIFEST`.

Dopiero po potwierdzeniu CI należy wybrać następną lukę. Nie zakładamy z góry, że będzie nią external delivery.

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
