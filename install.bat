@echo off
cls

:: Check if python is installed
:: https://stackoverflow.com/a/26241114
python --version >nul
if errorlevel 1 goto errorNoPython

:: If python IS installed
python -m pip install requests colorama tabulate
echo.
echo You may now close this window and open the main Python file
goto:end

:: If python ISNT installed
:errorNoPython
echo.
echo You don't seem to have Python isntalled.
echo Please install the latest version of Python to
echo install the needed packages and to be able
echo to run this program.
echo.
echo https://www.python.org/downloads/

:end
pause >nul
exit