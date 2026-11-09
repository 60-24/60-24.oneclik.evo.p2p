# Example: Minikernel v0.1 (Go, standard library only)

Przykład, nie wersja produkcyjna. Pokazuje najmniejszą działającą ideę z
koncepcji P2P 60-24: dwa węzły nawiązują handshake przez UDP i wymieniają
jedną podpisaną wiadomość (ed25519, ID z klucza publicznego).

Celowo pomija to, co jest w głównym projekcie: TCP/UDP według specyfikacji
protokołu, szyfrowanie, ochronę przed powtórzeniem, trwały stan i Buildera.
Służy jako punkt odniesienia i jako wariant do porównania.

## Uruchomienie

```bash
cd examples/minikernel
go test -race ./...
go run . -listen 127.0.0.1:6024
go run . -listen 127.0.0.1:6025 -peer 127.0.0.1:6024 -msg "hello"
```
