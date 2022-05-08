from pathlib import Path
import linecache

directory = Path.cwd()
merit_path = "merit.txt".format(directory)
demerit_path = "demerit.txt".format(directory)

print(merit_path)


def add_credits(discord_id, new_credit_value):
    d_id = str(discord_id)

    with open(merit_path, encoding='utf8') as file:
        content = file.readlines()
        for i, line in enumerate(file):
            if d_id in line.strip():
                current_merit_total = (linecache.getline(merit_path, i + 2)).strip()

                new_credit_total = current_merit_total + new_credit_value

                content[i + 1] = str(new_credit_total) + "\n"

                with open(merit_path, encoding='utf8') as f:
                    f.writelines(content)

                print(merit_path)
                print(current_merit_total)
                print(content[i + 1])


add_credits(583386313466708035, 1)
