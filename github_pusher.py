#!/usr/bin/env python3
"""
GITHUB PUSHER - Automated File Deployment to GitHub Repos
Push local files to any GitHub repository with one command
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path
from dotenv import load_dotenv
import git
from github import Github

load_dotenv()

class GitHubPusher:
    def __init__(self):
        self.token = os.getenv('GITHUB_TOKEN')
        self.username = os.getenv('USERNAME', 'mukulkk07')
        self.local_path = os.getenv('LOCAL_REPO_PATH')
        self.g = Github(self.token)
        
    def push_file(self, repo_name, file_path, branch='main', commit_message='Update file via GitHubPusher'):
        """Push single file to GitHub repo"""
        try:
            repo = self.g.get_user().get_repo(repo_name)
            branch_obj = repo.get_branch(branch)
            
            # Read file content
            content = Path(file_path).read_text()
            
            # Create or update file
            try:
                file_obj = repo.get_contents(file_path, ref=branch)
                repo.update_file(
                    path=file_path,
                    message=commit_message,
                    content=content,
                    sha=file_obj.sha,
                    branch=branch
                )
            except:
                repo.create_file(
                    path=file_path,
                    message=commit_message,
                    content=content,
                    branch=branch
                )
            
            print(f"✅ Pushed {file_path} to {repo_name}")
            return True
            
        except Exception as e:
            print(f"❌ Error pushing to {repo_name}: {e}")
            return False
    
    def push_dir(self, repo_name, dir_path, branch='main'):
        """Push entire directory"""
        repo = self.g.get_user().get_repo(repo_name)
        count = 0
        
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.py'):  # Only Python files
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.local_path)
                    self.push_file(repo_name, rel_path, branch)
                    count += 1
        
        print(f"✅ Pushed {count} files from {dir_path}")
        return count

def main():
    parser = argparse.ArgumentParser(description="GitHub Pusher - Deploy files to GitHub")
    parser.add_argument('--repo', required=True, help="Target repo (e.g. mukulkk07/my-repo)")
    parser.add_argument('--file', help="Single file to push")
    parser.add_argument('--dir', help="Directory to push")
    parser.add_argument('--branch', default='main', help="Target branch")
    parser.add_argument('--message', default='Update via GitHubPusher', help="Commit message")
    
    args = parser.parse_args()
    
    pusher = GitHubPusher()
    
    if args.file:
        pusher.push_file(args.repo, args.file, args.branch, args.message)
    elif args.dir:
        pusher.push_dir(args.repo, args.dir, args.branch)
    else:
        print("❌ Use --file or --dir")
        sys.exit(1)

if __name__ == "__main__":
    main()
