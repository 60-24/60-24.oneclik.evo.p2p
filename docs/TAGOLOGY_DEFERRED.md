# Tagologia — zapis koncepcji odłożonej do późniejszego powrotu

**Status:** PARKED / EXPERIMENTAL  
**Właściciel koncepcyjny:** P2P 60-24 OneClick Evo Positiv  
**Źródło:** SES-086, branch `ses-086-tagology-proposal`, PR #13  
**Decyzja:** zachować jako jeden z bytów systemowych; nie rozwijać teraz i nie uznawać za ontologię kanoniczną.

## Po co zachowujemy

Tagologia jest propozycją uporządkowania znaczeń i formalnych komunikatów. Może w przyszłości wspierać System Builder, ontologię i kontrakty, ale obecnie nie jest blokadą dla dalszego rozwoju P2P ani System Buildera.

## Zachowany model

- **Tagologia H (Human):** pojęcia, definicje, kontekst, relacje, przykłady, pochodzenie, rewizje i jawne spory.
- **Tagologia S (System):** typowane, wersjonowane i deterministycznie walidowane komunikaty maszynowe.
- **Most H↔S:** opcjonalne, jawne i wersjonowane mapowanie, ze wskazaniem zakresu i strat informacji.

To model koncepcyjny, nie zatwierdzony kontrakt runtime ani format sieciowy.

## Niezmienniki do zachowania

1. Poprawna składnia nie dowodzi prawdziwości.
2. Definicja nie jest dowodem; dowód nie jest tożsamością.
3. Uwierzytelnienie nie oznacza autoryzacji ani zaufania.
4. Brakujące lub niejednoznaczne znaczenie nie może być zgadywane.
5. Zmiana definicji nie może po cichu zmieniać znaczenia starych danych.
6. Mapowanie H↔S musi jawnie ujawniać zakres i utratę informacji.
7. Tagologia nie zmienia automatycznie HELLO/WELCOME/AUTH, framingu TCP, NodeID, zaufania ani formatu wiadomości P2P.

## Artefakty źródłowe

- Propozycja: [TAGOLOGY_PROPOSAL_v0.1.md](../architecture/proposals/TAGOLOGY_PROPOSAL_v0.1.md) — dostępna na gałęzi eksperymentalnej SES-086.
- Eksperyment i ograniczenia: [SES-086_CLOSEOUT.md](../sessions/SES-086/SES-086_CLOSEOUT.md).
- Protokół oceny zrozumienia: [SES-086_HUMAN_COMPREHENSION_CHECK.md](../sessions/SES-086/SES-086_HUMAN_COMPREHENSION_CHECK.md).
- PR #13 pozostaje Draft i nie jest scalony: https://github.com/60-24/60-24.oneclik.evo.p2p/pull/13

Uwaga: odnośniki do artefaktów z gałęzi eksperymentalnej nie muszą być dostępne na `main`; PR #13 jest ich śladem źródłowym.

## Kiedy wrócić

Wrócić dopiero, gdy konkretny problem w System Builderze lub P2P pokaże, że niejednoznaczność pojęć albo brak formalnego kontraktu utrudnia projektowanie, walidację lub interoperacyjność. Wtedy wznowić od inspekcji istniejącej propozycji, nie od ponownego wymyślania koncepcji.

**Nie jest wymagane dopracowanie Tagologii teraz.**
