# Tagologia — model dwóch niezależnych warstw v0.2

**Status:** EXPERIMENTAL; brak zatwierdzenia ontologii kanonicznej, runtime i formatu sieciowego  
**Projekt:** P2P 60-24 OneClick Evo Positiv · SES-086

## 1. Proponowana decyzja architektoniczna

Tagologia nie jest jednym uniwersalnym językiem. Składa się z dwóch niezależnych systemów i opcjonalnego, jawnego mostu:

- **Tagologia H (Human):** wspólne pojęcia i znaczenia — wersjonowana, rozwijana wspólnie baza semantyczna, łącząca cechy słownika, encyklopedii i edytora ontologii.
- **Tagologia S (System):** formalne komunikaty dla programów, AI i węzłów — typowane, wersjonowane, deterministyczne i lokalnie walidowane.
- **Most H↔S:** jawne, wersjonowane mapowanie wybranych pojęć ludzkich na identyfikatory systemowe. To adapter, nie trzecia władza semantyczna.

H i S mogą rozwijać się niezależnie. Zmiana H nie zmienia automatycznie S ani komunikatów sieciowych. Zmiana S nie wymaga dodania każdego pola operacyjnego do ludzkiej ontologii. Mapowanie może być częściowe.

## 2. Tagologia H — wspólne rozumienie

H pomaga rozwiązać problem różnych interpretacji tych samych słów. Udostępnia definicje, kontekst, relacje, przykłady, pochodzenie, historię zmian i spory.

Rekord pojęcia powinien rozróżniać:
- stabilne ID pojęcia — niezależne od etykiety;
- etykietę preferowaną i etykiety lokalne/językowe;
- krótką definicję oraz zakres i kontekst użycia;
- relacje do innych pojęć, z określonym znaczeniem;
- przykłady pozytywne i negatywne, gdy są potrzebne;
- pochodzenie, autora/edytora i historię rewizji;
- cykl życia: draft, proposed, accepted, deprecated;
- znaną wieloznaczność, konkurencyjne definicje i nierozstrzygnięte spory.

H nie rozstrzyga prawdy przez głosowanie. Rejestruje definicje oraz sposób ich przyjęcia lub zakwestionowania. Podobne etykiety nie wystarczają, by połączyć pojęcia. Konflikty pozostają widoczne, a nie nadpisywane po cichu.

## 3. Tagologia S — jednoznaczne przetwarzanie

S opisuje komunikaty lub żądania w formalnej strukturze. Celem jest powtarzalne parsowanie, walidacja i przetwarzanie, a nie osiągnięcie filozoficznego konsensusu.

Kontrakt S musi określać:
- identyfikator i wersję schematu;
- rodzaj komunikatu i pola wymagane;
- stabilne identyfikatory typów/terminów;
- typy wartości, ograniczenia, referencje i sygnatury relacji;
- deterministyczną normalizację i serializację;
- obsługę nieznanych wymaganych pól/terminów i wersji;
- reguły rozszerzeń i zgodności wstecznej;
- kategorie błędów i wyniki walidacji.

Pierwszy PoC powinien użyć znanej reprezentacji z deterministycznymi regułami (np. JSON ze ścisłym schematem), zamiast od razu wymyślać własny zwarty język. Kompaktowe kodowanie można ocenić później na podstawie pomiarów. Abstrakcyjny kontrakt nie może zależeć od jednego kodowania.

Nieznanej wymaganej semantyki ani nieobsługiwanej wersji nie wolno zgadywać. Wynik „poprawny według schematu X” nie oznacza, że komunikat jest prawdziwy, autoryzowany lub godny zaufania.

## 4. Niezależność i granice

1. H definiuje znaczenia dla ludzi; S definiuje formalną strukturę i reguły przetwarzania.
2. ID jest tożsamością; etykieta jest prezentacją.
3. Wersje są jawne. Nie wolno po cichu zmieniać interpretacji starych danych.
4. Składnia, poprawność semantyczna, prawdziwość, dowody, tożsamość, autoryzacja i lokalne zaufanie to odrębne wymiary.
5. Uwierzytelniony nadawca ≠ nadawca godny zaufania; poprawny komunikat ≠ prawdziwe twierdzenie; zaakceptowana definicja ≠ powszechna zgoda.
6. H może zawierać pojęcia bez reprezentacji w S. S może zawierać pola operacyjne niewidoczne jako pojęcia H.
7. Mapowanie określa kierunek, wersje źródła i celu, zakres oraz utratę informacji. Mapowania niejednoznaczne lub wiele-do-jednego trzeba oznaczać.
8. Nie jest wymagany centralny serwer ani globalny autorytet semantyczny.
9. Częstość użycia może podsunąć kandydata, ale nie awansuje go automatycznie do kanonu.
10. Integracja sieciowa wymaga osobnej decyzji. Ta propozycja nie zmienia HELLO/WELCOME/AUTH, framingu TCP, NodeID, tożsamości ani zaufania.

