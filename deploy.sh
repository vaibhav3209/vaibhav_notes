#!/bin/bash

# ...............................................
# Instructions :
# deploy.sh — Build MkDocs site and push to gh-pages via git worktree


# 1. Open Git Bash (not Pycharm Treminal) in the Vaibhav_Notes Directory

# 2. Usage:
#   ./deploy.sh <remote-name> \"<commit-message>\"
#..................................................

set -e  # stop immediately if any command fails


# 1. Assign arguments to descriptive variable names
REMOTE_NAME=$1
COMMIT_MSG=$2

# 2. Check if the user forgot to provide the remote name
if [ -z "$REMOTE_NAME" ]; then
    echo "❌ Error: Missing remote name."
    echo "Usage: bash ./deploy.sh <remote-name> \"<commit-message>\""
    exit 1
fi


# 3. Check if the user forgot to provide a commit message
if [ -z "$COMMIT_MSG" ]; then
    echo "❌ Error: Missing commit message."
    echo "Usage: bash ./deploy.sh <remote-name> \"<commit-message>\""
    exit 1
fi


echo "🔨 Building site with MkDocs..."
./myenv/Scripts/python.exe -m mkdocs build

echo "🧹 Clearing old files in ../Deployed_Notes..."
rm -rf ../Deployed_Notes/*

echo "📦 Copying new build into ../Deployed_Notes..."
cp -r site/* ../Deployed_Notes/

echo "🚀 Committing and pushing to gh-pages..."
cd ../Deployed_Notes
git add .
git commit -m "$COMMIT_MSG"
git push $REMOTE_NAME gh-pages

echo "✅ Deployed with message: \"$COMMIT_MSG\""
