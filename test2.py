
with open("troll.txt", "r") as troll_file:
    content = troll_file.readlines()

    old_cc_number = content[0]


    with open("troll.txt", "w") as troll_file:
        int_cc_number = int(old_cc_number[0])
        new_cc_number = int_cc_number + 1

        content[0] = str(new_cc_number) + "\n"

        troll_file.writelines(content)