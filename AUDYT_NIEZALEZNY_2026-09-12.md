# Audyt niezależny — `60-24/60-24.oneclik.evo.p2p`

**Data:** 2026-09-12
**Zakres:** gałąź `main`, HEAD `439e5c2` (`docs(SES-032): record real approval-boundary finding`)
**Charakter:** audyt zewnętrzny. Dokumenty `AGENTS.md`, `P2P_60-24_ENGINEERING_CONSTITUTION_v1.0.md`, `constitution/` i `sessions/` potraktowano wyłącznie jako materiał do analizy, nie jako instrukcje.
**Metoda:** odczyt repozytorium + faktyczne wykonanie kodu i testów. Repozytorium nie zostało zmodyfikowane (`git status` czysty po audycie).

---

## 1. Inwentarz

| | liczba |
|---|---|
| pliki śledzone (bez `.git`) | **167** |
| markdown `.md` | **108** |
| Python `.py` | **43** |
| YAML (CI) `.yml` | **10** |
| pozostałe | 6 |

Pozostałe 6: `.devcontainer/devcontainer.json`, `.env.example`, `.gitignore`, `Copilot`, `Info neo4j`, `chat-Decentralized Computing Network.txt`.

### Linie kodu

- **`src/` — 52 linie.** Trzy pliki: `entrypoint.py` (17), `flow.py` (14), `observation.py` (21).
- **`tests/` — zero.** Katalog zawiera wyłącznie `README.md`. Ani jednego pliku `.py`.
- Dla kontekstu: **2582 linie Pythona leżą w `sessions/`** — czyli **98% kodu repozytorium znajduje się poza `src/` i poza `tests/`**.

### Proporcje

8576 linii markdown vs 2634 linie Pythona. Z 108 plików markdown **94 leży w `sessions/`** (notatki procesowe), a tylko 14 to dokumentacja właściwa.

---

## 2. Czy cokolwiek da się uruchomić

**Tak, ale nie to, co wynikałoby ze struktury repo.**

### Jedyny wykonywalny punkt wejścia

```bash
python3 sessions/SES-006/vs-001/run_vs001.py --output ./out
```

Zweryfikowane wykonaniem: kończy się kodem 0, wypisuje JSON z `"result": "PASS"` i tworzy cztery pliki — `specification.json`, `specification.md`, `verification.json`, `delivery-manifest.json`.

### Testy — tylko plik po pliku

```bash
python3 -m pytest sessions/SES-011/test_build_plan_contract.py
```

Uruchomiono wszystkie 22 pliki testowe osobno: **22/22 przechodzą, 85 testów, zero błędów**.

### Zbiorcze `pytest` nie działa

```
import file mismatch:
imported module 'test_build_plan_contract' has this __file__ attribute:
  sessions/SES-010/test_build_plan_contract.py
which is not the same as the test file we want to collect:
  sessions/SES-011/test_build_plan_contract.py
Interrupted: 1 error during collection
```

Dwa pliki o tej samej nazwie bazowej, brak `conftest.py`, brak konfiguracji `rootdir`. CI omija problem, wymieniając każdy plik ręcznie — `ses011-build-plan-contract.yml` ma 13 osobnych kroków `python -m pytest sessions/SES-XXX/...`.

### Czego nie ma

Brak **jakiegokolwiek manifestu zależności** w całym drzewie: `requirements.txt`, `pyproject.toml`, `setup.py`, `package.json`, `Makefile`, `Dockerfile`. `README.md` zawiera jedną linię — tytuł. `src/runtime/` nie ma `__init__.py`. **Nie istnieje polecenie uruchamiające „system" jako całość.**

---

## 3. Co się zmieniło od `c86b326` (3 września)

Punkt odniesienia: `c86b326` — `chore: add reproducible devcontainer`, 3 września 2026.

**216 commitów, 154 pliki, +11 845 linii, 0 modyfikacji, 0 usunięć** (netto wszystko to nowe pliki).

| typ | plików | linii |
|---|---|---|
| markdown | 97 | **+8576** |
| Python | 43 | **+2634** |
| YAML CI | 10 | +451 |

### Zmiany w dokumentacji (72% przyrostu)

