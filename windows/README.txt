P2P 60-24 OneClick Evo Positiv - native Windows test

1. Extract this package to a normal local folder, for example:
   C:\P2P60-24

2. On Windows Node B:
   - double-click start-node-b.cmd
   - the launcher checks that TCP 39001 is free, starts the native node, verifies that TCP 39001 is LISTENING, and prints the available non-loopback IPv4 addresses
   - note the displayed LAN IPv4 address
   - allow Windows Firewall access if Windows asks
   - keep the launcher/node window open

3. The launcher also prints the Windows Firewall profile state. This is diagnostic evidence only; it does not change firewall rules.

4. If the launcher reports `LISTENER READY`, the Windows application layer has reached the TCP LISTEN state. This does not yet prove that Android can reach the host; the Android → Windows test is the next evidence step.

5. On Windows Node A:
   - copy this package to the second Windows computer
   - double-click start-node-a.cmd
   - enter Node B's LAN IPv4 address

Expected Node A:
   pong-from-B

Expected Node B:
   node B received from A: hello-from-A

Important:
- Do not double-click P2P60-24Node.exe as the test itself. The executable requires command-line arguments.
- The executable is a console program, not a GUI application.
- If Windows SmartScreen or Defender blocks a downloaded artifact, use the repository's verified GitHub Actions artifact and record the exact Windows message before changing project code.
- Android -> Windows is a separate physical test. This package only removes the Windows execution/CLI barrier.

Self-test on one Windows PC:
Open PowerShell in the extracted folder and run:
  .\P2P60-24Node.exe --listen 127.0.0.1:39001 --node-id B

In a second PowerShell:
  .\P2P60-24Node.exe --connect 127.0.0.1:39001 --node-id A --message hello-from-A

Expected:
  pong-from-B

Node B should print:
  node B received from A: hello-from-A


### Android <-> native Windows bridge test (no LAN / no firewall dependency)

When the physical Android -> Windows LAN path is unavailable, use the ADB reverse bridge. This is an integration test, not a replacement for the final physical LAN proof.

1. Put P2P60-24Node.exe and start-android-adb-bridge.cmd in the same folder.
2. Connect the Android device by USB with USB debugging enabled.
3. Ensure Android platform-tools (adb) is available in PATH.
4. Run start-android-adb-bridge.cmd on Windows.
5. In the Android app enter Host 127.0.0.1, Port 39001, Node label A, Message hello-from-Android.
6. Press Connect.

The bridge is adb reverse tcp:39001 tcp:39001: Android loopback traffic is forwarded through ADB to the Windows loopback listener. No Wi-Fi routing, Windows LAN firewall rule, or port-forwarding configuration is involved.

Expected: Android returns OK response=pong-from-B and Windows Node B prints node B received from A: hello-from-Android.

Interpretation:
- PASS proves the Android adapter and native Windows runtime can complete the existing P2P protocol together.
- FAIL before Node B receives a TCP connection is an Android/ADB/runtime-path problem, not evidence of a protocol GAP.
- FAIL after the TCP connection reaches Node B becomes a protocol/runtime investigation.
- This test does not close the separate physical LAN evidence requirement.
