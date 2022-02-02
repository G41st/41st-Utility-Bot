with open("merit.txt", 'r') as f:
    get_all = f.readlines()

    for number, line in enumerate(f):

        if d_id in line:
            line_number = number

with open("merit.txt", 'w') as f:
    for i, line in enumerate(get_all):
        if i == int(item_number):
            f.writelines(str(new_item_total_sold) + "\n")
        else:
            f.writelines(line)