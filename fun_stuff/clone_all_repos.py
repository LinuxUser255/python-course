#!/usr/bin/env python3

"""
clone_all_repos.py
------------------
Clone every public repository from a given GitHub or GitLab user/account.

Usage:
    chmod +x clone_all_repos.py
    ./clone_all_repos.py --platform github --username torvalds
    ./clone_all_repos.py --platform gitlab --username gitterHQ
    ./clone_all_repos.py --platform github --username torvalds --dest ~/my_clones
    ./clone_all_repos.py --platform github --username torvalds --token ghp_yourtoken

Requirements:
    pip3 install requests
"""

import argparse          # Lets us accept command-line arguments (like --username)
import os                # For creating folders and working with file paths
import subprocess        # For running shell commands (git clone) from Python
import sys               # For exiting the script cleanly on errors
import requests          # For making HTTP requests to GitHub/GitLab APIs


# ─────────────────────────────────────────────
# STEP 1: Fetch repo list from GitHub
# ─────────────────────────────────────────────

def get_github_repos(username: str, token: str = None) -> list[dict]:
    """
    Hit the GitHub REST API and return a list of all public repos
    for the given username.

    Real-life analogy: Think of this like asking a library catalog,
    "Show me every book by Author X" — one page at a time.
    GitHub limits each response to 100 repos per page, so we loop
    through pages until there are no more results.

    Args:
        username: GitHub username (e.g. "torvalds")
        token:    Optional personal access token for higher rate limits
                  (unauthenticated = 60 req/hr, authenticated = 5000 req/hr)

    Returns:
        A list of dicts, each containing repo info (name, clone_url, etc.)
    """
    repos = []
    page = 1
    headers = {"Accept": "application/vnd.github+json"}

    # Add the token to headers if provided — this raises the API rate limit
    if token:
        headers["Authorization"] = f"Bearer {token}"

    print(f"\n Fetching repos from GitHub for user: {username}")

    while True:
        url = f"https://api.github.com/users/{username}/repos"
        params = {"per_page": 100, "page": page}  # Request 100 repos per page

        response = requests.get(url, headers=headers, params=params)

        # If the user doesn't exist, the API returns 404
        if response.status_code == 404:
            print(f"x GitHub user '{username}' not found.")
            sys.exit(1)

        # If we hit the rate limit, the API returns 403
        if response.status_code == 403:
            print("x GitHub API rate limit hit. Use --token to authenticate for higher limits.")
            sys.exit(1)

        response.raise_for_status()  # Raise an error for any other bad status code

        page_repos = response.json()

        # If the page is empty, we've fetched all repos — stop looping
        if not page_repos:
            break

        repos.extend(page_repos)
        print(f"    Page {page}: found {len(page_repos)} repos (total so far: {len(repos)})")
        page += 1

    return repos


# ─────────────────────────────────────────────
# STEP 2: Fetch repo list from GitLab
# ─────────────────────────────────────────────

def get_gitlab_repos(username: str, token: str = None) -> list[dict]:
    """
    Hit the GitLab REST API and return all public projects
    for the given username.

    GitLab calls users "users" and repos "projects".
    We first look up the user's numeric ID, then fetch their projects.

    Args:
        username: GitLab username (e.g. "gitterHQ")
        token:    Optional personal access token

    Returns:
        A list of dicts, each containing project info
    """
    headers = {}
    if token:
        headers["PRIVATE-TOKEN"] = token

    print(f"\n Fetching repos from GitLab for user: {username}")

    # Step 2a: Look up the user to get their numeric ID
    user_url = f"https://gitlab.com/api/v4/users?username={username}"
    user_response = requests.get(user_url, headers=headers)
    user_response.raise_for_status()
    users = user_response.json()

    if not users:
        print(f"x GitLab user '{username}' not found.")
        sys.exit(1)

    user_id = users[0]["id"]
    print(f"    Found GitLab user ID: {user_id}")

    # Step 2b: Fetch all projects for that user ID, page by page
    repos = []
    page = 1

    while True:
        projects_url = f"https://gitlab.com/api/v4/users/{user_id}/projects"
        params = {"per_page": 100, "page": page}

        response = requests.get(projects_url, headers=headers, params=params)
        response.raise_for_status()

        page_repos = response.json()
        if not page_repos:
            break

        repos.extend(page_repos)
        print(f"    Page {page}: found {len(page_repos)} repos (total so far: {len(repos)})")
        page += 1

    return repos


