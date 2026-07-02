@echo off
chcp 65001 > nul

:: ==========================================
:: BLOCO DE AUTORIZACAO ELEVADA (ADMIN)
:: ==========================================
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Solicitando privilegios de Administrador...
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "cmd.exe", "/c cd /d ""%~dp0"" && ""%~f0""", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /b
)
cd /d "%~dp0"
:: ==========================================

:MENU
cls
echo ===================================================
echo       GERENCIADOR DA TAREFA AGENDADA (BYPARR)
echo ===================================================
echo [1] Instalar Tarefa Agendada
echo [2] Remover Tarefa Agendada
echo [3] Sair
echo ===================================================
set /p opcao="Escolha uma opcao (1-3): "

if "%opcao%"=="1" goto INSTALAR
if "%opcao%"=="2" goto REMOVER
if "%opcao%"=="3" goto SAIR
goto MENU

:INSTALAR
cls
echo Instalando a tarefa "Byparr"...
echo.

set "UV_PATH=%USERPROFILE%\.local\bin\uv.exe"
set "XML_PATH=%temp%\byparr_task.xml"

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
echo       ^<WorkingDirectory^>C:\ProgramData\Byparr^</WorkingDirectory^>
echo     ^</Exec^>
echo   ^</Actions^>
echo ^</Task^>
) > "%XML_PATH%"

schtasks /create /tn "Byparr" /xml "%XML_PATH%" /f >nul 2>&1
set "task_error=%errorlevel%"

del "%XML_PATH%" >nul 2>&1

if %task_error% equ 0 (
    echo [SUCESSO] Tarefa "Byparr" criada e configurada com exito!
    echo Executavel: "%UV_PATH%"
    echo Iniciar em: C:\ProgramData\Byparr
) else (
    echo [ERRO] Falha ao configurar a tarefa.
)
echo.
pause
goto MENU

:REMOVER
cls
echo Removendo a tarefa "Byparr"...
echo.

schtasks /delete /tn "Byparr" /f >nul 2>&1

if %errorlevel% equ 0 (
    echo [SUCESSO] Tarefa "Byparr" removida com exito!
) else (
    echo [AVISO/ERRO] Falha ao remover ou a tarefa nao existia.
)
echo.
pause
goto MENU

:SAIR
exit
