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
