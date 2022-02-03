def add_credits(discord_id, new_credit_value):
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

    print(current_merit_total)

    new_credit_total = current_merit_total + new_credit_value

    with open("merit.txt", "r") as f:
        content = f.readlines()
        content[file_int2_read] = str(new_credit_total)


        print(content)

        with open("merit.txt", "w") as f:
            f.writelines(content)

            return new_credit_value

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

    print(current_demerit_total)

    new_credit_total = current_demerit_total + new_credit_value
    replacement = ""

    with open("demerit.txt", "r") as f:

        for line in f:
            line = line.strip()
            changes = line.replace(str(current_demerit_total), str(new_credit_total))
            replacement = replacement + changes + "\n"

    with open("demerit.txt", "w") as f:
        f.write(replacement)

    return new_credit_value
