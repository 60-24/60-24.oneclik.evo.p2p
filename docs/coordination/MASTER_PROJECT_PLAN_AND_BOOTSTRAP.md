# MASTER_PROJECT_PLAN.md
## Kamień milowy — wspólny model pracy i plan rozwoju

**Data:** 9 listopada 2026  
**Status:** STONE — uzgodniony kierunek strategiczny i operacyjny  
**Właściciel decyzji produktowych:** Tomek  
**Koordynacja i architektura:** ChatGPT  
**Miejsce pracy i źródło prawdy:** GitHub  
**Środowisko opcjonalne:** GitHub Codespaces

---

## 1. Cel dokumentu

Dokument ustanawia wspólne, zrozumiałe dla wszystkich uczestników rozumienie:

- kto pracuje nad projektami i za co odpowiada;
- gdzie znajduje się praca, dokumentacja, kod i historia decyzji;
- jakie są dwa główne cele produktowe;
- jak będziemy planować, wykonywać i kontrolować pracę;
- jakie są najbliższe kroki.

Dokument jest punktem odniesienia dla ChatGPT, Claude Code, GitHub Copilot i Tomka. Ma ograniczyć utratę kontekstu, dublowanie pracy i rozbieżności interpretacyjne.

**Ważne:** jest to zatwierdzony plan i model współpracy, a nie potwierdzenie wykonania audytu, migracji, konfiguracji organizacji ani zmian w kodzie.

## 2. Dwa cele strategiczne

### A. P2P 60-24 OneClick Evo Positiv

Zbudować modularną platformę P2P, która będzie rozwijać się w kierunku ewolucyjnego ekosystemu.

Pierwszym celem użytkowym jest możliwie prosty klient, pozwalający rozpocząć rzeczywiste korzystanie z P2P 60-24 EVO. Następnie platforma ma być rozszerzana o kolejne moduły i możliwości.

Kierunki i ograniczenia:

- P2P jest zdecentralizowaną platformą komunikacji i relacji, a nie blockchainem ani systemem tokenowym.
- Priorytetem jest lokalna autonomia, prywatność i relacje między ludźmi.
- Produkt końcowy nie może wymagać od zwykłego użytkownika instalowania Dockera, Kubernetes ani narzędzi deweloperskich.
- Narzędzia deweloperskie mogą być stosowane w procesie budowy i testowania, jeśli nie przenoszą dodatkowego ciężaru na użytkownika końcowego.
- Architektura ma pozostać modularna, możliwa do testowania i rozwijania bez naruszania stabilnego rdzenia.

Repozytorium główne rozpoznane na obecnym etapie:

`60-24/60-24.oneclik.evo.p2p`

### B. System Builder

Zbudować osobny system budowy systemów i modułów, który docelowo będzie wspierał użytkownika końcowego w ewolucyjnej rozbudowie P2P i całego ekosystemu.

Docelowy cykl działania Buildera:

1. Użytkownik opisuje potrzebę lub pomysł.
2. Builder pomaga przełożyć intencję na zrozumiałą specyfikację.
3. System analizuje wpływ na istniejącą architekturę.
4. Przygotowuje projekt rozwiązania, implementację i testy.
5. Uruchamia kontrolę jakości i przedstawia dowody.
6. Człowiek zatwierdza istotne decyzje i wdrożenie.

Builder ma być osobnym projektem. Nie może być warunkiem uruchomienia ani podstawowego działania P2P. Integracja ma następować stopniowo, przez jasno opisane interfejsy i zależności.

**Stan:** osobne repozytorium Buildera nie zostało jeszcze jednoznacznie wskazane ani zweryfikowane. Nie należy go zgadywać.

## 3. Zespół i odpowiedzialności

| Uczestnik | Główna odpowiedzialność |
|---|---|
| **ChatGPT** | Architektura całości, planowanie, koordynacja, analiza, audyty, specyfikacje, kryteria testów i kontrola dowodów |
| **Claude Code** | Główne zadania implementacyjne, analiza kodu, refaktoryzacja i testy w repozytoriach |
| **GitHub Copilot** | Niezależne zadania implementacyjne, testowe, poprawki i przegląd zmian |
| **Tomek** | Właścicielskie decyzje produktowe, ocena użyteczności, testy z perspektywy użytkownika i zatwierdzanie istotnych zmian |

Podział jest funkcjonalny, a nie sztywny. Zadanie należy powierzyć wykonawcy, który najlepiej nadaje się do jego realizacji.

### Zasady współpracy

