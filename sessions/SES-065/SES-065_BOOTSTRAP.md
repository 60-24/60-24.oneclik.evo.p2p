# SES-065 — SESSION BOOTSTRAP

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Data:** 2026-09-24  
**Status:** OPEN  
**Tryb:** AUTONOMICZNY

## Cel

Sprawdzić i — tylko jeśli potwierdzony — usunąć jeden konkretny brak po SES-064:

> Czy kryptograficzny NodeID pozostaje taki sam po restarcie tego samego Node'a?

## Granica

SES-064 zapewnił proof-of-possession dla bieżącej sesji. Klucz Ed25519 jest jednak generowany przy każdym starcie procesu, więc obecny NodeID zmienia się po restarcie.

Nie rozszerzamy teraz zakresu na:
- PKI;
- Web-of-Trust;
- certyfikaty;
- E2E encryption;
- discovery/mesh;
- authorization;
- System Builder.

## Plan kontrolowany

1. INSPECT — ustalić minimalny mechanizm trwałej tożsamości.
2. RED — test restartu z tym samym magazynem klucza.
3. IMPLEMENT — lokalny trwały klucz Ed25519; brak automatycznej podmiany istniejącego klucza.
4. GREEN — test + pełna regresja + executable smoke.
5. VERIFY / DOCUMENT — README + checkpoint/closeout.
6. STONE tylko po realnym GREEN.

## Kryterium zamknięcia

Ten sam lokalny identity store → ten sam public key → ten sam NodeID po restarcie.

Uszkodzony identity store ma powodować błąd, a nie ciche wygenerowanie nowej tożsamości.

**Limit sesji:** jeden GAP, jedna zmiana architektoniczna, jeden pełny cykl GREEN.
