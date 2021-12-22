#!/bin/bash
ECHO GIT STATUS
git status

ECHO GIT ADD example/export.html
git add example/export.html

ECHO GIT COMMIT -m 'push export.html from azure pipeline'
git commit -m 'push export.html from azure pipeline'

ECHO GIT PUSH
git push origin

ECHO GIT STATUS
git status