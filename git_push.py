import base64
import os
from github import Github
from github import InputGitTreeElement

with open("git_key.txt", "r") as f:
    git_key = f.read()


def upload():
    user = "G41st"
    password = f"{git_key}"
    g = Github(user, password)
    repo = g.get_user().get_repo('41st-Utility-Bot')
    file_list = [
        f"/home/container/merit.txt",
        f"/home/container/demerit.txt",
        f"/home/container/registry.txt",
        f"/home/container/reports.txt",
        f"/home/container/announcement.txt"
    ]
    file_names = [
        'merit.txt',
        'demerit.txt',
        'registry.txt',
        'reports.txt',
        'announcement.txt'
    ]
    commit_message = 'syncing files'
    master_ref = repo.get_git_ref('heads/main')
    master_sha = master_ref.object.sha
    base_tree = repo.get_git_tree(master_sha)

    element_list = list()
    for i, entry in enumerate(file_list):
        with open(entry) as input_file:
            data = input_file.read()
        if entry.endswith('.png'):  # images must be encoded
            data = base64.b64encode(data)
        element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
        element_list.append(element)

    tree = repo.create_git_tree(element_list, base_tree)
    parent = repo.get_git_commit(master_sha)
    commit = repo.create_git_commit(commit_message, tree, [parent])
    master_ref.edit(commit.sha)
