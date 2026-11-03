# SES-088 — BOOTSTRAP: FUNDAMENT BYTU I GAP SYSTEM BUILDERA

**Status:** przygotowanie kolejnej sesji; analiza wstępna wykonana, implementacja nie rozpoczęta  
**Branch:** `ses-088-foundation-and-system-builder-gap-audit`  
**Baza inspekcji:** `main` @ `a462b8f0073490f5423edf4d01dd0ce36642176f`  
**Repozytorium:** `60-24/60-24.oneclik.evo.p2p`  
**Tryb:** INSPECT → UNDERSTAND → GAP → RED → IMPLEMENT → GREEN → EVIDENCE → STONE

## 1. Geneza i cel nadrzędny

Pierwotnym pomysłem jest innowacyjny system P2P 60-24. W trakcie budowy okazało się, że system powinien móc ewoluować. Stąd potrzeba System Buildera: środowiska, które pozwoli osobie bez specjalistycznej wiedzy rozszerzać system — od pola formularza, przez pojęcia i relacje ontologii, aż po kompletny moduł.

System Builder wyrósł z potrzeb P2P; nie jest przypadkowym, niezależnym projektem. Należy rozdzielić odpowiedzialności, ale nie zakładać z góry rozdzielenia repozytoriów.

**Cel praktyczny:** człowiek opisuje potrzebę; system pomaga ją formalizować, budować, testować i weryfikować, zachowując ludzką kontrolę nad intencją i decyzjami chronionymi.

## 2. Zasada koncepcyjna

**Maksymalizacja przez minimalizację. Atomizacja. Autonomia. Modularność.**

Szukamy najmniejszego sensownego bytu informatycznego, który:
- ma określoną odpowiedzialność i granice;
- ma jawny kontrakt oraz stan;
- reaguje na jawnie zdefiniowane zdarzenia;
- może być niezależnie testowany i obserwowany;
- łączy się z innymi bytami bez ukrytego sprzężenia.

To kryteria robocze do sprawdzenia względem istniejących kontraktów, nie zatwierdzona nowa konstytucja.

## 3. Co potwierdza repozytorium

### 3.1 P2P runtime

Na `main` istnieje minimalny runtime P2P: tożsamość lokalna, handshake HELLO/WELCOME/AUTH, komunikacja TCP, ramkowanie i obsługa błędów protokołu. To działająca baza Node A ↔ Node B, ale nie kompletny produkt P2P ani globalny system zaufania.

Źródła:
- `docs/CURRENT_STATE.md`
- `docs/REPOSITORY_MAP.md`
- `sessions/SES-046/SES-046_MICROKERNEL_GENEALOGY.md`
- testy i workflow opisane w repozytorium.

### 3.2 System Builder

Istnieje rzeczywista ścieżka wykonawcza:
`Intent → Specification → BuildPlan → Authorization → Execution → Result/Effect → Observation/Evidence → Verification → Delivery Manifest`.

Kod wejściowy: `src/system_builder/entrypoint.py`.  
Executor: `src/execution/local_executor.py`.  
Demo: `demo/system_builder_demo.py`.  
Dowody historyczne: `BETA_COMPLETION_CLOSEOUT.md`, testy SES-034 i SES-035.

Istotne ograniczenie: aktualny executor dopuszcza akcję `create` i tworzy lokalne pliki tekstowe z treści kroków BuildPlan. Dowodzi to kontrolowanego, śledzalnego wykonania prostego artefaktu, ale **nie dowodzi jeszcze, że użytkownik potrafi rozszerzyć rzeczywisty runtime P2P lub ontologię przez System Buildera**.

Nie utożsamiać zamknięcia funkcjonalnej bety System Buildera z ukończeniem docelowej wizji.

### 3.3 Mikrokernel / Kernel-DNA / OmniKernel / StemCell

`sessions/SES-046/SES-046_MICROKERNEL_GENEALOGY.md` zachowuje ważne rozróżnienia:
- **OmniKernel** — wyższy poziom wspólnych mechanizmów/fundamentów ekosystemu;
- **Kernel-DNA** — kontrakty i niezmienniki dotyczące bytów, stanów, zdarzeń i relacji;
- **Microkernel** — minimalna techniczna infrastruktura/runtime;
- **Node** — konkretny autonomiczny uczestnik/runtime sieci, nie synonim Microkernela;
- **Module** — dołączana zdolność;
- **StemCell** — wzorzec modułu różnicującego się kontekstowo, nie synonim Node.

Ten model pozostaje roboczy/prowizoryczny, a nie zamrożoną architekturą. Nie tworzyć równoległego MiniKernelu bez wykazania luki w istniejącym rozwiązaniu.

### 3.4 Ontologia i autorytet

`sessions/SES-087/SES-087_GAP_ASSESSMENT.md` i `docs/ARCHITECTURE_AUTHORITY_INDEX.md` wskazują, że katalogi `ontology/` i `architecture/` są w dużej mierze strukturalne/dokumentacyjne. Historyczne propozycje nie stają się zatwierdzonymi kontraktami przez samo istnienie w repozytorium.

