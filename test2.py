from pathlib import Path
import linecache

directory = Path.cwd()
merit_path = "merit.txt"
demerit_path = "demerit.txt"


def merit_reader(discord_id):
    d_id = str(discord_id)

    with open(merit_path, encoding='utf8') as file:
        for i, line in enumerate(file):
            if line.strip() == d_id:
                merit_total = (linecache.getline(merit_path, i + 2)).strip()
                print(i)
    return merit_total


print(merit_path)


