# Agentic Engineering Environment v0.1

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repozytorium:** `60-24/60-24.oneclik.evo.p2p`  
**Status:** PROPOSAL / INSTRUCTION  
**Data:** 2026-09-27  

## 1. Cel

Zwiększyć tempo rozwoju projektu przez kontrolowaną współpracę wyspecjalizowanych agentów AI, bez utraty:

- repozytorium jako technicznego źródła prawdy;
- kontroli człowieka nad decyzjami RED;
- zasady „System suggests. Human decides.”;
- dowodów: testy, CI, artefakty, logi i dokumentacja;
- minimalnego, celowego zakresu zmian;
- rozróżnienia REAL GAP / FEATURE / TODO / OPINIA / DUPLIKAT.

Nie budujemy chaotycznego „swarmu”. Budujemy **Agentic Engineering System**.

## 2. Główna zasada

> Agenci wykonują pracę. Repozytorium przechowuje prawdę. Człowiek zachowuje decyzje RED.

## 3. Przepływ pracy

```text
INSPECT
  ↓
ARCHITECT / GAP-HUNTER
  ↓
TEST DESIGN
  ↓
RED
  ↓
IMPLEMENTATION
  ↓
REVIEW
  ↓
SECURITY REVIEW
  ↓
CI / VERIFICATION
  ↓
EVIDENCE
  ↓
DOCUMENTATION
  ↓
STONE / CLOSED
  ↓
NEXT REAL GAP
```

Żaden etap nie może być pominięty bez udokumentowanego powodu.

## 4. Minimalny skład agentów v0.1

### A0 — ORCHESTRATOR

Rola: Project Lead / Conductor.

Odpowiedzialność:

- odczyt aktualnego stanu repozytorium;
- kontrola sesji, GAP-ów, testów i CI;
- delegowanie zadań;
- pilnowanie zakresu;
- rozpoznanie GREEN / YELLOW / RED;
- zatrzymanie pracy przy konflikcie lub braku dowodów;
- przygotowanie checkpointu STONE.

Orchestrator nie powinien samodzielnie wykonywać dużych zmian architektonicznych.

### A1 — GAP-HUNTER

Rola: wykrywanie rzeczywistych luk.

Analizuje:

- kod;
- testy;
- workflow CI;
- artefakty;
- sesje;
- README i dokumentację;
- granice bezpieczeństwa.

Każdy kandydat musi zostać sklasyfikowany jako:

- REAL GAP;
- FEATURE;
- TODO;
- OPINIA;
- DUPLIKAT;
- brak wystarczających dowodów.

Agent nie może tworzyć sztucznego GAP-u tylko po to, aby kontynuować pracę.

### A2 — TEST-ENGINEER

Rola: przygotowanie dowodu RED.

Dostaje potwierdzony GAP i tworzy test, który:

1. pokazuje istniejący problem;
2. kończy się RED przed implementacją;
3. definiuje oczekiwane GREEN;
4. nie rozszerza niepotrzebnie zakresu.

### A3 — CODER

Rola: minimalna implementacja.

Dostaje wyłącznie:

- potwierdzony GAP;
- test RED;
- ograniczenia architektury;
- dozwolone pliki;
- oczekiwany rezultat.

Zasada:

> Smallest coherent change.

Coder nie może przy okazji przebudowywać protokołu, ontologii, modelu Trust ani innych warstw.

### A4 — REVIEWER

Rola: niezależna kontrola.

Sprawdza:

- czy GAP rzeczywiście istniał;
- czy RED był prawdziwy;
- czy implementacja rozwiązuje GAP;
- czy zakres nie został rozszerzony;
- czy nie powstały nowe problemy;
- czy test dowodzi rozwiązania;
- czy dokumentacja nie udaje dowodu.

## 5. Agenci opcjonalni po v0.1

### ARCHITECT

Kontroluje zgodność propozycji z Constitution, ontologią, warstwami i istniejącymi decyzjami.

### SECURITY

Analizuje m.in.:

- handshake;
- identity binding;
- authentication;
- malformed frames;
- replay;
- disconnect;
- resource exhaustion;
- granice zaufania.

### VERIFIER

Uruchamia i kontroluje:

- testy;
- build;
- packaging;
- smoke tests;
- CI;
- artefakty.

### DOCUMENTATION

Po GREEN aktualizuje:

- README;
- P2P_NODE.md;
- sesję;
- closeout;
- indeks dowodów.

Dokumentacja nie może być aktualizowana w celu zastąpienia brakującego testu lub CI.

## 6. Poziomy decyzji

### GREEN — autonomicznie

- testy;
- dokumentacja;
- refaktoryzacje bez zmiany kontraktu;
- bezpieczne poprawki błędów;
- małe, niełamliwe ulepszenia;
- przygotowanie dowodów.

### YELLOW — wymaga kontroli człowieka

- zmiana API;
- zmiana protokołu;
- zmiana modelu danych;
- zmiana kontraktu między warstwami;
- istotne nowe zależności;
- zmiana zachowania użytkowego o szerszym skutku.

### RED — decyzja człowieka

- Constitution;
- fundamentalna ontologia;
- model Trust;
- fundamentalne reguły bezpieczeństwa i governance;
- zasadnicza zmiana kierunku projektu.

### BLACK — STOP

Praca musi zostać zatrzymana przy:

