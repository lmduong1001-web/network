@echo off
cd /d %~dp0

echo ===== ADD =====
git add .

echo ===== COMMIT =====
git commit -m "network"

echo ===== PULL (rebase) =====
git pull origin master --rebase

echo ===== PUSH =====
git push origin master

echo ===== DONE =====
pause