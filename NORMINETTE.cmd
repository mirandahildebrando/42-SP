@echo off
setlocal
chcp 65001 >nul
set "SP42=%~dp0"
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
set "PY=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
if not exist "%PY%" set "PY=python"
if "%~1"=="" (
    "%PY%" -m norminette --no-colors -R CheckForbiddenSourceHeader "%SP42%piscina"
) else (
    "%PY%" -m norminette --no-colors -R CheckForbiddenSourceHeader %*
)
endlocal
