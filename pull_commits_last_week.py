import subprocess
import argparse
from datetime import datetime, timedelta

"""
Lol this is just doing 
git -C <repo_dir> log --since <date>
"""


def pull_commits_last_week(repo_dir):
    # Calculate the date a week ago
    week_ago = datetime.now() - timedelta(days=7)
    week_ago_str = week_ago.strftime('%Y-%m-%d')

    # Run the git log command
    result = subprocess.run(['git', '-C', repo_dir, 'log', '--since', week_ago_str],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)

    if result.stderr:
        print("Error:", result.stderr)
    else:
        print(result.stdout)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Pull commits from the last week.")
    parser.add_argument('--dir', type=str,
                        help='Directory of the git repository', required=True)

    args = parser.parse_args()
    pull_commits_last_week(args.dir)
