@echo off
REM ============================================================
REM  The Genre Machine — local server
REM
REM  Double-click this file to run the project.
REM
REM  Why not just open index.html? Because browsers block a
REM  file:// page from calling the Voice Creator Pro API on
REM  port 8100, so narration would silently fail. Serving over
REM  http fixes that.
REM ============================================================

cd /d "%~dp0"

echo.
echo   The Genre Machine  -  http://127.0.0.1:8123
echo   Close this window to stop the server.
echo.

start "" http://127.0.0.1:8123/index.html
python -m http.server 8123
