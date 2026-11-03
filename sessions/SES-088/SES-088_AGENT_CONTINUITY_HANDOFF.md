# SES-088 — HANDOFF: WYBÓR GOTOWEGO AGENTA CIĄGŁOŚCI

**Projekt:** P2P 60-24 OneClick Evo Positiv + System Builder  
**Repozytorium:** `60-24/60-24.oneclik.evo.p2p`  
**Branch dokumentu:** `ses-088-foundation-and-system-builder-gap-audit`  
**Baza znana z ostatniej inspekcji:** `main` @ `a462b8f0073490f5423edf4d01dd0ce36642176f` (2026-10-21)  
**Status:** przygotowanie przekazania; brak zmian runtime, brak instalacji narzędzi, brak decyzji zakupowej.

## 1. Cel

Użytkownik chce uzyskać **ciągłą, autonomiczną pracę nad istniejącym repozytorium**, zamiast samodzielnie budować własnego agenta. Należy wybrać gotowe rozwiązanie, które może pracować w chmurze/bez stałego nadzoru użytkownika, realizować wieloetapowe zadania, korzystać z GitHub, uruchamiać testy, wznawiać pracę i pozostawiać sprawdzalne dowody.

**Nie budować własnego agenta od zera. Nie instalować ani nie kupować niczego przed weryfikacją.**

## 2. Ustalone zasady

- Użytkownik zachowuje suwerenność; agent ma autonomię wykonawczą, nie prawo do samodzielnej zmiany fundamentalnych zasad.
- Repozytorium jest źródłem prawdy; dokumenty rozmowy służą przekazaniu kontekstu.
- Najpierw INSPECT → UNDERSTAND → GAP; potem minimalny test praktyczny.
- Nie deklarować GREEN/PASS bez rzeczywistych dowodów.
- Nie zmieniać `main` podczas wstępnej próby. Preferować osobną gałąź i PR.
- Nie scalać zmian chronionych ani nie zmieniać konstytucji/ontologii bazowej/modelu zaufania/bezpieczeństwa bez ludzkiej zgody.
- Nie wymagać Docker/Kubernetes ani dodatkowej instalacji od użytkownika końcowego produktu P2P.
- Oszczędzać tokeny i unikać rozbudowanej architektury bez wykazanego GAP.

## 3. Kandydaci z rozmowy

Lista wstępna obejmowała GitHub Copilot, Claude Code, OpenAI Codex, Cline, Aider, Cursor, OpenCode, Devin i OpenHands.

**Do najbliższego porównania zawężono:**
1. **Claude Code Routines** — kandydat ze względu na harmonogramy i uruchamianie przez zdarzenia/integracje; trzeba zweryfikować bieżącą dostępność, etap preview, plan, limity i koszt.
2. **GitHub Copilot Cloud Agent** — kandydat ze względu na bezpośredni przepływ GitHub Issues → praca agenta → pull request; trzeba zweryfikować możliwość dostatecznie ciągłego, autonomicznego wybierania/wznawiania zadań i wymagany plan.
3. **OpenAI Codex** — zachować jako punkt odniesienia, szczególnie dla zadań w chmurze i pracy/testowania repozytorium.
4. **Devin / OpenHands** — wcześniejsi kandydaci, ale nie uznawać ich za zwycięzców bez porównania.

To nie jest ostateczna decyzja. Wcześniejsze wskazanie Devin było wstępne; ostatnia rekomendacja robocza to sprawdzić najpierw Claude Code Routines i GitHub Copilot Cloud Agent.

## 4. Co oznacza „ciągłość”

Nie utożsamiać wykonywania pojedynczego zadania w chmurze z pełną ciągłością. Sprawdzić oddzielnie:
- trwały stan zadania i wznawianie po przerwie;
- wyzwalacze: harmonogram, GitHub Issues/PR/CI lub API;
- czy agent sam może wybrać następne zadanie z uzgodnionego planu, czy potrzebuje każdorazowego promptu;
- dostęp do repozytorium i minimalne uprawnienia;
- uruchamianie testów i obsługę niepowodzeń;
- audytowalność: logi, diff, branch, PR, dowody testów;
- bramki akceptacji i możliwość zatrzymania/wyłączenia;
- limity, koszt przewidywalny i koszty modeli/usług dodatkowych;
- dostępność w Polsce i wymagania planu/organizacji.

## 5. Plan następnej sesji

1. Odświeżyć aktualny stan `main`, gałęzi SES-088 i status CI. Nie zakładać, że stan z 2026-10-21 jest nadal aktualny.
2. Wyjaśnić status pozostałego zakresu SES-087: historyczny Git bundle pozostaje nierozstrzygnięty. Bezpiecznie można go jawnie odłożyć i nie używać; nie odtwarzać go bez pełnej walidacji.
3. Porównać na podstawie aktualnej dokumentacji oficjalnej przede wszystkim Claude Code Routines i GitHub Copilot Cloud Agent; Codex jako benchmark, jeśli wnosi istotną różnicę.
4. Zastosować kryteria z sekcji 4. Nie mnożyć opcji, jeśli jeden kandydat spełni wymagania wyraźnie lepiej.
5. Wybrać jeden kandydat do ograniczonej próby **read-only** na repozytorium: odczytać ten handoff, rozpoznać stan projektu, zaproponować kolejny krok i podać dowody/odnośniki. Nie zmieniać `main`.
6. Jeśli próba jest dobra, zaproponować minimalną konfigurację automatyzacji i uprawnień; uzyskać zgodę człowieka przed płatną subskrypcją, udzieleniem szerokich uprawnień lub uruchomieniem zmian.
7. Dopiero po weryfikacji agenta wrócić do mapowania GAP System Builder → rzeczywista, kontrolowana zmiana P2P.

## 6. Kontekst projektu, którego nie wolno zgubić

- Repo: `60-24/60-24.oneclik.evo.p2p`.
- Znany ostatni `main`: `a462b8f0073490f5423edf4d01dd0ce36642176f`; koniecznie odświeżyć.
- Istnieje wcześniejsza gałąź `ses-088-foundation-and-system-builder-gap-audit` z bootstrapem `sessions/SES-088/SES-088_BOOTSTRAP.md`.
- System Builder ma pipeline Intent → Specification → BuildPlan → Authorization → Execution → Result/Effect → Observation/Evidence → Verification → Delivery Manifest.
- Obecny executor tworzy proste lokalne pliki tekstowe; nie wykazano jeszcze E2E, w którym nietechniczny użytkownik bezpiecznie zmienia rzeczywistą funkcję P2P przez System Builder.
- P2P runtime pozostaje minimalnym PoC, nie produkcyjnym systemem P2P.
- Nie traktować roboczych modeli ontologii, Kernel-DNA, Microkernel ani StemCell jako automatycznie zatwierdzonej konstytucji.
- Nie uruchamiać historycznego skryptu publikacyjnego z root `.bin`, który ma niebezpieczny wzorzec PAT w URL.
- Brak podstaw do deklarowania pełnego GREEN produktu.

## 7. Kryterium zamknięcia fazy wyboru agenta

Wskazany zostaje jeden najlepszy kandydat z uzasadnieniem opartym na aktualnych źródłach; jawnie opisane są ograniczenia ciągłości, wymagany plan, uprawnienia i koszty; istnieje plan bezpiecznej próby bez zmian na `main`. Do tego czasu status to **DECISION PENDING**, nie GREEN.

---
**Zasada końcowa:** wybieramy gotowe narzędzie, nie budujemy własnego. Agent sugeruje i wykonuje w granicach uprawnień; człowiek zachowuje kontrolę nad intencją i decyzjami chronionymi.