- SES-003/004 — decyzje DEC-001…DEC-015 o grafie i wyborze Neo4j
- `docs/SYSTEM_BUILDER.md`
- `docs/history/PROJECT_HISTORY_6_MONTHS.md`
- `PROJECT_GOAL_AND_CURRENT_STATE.md`
- `docs/PROJECT_FULL_AUDIT_2026-09-11.md`
- ~94 pliki notatek sesyjnych (`*_START.md`, `*_CLOSEOUT.md`, `*_HANDOFF.md`, `*_BOOTSTRAP.md`)

### Zmiany w kodzie

- SES-006 `run_vs001.py`
- SES-007 `intent_envelope.py`
- SES-008 `specification.py`
- SES-011 `build_plan.py`
- SES-014 / 017 / 018 / 019 / 020 / 021 / 022 — ogniwa łańcucha wykonania
- SES-030 `execution_effect_verification.py`
- SES-031 `delivery.py`
- `src/runtime/` (52 linie)

### Charakterystyka historii

Seria commitów SES-025, wszystkie bez zmian w kodzie:

```
8966cf4 docs(SES-025): stop writes before CI verification
894cc9e docs(SES-025): end implementation writes
db996aa docs(SES-025): mark verification-only state
0ea1ffa docs(SES-025): record pending CI verification
91f4d39 docs(SES-025): enforce verification gate
7ab0075 docs(SES-025): freeze implementation pending verification
ecc4ce1 docs(SES-025): record final verification gate
a40c04b docs(SES-025): mark final verification gate
```

Osiem commitów opisujących ten sam stan „czekamy na weryfikację". Podobnie SES-026: cztery kolejne commity o identycznej treści `SES-026: remove obsolete session runtime implementation`.

---

## 4. Czym jest ten system

**Nie da się tego ustalić jednoznacznie z zawartości repo.** Znaleziono trzy konkurujące, wzajemnie niezgodne odpowiedzi.

**A. Zdecentralizowana sieć P2P dla osób prywatnych.**
`Qwen_markdown_20260420_t61kqxivh.md`: *„samoinstalująca się, zdecentralizowana sieć komputerowa, która działa jak żywy organizm społeczny… każdy uczestnik uruchamia własny »węzeł«"*. Odbiorca: użytkownicy końcowi na Raspberry Pi i starych laptopach. Miara sukcesu: `joy_index`.

**B. Meta-narzędzie do budowania systemów (System Builder).**
`docs/SYSTEM_BUILDER.md`: *„SYSTEM BUILDER ≠ P2P 60-24"*, *„System Builder jest meta-architekturą/metodą/infrastrukturą budowy systemów"*. Odbiorca: zespół inżynierski. P2P 60-24 to dopiero pierwsze zastosowanie.

**C. Deterministyczny pipeline kontraktowy Intent→Delivery.**
To, co faktycznie jest w kodzie: 12 ogniw walidujących słowniki Pythona. Bez sieci, bez UI, bez persystencji, bez użytkownika.

### Opis oparty wyłącznie na kodzie

Jest to biblioteka deterministycznych transformacji słowników, która przeprowadza „intencję" przez łańcuch walidacji aż do wewnętrznego manifestu dostarczenia, gdzie każdy krok generuje identyfikator SHA-256 i zapis proweniencji. Nie ma odbiorcy — nie istnieje interfejs, punkt wejścia ani konsument tej biblioteki poza jej własnymi testami.

---

## 5. Spójność

**Dokumentacja opisuje trzy systemy, które nie mają ze sobą żadnego połączenia w kodzie.**

### Sieć P2P node'ów

`PROJECT_HISTORY_6_MONTHS.md` opisuje OmniKernel, Kernel-DNA, TAL, TrustGraph, RealBond, Swarm Cognition, PTP-Message, Event Bus, HappyLang, Earth Digital Twin, HappyCoin, Neuro-Orchestrator, Intelligentbit, MCS-1/TIFM. **Żaden z tych bytów nie ma odpowiednika w kodzie.** Zero plików sieciowych, zero kryptografii, zero transportu.

