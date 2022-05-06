import datetime

now = datetime.datetime.now()


def register(user_id, author_display_name):
    with open("registry.txt", 'r') as f:
        line = f.read()
        if user_id in line:
            print(f"{author_display_name} - {user_id} \nis in registry.txt")
            with open("merit.txt", 'r') as f:
                line = f.read()
                if user_id in line:
                    print(f"{author_display_name} - {user_id} \nis in merit.txt")
                    with open("demerit.txt", 'r') as f:
                        line = f.read()
                        if user_id in line:
                            # in all three
                            # 01
                            print(f"{author_display_name} - {user_id} \nis in demerit.txt")
                            print(f"{author_display_name} - {user_id} \nis registered with 0 errors")
                            return "00"
                        if user_id not in line:
                            # in registry, in merit, not demerit
                            # 01
                            print(f"{author_display_name} - {user_id} \nis not in demerit.txt")
                            print(f"{author_display_name} - {user_id} \nis registered with 1 error")
                            return "01"
                if user_id not in line:
                    print(f"{author_display_name} - {user_id} \nis not in merit.txt")
                    with open("demerit.txt", 'r') as f:
                        line = f.read()
                        if user_id in line:
                            # in registry, not merit, in demerit
                            # 02
                            print(f"{author_display_name} - {user_id} \nis in demerit.txt")
                            print(f"{author_display_name} - {user_id} \nis registered with 1 error")
                            return "02"
                        if user_id not in line:
                            # in registry, not merit, not demerit
                            # 03
                            print(f"{author_display_name} - {user_id} \nis not in demerit.txt")
                            print(f"{author_display_name} - {user_id} \nis registered with 2 errors")
                            return "03"
        if user_id not in line:
            print(f"{author_display_name} - {user_id} \nis not in registry.txt")
            with open("merit.txt", 'r') as f:
                line = f.read()
                if user_id in line:
                    print(f"{author_display_name} - {user_id} \nis in merit.txt")
                    with open("demerit.txt", 'r') as f:
                        line = f.read()
                        if user_id in line:
                            # not registry, in merit, in demerit
                            # 04
                            print(f"{author_display_name} - {user_id} \nis in in demerit.txt")
                            print(f"{author_display_name} - {user_id} \nis registered with 2 errors")
                            return "04"
                        if user_id not in line:
                            # not registry, in merit, not demerit
                            # 05
                            print(f"{author_display_name} - {user_id} \nis not in demerit.txt")
                            print(f"{author_display_name} - {user_id} \nis registered with 1 error")
                            return "05"
                if user_id not in line:
                    print(f"{author_display_name} - {user_id} \nis not in merit.txt")
                    with open("demerit.txt", 'r') as f:
                        line = f.read()
                        if user_id in line:
                            # not registry, not merit, in demerit
                            # 06
                            print(f"{author_display_name} - {user_id} \nis in demerit.txt")
                            print(f"{author_display_name} - {user_id} \nis registered with 1 error")
                            return "06"
                        if user_id not in line:
                            # not registered
                            # 07
                            print(f"{author_display_name} - {user_id} \nis not in demerit.txt")
                            print(f"{author_display_name} - {user_id} \nis not registered")
                            with open("registry.txt", 'a') as f:
                                f.write(user_id + '\n')
                                print(
                                    f"{author_display_name} - {user_id} \nhas been added to registry.txt")
                            with open("merit.txt", 'a') as f:
                                f.write(user_id + '\n' + '0\n')
                                print(f"{author_display_name} - {user_id} \nhas been added to merit.txt")
                            with open("demerit.txt", 'a') as f:
                                f.write(user_id + '\n' + '0\n')
                                print(f"{author_display_name} - {user_id} \nhas been added to registry.txt")
                            print(
                                f"{author_display_name} - {user_id} \nhas been registered with 0 errors")
                            return "07"


def channel_reply(str_n, mention):
    reply_00 = (f"Registry integrity check for {mention} passed with `0` errors. \n"
                f"(You are already in the registry)")
    reply_01 = (f"`ERROR` - - - {mention}\n"
                f"Registry integrity check for {mention} failed with `1` error. "
                f"[ MERIT.txt ]\nPlease do not use .report, an error report has been "
                f"automatically generated.")
    reply_02 = (f"`ERROR` - - - {mention}\n"
                f"Registry integrity check for {mention} failed with `1` error. "
                f"[ DEMERIT.txt ]\nPlease do not use .report, an error report has been "
                f"automatically generated.")
    reply_03 = (f"`ERROR` - - - {mention}\n"
                f"Registry integrity check for {mention} failed with `2` errors. "
                f"[ MERIT.txt ], [ DEMERIT.txt ]\nPlease do not use .report, an error "
                f"report has been automatically generated.")
    reply_04 = (f"`ERROR` - - - {mention}\n"
                f"Registry integrity check for {mention} failed with `2` errors. "
                f"[ MERIT.txt ], [ DEMERIT.txt ]\nPlease do not use .report, an error "
                f"report has been automatically generated.")
    reply_05 = (f"`ERROR` - - - {mention}\n"
                f"Registry integrity check for {mention} failed with `1` error. "
                f"[ MERIT.txt ]\nPlease do not use .report, an error report has been "
                f"automatically generated.")
    reply_06 = (f"`ERROR` - - - {mention}\n"
                f"Registry integrity check for {mention} failed with `1` error. "
                f"[ DEMERIT.txt ]\nPlease do not use .report, an error report has been "
                f"automatically generated.")
    reply_07 = f"{mention} has been added to the registry with `0` errors."

    if str_n == "00":
        return reply_00
    if str_n == "01":
        return reply_01
    if str_n == "02":
        return reply_02
    if str_n == "03":
        return reply_03
    if str_n == "04":
        return reply_04
    if str_n == "05":
        return reply_05
    if str_n == "06":
        return reply_06
    if str_n == "07":
        return reply_07


