# SES-086 — SESSION BOOTSTRAP

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repo:** `60-24/60-24.oneclik.evo.p2p`  
**Branch roboczy:** `ses-086-tagology-proposal`  
**Branch docelowy:** `main`  
**Stan bazowy:** `3026d8149e2320a12ab0b0b6384d2242b459bd80`  
**Poprzednia sesja:** SES-085 — STONE  
**Temat:** Tagologia jako proponowana warstwa semantyczna

## Cel

Przygotować Tagologię krok po kroku, zachowując istniejący runtime P2P i wymagane granice zatwierdzania.

## Wykonana inspekcja

- Odczytano `AGENTS.md`, Engineering Constitution, `docs/CURRENT_STATE.md`, `docs/REPOSITORY_MAP.md`, `architecture/README.md`, `ontology/README.md`, `src/p2p/protocol.py` i `src/p2p/transport.py`.
- Istniejący runtime obsługuje uwierzytelnione połączenie Node A ↔ Node B; protokół obecnie opisuje handshake, a nie Tagologię.
- Architektura i ontologia mają katalogi kanoniczne, ale nie zawierają zatwierdzonego kontraktu Tagologii.
- Zmiana fundamentów ontologii jest w strefie RED; zmiana formatu komunikatu/protokołu wymaga zatwierdzenia YELLOW.

## Artefakty przygotowane na gałęzi roboczej

- `architecture/proposals/TAGOLOGY_PROPOSAL_v0.1.md` — propozycja koncepcji, typów, reguł kompozycji, ewolucji i kryteriów akceptacji.
- `sessions/SES-086/SES-086_TAGOLOGY_TEST_PLAN.md` — potwierdzone fakty, realny GAP dokumentacyjny, granice i plan testów.

To dokumenty propozycyjne. Nie są zatwierdzoną ontologią ani dowodem implementacji.

## Kolejność dalszych działań

1. **REVIEW:** człowiek zatwierdza lub koryguje kierunek i kandydackie typy.
2. **CONTRACT:** po decyzji opracować wersjonowany kontrakt semantyczny oraz przykłady poprawne i niepoprawne.
3. **RED:** napisać testy walidatora kontraktu, bez ingerencji w runtime.
4. **IMPLEMENT:** dodać najmniejszy czysty walidator, jeśli testy wykazują realny zakres implementacji.
5. **GREEN:** uruchomić testy lokalne i CI; raportować wyłącznie potwierdzone wyniki.
6. **INTEGRATION REVIEW:** osobno zaproponować sposób osadzenia struktury w wiadomości aplikacyjnej.
7. **EVIDENCE:** zapisać dokładne SHA, wyniki i ograniczenia.
8. **STONE:** dopiero po spełnieniu kryteriów i wymaganej akceptacji.

## Zakres zakazany na tym etapie

- Nie zmieniać HELLO/WELCOME/AUTH, framingu TCP, NodeID ani modelu zaufania.
- Nie promować propozycji do katalogu kanonicznej ontologii bez decyzji człowieka.
- Nie tworzyć GUI/autocomplete przed walidacją kontraktu.
- Nie utożsamiać poprawności składni z prawdą twierdzenia ani zaufaniem do nadawcy.
- Nie oznaczać sesji jako STONE bez dowodów.

## Stan

**PROPOSAL PREPARED — REVIEW REQUIRED.**  
Nie uruchamiano testów Tagologii, ponieważ implementacja jeszcze nie istnieje. Nie twierdzi się GREEN ani STONE.
