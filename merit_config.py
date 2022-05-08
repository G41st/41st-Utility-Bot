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

    with open(merit_path, encoding='utf8') as file:
        content = file.readlines()
        for i, line in enumerate(file):
            if line.strip() == d_id:
                current_merit_total = (linecache.getline(merit_path, i + 2)).strip()

                new_credit_total = current_merit_total + new_credit_value

                content[i + 1] = str(new_credit_total) + "\n"

                with open(merit_path, encoding='utf8') as f:
                    f.writelines(content)

        return new_credit_total


def remove_credits(discord_id, new_credit_value):
    d_id = str(discord_id)

    with open("demerit.txt", 'r') as f:
        current_demerit_total = 0

        for number, line in enumerate(f):
            if d_id in line:
                line_number = number

                with open("demerit.txt", 'r') as f:
                    file_read = f.readlines()
                    file_int1_read = int(line_number)
                    file_int2_read = (file_int1_read + 1)
                    file_to_read = file_read[file_int2_read]
                    file_to_read_stripped = file_to_read.strip()
                    current_demerit_total = int(file_to_read_stripped)

            if d_id not in line:
                pass

    new_credit_total = current_demerit_total + new_credit_value

    with open("demerit.txt", "r") as f:
        content = f.readlines()
        content[file_int2_read] = str(new_credit_total) + "\n"

        with open("demerit.txt", "w") as f:
            f.writelines(content)

            return new_credit_value


def subtract_merits(discord_id, new_credit_value):
    d_id = str(discord_id)

    with open("merit.txt", 'r') as f:
        current_merit_total = 0

        for number, line in enumerate(f):
            if d_id in line:
                line_number = number

                with open("merit.txt", 'r') as f:
                    file_read = f.readlines()
                    file_int1_read = int(line_number)
                    file_int2_read = (file_int1_read + 1)
                    file_to_read = file_read[file_int2_read]
                    file_to_read_stripped = file_to_read.strip()
                    current_merit_total = int(file_to_read_stripped)

            if d_id not in line:
                pass

    new_credit_total = current_merit_total - new_credit_value

    with open("merit.txt", "r") as f:
        content = f.readlines()
        content[file_int2_read] = str(new_credit_total) + "\n"

        with open("merit.txt", "w") as f:
            f.writelines(content)

            return new_credit_value


def subtract_demerits(discord_id, new_credit_value):
    d_id = str(discord_id)

    with open("demerit.txt", 'r') as f:
        current_demerit_total = 0

        for number, line in enumerate(f):
            if d_id in line:
                line_number = number

                with open("demerit.txt", 'r') as f:
                    file_read = f.readlines()
                    file_int1_read = int(line_number)
                    file_int2_read = (file_int1_read + 1)
                    file_to_read = file_read[file_int2_read]
                    file_to_read_stripped = file_to_read.strip()
                    current_demerit_total = int(file_to_read_stripped)

            if d_id not in line:
                pass

    new_credit_total = current_demerit_total - new_credit_value

    with open("demerit.txt", "r") as f:
        content = f.readlines()
        content[file_int2_read] = str(new_credit_total) + "\n"

        with open("demerit.txt", "w") as f:
            f.writelines(content)

            return new_credit_value