def report_message(str_n, user_id, author_display_name, message_channel):
    message_01 = (f"@here \n\n"
                  f"`{author_display_name} - {user_id}`\n"
                  f"`{now.month}/{now.day}/{now.year}` in channel "
                  f"'#{message_channel}'\n{author_display_name} "
                  f"reported a malfunction in the file: [ MERIT.TXT ].\n"
                  f"Specifics: `The user id was detected in registry.txt as "
                  f"well as demerit.txt but was not detected in merit.txt.`")
    message_02 = (f"@here \n\n"
                  f"`{author_display_name} - {user_id}`\n"
                  f"`{now.month}/{now.day}/{now.year}` in channel "
                  f"'#{message_channel}'\n{author_display_name} "
                  f"reported a malfunction in the file: [ DEMERIT.TXT ].\n"
                  f"Specifics: `The user id was detected in registry.txt as "
                  f"well as demerit.txt but was not detected in merit.txt.`")
    message_03 = (f"@here \n\n"
                  f"`{author_display_name} - {user_id}`\n"
                  f"`{now.month}/{now.day}/{now.year}` in channel "
                  f"'#{message_channel}'\n{author_display_name} "
                  f"reported a malfunction in the file: [ MERIT.TXT ], [ DEMERIT.TXT ].\n"
                  f"Specifics: `The user id was detected in registry.txt, "
                  f"but was not detected in merit.txt. or demerit.txt.`")
    message_04 = (f"@here \n\n"
                  f"`{author_display_name} - {user_id}`\n"
                  f"`{now.month}/{now.day}/{now.year}` in channel "
                  f"'#{message_channel}'\n{author_display_name} "
                  f"reported a malfunction in the file: [ MERIT.TXT ].\n"
                  f"Specifics: `The user id was not detected in registry.txt, "
                  f"but was detected in merit.txt. and demerit.txt.`")
    message_05 = (f"@here \n\n"
                  f"`{author_display_name} - {user_id}`\n"
                  f"`{now.month}/{now.day}/{now.year}` in channel "
                  f"'#{message_channel}'\n{author_display_name} "
                  f"reported a malfunction in the file: [ MERIT.TXT ].\n"
                  f"Specifics: `The user id was not detected in registry.txt as "
                  f"well as demerit.txt but was detected in merit.txt.`")
    message_06 = (f"@here \n\n"
                  f"`{author_display_name} - {user_id}`\n"
                  f"`{now.month}/{now.day}/{now.year}` in channel "
                  f"'#{message_channel}'\n{author_display_name} "
                  f"reported a malfunction in the file: [ DEMERIT.TXT ].\n"
                  f"Specifics: `The user id was not detected in registry.txt as "
                  f"well as merit.txt but was detected in demerit.txt.`")

    if str_n == "01":
        return message_01
    if str_n == "02":
        return message_02
    if str_n == "03":
        return message_03
    if str_n == "04":
        return message_04
    if str_n == "05":
        return message_05
    if str_n == "06":
        return message_06


def report_log(str_n, user_id, author_display_name, message_channel):
    log_01 = (f"{author_display_name} - {user_id}\n"
              f"{now.month}/{now.day}/{now.year} in channel "
              f"'#{message_channel}' \n{author_display_name} "
              f"reported a malfunction in the file: [ MERIT.TXT ].\n"
              f"Specifics: The user id was detected in registry.txt as "
              f"well as demerit.txt but was not detected in merit.txt.")
    log_02 = (f"{author_display_name} - {user_id}\n"
              f"{now.month}/{now.day}/{now.year} in channel "
              f"'#{message_channel}' \n{author_display_name} "
              f"reported a malfunction in the file: [ DEMERIT.TXT ].\n"
              f"Specifics: The user id was detected in registry.txt as "
              f"well as demerit.txt but was not detected in merit.txt.")
    log_03 = (f"{author_display_name} - {user_id}\n"
              f"{now.month}/{now.day}/{now.year} in channel "
              f"'#{message_channel}' \n{author_display_name} "
              f"reported a malfunction in the file: [ MERIT.TXT ].\n"
              f"Specifics: The user id was detected in registry.txt, "
              f"but was not detected in merit.txt. or demerit.txt.")
    log_04 = (f"{author_display_name} - {user_id}\n"
              f"{now.month}/{now.day}/{now.year} in channel "
              f"'#{message_channel}' \n{author_display_name} "
              f"reported a malfunction in the file: [ MERIT.TXT ].\n"
              f"Specifics: The user id was not detected in registry.txt, "
              f"but was detected in merit.txt. and demerit.txt.")
    log_05 = (f"{author_display_name} - {user_id}\n"
              f"{now.month}/{now.day}/{now.year} in channel "
              f"'#{message_channel}' \n{author_display_name} "
              f"reported a malfunction in the file: [ MERIT.TXT ].\n"
              f"Specifics: The user id was not detected in registry.txt as "
              f"well as demerit.txt but was detected in merit.txt.")
    log_06 = (f"{author_display_name} - {user_id}\n"
              f"{now.month}/{now.day}/{now.year} in channel "
              f"'#{message_channel}' \n{author_display_name} "
              f"reported a malfunction in the file: [ DEMERIT.TXT ].\n"
              f"Specifics: The user id was not detected in registry.txt as "
              f"well as merit.txt but was detected in demerit.txt.")

    if str_n == "01":
        return log_01
    if str_n == "02":
        return log_02
    if str_n == "03":
        return log_03
    if str_n == "04":
        return log_04
    if str_n == "05":
        return log_05
    if str_n == "06":
        return log_06
