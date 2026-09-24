# SES-064 — CLOSEOUT

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Data:** 2026-09-24  
**Status:** GREEN / CLOSED / STONE

## Cel

Sprawdzić hipotezę Issue #7:

> Czy Node B akceptuje NodeID przedstawiony w plaintextowym HELLO bez kryptograficznego proof-of-possession?

## Wynik

**REAL GAP — potwierdzony.**

Przed zmianą Node B zapisywał NodeID bez kryptograficznego uwierzytelnienia.

## Minimalne rozwiązanie

Wprowadzono:

- Ed25519;
- `NodeID = SHA-256(public key)`;
- client challenge;
- server challenge;
- podpis WELCOME;
- AUTH z podpisem klienta;
- weryfikację proof-of-possession przed ustawieniem `last_peer_id`.

Wire protocol:

```
HELLO   NodeID + PublicKey + Challenge
WELCOME NodeID + PublicKey + Challenge + Signature
AUTH    Signature
```

Etykieta `--node-id A/B` pozostaje wyłącznie lokalną etykietą prezentacyjną. Nie jest źródłem kryptograficznej tożsamości.

## RED evidence

`sessions/SES-064/test_identity_transport_binding.py`

Test obejmuje:

1. plaintextowy HELLO bez PoP;
2. NodeID niezwiązany z public key.

Oba przypadki są odrzucane.

## GREEN evidence

**P2P Linux executable**

- run: `35938275053`
- job: `107440184493`
- SES-064: **2 passed**
- wcześniejsze testy regresyjne: GREEN
- PyInstaller build: GREEN
- packaged two-node smoke: GREEN
- LAN smoke: GREEN

**Pozostałe P2P proofs**

- SES-043 two-node proof: run `35938275062` — GREEN
- P2P demo: run `35938275067` — GREEN
- SES-045/046/047/049 — GREEN

## Zakres kontrolowany

Nie dodano:

- PKI;
- certyfikatów;
- Web-of-Trust;
- blockchain;
- tokenów;
- libp2p;
- E2E encryption;
- mesh/routing;
- System Builder integration.

## Granica techniczna

Klucz Ed25519 jest obecnie generowany przy starcie procesu. Oznacza to, że obecny fix zapewnia kryptograficzne uwierzytelnienie bieżącej sesji, ale nie zapewnia jeszcze trwałej tożsamości NodeID między restartami.

To jest osobny, przyszły GAP/temat projektowy — nie rozszerzamy nim SES-064.

## Decyzja

```
OBSERVE
  ↓
REAL GAP
  ↓
RED
  ↓
MINIMAL Ed25519 PoP
  ↓
GREEN
  ↓
REGRESSION GREEN
  ↓
STONE
```

**SES-064 CLOSED / STONE.**
