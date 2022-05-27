#!/bin/bash
black=$'\e[0;30'
red=$'\e[0;31'
green$'\e[0;32'
yellow=$'\e[0;33'
blue=$'\e[0;34'
Black=$'\e[1:30'
Red=$'\e[1;31m'
Green=$'\e[1;32m'
Yellow=$'\e[1;33m'
Blue=$'\e[1;34m'
echo
git add .
echo "$red <><><><><><><><><><><><>"
echo
echo "$Red Enter commit message: "
echo
read $red cmtMsg
git commit -m "$cmtMsg"
echo
echo "$yellow <><><><><><><><><><><>"
echo
git branch
echo
echo “$Yellow Type out the branch you wish to push to?”
echo
read $yellow pushBranch
echo
git push origin $pushBranch
echo "$green <><><><><><><><><><><>"
echo
echo "$Green Push complete :) "
echo
echo "$blue <><><><><><><><><><><>"
echo
echo "$Blue Opening a browser tab for GH Pull Request..."
echo
gh pr create -w
echo