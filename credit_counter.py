global merit_total
global demerit_total
global role_total
global merit_sum


def credit_counter(role_names, discord_id):
    d_id = str(discord_id)

    global count1
    count1 = 0
    global count2
    count2 = 0
    global count3
    count3 = 0
    global count4
    count4 = 0
    global count5
    count5 = 0
    global count6
    count6 = 0

    medal1 = 'Medal of Valor'
    medal2 = 'Cadet Master'
    medal3 = 'Mythical Instructor'
    medal4 = 'Legendary Instructor'
    medal5 = 'Hero of The 41st'
    medal6 = 'Absolutely Demolished'

    try:
        if any(ext in medal1 for ext in role_names):
            count1 = 20000
        if any(ext in medal2 for ext in role_names):
            count2 = 3000
        if any(ext in medal3 for ext in role_names):
            count3 = 3000
        if any(ext in medal4 for ext in role_names):
            count4 = 3000
        if any(ext in medal5 for ext in role_names):
            count5 = 2500
        if any(ext in medal6 for ext in role_names):
            count6 = 2000

        role_total = count1 + count2 + count3 + count4 + count5 + count6

        with open("merit.txt", 'r') as f:

            for number, line in enumerate(f):
                if d_id not in line:
                    merit_total = 0
                if d_id in line:
                    line_number = number

                    with open("merit.txt", 'r') as f:
                        file_read = f.readlines()
                        file_int1_read = int(line_number)
                        file_int2_read = (file_int1_read + 1)
                        file_to_read = file_read[file_int2_read]
                        file_to_read_stripped = file_to_read.strip()
                        merit_total = int(file_to_read_stripped)

                        with open("demerit.txt", 'r') as f:
                            for number, line in enumerate(f):
                                if d_id not in line:
                                    demerit_total = 0
                                if d_id in line:
                                    line_number = number

                                    with open("demerit.txt", 'r') as f:
                                        file_read = f.readlines()
                                        file_int1_read = int(line_number)
                                        file_int2_read = (file_int1_read + 1)
                                        file_to_read = file_read[file_int2_read]
                                        file_to_read_stripped = file_to_read.strip()
                                        demerit_total = int(file_to_read_stripped)

                                        merit_sum = role_total + merit_total
                                        total = merit_sum - demerit_total

        return total
    except UnboundLocalError:
        return False

