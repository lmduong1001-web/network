@echo off
cd /d %~dp0

echo ===== ADD & COMMIT =====
git add .
git commit -m "update"

echo ===== PUSH =====
git push origin master

echo ===== DONE =====
pause