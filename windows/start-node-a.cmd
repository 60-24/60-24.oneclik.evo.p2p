@echo off
setlocal
title P2P 60-24 - Node A
echo ==========================================
echo P2P 60-24 OneClick Evo Positiv - Node A
echo ==========================================
echo.
set /p PEER_IP=Enter Windows Node B LAN IPv4 address:
if "%PEER_IP%"=="" goto :error
echo.
echo Connecting to %PEER_IP%:39001 ...
echo.
P2P60-24Node.exe --connect %PEER_IP%:39001 --node-id A --message hello-from-A
echo.
echo Node A finished with exit code %ERRORLEVEL%.
pause
exit /b 0
:error
echo.
echo ERROR: No IP address entered.
pause
exit /b 1
