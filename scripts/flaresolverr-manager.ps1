$Host.UI.RawUI.WindowTitle = "FlareSolverr Manager"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process PowerShell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

while ($true) {
    Clear-Host
    Write-Host "FlareSolverr Manager`n"
    Write-Host "[1] Install task"
    Write-Host "[2] Uninstall task"
    Write-Host "[3] Exit`n"

    $choice = Read-Host "Choose an option"

    switch ($choice) {
        '1' {
            $baseDir = "C:\Tools\FlareSolverr"
            $exePath = "$baseDir\flaresolverr.exe"
            $batPath = "$baseDir\autorun.bat"
            
            "@echo off`nset LANG=en-US`n`"$exePath`"" | Out-File -FilePath $batPath -Encoding ascii
            
            SchTasks.exe /Create /TN "FlareSolverr" /SC ONSTART /DELAY "0000:30" /RL HIGHEST /NP /TR "`"$batPath`"" > $null 2>&1
            Write-Host "Task installed successfully." -ForegroundColor Green
            
            SchTasks.exe /Run /TN "FlareSolverr" > $null 2>&1
            Write-Host "Task started successfully." -ForegroundColor Green
            Write-Host ""
            Write-Host -NoNewline "Press any key to back..."
            $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        }
        '2' {
            schtasks /query /tn "FlareSolverr" > $null 2>&1
            if ($LASTEXITCODE -eq 0) {
                Stop-Process -Name "flaresolverr" -Force -ErrorAction SilentlyContinue
                Stop-Process -Name "cmd" -Force -ErrorAction SilentlyContinue
                Write-Host "Task stopped successfully." -ForegroundColor Yellow
            }
            SchTasks.exe /Delete /TN "FlareSolverr" /F > $null 2>&1
            
            $batPath = "$env:AllUsersProfile\FlareSolverr\autorun.bat"
            if (Test-Path $batPath) { Remove-Item $batPath -Force }

            Write-Host "Task uninstalled successfully." -ForegroundColor Yellow
            Write-Host ""
            Write-Host -NoNewline "Press any key to back..."
            $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        }
        '3' {
            exit
        }
        default {
            Write-Host "Invalid option. Try again next time!" -ForegroundColor Red
            Start-Sleep -Seconds 2
        }
    }
}