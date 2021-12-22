#!/bin/bash
echo '####################################################'
echo 'git config'
echo '####################################################'
git config --global user.email "g.strainovic@gmail.com"
git config --global user.name "gstrainovic"

echo '####################################################'
echo 'git checkout master'
echo '####################################################'
git checkout master

echo '####################################################'
echo 'git add example/export.html'
echo '####################################################'
git add example/export.html

echo '####################################################'
echo 'git commit: push export.html from azure pipeline'
echo '####################################################'
git commit -m 'push export.html from azure pipeline'

echo '####################################################'
echo 'git push'
echo '####################################################'
git push origin

echo '####################################################'
echo 'git status'
echo '####################################################'
git status