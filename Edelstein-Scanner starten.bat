@echo off
chcp 65001 >nul
title Capybara Gem Scanner
cd /d "%~dp0"
echo ===================================================
echo    Capybara Gem Scanner  (Community Edition)
echo ===================================================
echo.

set "PY="
where python >nul 2>nul
if %errorlevel%==0 set "PY=python"
if not defined PY (
  py -3 --version >nul 2>nul
  if %errorlevel%==0 set "PY=py -3"
)

if not defined PY (
  echo Python wurde nicht gefunden / Python not found.
  where winget >nul 2>nul
  if %errorlevel%==0 (
    echo Installiere Python automatisch / installing Python ...
    winget install -e --id Python.Python.3.12 --silent --accept-package-agreements --accept-source-agreements
    echo.
    echo Bitte diese Datei NOCH EINMAL doppelklicken.
    echo Please double-click this file ONCE MORE.
    pause
    exit /b
  ) else (
    echo Bitte Python installieren: https://www.python.org/downloads/
    echo Haken bei "Add python.exe to PATH" setzen, dann erneut starten.
    pause
    exit /b
  )
)

echo Pruefe Bausteine / checking components ...
%PY% -m pip install --upgrade pip -q
%PY% -m pip install -q mss pillow numpy rapidfuzz rapidocr-onnxruntime
if %errorlevel% neq 0 (
  echo Problem beim Installieren / install problem. Internet pruefen.
  pause
  exit /b
)

echo Starte / starting ...
%PY% "%~dp0capybara_gem_scanner.py"
if %errorlevel% neq 0 (
  echo.
  echo Beendet / ended ^(evtl. Meldung oben / see message above^).
  pause
)
