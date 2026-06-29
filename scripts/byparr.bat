@echo off
:: Força o uso de UTF-8 para evitar problemas com acentos
chcp 65001 > nul

:: ==========================================
:: BLOCO DE AUTORIZAÇÃO ELEVADA (ADMIN) DO .BAT
:: ==========================================
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Solicitando privilégios de Administrador...
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /b
)
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
set /p opcao="Escolha uma opção (1-3): "

if "%opcao%"=="1" goto INSTALAR
if "%opcao%"=="2" goto REMOVER
if "%opcao%"=="3" goto SAIR
goto MENU

:INSTALAR
cls
echo Instalando a tarefa "Byparr"...
echo.

:: Define o caminho exato do executável uv.exe usando a variável nativa %USERPROFILE%
set "UV_PATH=%USERPROFILE%\.local\bin\uv.exe"

:: Gera o arquivo XML estruturado com nível de privilégio padrão e sem limite de 3 dias
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
) > "%temp%\byparr_task.xml"

:: Cria a tarefa no Agendador importando o XML gerado (Roda como SYSTEM pelo SID S-1-5-18)
schtasks /create /tn "Byparr" /xml "%temp%\byparr_task.xml" /f >nul 2>&1
set "task_error=%errorlevel%"

:: Apaga o arquivo XML temporário
del "%temp%\byparr_task.xml" >nul 2>&1

if %task_error% equ 0 (
    echo.
    echo [SUCESSO] Tarefa "Byparr" criada e configurada com êxito!
    echo Executável: "%UV_PATH%"
    echo Iniciar em: C:\ProgramData\Byparr
) else (
    echo.
    echo [ERRO] Falha ao configurar a tarefa.
)
pause
goto MENU

:REMOVER
cls
echo Removendo a tarefa "Byparr"...
echo.

schtasks /delete /tn "Byparr" /f >nul 2>&1

if %errorlevel% equ 0 (
    echo.
    echo [SUCESSO] Tarefa "Byparr" removida com êxito!
) else (
    echo.
    echo [AVISO/ERRO] Falha ao remover ou a tarefa não existia.
)
pause
goto MENU

:SAIR
exit
