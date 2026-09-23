# SES-063 — CHECKPOINT 01

**Projekt:** P2P 60-24 OneClick Evo Positiv  
**Repozytorium:** `60-24/60-24.oneclik.evo.p2p`  
**Branch:** `main`  
**Data weryfikacji:** 2026-09-23  
**Status:** BLOCKED — nie zamykać

## Cel

Zweryfikować rzeczywistą, niezależną ścieżkę użytkownika:

`download artifact → extract → Node B → Node A → TCP → HELLO/WELCOME → peer identity → message → response`

Wymagany observable proof:

- Node A: `pong-from-B`;
- Node B: `node B received from A: hello-from-A`.

## INSPECT

Sprawdzono:

- aktualny HEAD: `d292d49d181f6661135bd6eb386f83adf7e94309`;
- ostatni commit: `docs(SES-063): document independent artifact download and run path`;
- `README.md` — zawiera instrukcję pobrania artefaktu, ekstrakcji ZIP i tarballa oraz uruchomienia Node A/B;
- workflow `.github/workflows/build-p2p-linux.yml`;
- istniejący łańcuch runtime: `demo/p2p_node_cli.py → src/p2p/node.py → P2P60-24Node`;
- wcześniejsze dowody SES-057–061;
- `sessions/SES-063/` — przed tym checkpointem nie zawierała sprawdzalnego checkpointu ani closeoutu.

README i workflow są spójne co do nazwy artefaktu:

`P2P60-24Node-linux-x86_64`

Workflow buduje artefakt z bieżącego checkoutu, uruchamia regresje P2P, buduje one-file executable PyInstaller i wykonuje smoke test dwóch procesów.

## Częściowe evidence

Istnieje zakończony sukcesem run właściwego workflow:

- workflow: `P2P Linux executable`;
- run: [35837007992](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/runs/35837007992);
- status: `completed`;
- conclusion: `success`;
- workflow file: `.github/workflows/build-p2p-linux.yml`;
- deklarowany artefakt: `P2P60-24Node-linux-x86_64`.

Istnieją także wcześniejsze packaged smoke proofs, między innymi w evidence SES-057, SES-058, SES-060 i SES-061. Są to dowody historyczne i nie zastępują weryfikacji aktualnego artefaktu z aktualnego runu dla SES-063.

## Weryfikacja niezależnego użytkownika

### Potwierdzone z repozytorium

- instrukcja download → extract jest obecna;
- artefakt jest publikowany przez właściwy workflow;
- workflow zawiera packaged two-node smoke test;
- workflow sprawdza odpowiedź `pong-from-B`;
- workflow sprawdza po stronie B identyfikację i wiadomość `node B received from A` oraz `hello-from-A`.

### Niepotwierdzone w tej sesji

Nie uzyskano jeszcze niezależnego, reprodukowalnego dowodu obejmującego jednocześnie:

1. pobranie aktualnego artefaktu `P2P60-24Node-linux-x86_64` z runu `35837007992`;
2. ekstrakcję ZIP i zawartego tarballa w czystym katalogu poza checkoutem;
3. uruchomienie dwóch niezależnych procesów wyłącznie z rozpakowanego executable;
4. zapis rzeczywistego stdout Node A i Node B z wymaganymi liniami;
5. jednoznaczne powiązanie artefaktu z SHA commita runu.

Sam fakt istnienia artefaktu, instrukcji albo zielonego workflow nie jest wystarczającym dowodem niezależnej ścieżki użytkownika. Nie tworzę sztucznego PASS.

## GAP / blocker

**GAP-063-01 — brak dostępnego w tej sesji dowodu pobrania i uruchomienia aktualnego artefaktu poza checkoutem.**

To jest luka evidence, nie potwierdzony błąd implementacji P2P. Nie dodano testu RED ani zmian runtime, ponieważ nie stwierdzono realnego GAP-u funkcjonalnego i nie wolno tworzyć sztucznego RED.

Do zamknięcia brakuje:

- SHA commita przypisanego do runu `35837007992`;
- potwierdzenia nazwy/ID aktualnego artefaktu z tego runu;
- rzeczywistego logu z czystego katalogu po downloadzie i ekstrakcji;
- wyników Node A i Node B zawierających wymagane wartości.

## Kryterium decyzji

SES-063 **nie jest CLOSED**.

Nie wystawiono `SES-063_CLOSEOUT.md`, ponieważ nie są obecne wszystkie wymagane dowody. Status pozostaje:

**BLOCKED / OPEN — oczekuje na niezależną weryfikację aktualnego artefaktu.**

## Następny krok

W środowisku z możliwością pobrania artefaktów GitHub Actions wykonać dokładnie:

```bash
mkdir -p /tmp/ses-063-clean
cd /tmp/ses-063-clean
unzip P2P60-24Node-linux-x86_64.zip
mkdir extracted
tar -xzf P2P60-24Node-linux-x86_64/P2P60-24Node-linux-x86_64.tar.gz -C extracted
cd extracted
chmod +x P2P60-24Node
./P2P60-24Node --listen 127.0.0.1:39001 --node-id B >server.log 2>&1 &
server_pid=$!
sleep 1
./P2P60-24Node --connect 127.0.0.1:39001 --node-id A --message hello-from-A | tee client.log
wait "$server_pid"
cat client.log
cat server.log
```

Następnie zachować w evidence: SHA runu, run URL, artifact name/ID, SHA-256 pobranego pliku oraz pełne wyniki obu procesów. Dopiero po tym można utworzyć closeout ze statusem `GREEN / CLOSED / STONE`.
