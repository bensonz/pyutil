#!/bin/bash

# Default branch is 'master'. Change it to 'main' or any other default branch as needed.
BRANCH="master"
COMMIT_MESSAGE=""

# Parse command-line options
while getopts "b:" opt; do
  case $opt in
    b) BRANCH="$OPTARG";;
    \?) echo "Invalid option -$OPTARG" >&2; exit 1;;
  esac
done

# Remove the parsed options from the positional parameters
shift $((OPTIND -1))

# The first remaining argument is the commit message
COMMIT_MESSAGE=$1

# Check if a commit message was provided
if [ -z "$COMMIT_MESSAGE" ]; then
  echo "Please provide a commit message."
  exit 1
fi

# Perform Git operations
git add --all
if git commit -m "$COMMIT_MESSAGE"; then
  git push -u origin "$BRANCH"
  echo "Changes committed and pushed to branch: $BRANCH"
else
  echo "An error occurred while trying to commit and push changes."
  exit 1
fi