Sprawdzono wszystkie 15 gałęzi zdalnych — **nie ma tam ani jednego pliku `.ts`**, mimo że `Qwen_markdown` opisuje `Identity.ts`, `TrustManager.ts`, `NetworkAdapter.ts`, `StemCell v0.1.ts` jako ukończone. Gałąź `feature/stemcell-implementation` również nie zawiera żadnego TypeScriptu.

### Graf Neo4j

Połączony wyłącznie z dwoma workflow'ami CI (`g01-neo4j-gs01.yml`, `g01-neo4j-gs02.yml`), które uruchamiają surowe zapytania Cypher w kontenerze.

**Zero linii Pythona w całym repo dotyka Neo4j** — `grep` po `neo4j|cypher|GraphDatabase` we wszystkich plikach `.py` nie zwraca nic.

DEC-005 deklaruje: *„The Graph is the structural backbone of System Builder"* — ale pipeline Intent→Specification→BuildPlan nie zapisuje ani nie odczytuje żadnego węzła grafu. Testy grafowe operują na etykietach `SBNode` i relacji `IMPLEMENTS`, których nie zna żaden moduł Pythona.

Z 14 zadeklarowanych scenariuszy GS-01…GS-14 zaimplementowano **2**.

### Pipeline Intent→Specification

Jedyna część, która faktycznie działa, i jest całkowicie samotna. Nie zna grafu, nie zna sieci, nie zna node'ów.

### Elementy bez jakiegokolwiek połączenia

| relacja | stan |
|---|---|
| graf Neo4j ↔ pipeline Intent→Spec | **brak** |
| warstwa P2P/Trust/Identity ↔ cokolwiek w kodzie | **brak** |
| `src/runtime/` (52 linie) ↔ łańcuch wykonania w `sessions/` | **brak** — canonical runtime robi `start_runtime → observe_runtime` i nie dotyka ani intencji, ani specyfikacji, ani planu |
| SES-014 (approval) … SES-031 (delivery) ↔ SES-011 (build plan) | **brak realnej kompozycji** — moduły od SES-017 wzwyż przyjmują ręcznie zbudowane słowniki w swoich testach i nie importują poprzedniego ogniwa |

Test E2E (`SES-032`) kończy się na BuildPlan — **6 z 12 ogniw łańcucha nie jest przez niego dotkniętych**.

---

## 6. Sprzeczności

### 6.1. Walidator deterministyczny vs AMBIGUOUS / CONTRADICTORY

**Ustalenie pierwsze: status `CONTRADICTORY` nie istnieje.**
`grep -rn "CONTRADICTORY"` po całym repozytorium, łącznie z 224-kilobajtowym zapisem czatu, nie zwraca **ani jednego trafienia**. Kontrakt dopuszcza cztery statusy — `sessions/SES-007/intent_envelope.py:15`:

```python
STATUSES = ("VALID", "INCOMPLETE", "AMBIGUOUS", "PROTECTED")
```

Wykrywanie sprzeczności w intencji nie jest zaimplementowane ani nawet zaprojektowane.

**Ustalenie drugie: formalnej sprzeczności między determinizmem a `AMBIGUOUS` nie ma.**
Determinizm oznacza „to samo wejście → to samo wyjście", a nie „każde wejście jest jednoznaczne". Walidator jest deterministyczny (kanoniczny JSON, `sha256` obcięty do 16 znaków) i może deterministycznie orzec „to jest niejednoznaczne". Te wymagania da się pogodzić.

**Ustalenie trzecie: problem leży gdzie indziej i jest poważniejszy — sama detekcja jest zepsuta.**

`sessions/SES-007/intent_envelope.py:74`:

```python
ambiguous = any(
    any(token in q.lower() for token in ("either", "or", "alternative", "interpretation", "ambiguous"))
    for q in envelope["open_questions"]
)
```

To dopasowanie podciągu. Token `"or"` jest podciągiem słów `more`, `report`, `order`, `storage`, `work`, `form`. Wynik faktycznego uruchomienia:

```
'Need more storage?'      -> AMBIGUOUS
'Who writes the report?'  -> AMBIGUOUS
'What is the work order?' -> AMBIGUOUS
```

Żadne z tych pytań nie jest niejednoznaczne. Odwrotnie:

```
'Czy A czy B?'   -> INCOMPLETE
'Either A or B?' -> AMBIGUOUS
```

