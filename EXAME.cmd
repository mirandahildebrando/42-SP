@echo off
setlocal
chcp 65001 >nul
set "SP42=%~dp0"
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
set "PY=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
if not exist "%PY%" set "PY=python"
"%PY%" "%SP42%tools\exame\exame.py" %*
endlocal
