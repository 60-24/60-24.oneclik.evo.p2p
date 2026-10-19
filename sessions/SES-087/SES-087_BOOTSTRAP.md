# SES-087 — SESSION BOOTSTRAP

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repo:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Poprzednia sesja techniczna:** SES-085 — STONE  
**Przekierowanie:** Tagologia odłożona; patrz `docs/TAGOLOGY_DEFERRED.md`  
**Cel:** wrócić do planu rozwoju systemu, nie kontynuować teraz eksperymentu Tagologii.

## 1. Decyzja zakresu

Tagologia jest zachowana jako eksperymentalny byt systemowy do przyszłego wykorzystania. Nie należy teraz dążyć do jej perfekcji, scalać PR #13 ani integrować jej z runtime. PR #13 pozostaje osobną gałęzią propozycji, a `main` pozostaje źródłem prawdy.

## 2. Wcześniejszy plan

Kontynuować dwa powiązane, ale rozdzielone poziomy:

1. **System Builder — nadrzędny:** rozwijać sprawdzalny proces budowy systemów: Human Intent → Constitution → Ontology → Graph → Architecture → Contracts → Modules → Tests → Implementation → Runtime → Observation → Evidence → Validation → Learning → Controlled Evolution.
2. **P2P 60-24 — pierwszy system docelowy:** utrzymywać poprawność istniejącego węzła i stopniowo budować ścieżkę niezależnego użytkownika: pobranie artefaktu → uruchomienie dwóch węzłów → pierwsze połączenie.

Nie mieszać System Buildera z runtime P2P bez jawnego kontraktu. Nie dodawać funkcji tylko dlatego, że są koncepcyjnie atrakcyjne.

## 3. Najbliższe działanie — INSPECT

Przed jakąkolwiek zmianą:

1. Odczytać aktualny HEAD `main`, stan workflowów oraz otwarte PR.
2. Sprawdzić, czy artefakty SES-085 rzeczywiście znajdują się w aktualnym `main` i czy wymagane testy nadal są podpięte do CI.
3. Wrócić do priorytetu System Builder: przejrzeć `docs/SYSTEM_BUILDER.md`, `docs/history/PROJECT_HISTORY_6_MONTHS.md` oraz istniejące artefakty Constitution/Ontology/Graph/Kernel-DNA/Contracts.
4. Zidentyfikować jeden największy, udokumentowany GAP względem tego planu.
5. Dopiero wtedy wybrać minimalny następny krok. Nie implementować z góry.

## 4. Procedura

`INSPECT → UNDERSTAND → GAP → RED → IMPLEMENT → GREEN → EVIDENCE → STONE`

- RED tylko dla konkretnego, odtwarzalnego braku lub błędu.
- Nie zmieniać runtime, jeśli luka dotyczy wyłącznie dokumentacji lub testów.
- Nie deklarować GREEN bez wyniku dla dokładnego SHA.
- Zachować mały zakres zmian, testy i ślad dowodowy.
- Nie uznawać sukcesu CI za dowód gotowości produkcyjnej.

## 5. Granice

- Bez Docker/Kubernetes i bez wymogu pracy 24/7.
- Bez zmian protokołu, NodeID, modelu zaufania lub formatu wiadomości bez wykazanego GAP i osobnej decyzji.
- Nie scalać PR #13 jako części tej sesji.
- System Builder pozostaje nadrzędną metodą; P2P jest pierwszym systemem budowanym tą metodą.
- Repozytorium, testy i dowody są źródłem prawdy; historia rozmów jest kontekstem.

## 6. Kryterium zakończenia

SES-087 ma zakończyć się wskazaniem aktualnego stanu repozytorium, jednego priorytetowego GAP, minimalnego następnego działania oraz dowodów. Jeśli brak uzasadnionego GAP, zapisać NO GAP — bez wymuszania zmian.

**Stan początkowy:** READY FOR INSPECTION. Aktualny HEAD i CI wymagają ponownej weryfikacji.