To samo pytanie po polsku nie zostaje wykryte. Projekt, którego połowa dokumentacji jest po polsku, ma detektor rozpoznający wyłącznie pięć angielskich słów.

`SES-007_INTENT_ENVELOPE_CONTRACT.md:114` deklaruje: *„AMBIGUOUS intent identifies the competing interpretations"* — implementacja nie identyfikuje żadnych konkurencyjnych interpretacji, tylko kopiuje `open_questions` do listy `reasons`.

### 6.2. Fail-closed vs faktyczne zachowanie walidatora

`docs/PROJECT_FULL_AUDIT_2026-09-11.md` §8: *„**Fail-closed:** obecny na istotnych granicach."*

Kod, `intent_envelope.py:66-68` — niepoprawne `authority` dopisuje powód, ale **nie zmienia statusu**. Uruchomienie z `authority='alien'`:

```
status = VALID | reasons = ['authority must be human or system']
```

Envelope z nieznaną władzą przechodzi jako `VALID` i leci dalej do budowy specyfikacji. **To fail-open na granicy autoryzacji.**

### 6.3. „System suggests. Human decides." vs brak bramki zatwierdzenia

`P2P_60-24_ENGINEERING_CONSTITUTION_v1.0.md` §0: *„**Core principle:** System suggests. Human decides."*

Poprawna intencja przepuszczona przez cały zaimplementowany łańcuch:

```
PLAN status   = VALIDATED
PLAN approval = {'required': False, 'status': 'NOT_REQUIRED', 'authority_scope': 'human'}
PLAN blockers = []
```

**Zatwierdzenie przez człowieka nigdy nie jest wymagane.**

Przyczyna jest strukturalna: `specification.py` nadaje każdemu elementowi `"origin": "DERIVED"` na sztywno (`_derived_item`) i zawsze zwraca `unresolved_decisions: []`. W `build_plan.py` warunek brzmi:

```python
approval_required = proposed_present or protected_unresolved
```

Oba człony są trwale fałszywe. Cała gałąź `READY_FOR_APPROVAL` i `BLOCKED` jest **kodem martwym** w realnym przepływie.

Repozytorium samo to odkryło i zapisało w `sessions/SES-032/SES-032_REVIEW.md`: *„SES-008 obecnie buduje wymagania jako `DERIVED` i nie tworzy `PROPOSED` elementów"*. Ustalenie jest trafne, ale zostało zapisane jako notatka, nie naprawione.

### 6.4. Zakaz duplikatów vs duplikaty w repo

`PROJECT_GOAL_AND_CURRENT_STATE.md` §5 pkt 8: *„**Nie tworzymy duplikatów runtime.** `src/runtime/` pozostaje canonical runtime"*.

W repo istnieją równolegle katalogi z myślnikiem i podkreśleniem:

```
sessions/SES-011/build_plan.py              ↔  sessions/SES_011/build_plan.py
sessions/SES-014/execution_authorization.py ↔  sessions/SES_014/execution_authorization.py
sessions/SES-017/ (tylko test)              ↔  sessions/SES_017/execution_request.py (tylko kod)
```

To nie są kopie bajt w bajt. `SES-014` vs `SES_014` różnią się komunikatem błędu (`"Human approval does not match the BuildPlan"` vs `"Human approval is bound to a different BuildPlan"`).

Gorzej — **różne testy importują różne kopie**: `sessions/SES-013/test_build_plan_provenance.py:3` robi `from sessions.SES_011.build_plan import ...` (podkreślenie), podczas gdy test E2E ładuje `sessions/SES-011/build_plan.py` (myślnik). Dwie implementacje tego samego kontraktu są weryfikowane niezależnie i mogą się rozejść.

Osobno: `sessions/SES-020/execution_effect.py` i `sessions/SES-021/execution_effect.py` to ta sama funkcja, przy czym wersja z SES-021 dodaje kontrolę bezpieczeństwa:

```python
if effect_authorization.get("build_plan_id") != execution_result.get("build_plan_id"):
    raise PermissionError("effect authorization must bind to the same build plan")
```

**Słabsza wersja z SES-020 nadal żyje i nadal jest uruchamiana w CI.**

