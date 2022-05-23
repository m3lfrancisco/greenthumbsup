#!/bin/bash
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
echo
echo “Type out the branch you wish to push to?”
echo
read pushBranch
echo
git push origin $pushBranch
echo "<><><><><><><><><><><>"
echo
echo "Push complete :) "
echo
echo "<><><><><><><><><><><>"
echo
gh pr create -w
echo "Opening a browser tab for GH Pull Request..."