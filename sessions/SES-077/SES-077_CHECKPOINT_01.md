# SES-077 — Android UX GAP

**Status:** CLOSED
**Project:** P2P 60-24 OneClick Evo Positiv
**Scope:** Android live-demo entrypoint

## GAP-077-01 — default connection target mismatch

### Observed
The documented shortest Android ↔ native Windows path uses USB/ADB reverse and therefore requires Android Host = `127.0.0.1`, Port = `39001`. The Android application previously prefilled Host = `192.168.1.20`.

### Difference
A fresh installation could be opened and used with the wrong host for the project's current simplest live demo. This was a user-facing configuration mismatch, not a protocol failure.

### Minimal repair
Changed only the Android default Host to `127.0.0.1`. LAN use remains supported; the README now explicitly tells the user to replace Host with the real Node B LAN IPv4 for a physical LAN test.

### Evidence boundary
This change does not claim physical LAN connectivity. It aligns the Android UI with the already accepted USB/ADB integration path.

### Result
GAP-077-01 repaired. Android build/CI is the required verification gate for the change.
