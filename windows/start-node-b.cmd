@echo off
setlocal
title P2P 60-24 - Node B
echo ==========================================
echo P2P 60-24 OneClick Evo Positiv - Node B
echo ==========================================
echo.
echo Listening on all IPv4 interfaces, port 39001...
echo Keep this window open while Node A connects.
echo.
P2P60-24Node.exe --listen 0.0.0.0:39001 --node-id B
echo.
echo Node B finished with exit code %ERRORLEVEL%.
pause