- Każde zadanie ma jednego wskazanego właściciela wykonania.
- Równoległa praca jest mile widziana, ale zakresy zadań nie mogą powodować nieuzgodnionych konfliktów.
- Agenci przekazują wyniki w formie możliwej do sprawdzenia: commit, PR, test, raport lub dokument.
- Nie uznajemy deklaracji „zrobione” bez odpowiedniego dowodu.
- Decyzje produktowe i istotne zmiany architektoniczne pozostają pod kontrolą Tomka.
- ChatGPT koordynuje pracę, ale nie zastępuje dowodów z repozytorium ani testów.

## 4. Miejsce pracy i środowisko techniczne

### GitHub — centrum projektu

GitHub jest wspólnym miejscem pracy i źródłem prawdy dla:

- kodu i wersji;
- dokumentacji i decyzji architektonicznych;
- Issues i zadań;
- Pull Requests i przeglądów;
- GitHub Actions, testów i budowania;
- historii zmian i dowodów wykonania.

Dokumentacja projektu powinna wyjaśniać stan rzeczywisty, a nie tylko zamierzenia.

### GitHub Codespaces — środowisko opcjonalne

Codespaces może służyć jako chmurowe środowisko Linux do:

- pracy Claude Code i innych narzędzi;
- budowania i uruchamiania projektu;
- testów integracyjnych;
- odizolowanych eksperymentów;
- ograniczenia obciążenia komputera lokalnego.

Nie zakładamy, że Codespaces musi działać bez przerwy. Należy kontrolować koszty, uprawnienia, bezpieczeństwo i czas działania.

### GitHub Actions — automatyczna kontrola

Actions powinny zapewniać powtarzalne:

- testy;
- lint i kontrole statyczne;
- buildy;
- testy regresyjne;
- publikowanie artefaktów, jeśli jest to uzasadnione.

### Testy lokalne i rzeczywiste

Niektóre testy wymagają rzeczywistych urządzeń lub sieci, np. Windows, Android, LAN i komunikacji między węzłami. Codespaces nie zastępuje takich testów.

## 5. Stan organizacyjny — do zweryfikowania

Na moment ustanowienia tego kamienia milowego zgłoszony stan obejmuje:

- trzy istniejące repozytoria;
- jedną organizację GitHub, która nie została jeszcze skonfigurowana;
- dwa cele produktowe: P2P i System Builder.

Rozpoznane repozytoria:

1. `60-24/60-24.oneclik.evo.p2p` — główna baza implementacyjna P2P.
2. `60-24/Html-P2P-60-24-` — starsze laboratorium koncepcji, eksperymentów i dokumentacji; rola wymaga audytu.
3. `60-24/p2p.oneclik` — wcześniejszy fundament koncepcyjny i architektoniczny; rola wymaga audytu.

Dokładny status organizacji GitHub, uprawnienia, konfiguracja i ewentualne repozytorium Buildera wymagają sprawdzenia bezpośrednio na GitHubie.

### Zasada bezpieczeństwa danych

Do czasu zakończenia inwentaryzacji:

- nie usuwamy repozytoriów;
- nie przenosimy repozytoriów;
- nie łączymy historii projektów;
- nie zmieniamy bez potrzeby gałęzi `main`;
- nie uznajemy starszych repozytoriów za niepotrzebne bez analizy;
- nie tworzymy na podstawie domysłów nowej struktury organizacyjnej.

Repozytoria mogą zawierać unikalną dokumentację, decyzje i działające wersje. Najpierw trzeba ustalić ich rzeczywistą wartość.

## 6. Zasady techniczne i produktowe

1. P2P i System Builder pozostają odrębnymi projektami.
2. Builder ma wspierać rozwój P2P, ale nie może blokować podstawowego działania P2P.
3. Repozytorium jest źródłem prawdy dla kodu i historii zmian.
4. Dokumentacja musi odróżniać stan wykonany od propozycji i planów.
5. Nie wprowadzamy technologii tylko dlatego, że jest popularna.
6. Każda zależność ma uzasadnienie, koszt i wpływ na użytkownika końcowego.
7. Użytkownik końcowy nie powinien potrzebować wiedzy programistycznej do podstawowego korzystania z P2P.
8. Istotne zmiany powinny być modularne, testowalne i możliwe do wycofania.
9. Nie deklarujemy GREEN bez przeprowadzonych testów i widocznych wyników.
10. Nie deklarujemy STONE bez utrwalenia decyzji, zakresu i dowodów.

## 7. Wspólny standard realizacji zadań

Stosujemy cykl:

`INSPECT → UNDERSTAND → GAP → RED → IMPLEMENT → GREEN → EVIDENCE → STONE`

Znaczenie:

- **INSPECT** — sprawdzenie aktualnego repozytorium, gałęzi i stanu.
- **UNDERSTAND** — zrozumienie celu, ograniczeń i istniejących decyzji.
- **GAP** — wskazanie różnicy między stanem obecnym a wymaganym.
- **RED** — przygotowanie testu, który ujawnia brak lub błąd.
- **IMPLEMENT** — najmniejsza uzasadniona zmiana.
- **GREEN** — testy przechodzą.
- **EVIDENCE** — zapis dowodów: wyniki testów, commit, PR, logi.
- **STONE** — utrwalenie stabilnego wyniku i aktualizacja dokumentacji.

Nie każdy rodzaj zadania wymaga testu kodu, ale każde zadanie musi mieć odpowiednie kryterium odbioru i dowód.

## 8. Plan etapów i orientacyjny harmonogram

Terminy są szacunkami planistycznymi. Po audycie zostaną skorygowane na podstawie rzeczywistego stanu repozytoriów, dostępności wykonawców i ryzyka.

| Etap | Zakres | Orientacyjny czas |
|---|---|---|
| **0. Inwentaryzacja** | Audyt trzech repozytoriów, organizacji, dokumentacji, wersji, uprawnień i automatyzacji | 2–3 dni pracy analitycznej |
| **1. Organizacja środowiska** | Docelowy podział repozytoriów, organizacja GitHub, role, zasady agentów, Codespaces według potrzeby | około 1 tygodnia |
| **2. Automatyzacja produkcji** | CI, testy, buildy, standard PR, raportowanie dowodów | 1–2 tygodnie |
| **3. P2P — pierwszy używalny klient** | Uruchomienie węzła, tożsamość, zaufany kontakt, połączenie dwóch węzłów, wiadomości, pakiety instalacyjne | 2–4 tygodnie |
| **4. Builder — pierwszy prototyp** | Intencja użytkownika → specyfikacja → propozycja modułu → implementacja → testy → zatwierdzenie | 2–4 tygodnie, częściowo równolegle z etapem 3 |
| **5. Pierwszy cykl ewolucyjny** | Builder przygotowuje rozszerzenie P2P, a P2P dostarcza środowisko testowe; kontrola, wdrożenie i możliwość wycofania | 1–2 tygodnie na pierwszy cykl |

Harmonogram nie jest obietnicą daty ukończenia produktu. Jego zadaniem jest porządkowanie zależności i wykorzystanie możliwości zespołu.

## 9. Model wykorzystania potencjału produkcyjnego

Docelowo pracujemy równolegle w dwóch strumieniach:

### Strumień P2P

- stabilizacja i rozwój rdzenia;
- pierwszy używalny klient;
- testy komunikacji między węzłami;
- bezpieczeństwo tożsamości i zaufanych kontaktów;
- przygotowanie modułowości i rozszerzalności.

### Strumień Builder

- inwentaryzacja wcześniejszych prac;
- określenie minimalnego zakresu Buildera;
- prototyp przepływu od intencji do specyfikacji;
- generowanie testów i propozycji zmian;
- kontrola przez człowieka.

Wspólne elementy:

- standard dokumentacji;
- automatyzacja testów;
- standard PR i przeglądu;
- zarządzanie zadaniami;
- rejestr decyzji;
- kontrola kosztów i uprawnień.

Nie uruchamiamy dwóch strumieni pełną mocą, zanim zakończymy inwentaryzację i ustalimy bezpieczne granice pracy.

## 10. Pierwszy krok po tym kamieniu milowym

**Etap 0 — inwentaryzacja. Bez zmian w kodzie, bez migracji i bez ingerencji w `main`.**

Zakres audytu:

1. Sprawdzić wszystkie trzy repozytoria: strukturę, gałęzie, ostatnie commity, README, dokumentację, workflow, testy i wydania.
2. Ustalić, co jest aktualne, co historyczne, co eksperymentalne i co może być unikalne.
3. Zidentyfikować materiały dotyczące System Buildera.
4. Sprawdzić organizację GitHub, członków, uprawnienia i ustawienia bezpieczeństwa — bez zmian.
5. Ocenić gotowość do użycia Codespaces i GitHub Actions.
6. Przygotować mapę repozytoriów i rekomendowany układ docelowy.
7. Wskazać luki, ryzyka, koszty i zależności.
8. Przedstawić plan konfiguracji jako osobny zestaw działań do zatwierdzenia.

### Kryteria zakończenia etapu 0

Etap można uznać za zakończony, gdy istnieje:

- mapa repozytoriów i ich rzeczywistych ról;
- wskazanie źródeł prawdy dla P2P i Buildera;
- lista istniejących i brakujących dokumentów;
- raport stanu testów i automatyzacji;
- raport stanu organizacji i uprawnień;
- rekomendacja docelowej struktury;
- uporządkowana lista kolejnych zadań z właścicielami i kryteriami odbioru.

## 11. Reguły dla nowej sesji i współpracowników AI

Każdy współpracownik powinien:

