# SES-064 — CHECKPOINT 01

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repo:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Data:** 2026-09-24  
**Status:** OPEN — IMPLEMENTED, oczekuje na GREEN CI

## Wynik audytu

Issue #7 wskazało hipotezę Identity & Transport Binding Gap.

Inspekcja repo potwierdziła, że wcześniejszy protokół przyjmował:

`HELLO <NodeID>`

i zapisywał przekazany tekst jako `last_peer_id` bez kryptograficznego proof-of-possession.

**Decyzja: REAL GAP.**

## RED

Dodano test:

`sessions/SES-064/test_identity_transport_binding.py`

Test sprawdza dwa przypadki:

1. surowy plaintext `HELLO A` bez dowodu posiadania klucza;
2. `NodeID` niespójny z przedstawionym kluczem publicznym.

W obu przypadkach Node B ma odrzucić peer'a i nie ustawić `last_peer_id`.

## Minimalny fix

Zaimplementowano Ed25519 proof-of-possession.

Nowy handshake:

```
HELLO
  NodeID + public key + client challenge
        ↓
WELCOME
  NodeID + public key + server challenge + signature
        ↓
AUTH
  signature(client private key)
        ↓
ESTABLISHED
```

`NodeID = SHA-256(public key)`.

Serwer weryfikuje podpis klienta przed ustawieniem `last_peer_id`. Klient również weryfikuje podpis serwera.

Nie wprowadzono PKI, Web-of-Trust, certyfikatów, E2E encryption ani libp2p.

## Zgodność

Zachowano:

- TCP;
- Node A ↔ Node B;
- istniejący model `P2PNode`;
- CLI `--listen / --connect`;
- lokalną etykietę `--node-id`;
- komunikat aplikacyjny i `pong-from-B`.

Zmiana polega na tym, że `last_peer_id` jest teraz kryptograficznym NodeID, a nie dowolnym tekstem podanym przez peer'a.

## Zmiany repo

- `src/p2p/protocol.py`
- `src/p2p/node.py`
- `requirements.txt`
- `sessions/SES-064/test_identity_transport_binding.py`
- aktualizacja testów SES-046/047/055/058
- `README.md`
- workflow CI zawiera test SES-064

## Evidence

Commity implementacyjne:

- `91eea197` — authenticated protocol
- `e01a4a8` — cryptography dependency
- `8168e0d2` — authenticated node handshake
- `850cb355` — SES-064 security tests
- `8d95700b`, `759641f8`, `60ee8938`, `173f2261`, `6a8d39f4` — aktualizacja regresji
- `5da465a7` — README

CI musi jeszcze potwierdzić:

- SES-064 GREEN;
- wszystkie istniejące testy GREEN;
- packaged executable GREEN;
- LAN smoke GREEN.

## Status

**REAL GAP → RED → MINIMAL FIX → OCZEKUJE NA GREEN**

Nie zamykać SES-064 przed uzyskaniem pełnego regression evidence.
