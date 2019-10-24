#!/bin/bash
# Forces merge, rebase, squash to bring both branches to the same place

echo -e "\ngit push origin CLI_Dev --force"
git push origin CLI_Dev --force

echo -e "\ngit checkout master"
git checkout master

echo -e "\ngit pull origin master"
git pull origin master

echo -e "\ngit checkout CLI_Dev"
git checkout CLI_Dev

echo -e "\ngit rebase master"
git rebase master

echo -e "\ngit push origin CLI_Dev --force"
git push origin CLI_Dev --force

echo -e "\ngit checkout master"
git checkout master

echo -e "\ngit merge CLI_Dev"
git merge CLI_Dev

echo -e "\ngit push origin master"
git push origin master

# force checkouot of CLI_Dev to restore focus to Dev branch
# Absent this, I end up in "master"
# which causes no end of trouble the next time
# I try a commit, it pushes to master and not dev!

echo -e "\ngit checkout CLI_Dev"
git checkout CLI_Dev
