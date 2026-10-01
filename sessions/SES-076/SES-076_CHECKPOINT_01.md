# SES-076 — Windows LAN Evidence Checkpoint 01

**Project:** P2P 60-24 OneClick Evo Positiv  
**Branch:** main  
**Date:** 2026-10-01  
**Mode:** CONTROL → BUILD → EVIDENCE

## INSPECT

Current HEAD after the controlled change:

`94fb477b4340f12ac320867409502a093f0c3240`

Repository inspection confirmed:

- native Windows executable workflow exists;
- packaged Windows artifact contains `P2P60-24Node.exe`, `start-node-a.cmd`, `start-node-b.cmd`, `README.txt`;
- runtime still binds the requested listener through `socket.bind((host, port))`;
- `start-node-b.cmd` previously started `0.0.0.0:39001` without observable preflight;
- no existing repository check verified the Windows listener state or displayed the usable LAN IPv4 address before the Android test.

## Finding

### GAP-076-01 — Windows LAN evidence preflight gap

This is a **test/evidence-layer gap**, not a P2P protocol GAP.

Before SES-076, a failed Android connection could leave these states ambiguous:

```
process started?
listener exists?
port already occupied?
usable LAN IPv4?
firewall profile active?
```

The launcher did not expose those states in a deterministic way.

## Minimal change

Updated:

`windows/start-node-b.cmd`

The launcher now:

1. verifies that `P2P60-24Node.exe` exists beside the launcher;
2. checks that TCP `39001` is not already listening;
3. starts Node B on `0.0.0.0:39001`;
4. waits up to 5 seconds for TCP `39001` to reach LISTENING;
5. prints the listening endpoint and owning process;
6. prints non-loopback IPv4 addresses;
7. prints Windows Firewall profile state;
8. reports `LISTENER READY` before the physical Android test proceeds.

Updated:

`windows/README.txt`

to describe the new evidence boundary.

No changes were made to:

- `src/p2p/node.py`;
- HELLO/WELCOME/AUTH;
- Ed25519 identity;
- NodeID;
- transport;
- `MAX_FRAME_SIZE = 64 KiB`;
- ontology or trust architecture.

## Evidence

Change commits:

- `8e604931e2e2036ba23e05fbd3281de2d1d0135a` — native listener preflight
- `26bab0ef7b9a4b6ef715ea0f93991a4180fe78b4` — documentation
- `94fb477b4340f12ac320867409502a093f0c3240` — documentation numbering correction

The repository status check for the latest commit currently reports no combined status entries. This checkpoint therefore does **not** claim CI GREEN for the new change.

## Current state

```
Windows package
      ↓
launcher preflight
      ↓
TCP 39001 LISTENING
      ↓
LAN IPv4 visible
      ↓
Android → Windows physical test
      ↓
TCP reachability
      ↓
HELLO/WELCOME/AUTH
      ↓
application message
```

The next physical observation must determine where the chain stops.

## Classification

**No protocol RED opened.**

The previous WSL/portproxy result remains non-protocol evidence.

SES-076 remains **OPEN / awaiting physical Windows LAN evidence**.

## Rule

**TCP failure is not a protocol failure.**

Only a reproducible failure after the TCP connection reaches the native Windows runtime can open a protocol/runtime GAP.
