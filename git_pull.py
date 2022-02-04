import os
from git.repo.base import Repo
import shutil
import time

def download(filename):
    cwd = os.getcwd()

    try:
        shutil.rmtree(f"{cwd}/41st-bot", ignore_errors=False, onerror=None)

        Repo.clone_from("https://github.com/G41st-Bot/41st-utility-bot", f"{cwd}/41st-bot")

        os.remove(filename)

        shutil.copy(f"{cwd}/41st-bot/{filename}", f"{cwd}")

        os.remove(f"41st-bot/{filename}")

        time.sleep(10)

    except FileNotFoundError:
        Repo.clone_from("https://github.com/G41st-Bot/41st-utility-bot", f"{cwd}/41st-bot")

        os.remove(filename)

        shutil.copy(f"{cwd}/41st-bot/{filename}", f"{cwd}")

        os.remove(f"41st-bot/{filename}")

        time.sleep(10)
