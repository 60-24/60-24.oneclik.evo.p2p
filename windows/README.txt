P2P 60-24 OneClick Evo Positiv - native Windows test

1. Extract this package to a normal local folder, for example:
   C:\P2P60-24

2. On Windows Node B:
   - double-click start-node-b.cmd
   - allow Windows Firewall access if Windows asks
   - keep the window open

3. Find Node B's LAN IPv4 address:
   ipconfig

4. On Windows Node A:
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
