@echo off
chcp 65001 > nul

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Solicitando privilégios de Administrador...
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "cmd.exe", "/c cd /d ""%~dp0"" && ""%~f0""", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /b
)
cd /d "%~dp0"

set "TASK_NAME=Byparr"
set "UV_PATH=%USERPROFILE%\.local\bin\uv.exe"
set "XML_PATH=%temp%\byparr_task.xml"
set "WORK_DIR=C:\ProgramData\Byparr"

:MENU
cls
echo.
echo ==================================
echo Configurar Inicialização do Byparr
echo ==================================
echo.
echo [1] Instalar Tarefa Agendada
echo [2] Desinstalar Tarefa Agendada
echo [3] Sair
echo.
set /p opcao="Digite uma opção (1-3): "

if "%opcao%"=="1" goto INSTALAR
if "%opcao%"=="2" goto DESINSTALAR
if "%opcao%"=="3" goto SAIR
goto MENU

:INSTALAR
cls
echo.

(
echo ^<?xml version="1.0" encoding="UTF-16"?^>
echo ^<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task"^>
echo   ^<Triggers^>
echo     ^<BootTrigger^>
echo       ^<Enabled^>true^</Enabled^>
echo     ^</BootTrigger^>
echo   ^</Triggers^>
echo   ^<Principals^>
echo     ^<Principal id="Author"^>
echo       ^<UserId^>S-1-5-18^</UserId^>
echo     ^</Principal^>
echo   ^</Principals^>
echo   ^<Settings^>
echo     ^<MultipleInstancesPolicy^>IgnoreNew^</MultipleInstancesPolicy^>
echo     ^<AllowHardTerminate^>true^</AllowHardTerminate^>
echo     ^<StartWhenAvailable^>false^</StartWhenAvailable^>
echo     ^<RunOnlyIfNetworkAvailable^>false^</RunOnlyIfNetworkAvailable^>
echo     ^<AllowStartOnDemand^>true^</AllowStartOnDemand^>
echo     ^<Enabled^>true^</Enabled^>
echo     ^<Hidden^>false^</Hidden^>
echo     ^<ExecutionTimeLimit^>PT0S^</ExecutionTimeLimit^>
echo     ^<Priority^>7^</Priority^>
echo   ^</Settings^>
echo   ^<Actions Context="Author"^>
echo     ^<Exec^>
echo       ^<Command^>"%UV_PATH%"^</Command^>
echo       ^<Arguments^>run "main.py"^</Arguments^>
echo       ^<WorkingDirectory^>%WORK_DIR%^</WorkingDirectory^>
echo     ^</Exec^>
echo   ^</Actions^>
echo ^</Task^>
) > "%XML_PATH%"

schtasks /create /tn "%TASK_NAME%" /xml "%XML_PATH%" /f >nul 2>&1
schtasks /run /tn "%TASK_NAME%" >nul 2>&1
set "task_error=%errorlevel%"

del "%XML_PATH%" >nul 2>&1

if %task_error% equ 0 (
    echo Tarefa "%TASK_NAME%" criada com êxito.
) else (
    echo Erro ao configurar a tarefa "%TASK_NAME%".
)
echo.
echo Pressione alguma tecla para voltar...
pause >nul
goto MENU

:DESINSTALAR
cls
echo.

taskkill -im python.exe /f >nul 2>&1
schtasks /delete /tn "%TASK_NAME%" /f >nul 2>&1

if %errorlevel% equ 0 (
    echo Tarefa "%TASK_NAME%" desinstalada com êxito.
) else (
    echo Erro ao desinstalar a tarefa "%TASK_NAME%".
)
echo.
echo Pressione alguma tecla para voltar...
pause >nul
goto MENU

:SAIR
exit