- sprzeczności z Constitution;
- naruszeniu niezmiennika;
- niebezpiecznym lub nieznanym stanie;
- braku wystarczających dowodów;
- konflikcie między agentami bez rozstrzygnięcia.

## 7. WORK_PACKET

Każde zadanie przekazywane między agentami powinno mieć formalny pakiet:

```yaml
work_packet:
  id: GAP-XXX
  type: real_gap
  status: RED

  source:
    session: SES-XXX
    evidence:
      - path: ...
      - test: ...
      - ci_run: ...

  scope:
    allowed:
      - src/...
      - tests/...
    forbidden:
      - protocol redesign
      - trust model
      - ontology

  expected:
    red: true
    green: true

  decision_level: GREEN
```

WORK_PACKET musi zawierać co najmniej:

- identyfikator;
- źródło i dowody;
- opis GAP-u;
- zakres dozwolony;
- zakres zakazany;
- oczekiwany RED;
- oczekiwany GREEN;
- poziom decyzji;
- właściciela zadania.

## 8. Dostęp agentów

| Agent | Odczyt repo | Edycja | Testy | GitHub | Merge |
|---|---:|---:|---:|---:|---:|
| Orchestrator | tak | ograniczona | tak | tak | kontrola |
| Architect | tak | nie | tak | tak | nie |
| Gap Hunter | tak | nie | tak | tak | nie |
| Test Engineer | tak | testy | tak | nie | nie |
| Coder | tak | kod i testy | tak | nie | nie |
| Reviewer | tak | nie | tak | tak | nie |
| Security | tak | nie | tak | tak | nie |
| Verifier | tak | nie | tak | tak | nie |
| Documentation | tak | docs | tak | nie | nie |

Żaden agent nie powinien mieć nieograniczonego prawa do zmiany wszystkiego.

## 9. Branching

Zmiany nie powinny być wykonywane bezpośrednio na `main`.

```text
main
 └── agent/gap-XXX
       ├── RED
       ├── implementation
       ├── tests
       ├── review
       ├── CI
       ├── evidence
       └── PR
```

Do `main` trafia wyłącznie zmiana z kompletem dowodów i zamkniętym zakresem.

## 10. Pamięć systemu

Na początku repozytorium pozostaje główną pamięcią systemu.

Proponowana struktura przyszłej warstwy pomocniczej:

```text
.agent/
  state.yaml
  rules.md
  decisions/
  work/
  evidence/
  checkpoints/
```

Nie tworzymy od razu osobnej bazy wektorowej. Najpierw porządkujemy stan w repo.

## 11. Dwa tory pracy

### TOR A — CONTROL

```text
INSPECT → GAP → RED → REVIEW → CI → EVIDENCE → STONE
```

### TOR B — BUILD

```text
ARCHITECT → DESIGN → CODE → TEST → BUILD
```

Tor B może przyspieszać projekt, ale nie może omijać potwierdzenia GAP-u, RED, review i weryfikacji.

Równolegle można prowadzić:

- badania;
- analizę architektury;
- niezależne propozycje;
- przygotowanie testów dla niezależnych obszarów.

Nie wolno równolegle modyfikować tych samych plików bez koordynacji.

## 12. Automatyzacja docelowa

Docelowy cykl może być uruchamiany poleceniem typu:

```text
RUN PROJECT CYCLE
```

Cykl:

1. inspect repo;
2. inspect latest CI;
3. inspect sessions;
4. find candidate GAPs;
5. eliminate false GAPs;
6. select one real GAP;
7. generate RED test;
8. run RED;
9. implement;
10. run tests;
11. reviewer;
12. security review;
13. CI;
14. collect evidence;
15. update docs;
16. prepare STONE.

Jeśli RED nie potwierdzi problemu — STOP i powrót do GAP-HUNTER.  
Jeśli pojawi się konflikt architektoniczny — YELLOW/RED.  
Jeśli GREEN i dowody są kompletne — STONE.

## 13. Zasada technologiczna v0.1

Nie budujemy teraz własnego frameworka agentowego.

Pierwsza implementacja środowiska powinna wykorzystywać:

- GitHub jako repozytorium, Issues, PR i Actions;
- custom agents / role agents;
- CI jako warstwę weryfikacji;
- artefakty i logi jako dowody;
- repo jako pamięć i stan.

Dopiero po sprawdzeniu pętli można dodawać:

- większą równoległość;
- automatyczne PR;
- trwalszą pamięć;
- dodatkowych agentów;
- bardziej rozbudowany orchestrator.

## 14. Kryterium sukcesu

Środowisko uznajemy za udane, jeśli:

- skraca czas od REAL GAP do GREEN;
- zwiększa ilość dostarczonego, działającego kodu;
- nie osłabia jakości dowodów;
- nie tworzy sztucznych GAP-ów;
- nie narusza granic GREEN/YELLOW/RED;
- utrzymuje repozytorium jako Source of Truth;
- kończy pracę kontrolowanym STONE.

## 15. Najbliższy krok

Zaprojektować i wdrożyć minimalne elementy v0.1:

1. strukturę `.github/agents/`;
2. kontrakt `WORK_PACKET`;
3. stany `RED / GREEN / STONE`;
4. pierwszego Orchestratora;
5. test pilotażowy na następnym rzeczywistym GAP-ie.

Nie rozpoczynać od wielkiego swarmu. Najpierw udowodnić działanie jednej pełnej pętli:

```text
REAL GAP → RED → CODE → REVIEW → CI → EVIDENCE → STONE
```
