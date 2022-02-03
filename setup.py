import sys
import time


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)


def instalation_check():
    setup_file = open("setup.txt", "w")
    setup_file.write("setup completion = false \n")
    setup_file.write("\n Version 0.1")
    setup_file.close()


def log_creation():
    setup_log = open("setup_log.txt", "w")
    setup_log.write("logging setup at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()


def merit_file_setup():
    merit_file = open("merit.txt", "w")
    merit_file.write("file test")
    merit_file.close()

    merit_file = open("merit.txt")
    content = merit_file.read()

    if content == "file test":
        merit_file.close()
        print("merit file created succesfuly")
        merit_file = open("merit.txt", "w")
        merit_file.write("merits:\n")
        merit_file.close()
        demerit_file_complete()
    else:
        demerit_setup_err()


def merit_file_complete():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("merit text file created succesfully at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)


def merit_setup_err():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("merit text file failed at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)

    attempt_number = +1

    print("setup has failed")
    print(attempt_number)
    print("time(s). retrying in 5 seconds")
    time.sleep(5)
    merit_file_setup()

    if attempt_number > 3:
        print("Setup has failed more than 3 times; exiting program")
        time.sleep(5)
        sys.exit()
    else:
        pass


def demerit_file_setup():
    demerit_file = open("demerit.txt", "w")
    demerit_file.write("file test")
    demerit_file.close()

    demerit_file = open("demerit.txt")
    content = demerit_file.read()

    if content == "file test":
        demerit_file.close()
        print("demerit file created succesfuly")
        demerit_file = open("demerit.txt", "w")
        demerit_file.write("demerits:\n")
        demerit_file.close()
        demerit_file_complete()
    else:
        demerit_setup_err()


def demerit_file_complete():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("demerit text file created succesfully at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)


def demerit_setup_err():
    setup_log = open("setup_log.txt", "a")
    setup_log.write("demerit text file creation failed at:")
    setup_log.write(current_time)
    setup_log.write("\n")
    setup_log.close()

    time.sleep(1)

    attempt_number = +1

    print("setup has failed")
    print(attempt_number)
    print("time(s). retrying in 5 seconds")
    time.sleep(5)
    demerit_file_setup()

    if attempt_number > 3:
        print("Setup has failed more than 3 times; exiting program")
        time.sleep(5)
        sys.exit()
    else:
        pass


def setup():
    instalation_check()
    log_creation()
    merit_file_setup()
    demerit_file_setup()

    setup_file = open("setup.txt", "w")
    setup_file.write("setup completion = \n true")
    setup_file.write("\n Version 0.1")
    print("setup complete! starting full aplication...")
    time.sleep(5)

    return True
