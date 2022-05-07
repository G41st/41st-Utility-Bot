from pathlib import Path
import linecache

directory = Path.cwd()
userID = "583386313466708035"
path = "merit.txt".format(directory)

# Does not account for searching for userids that equals a credit balance
def function1():
    with open(path, encoding='utf8') as file:
        for i, line in enumerate(file):
            if line.strip() == userID:
                print((linecache.getline(path, i + 2)).strip())
                break

