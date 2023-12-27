import subprocess
import sys


def git_commit_push(commit_message, branch_name):
    try:
        # Add all files to the staging area
        subprocess.check_call(['git', 'add', '--all'])

        # Commit the changes
        subprocess.check_call(['git', 'commit', '-m', commit_message])

        # Push the changes to the remote repository
        subprocess.check_call(['git', 'push', '-u', 'origin', branch_name])

        print("Changes committed and pushed to branch:", branch_name)
    except subprocess.CalledProcessError as e:
        print("An error occurred while trying to commit and push changes:", e)


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Please provide a commit message.")
        return
    commit_message = args[0]
    branch_name = "master"
    git_commit_push(commit_message, branch_name)


if __name__ == "__main__":
    main()
