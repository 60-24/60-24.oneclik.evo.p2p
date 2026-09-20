# 60-24.oneclik.evo.p2p

## Minimal Node A ↔ Node B

The repository contains a small standalone P2P executable: `P2P60-24Node`.

### Start Node B (listener)

```bash
./P2P60-24Node --listen 127.0.0.1:39001 --node-id B
```

### Connect Node A

In a second terminal:

```bash
./P2P60-24Node --connect 127.0.0.1:39001 --node-id A --message hello-from-A
```

Expected response:

```
pong-from-B
```

Node B prints the received peer identity and application message:

```
node B received from A: hello-from-A
```

### LAN use

The CLI accepts normal IPv4 host:port addresses. A listener can bind to an interface address or `0.0.0.0`, and Node A can connect to Node B using Node B's LAN address:

```bash
./P2P60-24Node --listen 0.0.0.0:39001 --node-id B
./P2P60-24Node --connect 192.168.1.20:39001 --node-id A --message hello-from-A
```

The current automated executable proof verifies the two-process flow on localhost. LAN operation is supported by the address interface but is not yet a separate CI execution proof.

### Current boundary

This is a minimal runtime proof, not yet a production-ready P2P product. It does not provide encryption, authentication, discovery, NAT traversal, GUI, installation, or automatic peer discovery.

## Verified executable proof

SES-057 verified a packaged Linux executable with two independent processes, HELLO/WELCOME, bidirectional peer identity, application message delivery, response, and artifact publication in GitHub Actions.
