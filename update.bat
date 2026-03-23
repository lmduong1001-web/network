@echo off
cd /d %~dp0

echo ===== FORCE SYNC FROM GIT CHA (master) =====

git fetch origin
git reset --hard origin/master

echo ===== DONE =====
pause