@echo off
REM One-time publish of The Genre Machine to GitHub Pages.
cd /d "%~dp0.."

gh repo create genre-machine --public --source=. --remote=origin --description "Four fairy tales x 32 genres. A classroom tool for teaching genre and voice." --push
if errorlevel 1 goto :done

echo.
echo ---- enabling pages ----
gh api -X POST repos/Kaminczak/genre-machine/pages -f "source[branch]=main" -f "source[path]=/"

:done
echo.
gh repo view Kaminczak/genre-machine --json url,visibility,pushedAt
