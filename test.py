def bruh():

    d_id = "583386313466708035"

    with open("merit.txt", 'r') as f:
        for number, line in enumerate(f):
            if d_id in line:
                line_number = number

                with open("merit.txt", 'r') as f:
                    file_read = f.readlines()
                    file_int1_read = int(line_number)
                    file_int2_read = (file_int1_read + 1)
                    file_to_read = file_read[file_int2_read]
                    file_to_read_stripped = file_to_read.strip()
                    print(file_to_read_stripped)
                    merit_total = int(file_to_read_stripped)

                    print(merit_total)


bruh()
