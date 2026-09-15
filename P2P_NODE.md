# Standalone P2P node

Minimal two-process P2P communication proof for P2P 60-24 OneClick Evo.

## Requirements

- Python 3.x
- No external packages
- Two terminals or two machines that can reach the listening address

## Start node B

```bash
python p2p_node.py --listen 0.0.0.0:9000 --node-id B
```

## Start node A

On the same machine:

```bash
python p2p_node.py --connect 127.0.0.1:9000 --node-id A --message ping-from-A
```

For another machine, replace `127.0.0.1` with the reachable IP address of node B.

Expected result on node A:

```text
pong-from-B
```

Node B also prints the received message.

## What this proves

- two independently started processes;
- TCP connection A → B;
- message A → B;
- response B → A.

## Scope

This is a minimal experimental communication primitive. It does **not** claim to provide discovery, NAT traversal, authentication, encryption, persistence, Internet production readiness, or a final P2P transport architecture.

Automated proof:

`sessions/SES-044/test_downloadable_two_nodes.py`

CI workflow:

`.github/workflows/ses-044-p2p-download.yml`