## 5. Model danych — szkic, nie kanon

**H / pojęcie:** concept_id, labels, definition, scope, relations, examples, provenance, lifecycle, revision. Każdy typ relacji określa własne znaczenie, sygnaturę źródła/celu i liczność. Rewizje zachowują historię.

**S / komunikat — przykładowy kształt:**

```json
{
  "schema": "urn:60-24:tagologia-s:resource-request",
  "version": "0.1",
  "kind": "resource.request",
  "statement_id": "urn:example:statement:001",
  "subject": {"type": "node", "id": "node:abc"},
  "resource": {"type": "resource", "id": "resource:17"},
  "intent": "access",
  "constraints": {},
  "references": []
}
```

To ilustracja struktury, nie zatwierdzony kontrakt sieciowy. Przed implementacją trzeba zdefiniować dozwolone identyfikatory, pola, reguły walidacji i błędy.

## 6. Most H↔S

Mapowanie może mieć postać: ID pojęcia i rewizja H → ID terminu/typu S i wersja schematu.

Każdy wpis mapowania określa:
- pojęcie/revizję źródłową i identyfikator/wersję docelową;
- regułę i zakres mapowania;
- charakter: dokładne, węższe, szersze lub stratne;
- obsługę pojęcia brakującego, niejednoznacznego, przestarzałego lub spornego;
- przykłady i testy konwersji.

Nie wolno automatycznie przekładać dowolnego tekstu na wykonywalne znaczenie systemowe. AI może zaproponować mapowanie, ale musi ono być jawne i sprawdzalne; nie daje to uprawnień do wykonania operacji.

## 7. Ewolucja i zgodność

**H:** propozycja → dyskusja i przykłady → przegląd definicji/zakresu → przyjęcie rewizji → zachowanie historii. Definicje konkurencyjne mogą współistnieć z jawnym kontekstem.

**S:** szkic kontraktu → fixtures → klasyfikacja zgodności → jawne wydanie wersji → wsparcie walidatora. Zmiany łamiące zgodność wymagają nowej wersji głównej. Zmiany addytywne są zgodne tylko wtedy, gdy określono reguły nieznanych pól i rozszerzeń.

**Most:** wersjonowany niezależnie. Zmiana mapowania nie może po cichu przepisywać pojęć, zapisanych komunikatów ani starych mapowań.

Numery wersji, np. 0.1, są robocze do czasu zatwierdzenia polityki zgodności. Interpretację wyznaczają ID i wersje, nie same etykiety.

## 8. Pierwszy ograniczony eksperyment

Domena: **prośba o dostęp/udostępnienie zasobu**.

1. H PoC: 10–20 pojęć, definicje, relacje, przykłady i co najmniej jedno celowo wieloznaczne/sporne pojęcie.
2. S PoC: mały typowany kontrakt dla request, offer, accept, refuse oraz wyniku/odwołań do dowodów.
3. Most PoC: mapować wyłącznie pojęcia niezbędne dla komunikatów; opisać znaczenia niemapowalne.
4. Najpierw walidacja lokalna; bez sieci i GUI/autocomplete.
5. Testy poprawnych/błędnych przykładów, niezgodnych wersji, brakujących referencji, złych sygnatur relacji, nieznanych wymaganych ID, deterministycznej normalizacji i rozdzielenia prawdy od zaufania.

Około 20 pojęć to orientacyjny limit minimalizmu, nie quota. Dodawać tylko to, czego wymagają przykłady.

## 9. Kryteria akceptacji

- [ ] Zatwierdzone granice i odpowiedzialności H oraz S.
- [ ] Określone ID, rewizje, cykl życia i governance H.
- [ ] Określone wersjonowanie, normalizacja i obsługa nieznanych pól S.
- [ ] Jawne wersjonowanie i zasady stratności mapowania H↔S.
- [ ] Przykłady oddzielają składnię, znaczenie, prawdę, dowody, autoryzację i zaufanie.
- [ ] Fixtures i testy istnieją i przechodzą przed deklaracją GREEN.
- [ ] Integracja runtime/protokołu ma osobną zatwierdzoną decyzję.
- [ ] Akceptacja człowieka jest zapisana przed awansem do kanonu.

## 10. Decyzja do przeglądu

Najpierw ocenić **model dwóch warstw i jawnego mostu**. Dopiero potem wybierać kanoniczne typy, dokładne schematy i format komunikatu. Do czasu decyzji jest to propozycja eksperymentalna.
