#!/opt/homebrew/bin/python3.11
import subprocess
import argparse


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
    # Create the parser
    parser = argparse.ArgumentParser(
        description='Commit and push changes to a Git repository.')

    # Add the arguments
    parser.add_argument('commit_message', type=str, help='The commit message.')
    parser.add_argument('-b', '--branch', type=str, default='master',
                        help='The branch name to push to. Default is "master".')

    # Parse the arguments
    args = parser.parse_args()

    git_commit_push(args.commit_message, args.branch)


if __name__ == "__main__":
    main()
