# SES-071 — SESSION BOOTSTRAP

**Projekt:** P2P 60-24 OneClick Evo Positiv
**Repo:** 60-24/60-24.oneclik.evo.p2p
**Branch:** main
**Poprzednia sesja:** SES-070
**Stan wejściowy:** GREEN / CLOSED / STONE

## START
Nie zakładaj GAP-u.

Wykonaj:
**INSPECT aktualnego repo → architektura → runtime → testy → CI → Evidence → artifact → dokumentacja → jeden REAL GAP albo STOP.**

## Zasada
GAP musi posiadać: konkretny obecny stan; oczekiwane zachowanie; reprodukowalną różnicę; jednoznaczny RED test lub dowód; minimalny zakres naprawy.

Brak GAP-u = brak implementacji.

## CONTROL
Kontroluj: Node A ↔ Node B; framing i parser; handshake; identity/authentication; timeout/disconnect; malformed input; resource limits; persistent identity; test contracts; CI; p2p/evidence; artifact + attestation; spójność code ↔ test ↔ evidence ↔ docs.

## BUILD
Tylko po potwierdzeniu realnego GAP-u:
**RED → minimal CODE → REVIEW → CI → EVIDENCE → STONE**

Jeden GAP naraz.

**Repo = Source of Truth.**
**Maksymalizacja przez minimalizację.**
**System sugeruje — człowiek decyduje.**