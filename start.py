import os
import sys
import time
import git_push
import git_pull

sys.path.insert(0, f'{os.getcwd()}/41st-bot')

from launcher import launch


git_pull.download1("merit.txt")
git_pull.download2("demerit.txt")


start_time = time.time()
seconds = 86400

import datetime
now = datetime.datetime.now()

print(now.year, now.month, now.day, now.hour, now.minute, now.second)
# 2015 5 6 8 53 40


while True:
    now = datetime.datetime.now()
    launch()

    if 23 >= now.hour:
        if 59 >= now.minute:
            break



git_push.upload("merit.txt", "merit.txt", "main")
git_push.upload("demerit.txt", "demerit.txt", "main")

