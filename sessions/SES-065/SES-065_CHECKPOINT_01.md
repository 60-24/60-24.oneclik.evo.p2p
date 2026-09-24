# SES-065 — CHECKPOINT 01

**Status:** GREEN
**Date:** 2026-09-24

## GAP
Po SES-064 Ed25519 key był generowany przy każdym starcie procesu. NodeID nie był trwały między restartami.

## Wykonanie
- lokalny Ed25519 private key jest ładowany z identity store;
- brakujący store jest tworzony;
- istniejący uszkodzony store jest odrzucany;
- NodeID nadal wynika wyłącznie z public key;
- dodano test restartu i test uszkodzonego store;
- README i CI zostały zaktualizowane.

## Dowód
P2P Linux executable workflow: **35942270767 — completed / success**.
Workflow zawiera regresję SES-065, budowę executable oraz packaged two-node smoke.

## Kontrola zakresu
Nie dodano PKI, Web-of-Trust, E2E, discovery ani authorization.

**Decyzja:** GAP SES-065 usunięty. Przejście do VERIFY/CLOSEOUT.
