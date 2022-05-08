from pathlib import Path
import linecache

directory = Path.cwd()
merit_path = "merit.txt".format(directory)
demerit_path = "demerit.txt".format(directory)


def merit_reader(discord_id):
    d_id = str(discord_id)

    with open(merit_path, encoding='utf8') as file:
        for i, line in enumerate(file):
            if line.strip() == d_id:
                merit_total = (linecache.getline(merit_path, i + 2)).strip()
    return merit_total


def demerit_reader(discord_id):
    d_id = str(discord_id)

    with open(demerit_path, encoding='utf8') as file:
        for i, line in enumerate(file):
            if line.strip() == d_id:
                demerit_total = (linecache.getline(demerit_path, i + 2)).strip()
    return demerit_total


def add_credits(discord_id, new_credit_value):
    d_id = str(discord_id)

    print("hello")

    old_merit_value = merit_reader(discord_id)

    new_credit_total = int(old_merit_value) + new_credit_value

    with open(merit_path, encoding='utf8') as file:
        for i, line in enumerate(file):
            if line.strip() == d_id:
                line_to_replace = i + 1

    with open(merit_path, "r") as f:
        content = f.readlines()
        content[line_to_replace] = str(new_credit_total) + "\n"

        with open(merit_path, "w") as f:
            f.writelines(content)

            return new_credit_value


def remove_credits(discord_id, new_credit_value):
    d_id = str(discord_id)

    print("hello")

    old_demerit_value = demerit_reader(discord_id)

    new_credit_total = int(old_demerit_value) + new_credit_value

    with open(merit_path, encoding='utf8') as file:
        for i, line in enumerate(file):
            if line.strip() == d_id:
                line_to_replace = i + 1

    with open(demerit_path, "r") as f:
        content = f.readlines()
        content[line_to_replace] = str(new_credit_total) + "\n"

        with open(demerit_path, "w") as f:
            f.writelines(content)

            return new_credit_value


def subtract_merits(discord_id, new_credit_value):
    d_id = str(discord_id)

    print("hello")

    old_merit_value = merit_reader(discord_id)

    new_credit_total = int(old_merit_value) - new_credit_value

    with open(merit_path, encoding='utf8') as file:
        for i, line in enumerate(file):
            if line.strip() == d_id:
                line_to_replace = i + 1

    with open(merit_path, "r") as f:
        content = f.readlines()
        content[line_to_replace] = str(new_credit_total) + "\n"

        with open(merit_path, "w") as f:
            f.writelines(content)

            return new_credit_value


def subtract_demerits(discord_id, new_credit_value):
    d_id = str(discord_id)

    print("hello")

    old_demerit_value = demerit_reader(discord_id)

    new_credit_total = int(old_demerit_value) - new_credit_value

    with open(merit_path, encoding='utf8') as file:
        for i, line in enumerate(file):
            if line.strip() == d_id:
                line_to_replace = i + 1

    with open(demerit_path, "r") as f:
        content = f.readlines()
        content[line_to_replace] = str(new_credit_total) + "\n"

        with open(demerit_path, "w") as f:
            f.writelines(content)

            return new_credit_value
