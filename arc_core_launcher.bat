@echo off
title ARC_CORE_Ai Stack Launcher
cd /d "%~dp0"

echo.
echo Launching ARC_CORE_Ai System...
echo ---------------------------------
echo Activating Emotion Chip Engine...

:: Optional: Activate virtual environment if used
:: call venv\Scripts\activate

python launcher.py

echo ---------------------------------
echo ARC_CORE_Ai session ended.
pause
