@echo off

if /I "%radarr_eventtype%"=="Test" exit /b 0
if /I "%sonarr_eventtype%"=="Test" exit /b 0

"C:\Users\Wagner Gradaschi\AppData\Local\Python\pythoncore-3.14-64\python.exe" "C:\GitHub\wiki\scripts\remux-mkv.py" %*

exit /b %errorlevel%