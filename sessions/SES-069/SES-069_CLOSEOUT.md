# SES-069 — CLOSEOUT / STONE

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repo:** 60-24/60-24.oneclik.evo.p2p  
**Branch:** main  
**Data:** 2026-09-28  
**Status:** GREEN / CLOSED / STONE

## 1. Cel

SES-069 rozpoczęła się od pełnego INSPECT po SES-068.

Znaleziony realny GAP dotyczył niepełnej obsługi strumienia TCP: `_receive_line()` zwracał pierwszą ramkę znalezioną w buforze, ale odrzucał bajty znajdujące się za pierwszym separatorem `\\n`.

W protokole strumieniowym jeden `recv()` może zawierać więcej niż jedną ramkę. Python dokumentuje ten charakter TCP i konieczność zachowania nadmiarowych bajtów przy protokole delimitowanym. 

## 2. Konkretna awaria

Po poprawnym handshake:

```
AUTH\\nMESSAGE\\n
```

mogło trafić do jednego `recv()`.

Dotychczasowy odbiornik:
1. odczytywał `AUTH\\n`;
2. usuwał cały odebrany bufor;
3. tracił `MESSAGE\\n`;
4. kolejne `_receive_line()` czekało na dane;
5. kończyło się `ValueError("incomplete frame")`.

Był to rzeczywisty GAP integralności framingu, potwierdzony deterministycznym testem CI.

## 3. RED

Dodano:

`sessions/SES-069/test_coalesced_frames.py`

Test wymusza wysłanie:

```
AUTH\\ncoalesced-message\\n
```

w jednym zapisie TCP i wymaga:
- poprawnego uwierzytelnienia;
- zachowania drugiej ramki;
- odebrania `coalesced-message`;
- odpowiedzi `pong-from-B`.

### RED evidence

PR #8, run:

**36397561497 — P2P Linux executable — FAILURE**

Regression-test step zakończył się failure na SES-069, podczas gdy wcześniejsze testy przeszły. Build, packaging i smoke zostały pominięte zgodnie z fail-fast CI.

Commit RED:

`79b3158671dcef26ba84727b9f2d11f148cf4122`

## 4. Minimalna implementacja

Zmiana objęła wyłącznie framing runtime:

`src/p2p/node.py`

Wprowadzono per-connection buffer przekazywany do `_receive_line()`.

Nowa reguła:
- odczytaj dane do separatora;
- zachowaj wszystko po pierwszym separatorze;
- następne wywołanie czyta zachowane bajty przed kolejnym `recv()`;
- limit `MAX_FRAME_SIZE = 64 KiB` pozostaje zachowany.

Nie zmieniono formatu HELLO/WELCOME/AUTH ani kryptograficznego modelu identity.

## 5. GREEN

Po implementacji:

**P2P Linux executable**

Run:

`36397928843`

Commit:

`e3071bd329d8413817fe434e0cc2538010abaaa7`

Wyniki:
- regression tests — SUCCESS;
- Linux build — SUCCESS;
- packaged two-node smoke — SUCCESS;
- artifact attestation — SUCCESS;
- artifact upload — SUCCESS.

## 6. Main po scaleniu

PR #8 został scalony do `main`.

Finalny commit:

`8e76307716db732280202a5c64603966fb731d7c`

Dla tego SHA główny workflow:

**36398070779**

przeszedł:
- regression tests — SUCCESS;
- build — SUCCESS;
- package — SUCCESS;
- two-node smoke — SUCCESS;
- attestation — SUCCESS;
- artifact upload — SUCCESS.

## 7. Evidence

Dla finalnego SHA:

`p2p/evidence = success`

Status wskazuje na workflow run:

`36398070779`

Artefakt:

`P2P60-24Node-linux-x86_64`

SHA-256:

`41efb597ac8d76cd9bb7e71fe357d8db6c31a554af2f53f0216f03b84d25fb7a`

## 8. Zakres

Zmiany SES-069:
- nowy test framingu;
- rejestracja testu w CI;
- minimalny bufor per połączenie w runtime.

Nie zmieniano:
- identity;
- authentication;
- handshake contract;
- trust;
- authorization;
- ontologii;
- transportu;
- architektury wielowęzłowej.

## 9. Wniosek

SES-069 potwierdziła, że po wcześniejszym usunięciu GAP-u EOF/truncated-frame pozostawała jeszcze druga, niezależna klasa błędu framingu: **coalesced TCP frames**.

GAP został:
**zaobserwowany → zreprodukowany RED → minimalnie naprawiony → zweryfikowany GREEN → potwierdzony Evidence → scalony do main.**

## 10. Następna sesja

Nie zakładać kolejnego GAP-u.

Następny start:

**INSPECT aktualnego repo → architektura → dowody → jeden REAL GAP albo STOP.**

Nie zwiększać zakresu tylko po to, aby kontynuować implementację.

**SES-069 = CLOSED / STONE.**
