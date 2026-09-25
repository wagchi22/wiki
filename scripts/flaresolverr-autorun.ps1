$Host.UI.RawUI.WindowTitle = "FlareSolverr Autorun"

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process PowerShell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

$baseDir = Split-Path -Parent $PSCommandPath
$exePath = Join-Path $baseDir "flaresolverr.exe"
$batPath = Join-Path $baseDir "autorun.bat"

while ($true) {
    Clear-Host
    Write-Host "FlareSolverr Autorun`n"
    Write-Host "[1] Install task"
    Write-Host "[2] Uninstall task"
    Write-Host "[3] Exit`n"

    $choice = Read-Host "Choose an option"

    switch ($choice) {
        '1' {
            if (-not (Test-Path -LiteralPath $exePath -PathType Leaf)) {
                Write-Host "flaresolverr.exe not found!" -ForegroundColor Red
                Write-Host ""
                Write-Host -NoNewline "Press any key to back..."
                $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
                continue
            }

            "@echo off`nset LANG=en-US`ncd /d `"%~dp0`"`n`"%~dp0flaresolverr.exe`"" | Out-File -FilePath $batPath -Encoding ascii -Force

            SchTasks.exe /Delete /TN "FlareSolverr" /F > $null 2>&1

            SchTasks.exe /Create /TN "FlareSolverr" /SC ONSTART /DELAY "0000:30" /RL HIGHEST /NP /TR "`"$batPath`"" /F > $null 2>&1

            if ($LASTEXITCODE -eq 0) {
                Write-Host "Task installed successfully." -ForegroundColor Green

                SchTasks.exe /Run /TN "FlareSolverr" > $null 2>&1

                if ($LASTEXITCODE -eq 0) {
                    Write-Host "Task started successfully." -ForegroundColor Green
                }
                else {
                    Write-Host "Task installed, but could not be started." -ForegroundColor Yellow
                }
            }
            else {
                Write-Host "Failed to install task." -ForegroundColor Red
            }

            Write-Host ""
            Write-Host -NoNewline "Press any key to back..."
            $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        }

        '2' {
            schtasks /query /tn "FlareSolverr" > $null 2>&1

            if ($LASTEXITCODE -eq 0) {
                SchTasks.exe /End /TN "FlareSolverr" > $null 2>&1

                Start-Sleep -Milliseconds 500

                Stop-Process -Name "flaresolverr" -Force -ErrorAction SilentlyContinue

                Write-Host "Task stopped successfully." -ForegroundColor Yellow
            }

            SchTasks.exe /Delete /TN "FlareSolverr" /F > $null 2>&1

            if (Test-Path -LiteralPath $batPath) {
                Remove-Item -LiteralPath $batPath -Force -ErrorAction SilentlyContinue
            }

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