`sessions/SES-006/02_SYSTEM_BUILDER_MINIMAL_MODEL.md` to **WORKING MODEL — NOT CONSTITUTIONAL APPROVAL**. Jest wartościowym źródłem modelu Intent → Specification → Model → Build Plan → Artifact → Test/Evidence → Delivery, ale nie wolno przedstawiać go jako zatwierdzonej konstytucji.

### 3.5 Gałąź StemCell

`feature/stemcell-implementation` jest o 577 commitów za `main` i nie zawiera commitów wyprzedzających `main` według porównania wykonanego podczas inspekcji. Nie traktować jej jako aktualnej, niezależnej implementacji do scalania. Ewentualne wykorzystanie historycznych treści wymaga wskazania konkretnego artefaktu i sprawdzenia jego pochodzenia.

## 4. Wstępny GAP — do potwierdzenia przez dokładniejszą inspekcję

**GAP główny:** repozytorium ma działający, kontrolowany pipeline tworzenia prostych artefaktów oraz osobno działający runtime P2P, ale nie wykazano jeszcze ścieżki end-to-end, w której osoba nietechniczna opisuje potrzebę, a System Builder bezpiecznie tworzy i weryfikuje nową funkcję rzeczywistego systemu docelowego.

Brak potwierdzonego dowodu nie oznacza, że nie ma żadnych częściowej implementacji. Przed decyzją należy zmapować istniejące modele, kontrakty, wykonawcę, dozwolone operacje, testy i zależności.

## 5. Zasady nieprzekraczalne

- Repozytorium jest źródłem prawdy; rozmowa stanowi kontekst.
- Najpierw REUSE → INTEGRATE → IMPROVE → INVENT.
- Nie zmieniać po cichu Konstytucji, ontologii bazowej, modelu Trust ani fundamentalnych reguł bezpieczeństwa.
- Nie dodawać tokenów finansowych, portfeli ani globalnych ocen ludzi.
- Brak obowiązku użycia Docker/Kubernetes w produkcie końcowym lub wymuszania dodatkowej instalacji u użytkownika. Narzędzia developerskie nie mogą stać się zależnością użytkownika końcowego.
- Nie wykonywać historycznego skryptu publikacyjnego z pliku root `.bin`; zawiera niebezpieczny wzorzec umieszczania PAT w URL.
- Nie wykonywać masowych przenosin, nie scalać przestarzałej gałęzi StemCell i nie wprowadzać zmian runtime bez wykazanego GAP.
- Dla zmian YELLOW/RED przygotować propozycję i zachować granicę ludzkiej decyzji.

## 6. Pierwsze zadania nowej sesji

1. Odświeżyć HEAD `main` i dowody CI przed każdą decyzją.
2. Przeprowadzić mapowanie komponentów i kontraktów: P2P runtime, System Builder, Kernel-DNA/Microkernel, ontologia, testy oraz workflow.
3. Ustalić, które elementy minimalnego bytu są już rzeczywiście zaimplementowane i testowane, a które występują tylko w dokumentacji.
4. Wyznaczyć **jeden** najmniejszy demonstrator zgodny z istniejącymi kontraktami. Preferowany rezultat końcowy: kontrolowana zmiana funkcjonalności systemu docelowego, a nie samo wygenerowanie tekstu.
5. Najpierw określić test akceptacyjny i dowód. Dopiero potem RED → minimalna implementacja → GREEN → evidence.
6. Jeżeli zmiana wymaga zatwierdzenia konstytucyjnego/ontologicznego lub zmienia granice bezpieczeństwa, zatrzymać implementację i przedstawić decyzję człowiekowi.

### Kandydat na kryterium demonstratora (niezatwierdzony)

Osoba opisuje prostą, niechronioną zmianę; System Builder tworzy jawny model i plan, przedstawia zakres zmiany, wykonuje tylko dozwolone działania, uruchamia testy i pokazuje pochodzenie artefaktu oraz dowody. Test musi wykazać zmianę w docelowym systemie, nie tylko wygenerowanie dokumentu. Konkretną funkcję wybrać dopiero po sprawdzeniu istniejących interfejsów i kontraktów.

## 7. Granica statusu i kolejnej sesji

To jest przygotowanie bootstrapu, nie zamknięcie całego audytu SES-087 i nie deklaracja GREEN całego projektu. SES-087 zawiera jeszcze osobny temat bezpiecznego zbadania historycznego Git bundle; nie odtwarzać go bez walidacji.

Nowa sesja SES-088 powinna ruszyć po decyzji o zamknięciu/odłożeniu pozostałego zakresu SES-087. Ten dokument pozwala zachować kontekst bez traktowania propozycji jako zatwierdzonych decyzji.

## 8. Kryterium zakończenia SES-088

Sesja nie kończy się przez samą dokumentację ani przez sukces CI. Musi dostarczyć:
- mapę rzeczywistego stanu z linkami do kodu/testów/kontraktów;
- rozstrzygnięcie jednego konkretnego GAP albo udokumentowane NO GAP;
- uzasadniony minimalny następny krok;
- testy i dowody dla każdej wykonanej zmiany;
- jawny zapis decyzji wymagających ludzkiej zgody.

**Cel:** znaleźć najmniejszy prawidłowy, autonomiczny i testowalny fundament, z którego P2P może ewoluować, oraz ustalić, jak System Builder bezpiecznie umożliwi taką ewolucję osobie nietechnicznej.
