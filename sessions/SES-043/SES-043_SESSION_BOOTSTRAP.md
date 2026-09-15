# SES-043 — Minimal P2P Network Proof

**Date:** 2026-09-15  
**Status:** RED TEST CONFIRMED / IMPLEMENTATION GATED  
**Project:** P2P 60-24 OneClick Evo  
**Repository:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`

## 1. Stone / checkpoint wejściowy

`SES-040 = GREEN / CLOSED REFERENCE`  
`SES-041 = BLOCKED / CLOSED` — Windows distributable CI pozostaje zaparkowane i nie jest częścią tej sesji.  
`SES-042 = OPENED` — przejście z System Buildera do pierwszego konkretnego systemu P2P.

**Zasada:** repozytorium jest Source of Truth. Nie uznajemy PASS/GREEN bez rzeczywistego testu i jednoznacznego dowodu.

## 2. Cel SES-043

Zbudować i udowodnić **najmniejszą możliwą, testową podstawę P2P 60-24 OneClick Evo**:

> **dwa niezależne węzły P2P potrafią nawiązać połączenie i wymienić prostą wiadomość.**

To jest **test fundamentu sieci**, a nie jeszcze pełny P2P 60-24.

### Relacja z System Builderem

**System Builder → narzędzie budujące systemy**  
**P2P 60-24 → pierwszy konkretny system, który ten proces ma zbudować i uruchomić.**

SES-043 ma sprawdzić tę relację na najprostszym realnym przykładzie.

## 3. Zakres — celowo minimalny

### MUSI działać

1. Uruchomienie co najmniej dwóch procesów/węzłów.
2. Każdy węzeł ma prostą identyfikację.
3. Węzeł A może połączyć się z węzłem B.
4. A wysyła prostą wiadomość do B.
5. B odbiera wiadomość i potrafi odpowiedzieć.
6. Test automatyczny potwierdza komunikację.
7. Istnieje jednoznaczny, powtarzalny dowód GREEN.

### NIE ROBIMY teraz

- Trust / LocalTrust / RealBond.
- blockchain / token / płatności.
- centralnego serwera.
- libp2p.
- rozbudowanego discovery.
- GUI.
- produkcyjnego bezpieczeństwa.
- wielkiej architektury.
- integracji z Internetem, jeśli lokalne połączenie wystarczy do dowodu.

**Zasada minimalności:** używamy najprostszego mechanizmu transportowego zgodnego z dotychczasową architekturą repozytorium. Nie projektujemy całego P2P — dowodzimy pierwszego działającego połączenia.

## 4. INSPECT / UNDERSTAND / GAP — wykonane

Audyt repo wykazał:

- brak istniejącego runtime P2P,
- brak istniejącej implementacji UDP/socket w bieżącym runtime,
- brak `libp2p` jako używanego transportu,
- wcześniejsze dokumenty Beta jednoznacznie pozostawiają P2P/UDP poza zakresem zamkniętej Beta.

**GAP:** nie ma istniejącej implementacji, którą można bezpiecznie REUSE/INTEGRATE.

## 5. RED TEST — wykonany i potwierdzony

Dodano:

`sessions/SES-043/test_p2p_two_nodes.py`

Test uruchamia dwa niezależne procesy i wymaga przepływu:

```text
NODE A ───── connection ─────> NODE B
NODE A ───── message ────────> NODE B
NODE A <──── response ──────── NODE B
```

Test oczekuje rzeczywistego modułu `src.p2p.node` oraz odpowiedzi `pong-from-B`.

### Dowód RED

Commit:
`d7bc03e7cf1c6e08ca133d8d4ca40171392019fb`

GitHub Actions:
`Beta local execution` — run `34927976826`

Job:
`test-local-executor` — `FAILURE`

Istniejący test Beta przeszedł:
`3 passed`

Następnie SES-043:
`1 failed`

Błąd jest rzeczywisty i zgodny z GAP: uruchomienie `python -m src.p2p.node ...` zakończyło się `exit status 1`, ponieważ wymagany runtime P2P jeszcze nie istnieje.

**RED = POTWIERDZONE.**

Po uzyskaniu dowodu RED tymczasowy wpis testu do workflow został usunięty. Główny workflow Beta został przywrócony bez zmiany funkcjonalnej.

## 6. Granica decyzyjna po RED

RED test ujawnił właściwą następną decyzję: **wybór minimalnego transportu i kontraktu uruchamiania węzła**.

To jest już decyzja techniczna klasy **YELLOW** (transport/protokół/runtime boundary), a nie zwykła poprawka implementacyjna.

Dlatego:

- nie wybieramy samowolnie `UDP`, `TCP`, `libp2p` ani innego transportu jako architektury docelowej,
- nie budujemy jeszcze runtime,
- zachowujemy RED test jako kontrakt zachowania,
- następny krok to przygotowanie minimalnej propozycji transportu zgodnej z Constitution/ADR i istniejącym repo.

**Rekomendacja Project Leada do rozważenia:** standard-library transport bez zewnętrznej zależności, wyłącznie dla lokalnego testu dwóch niezależnych procesów. Nie jest to jeszcze zatwierdzona architektura P2P.

## 7. Kryterium sukcesu

SES-043 może zostać zamknięta jako **GREEN** tylko wtedy, gdy mamy dowód:

```text
NODE A ───── connection ─────> NODE B
NODE A ───── message ────────> NODE B
NODE A <──── response ──────── NODE B

TEST RESULT = PASS
```

## 8. Cykl pracy

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CONTINUE`

Aktualny stan:

`INSPECT ✓ → UNDERSTAND ✓ → GAP ✓ → RED ✓ → IMPLEMENT GATED`

## 9. Odpowiedzialność

Project Lead prowadzi sesję autonomicznie w uzgodnionym zakresie, pilnuje minimalności rozwiązania, kolejności prac i końcowej weryfikacji.

Decyzje YELLOW/RED wymagające zatwierdzenia człowieka nie są obchodzone przez implementację „na próbę”.

## 10. Zasada końcowa

**GREEN = działający test + dowód.**  
**RED = test poprawnie ujawniający brak wymaganej zdolności.**  
**BLOCKED = uczciwie zatrzymane, z opisanym powodem.**  
Nigdy nie zamieniać braku dowodu w PASS.
