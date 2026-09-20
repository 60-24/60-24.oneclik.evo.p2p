# Downloadable P2P Node

Current downloadable two-node runtime for P2P 60-24 OneClick Evo.

## Build

GitHub Actions builds a self-contained Linux executable from the current runtime:

```text
demo/p2p_node_cli.py → src/p2p/node.py → P2P60-24Node
```

The workflow is:

`.github/workflows/build-p2p-linux.yml`

## Run

Download the GitHub Actions artifact `P2P60-24Node-linux-x86_64` and extract it.

Start node B:

```bash
./P2P60-24Node --listen 0.0.0.0:9000 --node-id B
```

Start node A:

```bash
./P2P60-24Node --connect <NODE-B-IP>:9000 --node-id A --message hello-from-A
```

Expected response on node A:

```text
pong-from-B
```

Node B records the peer identity and received application message.

## Current proof boundary

- two independent executable processes;
- current `src/p2p` runtime;
- HELLO/WELCOME handshake;
- bidirectional node identity;
- application message A → B;
- response B → A;
- one-file PyInstaller executable;
- GitHub Actions artifact;
- malformed peer handshake is handled as a user-facing CLI error on both sides.

## Historical SES-044

`sessions/SES-044/` is retained as historical evidence. Its test targets the former standalone `p2p_node.py` implementation and is no longer part of the current product CI proof.

The former root-level `p2p_node.py` runtime is retired to avoid two competing P2P runtimes.

## Troubleshooting

The CLI reports user-facing errors instead of Python tracebacks for common connection problems.

- **Invalid address:** use `IP:PORT`, for example `192.168.1.20:9000`.
- **Connection refused:** check that Node B is running and listening on the same IP and port.
- **Connection timed out:** check the Node B address, port, network reachability, and firewall rules.
- **Listening error:** check that the selected port is available.
- **Malformed handshake:** the peer must complete the HELLO/WELCOME handshake; invalid handshake input is rejected with an `ERROR:` message and exit code `1`.
