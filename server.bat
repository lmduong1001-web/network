@echo off
cd /d %~dp0

git add .
git commit -m "network"
git push origin master

echo DONE!
pause