# SES-068 — SESSION BOOTSTRAP

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repo:** 60-24/60-24.oneclik.evo.p2p  
**Branch:** main  
**Data otwarcia:** 2026-09-27  
**Stan wejściowy:** GREEN / po SES-067  
**Ostatni commit:** b8b233ad8c657d6b3240b5993a79f9b48cf1abe7  
**Ostatni zamknięty GAP:** GAP-066 / SES-067

## 1. Cel sesji

Kontynuować rozwój projektu dwutorowo:

1. **CONTROL** — pełna kontrola stanu repo, architektury i dowodów; identyfikacja jednego rzeczywistego GAP-u.
2. **BUILD** — spokojne, celowe generowanie kodu, ale wyłącznie w granicach potwierdzonego GAP-u lub jasno uzasadnionej zmiany GREEN.

Nie tworzyć sztucznych GAP-ów i nie pisać kodu tylko po to, aby zwiększać liczbę linii.

## 2. Stan potwierdzony

SES-067 zamknęła GAP-066 dotyczący braku maksymalnego rozmiaru odbieranej ramki.

Minimalna ochrona została dodana w `src/p2p/node.py`:
- `MAX_FRAME_SIZE = 64 * 1024`
- `_receive_line()` odrzuca nadmiarową ramkę kontrolowanym `ValueError`.

Dowód SES-067:
- RED: `sessions/SES-067/test_frame_size_limit.py`
- implementacja: commit `abddca185a19965a40c2fd959a1b367665eb6626`
- GREEN P2P Linux workflow: run `36071379942`
- closeout: commit `84c5916c3e96f55a5fc7dbe408b4efc4122a3137`

## 3. Ostatnia zmiana przed SES-068

Do repo dodano dokument:

`docs/AGENTIC_ENGINEERING_ENVIRONMENT_v0.1.md`

Commit:
`b8b233ad8c657d6b3240b5993a79f9b48cf1abe7`

Dokument opisuje docelowe środowisko wieloagentowe:
- ORCHESTRATOR
- GAP-HUNTER
- TEST-ENGINEER
- CODER
- REVIEWER
- dalsze role możliwe później
- WORK_PACKET
- CONTROL + BUILD
- RED → CODE → REVIEW → CI → EVIDENCE → STONE
- repo jako pamięć i Source of Truth
- człowiek zachowuje decyzje RED/YELLOW wymagające jego udziału.

## 4. Ważne zasady

### Repo jest Source of Truth

Chat jest tylko kontekstem. Fakty potwierdzamy przez:
- kod,
- testy,
- CI,
- artefakty,
- logi,
- session files,
- dokumentację.

### Kolejność

```
INSPECT
→ architektura/evidence control
→ REAL GAP
→ RED
→ minimal implementation
→ GREEN
→ review
→ evidence
→ documentation
→ STONE
```

### Poziomy decyzji

**GREEN:** testy, dokumentacja, refaktoryzacje, bezpieczne bug-fixy i niełamiące usprawnienia.

**YELLOW:** API, protokół, model danych, kontrakty międzywarstwowe, istotne zależności.

**RED:** Constitution, Ontology, Trust model, fundamental security/governance.

**BLACK:** sprzeczność, naruszenie invariantu, niebezpieczny/nieznany stan, brak wystarczających dowodów → STOP.

## 5. Pierwsze zadanie SES-068

Nie zakładać z góry GAP-067.

Najpierw:

1. INSPECT aktualnego repo od HEAD.
2. Sprawdzić ostatnie commity i CI.
3. Sprawdzić sessions i aktualny stan dokumentacji.
4. Zmapować istniejący runtime Node A ↔ Node B.
5. Przeanalizować realne failure modes istniejącego handshake/runtime:
   - disconnect na każdym etapie handshake,
   - truncated/missing frames,
   - bad signature,
   - replay starego AUTH,
   - disconnect po uwierzytelnieniu przed wiadomością,
   - wpływ błędów na stan noda.
6. Równolegle wskazać obszary, w których można bezpiecznie zwiększyć ilość wartościowego kodu.
7. Wybrać **jeden** rzeczywisty GAP.
8. Dopiero wtedy rozpocząć RED.

## 6. Agentic Engineering v0.1

Nie wdrażać od razu dużego swarmu.

Pierwsza wersja ma być minimalna:

```
ORCHESTRATOR
   ├── GAP-HUNTER
   ├── TEST-ENGINEER
   ├── CODER
   └── REVIEWER
            ↓
           CI
```

Pozostałe role (ARCHITECT, SECURITY, VERIFIER, DOCUMENTATION) mogą początkowo działać jako etapy Orchestratora i zostać rozdzielone dopiero, gdy realnie skracają cykl.

Agenci nie pracują bezpośrednio chaotycznie na `main`. Zmiana powinna być izolowana, zweryfikowana i dopiero potem integrowana.

## 7. WORK_PACKET

Każda praca agenta powinna mieć:
- ID,
- typ zadania,
- źródło/evidence,
- scope,
- dozwolone pliki,
- zakazane obszary,
- oczekiwany RED/GREEN,
- decision level.

Minimalizacja zakresu jest obowiązkowa.

## 8. Oczekiwany rezultat SES-068

Nie jest nim „dużo kodu”.

Rezultat to:

**jeden rzeczywisty GAP → dowód RED → minimalna implementacja → GREEN → pełne evidence → STONE**

Jeżeli INSPECT nie ujawni rzeczywistego GAP-u, nie tworzyć sztucznego problemu. Wtedy przygotować następny uzasadniony krok rozwoju i zachować stan GREEN.

## 9. Styl pracy

- autonomicznie,
- krok po kroku,
- kontrola całości,
- oszczędzanie tokenów,
- bez lania wody,
- repo jako prawda,
- maksymalizacja przez minimalizację,
- system jako organizm,
- system sugeruje, człowiek decyduje.

**Start SES-068: INSPECT.**
