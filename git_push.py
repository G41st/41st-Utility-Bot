import os
from github import Github
import time

g = Github("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")


def upload(localfilename, gitfilename, gitbranch):
    repo = '41st-utility-bot'

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
        repo.update_file(contents.path, f"sync {localfilename}", content, contents.sha, branch=f"{gitbranch}")
        print(git_file + ' UPDATED')
        time.sleep(5)
        return 'Updated'
    else:
        repo.create_file(git_file, f"sync {localfilename}", content, branch=f"{gitbranch}")
        print(git_file + ' CREATED')
        time.sleep(5)
        return 'Created'