1. Przeczytać ten dokument oraz wskazane dokumenty projektu.
2. Sprawdzić aktualny stan repozytorium przed proponowaniem zmian.
3. Nie zakładać, że wcześniejszy opis nadal odpowiada stanowi kodu.
4. Rozdzielać fakty, hipotezy, propozycje i wykonane działania.
5. Nie wykonywać nieuzgodnionych zmian destrukcyjnych.
6. Pracować na osobnej gałęzi lub przez PR, zgodnie z zasadami repozytorium.
7. Dołączać wyniki testów i identyfikatory commitów/PR.
8. Aktualizować dokumentację po zatwierdzonych zmianach.
9. Zgłaszać blokady i niepewności zamiast zgadywać.
10. Pozostawiać czytelny raport przekazania pracy.

## 12. Status kamienia milowego

**STONE — uzgodniony model współpracy i kierunek strategiczny.**

Zatwierdzone:

- dwa cele strategiczne: modularna platforma P2P oraz osobny System Builder;
- zespół: ChatGPT, Claude Code, Copilot i Tomek;
- GitHub jako centrum pracy i źródło prawdy;
- Codespaces jako opcjonalne środowisko chmurowe;
- praca etapami, równolegle tam, gdzie jest to bezpieczne;
- audyt przed migracją, porządkowaniem i implementacją zmian organizacyjnych;
- kontrola jakości przez testy, dowody i decyzje człowieka.

Niezrealizowane i wymagające dalszej pracy:

- pełny audyt trzech repozytoriów;
- weryfikacja i konfiguracja organizacji GitHub;
- jednoznaczna identyfikacja repozytorium Buildera;
- zatwierdzenie docelowej struktury repozytoriów;
- konfiguracja środowisk i automatyzacji;
- wykonanie kolejnych etapów produktu.

---

# BOOTSTRAP — otwarcie następnej sesji

## Sesja: MASTER-001 — Inwentaryzacja i przygotowanie środowiska

**Projekt nadrzędny:** P2P 60-24 OneClick Evo Positiv + System Builder  
**Data otwarcia:** 9 listopada 2026  
**Stan wejściowy:** MASTER_PROJECT_PLAN.md — STONE  
**Główne zadanie:** rozpocząć Etap 0 — inwentaryzację, bez zmian w kodzie i konfiguracji.

### Instrukcja dla ChatGPT

Przejmij rolę koordynatora i architekta całości. Pracuj autonomicznie w ramach zatwierdzonego zakresu.

1. Przeczytaj cały `MASTER_PROJECT_PLAN.md`.
2. Zweryfikuj aktualny stan trzech repozytoriów GitHub.
3. Zbadaj organizację GitHub i jej rzeczywisty stan, ale niczego jeszcze nie zmieniaj.
4. Odszukaj istniejące materiały dotyczące System Buildera.
5. Przygotuj raport inwentaryzacji i mapę zależności.
6. Zaproponuj docelową strukturę repozytoriów oraz kolejność konfiguracji.
7. Rozdziel zadania dla Claude Code i Copilota, jeśli będą mogły pracować niezależnie.
8. Przygotuj zrozumiałe instrukcje dla każdego agenta, z kontekstem, zakresem, kryteriami akceptacji i zakazanymi zmianami.
9. Nie deklaruj wykonania czynności, których nie potwierdzają narzędzia lub repozytorium.

### Granice uprawnień

Bez dodatkowego zatwierdzenia nie:

- usuwaj ani nie przenoś repozytoriów;
- zmieniaj ustawień organizacji i uprawnień;
- zmieniaj `main`;
- łącz projektów P2P i Builder;
- instaluj płatnych usług ani nie uruchamiaj kosztownych środowisk;
- wdrażaj zmian w produkcie.

Audyt, analiza, dokumentacja propozycji i przygotowanie zadań są dozwolone.

### Oczekiwany rezultat sesji

`MASTER-001_INVENTORY_REPORT.md`

Raport ma zawierać:

- faktyczny stan repozytoriów;
- mapę dokumentacji i wersji;
- rozpoznanie prac P2P i Buildera;
- stan organizacji i środowiska;
- luki, ryzyka i zależności;
- rekomendowaną strukturę;
- plan następnych działań;
- listę decyzji wymagających zatwierdzenia przez Tomka.

**Kryterium zamknięcia:** kompletna, oparta na dowodach inwentaryzacja i rekomendacja kolejnego etapu. Nie jest wymagane wprowadzanie zmian w kodzie.

---

**Zasada nadrzędna:** najpierw rozumiemy i zabezpieczamy istniejący dorobek, potem porządkujemy środowisko, a następnie zwiększamy tempo budowy. Repozytorium jest źródłem prawdy. Człowiek zachowuje kontrolę nad istotnymi decyzjami.