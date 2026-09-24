# 60-24.oneclik.evo.p2p

Minimal, standalone P2P runtime for direct Node A ↔ Node B communication.

## Download and run

The repository publishes a self-contained Linux x86_64 executable named `P2P60-24Node` as the GitHub Actions artifact `P2P60-24Node-linux-x86_64`.

### 0. Download and extract the artifact

1. Open the [P2P Linux executable workflow](https://github.com/60-24/60-24.oneclik.evo.p2p/actions/workflows/build-p2p-linux.yml).
2. Open a successful run on `main`.
3. In the run's **Artifacts** section, download `P2P60-24Node-linux-x86_64`.
4. Extract the downloaded GitHub artifact archive, then extract the included tarball:

```bash
unzip P2P60-24Node-linux-x86_64.zip
mkdir P2P60-24Node-linux-x86_64
 tar -xzf P2P60-24Node-linux-x86_64/P2P60-24Node-linux-x86_64.tar.gz -C P2P60-24Node-linux-x86_64
cd P2P60-24Node-linux-x86_64
chmod +x P2P60-24Node
```

The executable is self-contained: after extraction it can be run from this directory without a checkout, Python installation, or repository files. It targets Linux x86_64. GitHub Actions artifacts are retained according to the repository's Actions retention policy; for a permanent public download, a release asset would be a separate distribution decision and is not required for this CI proof.

### 1. Start Node B

In the first terminal:

```bash
./P2P60-24Node --listen 127.0.0.1:39001 --node-id B
```

The program stays in listening mode, ready for one connection.

### 2. Connect Node A

In a second terminal:

```bash
./P2P60-24Node --connect 127.0.0.1:39001 --node-id A --message "hello-from-A"
```

Expected output from Node A:

```text
pong-from-B
```

Expected output from Node B:

```text
node B received from A: hello-from-A
```

The two commands use the same freshly downloaded executable. The executable performs TCP connection, HELLO/WELCOME handshake, peer identification, application message delivery, and the response.

### 3. Use on a local network (LAN)

The CLI accepts IPv4 `IP:PORT` addresses.

On the computer running Node B:

```bash
./P2P60-24Node --listen 0.0.0.0:39001 --node-id B
```

On the computer running Node A, use the real LAN address of Node B:

```bash
./P2P60-24Node --connect 192.168.1.20:39001 --node-id A --message "hello-from-LAN"
```

The LAN address path is supported by the runtime. SES-058 also verified a non-loopback IPv4 executable path in CI.

## CLI help

Use the built-in help without inspecting the source code:

```bash
./P2P60-24Node --help
```

Available modes and arguments:

- `--listen IP:PORT` — listen for one incoming peer connection.
- `--connect IP:PORT` — connect to Node B.
- `--node-id ID` — identifier sent during the handshake.
- `--message TEXT` — application message; required with `--connect`.

## Troubleshooting

The CLI reports expected connection, address, and handshake errors as short messages and exits with code `1`; it does not expose a Python traceback for these cases.

### Invalid address

Example:

```text
ERROR: invalid address: '192.168.1.10'. Use the format IP:PORT (for example 192.168.1.10:9000).
```

Use the form:

```text
192.168.1.10:9000
```

### Connection refused

```text
ERROR: Connection refused. Make sure Node B is listening at this address and port.
```

Check that Node B is running and that the IP address and port in `--connect` match the listener.

### Connection timeout

```text
ERROR: Connection timed out. Check that Node B is running and the address/port are correct.
```

Check the Node B address, port, network path, and firewall.

### Cannot start listening

```text
ERROR: Cannot start listening: ... Check that the port is available.
```

Check whether another process already uses the port. Prefer an available high port such as `39001` or `9000`.

### Authenticated peer identity

Since SES-064, the transport handshake binds the cryptographic `NodeID` to an Ed25519 public key.

The wire flow is:

```
HELLO  (NodeID + public key + client challenge)
WELCOME (NodeID + public key + server challenge + signature)
AUTH   (signature proving possession of the client private key)
```

`NodeID = SHA-256(public key)`. A peer is recorded in `last_peer_id` only after proof-of-possession succeeds. The CLI `--node-id` value remains a local display label; it is not accepted as a cryptographic identity.

This is authentication of the presented key, not a global trust or authorization system.

### Malformed peer handshake

If a peer sends an invalid HELLO or WELCOME during the handshake, the CLI rejects it with an actionable error and exits with code `1`, without exposing a Python traceback.

## Current boundary

This is a minimal runtime proof, not yet a production-ready P2P product. It does not provide:

- end-to-end encryption,
- advanced authentication,
- automatic peer discovery,
- NAT traversal,
- GUI,
- automatic installation,
- central relay infrastructure.

The current phase proves the direct Node A ↔ Node B runtime and its executable delivery path. It does not claim production security, Internet-wide connectivity, or automatic discovery.

## Verified executable proof

SES-057 verified the packaged Linux executable with two independent processes, HELLO/WELCOME, bidirectional peer identity, application message delivery, response, and artifact publication.

SES-058 extended the executable proof with a non-loopback IPv4 path and automated verification.

SES-059 added actionable CLI error handling, regression tests, and user troubleshooting documentation.

SES-060 extended the CLI error boundary to malformed peer handshakes on both listener and connector paths.

SES-063 confirmed that the current packaged executable, artifact workflow, and user instructions cover the independent-user path from download through the first P2P exchange. The exact CI proof is recorded in `sessions/SES-063/SES-063_CHECKPOINT_01.md`.

The current GitHub Actions build publishes the artifact:

`P2P60-24Node-linux-x86_64`
