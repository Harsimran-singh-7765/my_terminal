import subprocess
import os
import shutil


def run(cmd):
    return subprocess.getoutput(cmd)


def git_start():
    print("🚀 Starting new Git repo...")

    # Initialize repo
    run("git init")
    run("git add .")
    
    # Ask for commit message
    commit_msg = input("📥 Enter initial commit message: ").strip() or "Initial commit"
    run(f'git commit -m "{commit_msg}"')
    
    # Check if gh (GitHub CLI) is installed
    if not shutil.which("gh"):
        print("❌ GitHub CLI (gh) not found.")
        print("🔗 Please manually create a repo at https://github.com/new")
        remote_url = input("📎 Paste the GitHub repo URL: ").strip()
        run(f"git remote add origin {remote_url}")
        run("git branch -M main")
        run("git push -u origin main")
        return

    # Get GitHub username
    username = run("gh api user --jq .login")
    print(f"👤 GitHub Username: {username}")

    # Ask for repo name
    repo_name = input("📁 Enter new GitHub repo name: ").strip()

    # Create repo
    run(f"gh repo create {username}/{repo_name} --public --source=. --remote=origin --push")

    print(f"✅ Repo created: https://github.com/{username}/{repo_name}")


def git_push(filename=None, branch=None):
    if filename is None:
        filename = "."

    # Get current branch if not provided
    if branch is None:
        branch = run("git rev-parse --abbrev-ref HEAD")

    run(f"git add {filename}")

    commit_msg = input("📝 Enter commit message: ").strip() or "Update"
    run(f'git commit -m "{commit_msg}"')
    run(f"git push origin {branch}")

    print(f"✅ Changes pushed to branch `{branch}`.")


# Optional: allow direct CLI testing
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "start":
        git_start()
    elif len(sys.argv) > 1 and sys.argv[1] == "push":
        fname = sys.argv[2] if len(sys.argv) > 2 else None
        br = sys.argv[3] if len(sys.argv) > 3 else None
        git_push(fname, br)
    else:
        print("Usage:\n python gitops.py start\n python gitops.py push [filename] [branch]")
