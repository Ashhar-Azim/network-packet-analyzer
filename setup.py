import os
import subprocess
import random
from datetime import datetime, timedelta


def run(cmd, env=None):
    subprocess.run(cmd, check=True, env=env)

        
def init_repo(repo_url):
    if not os.path.exists(".git"):
        run(["git", "init"])
        run(["git", "branch", "-M", "main"])
        run(["git", "remote", "add", "origin", repo_url])
    else:
        # Update existing remote
        run(["git", "remote", "remove", "origin"])
        run(["git", "remote", "add", "origin", repo_url])

    print(f"Using remote repository: {repo_url}")


def make_commit(commit_date, message="pixel"):
    env = os.environ.copy()
    ts = commit_date.strftime("%Y-%m-%dT%H:%M:%S")

    env["GIT_AUTHOR_DATE"] = ts
    env["GIT_COMMITTER_DATE"] = ts

    with open("activity.txt", "a") as f:
        f.write(ts + "\n")

    run(["git", "add", "."], env=env)
    run(["git", "commit", "-m", message], env=env)


def generate_year_dates(year):
    start = datetime(year, 1, 1)
    end = datetime(year, 12, 31)

    days = []
    current = start
    while current <= end:
        days.append(current)
        current += timedelta(days=1)

    return days


def main():
    print("\n=== GitHub Activity Bot ===\n")

    repo_url = input("Enter GitHub repository URL: ").strip()
    year = int(input("Enter year for activity (e.g. 2024): ").strip())
    probability = float(input("Probability of green box per day (0–1): ").strip())
    max_commits = int(input("Max commits per green box (1–10): ").strip())

    if not (0 <= probability <= 1):
        raise ValueError("Probability must be between 0 and 1")

    if not (1 <= max_commits <= 10):
        raise ValueError("Commit range must be between 1 and 10")

    init_repo(repo_url)

    print("\nGenerating activity...\n")

    days = generate_year_dates(year)
    active_days = 0

    for day in days:
        if random.random() < probability:
            intensity = random.randint(1, max_commits)
            for _ in range(intensity):
                make_commit(day)
            active_days += 1

    print(f"\nCreated activity on {active_days} days.")
    print("Pushing to GitHub...\n")

    run(["git", "push", "-u", "origin", "main"])

    print("Done. Check your GitHub activity graph in a few minutes.")


if __name__ == "__main__":
    main()
