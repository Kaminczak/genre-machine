@echo off
REM One-time publish of The Genre Machine to GitHub Pages.
cd /d "%~dp0.."

git init -b main
git add -A
git -c user.name="Steve Kaminczak" -c user.email="kaminczak@gmail.com" commit -q -m "The Genre Machine: 4 fairy tales x 32 genres, with designed-voice narration"

echo.
echo ---- tracked files ----
git ls-files | find /c /v ""
echo ---- repo size ----
git count-objects -vH | findstr size-pack
