import git

repo_dir = 'my_new_repo'
repo = git.Repo.init(repo_dir)

# List all branches
for branch in repo.branches:
    print(branch)

# Will create empty main.py within your repo directory
open(f'{repo_dir}/main.py', 'wb').close
# Provide a list of the files to stage
repo.index.add(['main.py'])
# Provide a commit message
repo.index.commit('Initial commit')