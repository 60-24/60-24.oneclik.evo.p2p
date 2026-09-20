# SES-060 — SESSION BOOTSTRAP

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repo:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Data:** 2026-09-20  
**Status:** OPEN  
**Tryb:** AUTONOMICZNY

## 1. Stan wejściowy

SES-059 został zamknięty jako GREEN/CLOSED.

Ostatni potwierdzony stan obejmuje pełny praktyczny przepływ użytkownika:

`download → run → configure → connect → handshake → identity → message → response`

oraz obsługę podstawowych błędów CLI bez surowych tracebacków.

SES-059 objął:
- poprawę komunikatów błędów CLI,
- regresję dla błędnego adresu i odmowy połączenia,
- rozszerzenie CI o testy ścieżki błędów,
- dokumentację README i troubleshooting,
- pełną weryfikację GitHub Actions.

Ostatni commit zamykający SES-059:

`d606340e20fc25c47efff4668c0ea563203198a3`

## 2. Dowód / STONE

Stan SES-059 jest traktowany jako punkt odniesienia projektu.

Nie wolno uznawać samego istnienia dokumentu za dowód funkcjonalności. Źródłem prawdy pozostaje repozytorium, testy, GitHub Actions i rzeczywiste artefakty wykonawcze.

Łańcuch wcześniejszych dowodów obejmuje m.in.:
- SES-055 — dwukierunkowa obserwowalność identity,
- SES-057 — listener proof of peer/message,
- SES-058 — rozszerzenie dowodu o non-loopback IPv4,
- SES-059 — używalna ścieżka CLI + obsługa błędów + dokumentacja.

## 3. Granica SES-060

Nie zakładamy z góry kolejnej funkcji ani nie rozpoczynamy dużej przebudowy architektury.

Pierwszym zadaniem SES-060 jest:

**INSPECT → UNDERSTAND → IDENTIFY GAP**

Najpierw należy sprawdzić aktualny stan repo i dowodów po SES-059, a następnie znaleźć **jeden rzeczywisty, istotny GAP**, który ogranicza przejście od obecnego działającego Node A ↔ Node B do kolejnego poziomu użyteczności projektu.

Dopiero po potwierdzeniu GAP wolno:
- przygotować RED TEST,
- wykonać minimalną implementację,
- uruchomić GREEN,
- zweryfikować dowód,
- udokumentować zmianę.

## 4. Zakres dozwolonej autonomii

Pracować autonomicznie w obrębie:
- audytu aktualnego P2P Node,
- testów,
- CI,
- dokumentacji,
- minimalnych zmian koniecznych do usunięcia potwierdzonego GAP.

Nie wykonywać bez osobnej decyzji:
- integracji z System Builder,
- GUI,
- centralnego serwera,
- discovery/relay/NAT jako dużej warstwy,
- blockchain/crypto/tokenów,
- dużej zmiany protokołu,
- dużego refaktoru bez wykazanego GAP.

## 5. Kryteria SES-060

SES-060 może zostać zamknięty dopiero, gdy istnieje:

1. jasno nazwany GAP,
2. dowód, że GAP jest rzeczywisty,
3. test RED wynikający z GAP — tylko jeśli implementacja jest potrzebna,
4. minimalna implementacja,
5. GREEN w odpowiednim środowisku,
6. niezależny dowód wykonania,
7. aktualizacja dokumentacji,
8. commit zamykający,
9. weryfikacja GitHub Actions / artefaktu, jeśli dotyczy,
10. SESSION_CLOSEOUT oraz nowy STONE.

**Zakaz sztucznego RED i sztucznego PASS.**

## 6. Zasada pracy

Repozytorium = Source of Truth.  
Chat = kontekst.

Standardowa kolejność:

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CONTINUE`

Jeżeli audyt nie znajdzie realnego GAP-u, nie tworzyć pracy tylko po to, aby otworzyć funkcję. W takim przypadku udokumentować wynik audytu i wyznaczyć kolejny punkt decyzji.

## 7. Pierwszy checkpoint

Pierwszy checkpoint SES-060 ma odpowiedzieć na trzy pytania:

- **Co dokładnie mamy teraz?**
- **Czego jeszcze brakuje w realnym Node A ↔ Node B?**
- **Jaki jeden GAP ma najwyższy priorytet do sprawdzenia jako następny?**

Dopiero odpowiedź na te pytania wyznacza dalszą implementację.

## 8. Oczekiwany rezultat

SES-060 ma nie „dodawać funkcję”, lecz **przesunąć granicę rzeczywiście udowodnionego programu P2P**.

Każdy krok musi być możliwy do odtworzenia z repozytorium i dowodów CI/runtime.

---
