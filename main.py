import git


repo = git.Repo.init('my_new_repo')

# List all branches
for branch in repo.branches:
    print(branch)


# Provide a list of the files to stage
repo.index.add(['main.py'])
# Provide a commit message
repo.index.commit('Initial commit')