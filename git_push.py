import os
from github import Github

g = Github("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")


def upload(repo, localfilename, gitfilename, gitbranch):
    repo = g.get_user().get_repo(str(repo))
    all_files = []
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

    cwd = os.getcwd()
    with open(f'{cwd}/{localfilename}', 'r') as file:
        content = file.read()

    git_file = f'{gitfilename}'
    if git_file in all_files:
        contents = repo.get_contents(git_file)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch=f"{gitbranch}")
        print(git_file + ' UPDATED')
        return 'Updated'
    else:
        repo.create_file(git_file, "committing files", content, branch=f"{gitbranch}")
        print(git_file + ' CREATED')
        return 'Created'
