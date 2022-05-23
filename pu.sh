#!/bin/bash
echo
git add .
echo "<><><><><><><><><><><><>"
echo
echo "Enter commit message: "
read cmtMsg
git commit -m "$cmtMsg"
echo "<><><><><><><><><><><>"
echo
git branch
echo
echo “Push to which branch?”
read pushBranch
echo
git push origin $pushBranch
echo "<><><><><><><><><><><>"
echo
echo "Push complete :) "
echo
echo "<><><><><><><><><><><>"
echo