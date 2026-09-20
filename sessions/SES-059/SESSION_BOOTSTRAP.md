# SES-059 — SESSION BOOTSTRAP

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repo:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Status:** OPEN  
**Tryb:** AUTONOMICZNY

## Cel

Przejść od technicznie udowodnionego Node A ↔ Node B do minimalnie używalnego programu dla realnego użytkownika.

## Stan wejściowy

SES-058 udowodniła packaged executable przez loopback i non-loopback IPv4.

Proof:
- commit: `28bae3b9806d78b653838ac939e5d5d1adb2a8ff`
- run: `35518765708`
- artifact: `P2P60-24Node-linux-x86_64`

## Zasada

Nie zakładamy GAP-u. Najpierw inspekcja istniejącej ścieżki:

`download → run → configure → connect → handshake → identity → message → result`

Jeżeli działa — brak sztucznego RED. Jeżeli nie działa — minimalny rzeczywisty fix.

## Zakres kontroli

1. pobranie executable,
2. uruchomienie Node B,
3. uruchomienie Node A,
4. adres/IP i port,
5. komunikaty błędów,
6. scenariusz bez znajomości kodu,
7. zachowanie istniejących testów i executable proof.

## Zakazy

Bez realnego GAP-u nie rozpoczynać GUI, discovery, NAT traversal, relay, centralnego serwera, System Builder integration ani dużej refaktoryzacji.

## Workflow

`INSPECT → UNDERSTAND → IDENTIFY GAP → RED only if real GAP → MINIMAL FIX → GREEN → VERIFY → DOCUMENT → COMMIT → CONTINUE`

Repozytorium jest Source of Truth.