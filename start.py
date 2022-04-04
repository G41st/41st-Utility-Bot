import os
import sys
import git_pull

sys.path.insert(0, f'{os.getcwd()}/41st-bot')

import launcher

git_pull.download1("merit.txt")
print("downloaded merit.txt")
git_pull.download2("demerit.txt")
print("downloaded demerit.txt")
git_pull.download3("registry.txt")
print("downloaded registry.txt")
git_pull.download4("reports.txt")
print("downloaded reports.txt")
git_pull.download5("announcement.txt")
print("downloaded announcement.txt")

os.remove(f"41st-bot/git_pull.py")
os.remove(f"41st-bot/git_push.py")


def start():
    launcher.launch()


start()
