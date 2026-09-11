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

SES-032 ustanowił rzeczywisty test end-to-end łączący istniejące elementy w jeden spójny przepływ od Intent do Delivery Manifest. Test obejmuje również rzeczywistą granicę Human Approval oraz propagację `authorization_source` do `EXECUTION_EFFECT`.

Aktualny commit `main`:

`c4753b34f864e84e5831ab7f1924955613c6cf90` — `fix(SES-021): propagate optional authorization provenance`

Na tym commicie SES-032 E2E jest potwierdzone przez GitHub Actions:

- workflow/job: `e2e`
- run: `34658589204`
- check: `103456173236`
- status: `completed / success`

Na tym samym commicie wszystkie wykryte checki GitHub Actions zakończyły się sukcesem. Poprawka SES-021 zachowuje kompatybilność z wcześniejszymi kontraktami.

Minimalny canonical runtime pozostaje:

`INPUT → ENTRYPOINT → OBSERVATION → EVIDENCE`

Canonical implementation runtime znajduje się w `src/runtime/`.

## 3. Stan celu pośredniego C0

C0 — Canonical Runtime Verification — jest osiągnięte na poziomie ustanowionych kontraktów runtime i regresji SES-023–028.

Pełna integracja późniejszego cyklu System Buildera ma teraz rzeczywisty dowód E2E w SES-032. Nie należy ponownie otwierać C0 bez konkretnej, wykazanej luki funkcjonalnej.

Nie będziemy sztucznie rozszerzać C0 ani tworzyć kolejnych sesji tylko po to, aby je numerować.

## 4. Cel najbliższy

### Ocena najmniejszej rzeczywistej luki prowadzącej do Beta

Cel integracyjny `INTENT → ... → VERIFICATION → DELIVERY MANIFEST` jest **zamknięty dowodem E2E**.

Następny krok nie polega na tworzeniu kolejnej abstrakcyjnej granicy. Należy ponownie przeanalizować cały przepływ względem kryterium funkcjonalnej Beta i znaleźć **najmniejszą rzeczywistą lukę**, która uniemożliwia uznanie System Buildera za użyteczny Beta.

Jeżeli luka nie istnieje na poziomie obecnego celu — nie dodawać kodu. Jeżeli istnieje — zamknąć ją minimalną zmianą, testem i dowodem CI.

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
