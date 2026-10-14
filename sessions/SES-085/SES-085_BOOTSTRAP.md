# SES-085 — SESSION BOOTSTRAP

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repo:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Stan bazowy:** `e3cb2e3a2416ed8d1f252db1e38c11938da59b5d`  
**Data:** 2026-10-14  
**Poprzednia sesja:** SES-084 — STONE

## 1. Cel nowej sesji

Kontynuować audyt poprawności framingu i obsługi rozłączenia TCP. Najpierw sprawdzić, czy istnieje luka w testach dla scenariusza:

1. Node B otrzymuje poprawny HELLO.
2. Node A i B kończą poprawny, kryptograficznie zweryfikowany handshake.
3. Po AUTH peer zamyka połączenie przed wysłaniem kompletnej ramki aplikacyjnej.
4. Oczekiwanie: Node B odrzuca niekompletną ramkę; `last_message` nie zostaje ustawione; nie powstaje fałszywa wiadomość.

Nie zakładać błędu implementacji. Najpierw potwierdzić GAP w testach i zachowanie kodu. Zmieniać runtime wyłącznie, jeśli dowód wykaże rzeczywisty błąd.

## 2. Stan repozytorium i dowody

HEAD `main`: `e3cb2e3a2416ed8d1f252db1e38c11938da59b5d`  
Poprzedni merge SES-084: `825b55a5fe7d5e887c4e3971aed8bb028796322c`

Po commicie dokumentującym SES-084 wszystkie sprawdzone workflowy na HEAD `e3cb2e3a2416ed8d1f252db1e38c11938da59b5d` zakończyły się sukcesem:
- P2P Linux executable — run `38440556269`
- P2P Windows executable — run `38440556188`
- P2P Android APK — run `38440556252`
- SES-032 E2E integration — run `38440556704`
- SES-043 P2P proof — run `38440556397`
- SES-045 concrete P2P node — run `38440556319`
- SES-011 BuildPlan Contract — run `38440556548`
- SES-023 Runtime Entry Point Contract — run `38440556329`
- SES-024 Runtime Observation Contract — run `38440556301`
- SES-025 Runtime Flow Contract — run `38440556380`
- Beta local execution — run `38440556203`
- P2P Evidence Check — runs `38440651126`, `38440669433`

To potwierdza stan CI dla wymienionych workflowów, nie oznacza produkcyjnej gotowości systemu.

## 3. Ostatnie zamknięte sesje

### SES-082 — STONE
- Zabezpieczono `P2PNode.send()` przed CR/LF, które mogły rozdzielić pojedynczą wiadomość na wiele ramek.
- Dodano testy regresyjne dla LF, CR i CRLF oraz włączono je do CI Linux/Windows.
- PR #9 scalony; merge commit `119610ffdd179874da99c4074409072cfa36623c`.

### SES-083 — STONE
- Wspólna walidacja pojedynczej linii obejmuje nadawcę i odbiorcę.
- Odbiorca odrzuca CR/LF w wiadomości aplikacyjnej.
- Regresja najpierw potwierdzona przez RED, potem Linux/Windows oraz pozostałe wskazane workflowy GREEN.
- PR #10 scalony; merge commit `4b9c33ce497e4307afe85f2a760a9d2783540299`.
- Closeout: `sessions/SES-083/SES-083_CLOSEOUT.md`.

### SES-084 — STONE
- GAP: test integracyjny wysyłający AUTH i wiadomość aplikacyjną przez jedno `sendall()` nie gwarantował, że oba frame'y trafią do jednego `recv()`.
- Dodano deterministyczny test ze stubem socketu, który zwraca obie ramki w jednym `recv()`.
- Test włączono do CI Linux/Windows; kod runtime bez zmian.
- PR #11 scalony; merge commit `825b55a5fe7d5e887c4e3971aed8bb028796322c`.
- Closeout: `sessions/SES-084/SES-084_CLOSEOUT.md`.

## 4. Pliki do inspekcji

- `src/p2p/node.py` — `_receive_line()`, `listen_once()`, kolejność ustawiania `last_peer_id` i `last_message`.
- `sessions/SES-068/test_incomplete_frame_eof.py` — aktualnie potwierdza EOF przed separatorem ramki HELLO.
- `sessions/SES-069/test_coalesced_frames.py` — test integracyjny koalescencji.
- `sessions/SES-084/test_deterministic_coalesced_frames.py` — deterministyczny test buforowania ramek.
- `.github/workflows/build-p2p-linux.yml`
- `.github/workflows/build-p2p-windows.yml`

## 5. Procedura obowiązkowa

`INSPECT → UNDERSTAND → GAP → RED → IMPLEMENT → GREEN → EVIDENCE → STONE`

1. Sprawdzić aktualny `main` i bieżące workflowy; nie ufać stanowi zapisanemu w starszym dokumencie bez weryfikacji.
2. Przeczytać istniejące testy i helpery protokołu. Ustalić, czy scenariusz EOF po poprawnym AUTH jest już pokryty.
3. Jeśli brak pokrycia, dodać minimalny deterministyczny test i uruchomić go jako RED/GREEN; wpiąć do CI Linux i Windows.
4. Nie zmieniać kodu produkcyjnego, jeśli zachowanie jest poprawne i brakuje jedynie testu.
5. Przejrzeć wyniki workflowów dla dokładnego SHA PR. Scalanie tylko po wymaganych zielonych dowodach.
6. Zaktualizować closeout dopiero po weryfikacji merge i CI na aktualnym `main`.

## 6. Granice i zasady

- Repozytorium i jego artefakty są źródłem prawdy.
- Nie twierdzić GREEN/PASS/STONE bez sprawdzalnego dowodu.
- Nie mieszać braku testu z błędem runtime.
- Minimalny zakres zmian; nie zmieniać protokołu bez wykazanego powodu.
- Ten proof-of-concept nie ma obecnie potwierdzonego E2E encryption, automatycznego discovery ani NAT traversal; nie sugerować produkcyjnej gotowości.

**Oczekiwany wynik SES-085:** albo udokumentowane NO GAP z uzasadnieniem, albo jeden precyzyjny test regresyjny z dowodem RED → GREEN i zweryfikowanym CI.
