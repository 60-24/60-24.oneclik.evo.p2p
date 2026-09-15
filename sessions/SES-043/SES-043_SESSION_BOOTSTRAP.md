# SES-043 — Minimal P2P Network Proof

**Date:** 2026-09-15  
**Status:** OPEN  
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

> **dwa lub kilka niezależnych węzłów P2P potrafią nawiązać połączenie i wymienić prostą wiadomość.**

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

## 4. Obowiązkowy pierwszy krok

Przed zmianą kodu:

1. `INSPECT` — sprawdzić aktualny stan repo.
2. Znaleźć istniejące elementy P2P, jeśli już istnieją.
3. Sprawdzić wcześniejsze ADR/Constitution/Ontology dotyczące transportu i węzła.
4. Ustalić najkrótszą drogę do testu dwóch węzłów.
5. Dopiero wtedy przygotować **RED test**.

Nie tworzyć równoległej architektury, jeżeli repo ma już odpowiedni fundament.

## 5. Kryterium sukcesu

SES-043 może zostać zamknięta jako **GREEN** tylko wtedy, gdy mamy dowód:

```text
NODE A ───── connection ─────> NODE B
NODE A ───── message ────────> NODE B
NODE A <──── response ──────── NODE B

TEST RESULT = PASS
```

Dla kilku węzłów można rozszerzyć test, ale **2 węzły są minimalnym wymaganiem**.

## 6. Kryterium jakości

Rozwiązanie ma być:

- małe,
- czytelne,
- lokalne-first,
- bez centralnego punktu zależności,
- łatwe do uruchomienia,
- łatwe do przetestowania,
- możliwe do późniejszego rozbudowania bez łamania fundamentu.

## 7. Cykl pracy

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CONTINUE`

Każdy etap musi mieć dowód w repo lub w wyniku testu.

## 8. Oczekiwany rezultat końcowy

Nie budujemy jeszcze „wielkiego P2P”.

Budujemy **pierwszy kamień rzeczywistego P2P**:

> **dwa niezależne węzły istnieją, widzą się, łączą i rozmawiają.**

Jeżeli ten fundament przejdzie GREEN, będzie to pierwszy konkretny, wykonywalny dowód przejścia:

**System Builder → buduje system → systemem jest P2P 60-24.**

## 9. Odpowiedzialność

Project Lead prowadzi sesję autonomicznie w uzgodnionym zakresie, pilnuje minimalności rozwiązania, kolejności prac i końcowej weryfikacji.

Nie pytać ponownie o zgodę na działania mieszczące się w powyższym zakresie.

## 10. Zasada końcowa

**GREEN = działający test + dowód.**  
**BLOCKED = uczciwie zatrzymane, z opisanym powodem.**  
Nigdy nie zamieniać braku dowodu w PASS.
