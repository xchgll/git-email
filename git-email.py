import requests
import argparse
from typing import List

banner = r"""
  ________.__  __            ___________              .__.__   
 /  _____/|__|/  |_          \_   _____/ _____ _____  |__|  |  
/   \  ___|  \   __\  ______  |    __)_ /     \\__  \ |  |  |  
\    \_\  \  ||  |   /_____/  |        \  Y Y  \/ __ \|  |  |__
 \______  /__||__|           /_______  /__|_|  (____  /__|____/
        \/                           \/      \/     \/         
"""

RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
PURPLE = "\033[35m"
CYAN   = "\033[36m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

COMMITS_BASE = "https://api.github.com/repos/%s/%s/commits"
REPOS_BASE   = "https://api.github.com/users/%s/repos"

unique_emails = []

print(BOLD + BLUE + banner)
print("Author: @xchgll" + RESET)


class Commit:
    def __init__(self):
        self.author = "None"
        self.committer = "None"
        self.hash = "None"
        self.email = "None"
        self.url = "None"


class Repo:
    def __init__(self):
        self.name = "Unknown"
        self.url = "None"
        self.commits: List[Commit] = []
        self.is_private = False
        self.stars_count = 0
        self.created_at = ""
        self.updated_at = ""


def print_commit(commit: Commit):
    print(GREEN + BOLD + "Hash:      " + commit.hash)
    print("Author:    " + commit.author)
    print("Committer: " + commit.committer)
    print("Email:     " + commit.email)
    print("URL:       " + commit.url + RESET)
    print("\n")

def print_repo(repo: Repo):
    print(BLUE + BOLD + "\n____REPO____" + RESET)
    print(BLUE + "Name:    " + repo.name)
    print("URL:     " + repo.url)
    print("Stars:   " + str(repo.stars_count))
    print("Private: " + str(repo.is_private))
    print("Created: " + repo.created_at)
    print("Updated: " + repo.updated_at + RESET)


def req_get_json(url: str) -> dict:
    resp = requests.get(url)

    if resp.status_code == 403:
        print(RED + BOLD + "[!] 403 Forbidden" + RESET)
        return []
    if resp.status_code == 404:
        print(RED + BOLD + "[!] 404 Not Found: " + url + RESET)
        return []

    return resp.json()


def find_commits(repo: Repo, username: str, verbosity: int) -> List[Commit]:
    global unique_emails

    if repo.is_private:
        if verbosity >= 1:
            print(BOLD + RED + f"[!] {repo.url} - Private Repository" + RESET)
        return []

    full_url = COMMITS_BASE % (username, repo.name)

    if verbosity >= 2:
        print(CYAN + f"[*] Fetching commits from: {full_url}" + RESET)

    commits_data = req_get_json(full_url)

    if isinstance(commits_data, dict):
        if verbosity >= 1:
            print(YELLOW + f"[$] {repo.name}: {commits_data.get('message', 'Unknown error')}" + RESET)
        return []

    if len(commits_data) == 0:
        if verbosity >= 1:
            print(YELLOW + f"[$] {repo.name}: No Commits" + RESET)
        return []

    for commit_data in commits_data:
        commit = Commit()

        commit.hash = commit_data.get("sha", "null")
        commit.url = commit_data.get("html_url", "null")

        author_obj = commit_data.get("author") or {}
        committer_obj = commit_data.get("committer") or {}

        commit.author = author_obj.get("login", "null")
        commit.committer = committer_obj.get("login", "null")
        commit.email = commit_data["commit"]["committer"]["email"] or "null"

        repo.commits.append(commit)

        exists = any(e["email"] == commit.email for e in unique_emails)
        if not exists and commit.email != "null":
            unique_emails.append({
                "email":     commit.email,
                "committer": commit.committer
            })

        if verbosity >= 2:
            print_commit(commit)

    return repo.commits


def get_repos_by_username(username: str) -> List[Repo]:
    url  = REPOS_BASE % username
    data = req_get_json(url)

    if isinstance(data, dict):
        print(RED + BOLD + f"[!] Error: {data.get('message', 'Unknown error')}" + RESET)
        return []

    repos = []
    for repo_data in data:
        repo = Repo()
        repo.name = repo_data.get("name", "Unknown")
        repo.url = repo_data.get("html_url", "None")
        repo.is_private = repo_data.get("private", False)
        repo.stars_count = repo_data.get("stargazers_count", 0)
        repo.created_at = repo_data.get("created_at", "")
        repo.updated_at = repo_data.get("updated_at", "")
        repos.append(repo)

    return repos


def get_single_repo(username: str, repo_name: str) -> Repo:
    url  = f"https://api.github.com/repos/{username}/{repo_name}"
    data = req_get_json(url)

    if isinstance(data, list) or not data:
        print(RED + BOLD + f"[!] Repo not found: {repo_name}" + RESET)
        return None

    repo = Repo()
    repo.name = data.get("name", "Unknown")
    repo.url = data.get("html_url", "None")
    repo.is_private = data.get("private", False)
    repo.stars_count = data.get("stargazers_count", 0)
    repo.created_at = data.get("created_at", "")
    repo.updated_at = data.get("updated_at", "")

    return repo


def run(username: str, verbosity: int, repo_name: str = None):
    print(BOLD + PURPLE + f"\n[~] Target: {username}" + RESET)

    if repo_name:
        repo = get_single_repo(username, repo_name)
        if not repo:
            return
        repos = [repo]
    else:
        repos = get_repos_by_username(username)
        if not repos:
            print(RED + "[$] User have no repos or invalid user" + RESET)
            return

    print(BOLD + CYAN + f"[+] Found {len(repos)} repositories\n" + RESET)

    for repo in repos:
        if verbosity >= 1:
            print_repo(repo)

        find_commits(repo, username, verbosity)

    print(BOLD + PURPLE + "\n========== Unique Emails Found ==========")
    if unique_emails:
        for entry in unique_emails:
            print(GREEN + f"  [>] {entry['committer']}  {entry['email']}" + RESET)
    else:
        print(YELLOW + "  [!] No emails found :(" + RESET)

    print(BOLD + PURPLE + f"[+] Total: {len(unique_emails)} unique email(s)" + RESET)


def main():
    parser = argparse.ArgumentParser(
        description="Git Email - Extract emails from GitHub commits"
    )
    parser.add_argument(
        "-u", "--username",
        required=True,
        help="GitHub username to target"
    )
    parser.add_argument(
        "-v", "--verbosity",
        type=int,
        default=1,
        choices=[0, 1, 2],
        help="Verbosity level: 0=quiet, 1=normal, 2=verbose"
    )
    parser.add_argument(
        "-r", "--repo",
        default=None,
        help="Specific repo name (optional)"
    )

    args = parser.parse_args()
    run(args.username, args.verbosity, args.repo)

main()