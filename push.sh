#!/bin/bash
echo 'git config'
git config --global user.email "g.strainovic@gmail.com"
git config --global user.name "gstrainovic"


echo 'git status'
git status

echo 'git add example/export.html'
git add example/export.html

echo 'git commit: push export.html from azure pipeline'
git commit -m 'push export.html from azure pipeline'

echo 'git push'
git push origin

echo 'git status'
git status