# ─────────────────────────────────────────────
# STEP 3: Extract the clone URL from repo data
# ─────────────────────────────────────────────

def get_clone_url(repo: dict, platform: str) -> str:
    """
    GitHub and GitLab store the clone URL under different keys.
    This function handles both so the rest of our code stays clean.

    GitHub uses: repo["clone_url"]
    GitLab uses: repo["http_url_to_repo"]
    """
    if platform == "github":
        return repo["clone_url"]
    elif platform == "gitlab":
        return repo["http_url_to_repo"]


# ─────────────────────────────────────────────
# STEP 4: Clone a single repo using subprocess
# ─────────────────────────────────────────────

def clone_repo(clone_url: str, destination: str) -> bool:
    """
    Run `git clone <url>` inside the destination folder.

    Real-life analogy: subprocess.run() is like having Python
    open a terminal and type commands for you — same as if you
    typed `git clone https://github.com/...` yourself.

    Args:
        clone_url:   The HTTPS URL to clone (e.g. https://github.com/user/repo.git)
        destination: The local folder to clone INTO

    Returns:
        True if clone succeeded, False if it failed
    """
    # Extract the repo name from the URL to use as the folder name
    # e.g. "https://github.com/torvalds/linux.git" → "linux.git" → "linux"
    repo_name = clone_url.rstrip("/").split("/")[-1].replace(".git", "")
    repo_path = os.path.join(destination, repo_name)

    # Skip if the repo folder already exists (already cloned)
    if os.path.exists(repo_path):
        print(f"    Skipping '{repo_name}' — folder already exists")
        return True

    print(f"    Cloning: {repo_name}  ←  {clone_url}")

    try:
        result = subprocess.run(
            ["git", "clone", clone_url, repo_path],
            capture_output=True,   # Capture stdout and stderr so we control the output
            text=True              # Return output as a string (not bytes)
        )

        if result.returncode == 0:
            print(f"    Done: {repo_name}")
            return True
        else:
            # git clone prints errors to stderr
            print(f"    Failed: {repo_name}\n      {result.stderr.strip()}")
            return False

    except FileNotFoundError:
        # This happens if `git` is not installed on the system
        print(" 'git' command not found. Please install Git first.")
        sys.exit(1)


# ─────────────────────────────────────────────
# STEP 5: Wire everything together
# ─────────────────────────────────────────────

def main():
    # Set up the argument parser — this is what reads your command-line flags
    parser = argparse.ArgumentParser(
        description="Clone all public repos from a GitHub or GitLab user."
    )
    parser.add_argument(
        "--platform",
        required=True,
        choices=["github", "gitlab"],
        help="Which platform to use: 'github' or 'gitlab'"
    )
    parser.add_argument(
        "--username",
        required=True,
        help="The username whose repos you want to clone"
    )
    parser.add_argument(
        "--dest",
        default="./cloned_repos",
        help="Local folder to clone repos into (default: ./cloned_repos)"
    )
    parser.add_argument(
        "--token",
        default=None,
        help="Optional API token (increases rate limits and allows private repos)"
    )

    args = parser.parse_args()

    # Create the destination folder if it doesn't already exist
    os.makedirs(args.dest, exist_ok=True)
    print(f"\n Cloning into folder: {os.path.abspath(args.dest)}")

    # ── Fetch the repo list ──────────────────────────────────
    if args.platform == "github":
        repos = get_github_repos(args.username, args.token)
    else:
        repos = get_gitlab_repos(args.username, args.token)

    if not repos:
        print(f"\n  No public repos found for '{args.username}' on {args.platform}.")
        sys.exit(0)

    print(f"\n Found {len(repos)} repos. Starting clone...\n")

    # ── Clone each repo ──────────────────────────────────────
    success_count = 0
    fail_count = 0

    for i, repo in enumerate(repos, start=1):
        print(f"[{i}/{len(repos)}]", end=" ")
        clone_url = get_clone_url(repo, args.platform)

        if clone_repo(clone_url, args.dest):
            success_count += 1
        else:
            fail_count += 1

    # ── Final summary ────────────────────────────────────────
    print(f"""
{'─' * 50}
 All done!
    Successful: {success_count}
    Failed:     {fail_count}
    Location:   {os.path.abspath(args.dest)}
{'─' * 50}
""")


# This block ensures main() only runs when you execute the script directly,
# not when it's imported as a module into another Python file.
if __name__ == "__main__":
    main()

