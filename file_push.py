import os
import subprocess
import git

# Configuration variables
repo_dir = 'C:/Users/hedi.mansouri/Desktop/creat_file_git/BE-SNFLK'  # The local repository path
new_file_name = 'new_file.txt'         # The file you want to create
commit_message = 'Add new_file.txt'    # Commit message
branch_name = 'main'                   # Branch to push the file to
# github_url = 'https://github.com/Med-Hedi-Mansouri/BE-SNFLK.git'
github_url = 'https://Med-Hedi-Mansouri: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@github.com/Med-Hedi-Mansouri/BE-SNFLK.git'  # GitHub repo URL with your token

# Step 1: Create a new file in the repository
file_path = os.path.join(repo_dir, new_file_name)
with open(file_path, 'w') as file:
    file.write('This is a new file.')

# Step 2: Initialize the git repository object
repo = git.Repo(repo_dir)

# Step 3: Add the new file to the staging area
repo.git.add(new_file_name)

# Step 4: Commit the new file
repo.index.commit(commit_message)

# Step 5: Set the remote repository (if not already set)
try:
    origin = repo.remote(name='origin')
except ValueError:
    origin = repo.create_remote('origin', github_url)

# Step 6: Push the changes to the remote repository
origin.push(branch_name)

print(f"File {new_file_name} created, committed, and pushed successfully.")