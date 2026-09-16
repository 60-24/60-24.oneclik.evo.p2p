# SES-047 — Session Bootstrap

**Data:** 2026-09-16  
**Status:** OPEN  
**Project:** P2P 60-24 OneClick Evo Positiv  
**Repository:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`

## 1. Cel sesji

Kontynuować budowę najmniejszej uzasadnionej podstawy P2P bez tworzenia sztucznej architektury.

Najbliższy cel techniczny:

> Ustalić i udowodnić minimalną granicę Microkernel/Node na podstawie istniejącego repozytorium, a następnie rozszerzyć dowód o poprawny lifecycle połączenia (disconnect/reconnect oraz obsługę błędnego protokołu), wyłącznie jeśli audyt wykaże rzeczywisty GAP.

## 2. Zasady pracy

Stała sekwencja:

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED TEST → IMPLEMENT → GREEN → VERIFY → DOCUMENT → COMMIT → CONTINUE`

Reguły:
- Repozytorium jest Source of Truth; pamięć rozmowy jest tylko kontekstem.
- Nie ma sztucznego RED.
- Nie deklarować PASS bez rzeczywistego dowodu.
- Najmniejsza spójna zmiana.
- Test to część kontraktu, nie ozdoba.
- Nie tworzyć nowej architektury, jeśli istniejący kod już spełnia wymaganie.
- Nie rozszerzać zakresu bez rzeczywistego GAP-u.
- Maksymalnie kilka istotnych działań między checkpointami.
- Zmiany fundamentalne dotyczące Constitution/Ontology/Trust/Governance wymagają decyzji człowieka.

## 3. Stan wejściowy

SES-044 udowodniła działający przepływ:

`Node A → connect → Node B → message → response`

SES-045 dodała konkretną, reusable API w `src/p2p/node.py`:

- `P2PNode`
- `listen_once()`
- `send()`
- `close()`
- eksport przez `src.p2p`

SES-046 przeprowadziła audyt genealogii Microkernel/Kernel-DNA/OmniKernel/Node/Module i wykazała rzeczywisty GAP: brak jawnego handshake'u tożsamości w istniejącym przepływie.

SES-046 dodała minimalny handshake `HELLO/WELCOME` oraz test handshake proof.

Ostatni potwierdzony CI run: `35067174398` — wszystkie trzy istotne joby GREEN:

- `ses-046-handshake` — SUCCESS
- `concrete-node-api` — SUCCESS
- `regression-standalone-two-node` — SUCCESS

SES-046 checkpoint commit:

`e48f4b8ca9a1d61c2be522b1da600acd7ded4fec`

## 4. Ustalenia terminologiczne SES-046

Na podstawie dostępnej genealogii, z zastrzeżeniem że nie są to nowe zmiany Konstytucji:

- **OmniKernel** — wyższy poziom mechanizmów/fundamentów ekosystemu.
- **Kernel-DNA** — warstwa kontraktów, niezmienników i prymitywów dotyczących bytów, stanu, zdarzeń i relacji.
- **Microkernel** — minimalna techniczna granica/runtime infrastruktury; nie jest centrum inteligencji systemu.
- **Node** — konkretny autonomiczny uczestnik/runtime sieci; nie jest automatycznie synonimem Microkernel.
- **Module** — dołączalna zdolność/funkcja powyżej minimalnej infrastruktury.
- **StemCell** — wzorzec biologiczno-architektoniczny; nie jest równoważny Node.

Ważne: historyczne materiały są dowodem genealogicznym, nie automatyczną władzą nad aktualną architekturą.

## 5. Czego NIE przyjmujemy jako zamrożonej architektury

Nie zatwierdzono jeszcze:

- `Node = Microkernel`
- `ModuleLoader` jako obowiązkowego elementu kernela
- konkretnego `StateVault`/MVCC
- Ed25519 jako ostatecznego kontraktu Identity Microkernel
- nowej nazwy/warstwy `MiniKernel`
- osobnej implementacji zastępującej istniejące `P2PNode`
- Marketplace Modułów jako aktualnego zakresu fundamentu

## 6. Kierunek zaproponowany przez inne LLM

Propozycja `MiniKernel Foundation` jest traktowana jako eksperyment rozwojowy:

- Node A ↔ Node B
- start
- identity
- connect
- handshake
- message exchange
- disconnect
- reconnect
- logs
- correctness before optimization
- bez blockchaina, kryptowaluty, DHT, NAT traversal i przedwczesnego discovery/routingu

Jest zgodna z kierunkiem minimalizacji, ale nie zastępuje genealogii ani istniejących kontraktów repozytorium.

## 7. Zakres SES-047

### Najpierw INSPECT

Sprawdzić aktualny kod i testy dla:

1. lifecycle `P2PNode`;
2. `HELLO/WELCOME` i granicy protocol;
3. zachowania przy zamknięciu połączenia;
4. ponownego połączenia;
5. błędnego/malformed protocol input;
6. logowania i obserwowalności;
7. aktualnego modelu identity;
8. ewentualnych hooków modułów/capabilities.

### Następnie

Zidentyfikować **jeden rzeczywisty GAP**.

Jeżeli GAP istnieje:

`RED TEST → najmniejsza implementacja → GREEN → regresja → dokumentacja → commit`

Jeżeli GAP nie istnieje:

`NO ARTIFICIAL WORK → checkpoint → następny rzeczywisty requirement`

## 8. Poza zakresem

Na tym etapie nie dodawać bez wykazanego wymagania:

- peer discovery
- DHT
- routing wielowęzłowy
- NAT traversal
- blockchain/kryptowaluty
- consensus
- reputacji
- storage rozproszonego
- AI/agent runtime
- GUI
- Marketplace

## 9. Kryterium końcowe SES-047

Sesja może zostać zamknięta tylko wtedy, gdy:

- znaleziony GAP został potwierdzony testem, albo udokumentowano brak GAP-u;
- jeśli implementowano zmianę, wszystkie odpowiednie testy i regresje są GREEN;
- aktualny stan repo jest zapisany;
- powstaje jednoznaczny checkpoint/stone;
- nie ma fałszywego PASS.

## 10. Następny krok po otwarciu sesji

**INSPECT aktualnego repozytorium i kodu `P2PNode` przed jakąkolwiek dalszą implementacją.**
