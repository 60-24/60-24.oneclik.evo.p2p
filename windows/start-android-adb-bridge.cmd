@echo off
setlocal
title P2P 60-24 - Android <-> Windows ADB Bridge

echo ==========================================
echo P2P 60-24 Android <-> Windows bridge test
echo ==========================================
echo.
if not exist "%~dp0P2P60-24Node.exe" (
  echo ERROR: P2P60-24Node.exe was not found beside this script.
  exit /b 1
)

where adb >nul 2>&1
if errorlevel 1 (
  echo ERROR: adb.exe was not found in PATH.
  echo Install Android platform-tools and enable USB debugging on the Android device.
  exit /b 1
)

echo Checking Android device...
adb devices
if errorlevel 1 exit /b 1

echo.
echo Creating ADB reverse bridge:
echo Android 127.0.0.1:39001 ^> Windows 127.0.0.1:39001
adb reverse tcp:39001 tcp:39001
if errorlevel 1 (
  echo ERROR: adb reverse failed.
  exit /b 1
)

echo.
echo Starting native Windows Node B on loopback...
start "P2P Node B" "%~dp0P2P60-24Node.exe" --listen 127.0.0.1:39001 --node-id B
echo.
echo In Android app use:
echo   Host: 127.0.0.1
echo   Port: 39001
echo   Node label: A
echo   Message: hello-from-Android
echo.
echo Expected Android response: OK response=pong-from-B
echo Expected Windows Node B: node B received from A: hello-from-Android
echo.
pause