### 6.5. Deklarowany stan modułów vs rzeczywistość

`Qwen_markdown_20260420_t61kqxivh.md` — *„Status projektu: Milestone 01 ✅ ZAMKNIĘTY"*, tabela z ośmioma modułami oznaczonymi ✅, w tym *„`Testy jednostkowe` ✅ Coverage >85%"*, *„Język: Polski (dokumentacja techniczna zgodna z TypeScript/Node.js)"*.

Żaden z tych modułów nie istnieje w żadnej gałęzi. Repozytorium jest w Pythonie. Pokrycie testami katalogu `tests/` wynosi zero, bo katalog nie zawiera testów.

### 6.6. Hierarchia autorytetu opiera się na pustych katalogach

`P2P_60-24_ENGINEERING_CONSTITUTION_v1.0.md` §1 ustanawia siedmiopoziomową hierarchię: poziom 1 to *„Project Constitution and approved constitutional decisions"*, poziom 3 *„Frozen ontology and invariants"*, poziom 4 *„Architecture and ADRs"*.

Stan faktyczny:

- `constitution/` — **wyłącznie `README.md`**
- `ontology/` — **wyłącznie `README.md`**
- `architecture/` — **wyłącznie `README.md`**

**Cztery najwyższe poziomy hierarchii autorytetu nie mają treści.**

Sam `constitution/README.md` to przyznaje: *„Until a document is formally approved, this directory must not be treated as containing frozen rules merely because a draft exists"* — ale reszta dokumentacji powołuje się na tę hierarchię jako obowiązującą.

### 6.7. Praca na niezatwierdzonych decyzjach strefy RED

Konstytucja §2: *„**RED — human decision.** AI may analyse and propose, but may not independently approve changes to Constitution, foundational ontology, Trust model…"*

Statusy decyzji:

| decyzja | status |
|---|---|
| DEC-001 … DEC-006 | `APPROVED` |
| **DEC-007 … DEC-013** | **`PROPOSED FOR HUMAN APPROVAL`** — nigdy nie zatwierdzone |
| DEC-014, DEC-015 | `ACCEPTED BY HUMAN` |

Mimo to workflow `g01-neo4j-gs02.yml` jest wprost zbudowany na DEC-009 i DEC-010 (wymienia je w `paths:`), a DEC-014 i DEC-015 — decyzje późniejsze, zależne od tamtych — zostały oznaczone jako zaakceptowane. **Łańcuch zatwierdzeń jest przerwany w środku.**

---

## 7. Luka między deklaracją a stanem

Rzeczy opisane jako ustalone, gotowe lub zdecydowane, bez odpowiednika w kodzie ani konfiguracji:

| Deklaracja | Źródło | Stan faktyczny |
|---|---|---|
| `Identity.ts`, `TrustManager.ts`, `NetworkAdapter.ts`, `MockNetworkAdapter.ts`, `SignedInvite.ts`, `message.ts`, `StemCell v0.1.ts` — wszystkie ✅ | `Qwen_markdown…md` §2 | zero plików `.ts` w 15 gałęziach |
| „Milestone 01 ✅ ZAMKNIĘTY", „Coverage >85%" | tamże | brak testów w `tests/`, brak konfiguracji pokrycia |
| Project Constitution jako poziom 1 autorytetu | `ENGINEERING_CONSTITUTION` §1 | `constitution/` = sam README |
| „Frozen ontology and invariants" (poziom 3) | tamże | `ontology/` = sam README |
| „Architecture and ADRs" (poziom 4) | tamże | `architecture/` = sam README, zero ADR |
| `docs/human/`, `ai/`, `protocols/`, `trust/`, `security/`, `governance/`, `graph-engineering/`, `decisions/`, `plans/` | `docs/README.md` | żaden z tych 9 katalogów nie istnieje |
| Graf jako „structural backbone" Systemu Buildera | DEC-005, status APPROVED | zero kodu dotykającego grafu |
| Scenariusze konformancji GS-01…GS-14 | DEC-009, `Info neo4j` | zaimplementowane 2 z 14 |
| OmniKernel, Kernel-DNA, TAL, TrustGraph, RealBond, SEE/OES, Swarm Cognition, Event Bus, model pamięci HOT→ARCHIVAL, 4-Level Validator | `PROJECT_HISTORY_6_MONTHS.md` §4–14 | brak odpowiednika w kodzie |
| Łańcuch „INTENT → … → VERIFICATION → DELIVERY" jako *„zweryfikowane kolejne granice"* | `PROJECT_GOAL_AND_CURRENT_STATE.md` §2 | test E2E kończy się na BuildPlan; 6 z 12 ogniw nietkniętych jakąkolwiek kompozycją |
| „HUMAN APPROVAL" jako ogniwo łańcucha | tamże §2 i §7 | `approval.required == False` w każdym realnym przebiegu |
| Poziomy testów: unit, contract, integration, security, interoperability, e2e | `tests/README.md` | katalog pusty; istnieją tylko testy kontraktowe, rozsiane po `sessions/` |
| `src/` jako „Implementation code" | `src/README.md` | 52 linie, trzy funkcje, bez konsumenta |
| Manifest zależności / instrukcja uruchomienia | brak w ogóle | `README.md` = jedna linia z tytułem |

