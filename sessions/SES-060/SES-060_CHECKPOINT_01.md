# SES-060 — CHECKPOINT 01

**Data:** 2026-09-20  
**Status:** GREEN — GAP CLOSED  
**HEAD:** `a385cc4d1902b7671a4753efb1e2b93e35e125e5`

## INSPECT

Po SES-059 obecny runtime pozostaje minimalnym, standalone Node A ↔ Node B z:
- executable Linux x86_64;
- HELLO/WELCOME;
- bidirectional peer identity;
- application message + response;
- loopback i non-loopback IPv4 proof;
- actionable CLI errors dla address/connection failures;
- regression CI i publikowany artifact.

## IDENTIFIED GAP

**GAP-060-01 — malformed peer handshake was not handled at the CLI boundary.**

Audyt `src/p2p/node.py` wykazał, że `parse_hello()` i `parse_welcome()` zgłaszają `ValueError`, ale CLI obsługiwało te wyjątki tylko częściowo:
- listener mógł zakończyć się surowym tracebackiem po niepoprawnym HELLO;
- connector mógł zakończyć się surowym tracebackiem po niepoprawnym WELCOME.

To był rzeczywisty GAP, potwierdzony testem RED.

## RED EVIDENCE

Commit testowy:
`662542cd944f635e4b5153b361f6073ca549630b`

P2P Linux run:
`35530322573`

Wynik:
- 3 istniejące CLI tests — PASS;
- 2 nowe malformed-handshake tests — FAIL;
- workflow zakończył się FAILURE;
- log zawierał rzeczywiste `ValueError: invalid handshake` oraz `ValueError: handshake failed`.

Nie był to sztuczny RED.

## MINIMAL FIX

Commit:
`a385cc4d1902b7671a4753efb1e2b93e35e125e5`

Zmiana ograniczona do CLI boundary:
- `_listen()` obsługuje `ValueError` z peer handshake;
- `_connect()` obsługuje `ValueError` z peer handshake;
- użytkownik otrzymuje krótki komunikat `ERROR: Invalid peer handshake...`;
- protokół i architektura Node nie zostały zmienione.

## GREEN EVIDENCE

P2P Linux executable:
- run: `35530354510`
- conclusion: **success**
- artifact: `P2P60-24Node-linux-x86_64`
- artifact ID: `10611047695`
- SHA-256: `e45c6082bd7a74fdcdd3291d768ade427a812b1a2c3ec89d0758540f785506a9`
- artifact: not expired at verification
- all P2P regression tests passed before build
- packaged executable build and smoke test completed successfully.

## RESULT

Granica dowodu została przesunięta: nie tylko błędne adresy i połączenia, ale także niepoprawny handshake peer-to-peer jest obsługiwany bez surowego tracebacku na CLI.

Brak potrzeby zmiany protokołu, discovery, GUI, NAT, relay lub System Builder integration.
