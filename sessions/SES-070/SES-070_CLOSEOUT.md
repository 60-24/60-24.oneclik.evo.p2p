# SES-070 — CONTROL AUDIT / STONE

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repo:** 60-24/60-24.oneclik.evo.p2p  
**Branch:** main  
**Data:** 2026-09-28  
**Status:** GREEN / CLOSED / STONE

## Cel
Po SES-069 wykonano autonomiczny INSPECT bez zakładania z góry kolejnego GAP-u.

Zakres: runtime Node A ↔ Node B; framing; EOF/truncated; oversized frames; coalesced frames; handshake; cryptographic identity; proof-of-possession; persistent identity; timeout/disconnect; malformed input; CI; Evidence; artifact/attestation; test ↔ code ↔ documentation; wcześniejszy External Review / Issue #7.

## Wynik
**Nie potwierdzono nowego REAL GAP-u wymagającego RED → CODE.**

Nie wykonano sztucznej implementacji.

### Potwierdzone zabezpieczenia
1. NodeID jest deterministycznie związany z Ed25519 public key.
2. HELLO odrzuca niespójne NodeID / public key.
3. WELCOME jest weryfikowany kryptograficznie względem client challenge.
4. AUTH dowodzi posiadania klucza klienta względem świeżego server challenge.
5. last_peer_id jest ustawiany dopiero po poprawnej weryfikacji AUTH.
6. EOF przed delimiterem kończy się incomplete frame.
7. Frame limit 64 KiB pozostaje aktywny.
8. Coalesced TCP frames są zachowywane przez per-connection buffer.
9. Timeout handshake/listenera istnieje.
10. Persistent identity jest odtwarzana z lokalnego klucza, a uszkodzony klucz jest odrzucany.
11. Main posiada działający p2p/evidence.
12. Finalny packaged two-node smoke test oraz attestation przechodzą.

## External Review
Issue #7 wskazywał pierwotnie na Identity & Transport Binding Gap.
Ten GAP został już wcześniej rzeczywiście potwierdzony i zamknięty w SES-064/065. Aktualny kod nie pozostaje w stanie opisanym przez zewnętrzną obserwację.

## Ważna obserwacja
Brak nowego GAP-u nie oznacza, że runtime jest produkcyjnie kompletny.

Oznacza wyłącznie:
> w obecnym, świadomie ograniczonym zakresie Node A ↔ Node B nie znaleziono nowej, jednoznacznie reprodukowalnej luki wymagającej natychmiastowej zmiany fundamentu.

Nie wdrażano reconnect, multi-peer concurrency, discovery, E2E encryption, trust, mesh ani GUI. Są to przyszłe kierunki, nie potwierdzone GAP-y obecnej sesji.

## Decyzja
**STOP IMPLEMENTATION.**

Repo pozostaje w zweryfikowanym stanie.

Następna sesja powinna ponownie wykonać INSPECT albo wykorzystać nowy, konkretny materiał dowodowy.

**SES-070 = GREEN / CLOSED / STONE.**