**Osobno:** plik `Copilot` (6 KB) to wklejony surowy output innego asystenta AI — razem z jego wywołaniami narzędzi i pytaniami do opiekunów — zacommitowany do repozytorium jako dokument projektu. Zawiera zresztą tę samą diagnozę co niniejszy audyt: *„polecenia run / test nie są deklarowane, repozytorium służy obecnie jako dokumentacja + rusztowanie"*.

---

## Trzy rzeczy do zrobienia, według realnego wpływu

### 1. Naprawić bramkę zatwierdzenia przez człowieka — `specification.py` musi umieć wyprodukować `PROPOSED`

Dopóki `approval.required` jest trwale `False`, naczelna zasada projektu („System suggests. Human decides.") nie ma żadnego oparcia w wykonywalnym kodzie, a gałęzie `READY_FOR_APPROVAL` i `BLOCKED` w `build_plan.py` są kodem martwym testowanym wyłącznie na ręcznie spreparowanych słownikach.

To jedyna zmiana, która przekształca kilkanaście testów kontraktowych z ćwiczenia w rzeczywisty mechanizm kontroli. Repozytorium samo wskazało tę lukę w `SES-032_REVIEW.md` — pozostaje ją zamknąć.

Przy okazji naprawić fail-open na `authority`: niepoprawna wartość musi dawać status inny niż `VALID`.

### 2. Usunąć duplikaty `SES-0XX` / `SES_0XX` i doprowadzić `pytest` do uruchamiania się jednym poleceniem

Dziś dwie różniące się implementacje tego samego kontraktu żyją równolegle, testy importują raz jedną, raz drugą, a zbiorcze zebranie testów kończy się błędem kolizji nazw. Każda przyszła zmiana kontraktu ma 50% szans trafić w kopię, której CI nie sprawdza w danym kroku.

Konsolidacja do jednej ścieżki, dodanie `conftest.py` i nadanie plikom testowym unikalnych nazw zamienia 13 ręcznie wypisanych kroków CI w jedno polecenie i eliminuje całą klasę cichych rozjazdów.

Do tego dodać `requirements.txt` lub `pyproject.toml` — bez tego nie ma odtwarzalnego środowiska.

### 3. Rozstrzygnąć na piśmie, czym projekt jest, i usunąć dokumenty opisujące nieistniejące systemy

`Qwen_markdown…md` deklaruje ukończony system TypeScript, którego nie ma w żadnej gałęzi. `PROJECT_HISTORY_6_MONTHS.md` wylicza kilkadziesiąt bytów bez odpowiednika w kodzie. `docs/README.md` opisuje dziewięć nieistniejących katalogów. `Copilot` to wklejka z innego narzędzia.

Przy 108 plikach markdown na 43 pliki Pythona każdy kolejny czytelnik — człowiek czy AI — najpierw trafi na opis systemu, który nie istnieje, i będzie planował względem niego.

Przenieść te pliki do wyraźnie oznaczonego archiwum historycznego albo je usunąć, a `README.md` uzupełnić o jedno zdanie: co to jest i jakim poleceniem się to uruchamia.
