@echo off
setlocal
title P2P 60-24 - Node B
echo ==========================================
echo P2P 60-24 OneClick Evo Positiv - Node B
echo ==========================================
echo.
echo Preparing native Windows LAN listener on TCP 39001...
echo.

if not exist "%~dp0P2P60-24Node.exe" (
  echo ERROR: P2P60-24Node.exe was not found next to this launcher.
  echo Extract the complete Windows artifact and run this file from that folder.
  pause
  exit /b 1
)

powershell -NoProfile -Command "$c=Get-NetTCPConnection -LocalPort 39001 -State Listen -ErrorAction SilentlyContinue; if($c){Write-Host 'ERROR: TCP 39001 is already listening.'; $c ^| Format-Table -AutoSize; exit 1}"
if errorlevel 1 (
  pause
  exit /b 1
)

start "" "%~dp0P2P60-24Node.exe" --listen 0.0.0.0:39001 --node-id B

echo Waiting for the P2P listener...
powershell -NoProfile -Command "$ok=$false; 1..10 ^| %% { Start-Sleep -Milliseconds 500; $c=Get-NetTCPConnection -LocalPort 39001 -State Listen -ErrorAction SilentlyContinue; if($c){$ok=$true; Write-Host 'LISTENER: TCP 39001 is LISTENING'; $c ^| Format-Table LocalAddress,LocalPort,State,OwningProcess -AutoSize; break } }; if(-not $ok){Write-Host 'ERROR: P2P process did not expose TCP 39001 within 5 seconds.'; exit 1}"
if errorlevel 1 (
  echo.
  echo Check the P2P executable output window for the exact startup error.
  pause
  exit /b 1
)

echo.
echo Windows LAN IPv4 addresses:
powershell -NoProfile -Command "Get-NetIPAddress -AddressFamily IPv4 -PrefixOrigin Dhcp,Manual -ErrorAction SilentlyContinue ^| Where-Object {$_.IPAddress -notlike '127.*' -and $_.IPAddress -notlike '169.254.*'} ^| Select-Object IPAddress,InterfaceAlias,PrefixLength ^| Format-Table -AutoSize"

echo.
echo Firewall profiles:
powershell -NoProfile -Command "Get-NetFirewallProfile ^| Select-Object Name,Enabled ^| Format-Table -AutoSize"

echo.
echo LISTENER READY: Android may now connect to one of the displayed LAN IPv4 addresses on TCP 39001.
echo Keep this window open while testing.
echo.
pause
