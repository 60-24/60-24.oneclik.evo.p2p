# Podsumowanie sesji i plan dalszej pracy — 2026-11-09

## Cele na następną sesję

1. **Dostęp do Copilota jako wykonawcy zadań.** Obecnie nie ma narzędzia Copilota w sesji Claude, a agent Copilot nie daje się przypisać do issue (błąd 422). Do odblokowania: włączyć Copilot coding agent dla repo `60-24/60-24.oneclik.evo.p2p` w ustawieniach organizacji 60-24 (albo sprawdzić plan) i ponowić przypisanie issue #18.
2. **Rozwój komunikacji dwóch węzłów.** Punkt startu: handshake + podpisana wiadomość (przykład `examples/minikernel`) oraz zadanie ochrony przed powtórzeniem (issue #18).

## Stan repozytoriów

| Repo | Rola | Stan |
|---|---|---|
| `60-24/60-24.oneclik.evo.p2p` | **Główny projekt P2P** (Python, dokumenty, Builder w dokumentacji) | Testy `src`+`tests`: 13 przechodzi. Dodany przykład `examples/minikernel` na gałęzi `claude/example-minikernel` (commit `5716f48`), PR do otwarcia ręcznie. Issue #18: ochrona przed powtórzeniem. |
| `60-24/p2p.oneclik` (dawniej `p2p.60-24.oneclik.evo`) | Duplikat wcześniejszego stanu | Gałąź `claude/minikernel-v0.1-handshake` (`55b9cb4`). Do decyzji: usunąć albo zostawić. |
| `60-24/Html-P2P-60-24-` | Projekt z wizualizacji HTML i Go | Nie buduje testów: dwa pakiety nie kompilują się, jeden test pada. Zależności (`x/crypto`, `yaml`, `cobra`) i Dockerfile sprzeczne z CLAUDE.md. |

Builder (system budowania systemów) jest w tym samym repo co P2P z powodów dokumentacyjnych. P2P powstał pierwszy, Builder dołożony później.

## Wnioski techniczne

- Repo Python realizuje handshake i podpisy Ed25519, ale transport to **TCP**, a CLAUDE.md wymaga **UDP**. Zależność `cryptography` też jest sprzeczna z zasadą zerowych zależności.
- Minikernel: podpisuje ramki i odrzuca zmienione lub podszywające się, ale **nie ma ochrony przed powtórzeniem** i nie szyfruje (zgodnie z zakresem przykładu).
- Aplikacja na telefonie (zrzut z sesji) ma działający handshake, PING, ponowne połączenie i licznik odrzuconych ramek, w tym ochronę przed powtórzeniem. To punkt odniesienia dla funkcji komunikacji.
- CLAUDE.md w `p2p.oneclik` opisuje 28 plików Go i 14 000 linii, których w tym repo nie ma. Dokument wymaga korekty, żeby pokazywał stan faktyczny.

## Zasady pracy

- Praca wyłącznie przez GitHub (gałęzie i PR). Bez trwałej lokalnej kopii repo.
- Zmiany zgodnie z `AGENTS.md`: strefa GREEN (kod, testy, dokumentacja) może być wykonana samodzielnie. YELLOW (protokół, API, format danych) wymaga zgody. RED (konstytucja, model zaufania, bezpieczeństwo) wymaga decyzji człowieka.
- Commit z trailerami: `Co-Authored-By: Claude Haiku 5.5` i `Claude-Session`.

## Otwarte decyzje

- Czy scalić `claude/example-minikernel` do `main` (po przeglądzie PR).
- Czy usunąć duplikat `p2p.oneclik`.
- Czy przenieść transport na UDP zgodnie z CLAUDE.md (zmiana protokołu = YELLOW).
- Czy usunąć zależność `cryptography` (YELLOW/RED zależnie od zakresu).

## Pierwsze kroki w nowej sesji

1. Sprawdzić, czy Copilot jest włączony dla repo; jeśli tak, przypisać issue #18.
2. Dopiąć repo P2P do sesji z prawem zapisu (`add_repo` push), jeśli nie jest dopięte.
3. Zrobić płytki klon do `/home/claude/60-24.oneclik.evo.p2p`, ustawić upstream dla gałęzi roboczej, zanim hook zacznie zgłaszać „unpushed".
