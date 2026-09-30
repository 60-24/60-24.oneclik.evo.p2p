# Linux ↔ Android — Real Device Test

**Status:** READY FOR REAL DEVICE TEST  
**Scope:** first physical Android ↔ Linux interoperability test  
**Principle:** test the existing P2P runtime; do not introduce new protocol behavior.

## 1. Evidence baseline

### Linux

Reference workflow:

- Workflow: **P2P Linux executable**
- Run: `36385955091`
- Commit: `33ae5c47f31a03992ee010a5f4e2625c482ac062`
- Status: **Success**
- Artifact: `P2P60-24Node-linux-x86_64`

### Android

Reference workflow:

- Workflow: **P2P Android APK**
- Run: `36544449740`
- Commit: `54b08d5dab6424b84c719402b34aca6d6d792f81`
- Status: **Success**
- Artifact: `P2P60-24Node-android-arm64-debug`
- Artifact SHA-256: `fd683c1410ca86cae98190b3867823a5bf8b68a93fb15e0d7f33148adf04a04d`

**Important:** CI GREEN proves that the APK was built, attested and published. It does **not** prove execution on a physical Android device.

## 2. Network topology

Use one local network:

```
Android phone  ── Wi-Fi/LAN ──>  Linux computer
Node A                       Node B
```

The phone must be able to reach the Linux computer on the selected TCP port.

Record before the test:

- Android device model: __________________
- Android version: __________________
- Linux host LAN IP: __________________
- TCP port: `39001`

## 3. Download and install Android APK

1. Open the successful **P2P Android APK** workflow run.
2. Download artifact `P2P60-24Node-android-arm64-debug`.
3. Install the APK on an **arm64-v8a** Android device.
4. Start **P2P 60-24 Android Node**.

The app provides:

- `Node label`
- `Host`
- `Port`
- `Message`
- `Connect`
- `Listen once`

## 4. Start Linux Node B

On the Linux computer, use the already verified executable.

Replace `/path/to/P2P60-24Node` with the extracted executable path:

```bash
cd /path/to/P2P60-24Node-linux-x86_64
./P2P60-24Node --listen 0.0.0.0:39001 --node-id B
```

The Linux node remains listening for one connection.

## 5. Connect Android Node A

On the Android phone enter:

- **Node label:** `A`
- **Host:** LAN IP address of the Linux computer, for example `192.168.1.20`
- **Port:** `39001`
- **Message:** `hello-from-Android`

Press **Connect**.

The Android adapter calls the existing `p2p.node.P2PNode`; it does not implement a second P2P protocol.

## 6. Expected result

Android should display a result beginning with:

```text
OK response=pong-from-B
```

and should also report:

```text
local_node_id=<Android NodeID>
peer_node_id=<Linux NodeID>
```

Linux should report the received application message in the established CLI form:

```text
node B received from A: hello-from-Android
```

The successful path therefore demonstrates:

```
Android
  ↓ TCP
Linux listener
  ↓
HELLO / WELCOME / AUTH
  ↓
authenticated peer identity
  ↓
application message
  ↓
response
  ↓
Android
```

## 7. Evidence record

After the test, record:

| Item | Value |
|---|---|
| Android artifact | `P2P60-24Node-android-arm64-debug` |
| Android SHA-256 | `fd683c1410ca86cae98190b3867823a5bf8b68a93fb15e0d7f33148adf04a04d` |
| Android workflow run | `36544449740` |
| Linux workflow run | `36385955091` |
| Linux commit | `33ae5c47f31a03992ee010a5f4e2625c482ac062` |
| Android device | __________________ |
| Android version | __________________ |
| Linux LAN IP | __________________ |
| TCP port | `39001` |
| Message | `hello-from-Android` |
| Android NodeID | __________________ |
| Linux NodeID | __________________ |
| Response | __________________ |
| Linux received message | __________________ |
| Screenshot/log evidence | __________________ |

## 8. Result classification

### DEVICE TEST GREEN

Only use **DEVICE TEST GREEN** when the physical phone produces the expected result and the evidence above is recorded.

### If the test fails

Do not modify the protocol immediately.

First record:

1. exact Android error;
2. Linux output;
3. phone Android version/device architecture;
4. Linux IP and port;
5. whether the phone can reach the Linux host;
6. whether the Linux firewall allows TCP `39001`.

Then classify the failure as:

```
network / installation / Android runtime / protocol / evidence
```

A failure is not automatically a new GAP. A GAP requires a reproducible difference between current and expected behavior.

## 9. Deliberate scope boundary

This test does **not** yet cover:

- Android ↔ Android;
- Internet/NAT traversal;
- automatic discovery;
- production APK signing/distribution;
- GUI redesign.

Those remain out of scope until the first physical Linux ↔ Android exchange is proven.
