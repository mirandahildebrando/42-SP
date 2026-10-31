@echo off
setlocal
chcp 65001 >nul
set "SP42=%~dp0"
set "PATH=%SP42%tools\mingw64\bin;%SP42%tools\shell\bin;%SP42%tools\win;%PATH%"
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
set "GIT_BASH=%ProgramFiles%\Git\bin\bash.exe"
if not exist "%GIT_BASH%" set "GIT_BASH=%ProgramFiles(x86)%\Git\bin\bash.exe"
if not exist "%GIT_BASH%" set "GIT_BASH=%LOCALAPPDATA%\Programs\Git\bin\bash.exe"
if not exist "%GIT_BASH%" (
    echo.
    echo Git Bash nao encontrado. Instale o Git for Windows e rode este arquivo de novo.
    echo.
    pause
    exit /b 1
)
"%GIT_BASH%" --rcfile "%SP42%tools\shell\42rc" -i
endlocal
