# SES-048 — SESSION BOOTSTRAP

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repo:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Status:** OPEN  
**Data:** 2026-09-17

## 1. Cel sesji

Kontynuować budowę **minimalnego, działającego fundamentu P2P** po zamknięciu SES-047.

Najbliższy cel techniczny pozostaje konkretny:

> **Node A ↔ Node B: uruchomienie dwóch węzłów, połączenie, handshake, wymiana wiadomości i poprawny cykl życia połączenia.**

SES-048 nie rozszerza zakresu bez rzeczywistego wymagania wynikającego z repozytorium lub dowodu testowego.

## 2. Stan wejściowy

### System Builder
- Functional Beta: **GREEN / CLOSED**.
- Jest punktem odniesienia i nie należy go naruszać bez nowego, uzasadnionego wymagania.

### P2P
- SES-043: minimalny dowód P2P.
- SES-044: standalone/downloadable two-node regression.
- SES-045: konkretne API `src.p2p.P2PNode`.
- SES-046: HELLO/WELCOME handshake + zdalna tożsamość.
- SES-047: lifecycle/protocol audit — reconnect + malformed HELLO rejection + poprawne działanie po błędnym wejściu.

### Ostatni stan SES-047
SES-047 pozostawała w stanie **AWAITING CI** do czasu uzyskania rzeczywistego wyniku GitHub Actions.

Workflow:
`.github/workflows/ses-045-p2p.yml`

Zawiera cztery istotne joby:
1. `concrete-node-api`
2. `regression-standalone-two-node`
3. `ses-046-handshake`
4. `ses-047-lifecycle`

Dodano `workflow_dispatch` oraz:
```yaml
permissions:
  contents: read
```

Ostatni commit przed otwarciem tej sesji:
`524f22c95f9d689d3a70fd42e961ae6b035716e6`

**Uwaga:** sam brak automatycznego runu po tym commicie nie jest dowodem PASS ani FAIL. SES-047 należy zamknąć dopiero na podstawie rzeczywistego wyniku CI.

## 3. Zasada zamknięcia SES-047

Jeżeli ręcznie uruchomiony workflow przejdzie GREEN dla wszystkich wymaganych jobów:

1. zapisać numer runu CI jako evidence,
2. zaktualizować checkpoint SES-047 na CLOSED/GREEN,
3. postawić stone,
4. nie wykonywać dodatkowych zmian w SES-047.

Jeżeli CI jest RED:

- pobrać rzeczywisty błąd z joba,
- ustalić GAP,
- dopiero wtedy wykonać minimalną poprawkę.

**Zakaz:** nie ogłaszać PASS na podstawie samego kodu, lokalnej rekonstrukcji testu ani starego runu.

## 4. Zasada pracy SES-048

Stały cykl:

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CONTINUE`

Reguły:
- repozytorium = Source of Truth,
- chat = kontekst,
- zero artificial RED,
- nie wymyślać funkcji bez wymagania,
- maksymalnie 5 ważnych działań na checkpoint,
- autonomicznie wykonywać działania w delegowanym zakresie,
- nie naruszać zamkniętych dowodów bez konieczności,
- żadnego „PASS” bez rzeczywistego evidence.

## 5. Granica architektoniczna

Dokument **MICROKERNEL V0.1 SPECIFICATION** z 2026-09-15 jest materiałem informacyjnym/specyfikacją kierunkową.

Nie traktować go jako dowodu implementacji.

W szczególności nie implementować automatycznie całego Microkernel v0.1. Najpierw musi istnieć konkretne wymaganie wynikające z aktualnego stanu P2P.

Docelowa architektura może rozwijać się później, ale obecnym priorytetem jest niezawodny minimalny runtime dwóch węzłów.

## 6. Najbliższy krok

Po otwarciu SES-048:

**INSPECT aktualnego repo i evidence po SES-047 → ustalić rzeczywisty GAP → wybrać jeden minimalny następny krok.**

Nie zaczynać implementacji przed wykonaniem audytu wejściowego.

## 7. Kryterium sukcesu SES-048

Sesja ma zakończyć się wyłącznie wtedy, gdy zostanie uzyskany i zapisany rzeczywisty dowód dla konkretnego wymagania. Jeśli audyt wykaże brak uzasadnionego nowego wymagania, sesja nie tworzy sztucznej funkcji.

---

**BOOTSTRAP STATUS:** READY  
**NEXT:** INSPECT repo + CI evidence po SES-047.