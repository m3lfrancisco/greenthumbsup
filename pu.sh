#!/bin/bash
git add .
echo "<><><><><><><><><><><><>"
echo
echo "Enter commit message: "
read cmtMsg
git commit -m "$cmtMsg"
echo "<><><><><><><><><><><>"
echo
echo “Push to which branch?”
read pushBranch
git push origin $pushBranch
echo "<><><><><><><><><><><>"
echo
echo "Push complete :) "
echo
echo "<><><><><><><><><><><>"