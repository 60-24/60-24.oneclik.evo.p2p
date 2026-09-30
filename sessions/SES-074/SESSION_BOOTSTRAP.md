# SES-074 — SESSION BOOTSTRAP

**Projekt:** P2P 60-24 OneClick Evo Positiv
**Data otwarcia:** 2026-09-30
**Tryb:** autonomiczny / evidence-first
**Źródło prawdy:** repozytorium GitHub
**Cel:** pierwszy rzeczywisty test Android ↔ Linux

## Stan otwarcia
HEAD `main`: `98b1ff75536db777b4bf2072ef6b1283baff8b90`

Status: **READY FOR REAL DEVICE TEST**

Dokument testu: `docs/ANDROID_LINUX_REAL_TEST.md`

## Zasada
Nie rozwijamy protokołu przed wykonaniem testu fizycznego.

**TEST → EVIDENCE → CLASSIFY → GAP? → RED → CODE → GREEN**

Jeżeli test przejdzie: **DEVICE TEST GREEN → EVIDENCE → STONE**.

## Artefakty
Linux: workflow `36385955091`, commit `33ae5c47f31a03992ee010a5f4e2625c482ac062`, artifact `P2P60-24Node-linux-x86_64`.

Android: workflow `36544449740`, commit `54b08d5dab6424b84c719402b34aca6d6d792f81`, artifact `P2P60-24Node-android-arm64-debug`, SHA-256 `fd683c1410ca86cae98190b3867823a5bf8b68a93fb15e0d7f33148adf04a04d`.

## Test
Linux Node B: `./P2P60-24Node --listen 0.0.0.0:39001 --node-id B`

Android Node A: label `A`, Host = LAN IP Linux, Port `39001`, Message = `hello-from-Android`, następnie `Connect`.

Oczekiwany Android: `OK response=pong-from-B`.
Oczekiwany Linux: `node B received from A: hello-from-Android`.

Zapisać także Android NodeID, Linux NodeID, model telefonu, wersję Androida, ABI, LAN IP oraz screenshot/log.

## GREEN
`DEVICE TEST GREEN` wyłącznie po fizycznym sukcesie i zapisaniu evidence.

**CI GREEN ≠ DEVICE TEST GREEN.**

## Failure protocol
Nie tworzyć GAP-u z samego faktu błędu. Zebrać dokładny błąd Android, output Linux, model/wersję/ABI, IP/port, reachability, firewall i etap przepływu.

Klasyfikacja: **network / installation / Android runtime / protocol / evidence**.

GAP wymaga: **CURRENT STATE + EXPECTED STATE + REPRODUCIBLE DIFFERENCE**.

## Poza zakresem
Android ↔ Android, Internet/NAT traversal, automatic discovery, production signing/distribution i redesign GUI.

## Zasada operacyjna
**Maksymalizacja przez minimalizację.** Najpierw dowód działania istniejącego systemu. Dopiero potem następna decyzja architektoniczna lub implementacyjna.
