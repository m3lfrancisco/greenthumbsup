#!/bin/bash
logoansi=$'\e[38;5;0;48;5;148m'
inversvid=$'\e[7m'
resetvid=$'\e[0m'
blkredback=$'\e[1;30;41m'
whtredback=$'\e[1;37;41m'
blkgrnback=$'\e[1;30;42m'
whtgrnback=$'\e[1;37;42m'
blkbluback=$'\e[1;30;44m'
whtbluback=$'\e[1;37;44m'
black=$'\e[0;30'
red=$'\e[0;31'
green=$'\e[0;32'
yellow=$'\e[0;33'
blue=$'\e[0;34'
Black=$'\e[1:30'
Red=$'\e[1;31m'
Green=$'\e[1;32m'
Yellow=$'\e[1;33m'
Blue=$'\e[1;34m'

echo $Red
git add .
echo "<><><><><><><><><><><><>"
echo
echo "Enter commit message: "
echo
read cmtMsg
git commit -m "$cmtMsg"
echo
echo "<><><><><><><><><><><>"
echo 
git branch
echo $Green
echo “Type out the branch you wish to push to?”
echo
read pushBranch
echo $blkgrnback
git push origin $pushBranch
echo $resetvid
echo $Yellow
echo "<><><><><><><><><><><>"
echo
echo "Push complete :) "
echo
echo "<><><><><><><><><><><>"
echo $Blue
echo "Opening a browser tab for GH Pull Request..."
echo
gh pr create -w
echo
echo $resetvid
