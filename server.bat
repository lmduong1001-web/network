@echo off
cd /d %~dp0

git add .
git commit -m "update"
git pull origin master
git push origin master

echo DONE!
pause