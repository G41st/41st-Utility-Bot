def store_command(mention, credit_emoji,  str_n):
    description = (f"<@!{mention}>\n\n"
                   f"Please use the extended command `.store-#` to view all the items in each price category. "
                   f"Here is a key:\n"
                   f"{credit_emoji} `7,500` - `.store-1` \n"
                   f"{credit_emoji} `10,000` - `.store-2` \n"
                   f"{credit_emoji} `12,500` - `.store3` \n"
                   f"{credit_emoji} `15,000` - `.store4` \n"
                   f"{credit_emoji} `20,000` - `.store5` \n"
                   f"{credit_emoji} `25,000` - `.store6` \n"
                   f"{credit_emoji} `30,000` - `.store7` \n"
                   f"{credit_emoji} `40,000` - `.store8` \n"
                   f"{credit_emoji} `45,000` - `.store9` \n"
                   f"{credit_emoji} `ALL` - `.store-all`")

    store = f"**41st Elite Corps store:** <@!{mention}> \n"

    store1 = (f"\n- - - {credit_emoji} `7,500` - - -\n"
              f"{credit_emoji} `7,500` - 'Helmet Attachments' \n- Choose from one of our pre-existing helmet attachment"
              f" options. These options currently include: Flashlights, Antennas, Communicators, and the Heavy "
              f"Sunvisor.\n"
              f"{credit_emoji} `7,500` - 'Rangefinder Down' \n- A Rangefinder lowered over the eyes. (For SGT+ only.)\n"
              f"{credit_emoji} `7,500` - 'Helmet Tubes/Pipes' \n- A tube for the base class pilot helmets. "
              f"(Naval helmets only.)\n")

    store2 = (f"\n- - - {credit_emoji} `10,000` - - -\n"
              f"{credit_emoji} `10,000` - '*Build-Your-Own* Attachment' \n- A custom attachment brainstormed by you, "
              f"built by the Art Team Leads. NOTE: Your attachment can not resemble other attachments, "
              f"such as a rangefinder.\n"
              f"{credit_emoji} `10,000` - 'Specialist Binoculars' \n- Allows for binoculars to be added to your helmet."
              f"NOTE: Not all helmets are compatible.\n"
              f"{credit_emoji} `10,000` - 'Specialist Binoculars Up' \n- Allows for raised binoculars. "
              f"NOTE: You must already have access to the binoculars.\n"
              f"{credit_emoji} `10,000` - 'Phase 2 Arc Trooper' \n- Access to a Phase 2 ARC helmet. (For ARC only.)\n")

    store3 =  (f"\n- - - {credit_emoji} `12,500` - - -\n"
              f"{credit_emoji} `12,500` - 'Phase 1 Clone In-Game Skin' \n- Allows for a trooper to use Phase 1 variants "
              f"of the 41st skins. (Not applicable to ARC's)")

    store4 = (f"\n- - - {credit_emoji} `15,000` - - -\n"
              f"{credit_emoji} `15,000` - 'Clone Gunner Helmet' \n- A new helmet template. Google 'Clone Heavy Gunner' "
              f"for reference.\n"
              f"{credit_emoji} `15,000` - 'Flight Computer/Targeting Visor' \n- An external holographic visor. "
              f"(The Flight Computer is only available to ACE pilots of SGT+. The Targeting visor is only "
              f"available to Spec Ops helmets (Strike Cadre Helmet).)\n")

    store5 = (f"\n- - - {credit_emoji} `20,000` - - -\n"
              f"{credit_emoji} `20,000` - 'Phase 1 Helmet' \n- A Phase 1 helmet.\n"
              f"{credit_emoji} `20,000` - 'BARC Helmet' \n- For the mysterious types.\n"
              f"{credit_emoji} `20,000` - 'Hooded Helmet' \n- Stylish and Sneaky. (Only for Shadow Cadre and SOF.)\n"
              f"{credit_emoji} `20,000` - 'Phase 1 ARF Helmet' \n- The ARF Helmet from 'Star Wars The Clone Wars'.\n")

    store6 = (f"\n- - - {credit_emoji} `25,000` - - -\n"
              f"{credit_emoji} `25,000` - 'Snowtrooper/Flametrooper Helmet' \n- BRING IN THE FLAMETHROWERS!\n")

    store7 = (f"\n- - - {credit_emoji} `30,000` - - -\n"
              f"{credit_emoji} `30,000` - 'Custom Visor' \n- Clearence to a one color visor. NOTE: Troopers may get a "
              f"refund apon reaching the rank of 2LT or higher, or RC.\n")

    store8 = (f"\n- - - {credit_emoji} `40,000` - - -\n"
              f"{credit_emoji} `40,000` - '2003 Helmet Varients' \n- The classic style. Avalible for all helmet "
              f"templates.\n")

    store9 = (f"\n- - - {credit_emoji} `45,000` - - -\n"
              f"{credit_emoji} `45,000` - 'Blaze Trooper Helmet' \n- 'Need a light?' NOTE: Google Clone Blaze Trooper "
              f"for a reference.\n"
              f"{credit_emoji} `45,000` - 'Desert Trooper Helmet' \n- 'I hate sand.' NOTE: Google Clone Desert Trooper "
              f"for a reference.\n")

    if str_n == 0:
        return store
    elif str_n == 1:
        return store1
    elif str_n == 2:
        return store2
    elif str_n == 3:
        return store3
    elif str_n == 4:
        return store4
    elif str_n == 5:
        return store5
    elif str_n == 6:
        return store6
    elif str_n == 7:
        return store7
    elif str_n == 8:
        return store8
    elif str_n == 9:
        return store9
    elif str_n == 69:
        return description


def shop_command(mention):
    credit_emoji = '<:credits:937788738950545464>'

    shop = (f"**41st Elite Corps Store:** <@!{mention}> \n"
            f"{credit_emoji} `7,500` - 'Helmet Attachments' \n"
            f"{credit_emoji} `7,500` - 'Rangefinder Down' \n"
            f"{credit_emoji} `7,500` - 'Helmet Tubes/Pipes' \n"
            f"{credit_emoji} `10,000` - '*Build-Your-Own* Attachment' \n"
            f"{credit_emoji} `10,000` - 'Specialist Binoculars' \n"
            f"{credit_emoji} `10,000` - 'Specialist Binoculars Up' \n"
            f"{credit_emoji} `10,000` - 'Phase 2 Arc Trooper' \n"
            f"{credit_emoji} `12,500` - 'Phase 1 Clone In-Game Skin' \n"
            f"{credit_emoji} `15,000` - 'Clone Gunner Helmet' \n"
            f"{credit_emoji} `15,000` - 'Flight Computer/Targeting Visor' \n"
            f"{credit_emoji} `20,000` - 'Phase 1 Helmet' \n"
            f"{credit_emoji} `20,000` - 'BARC Helmet' \n"
            f"{credit_emoji} `20,000` - 'Hooded Helmet' \n"
            f"{credit_emoji} `20,000` - 'Phase 1 ARF Helmet' \n"
            f"{credit_emoji} `25,000` - 'Snowtrooper/Flametrooper Helmet' \n"
            f"{credit_emoji} `30,000` - 'Custom Visor' \n"
            f"{credit_emoji} `40,000` - '2003 Helmet Varients' \n"
            f"{credit_emoji} `45,000` - 'Blaze Trooper Helmet' \n"
            f"{credit_emoji} `45,000` - 'Desert Trooper Helmet' \n")

    return shop


def troll_command():
    troll = ("░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░\n░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░\n░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░\n░░░█░"
             "░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░\n░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░\n█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█\n█░▒█░█▀▄▄"
             "░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█\n░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░\n░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░\n░░░█░░░░██░░▀"
             "█▄▄▄█▄▄█▄████░█░░░\n░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░\n░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░\n░░░░░░░▀▄▄░▒▒▒▒░░"
             "░░░░░░░░▒░░░█░\n░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░\n░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░")

    return troll


def rage():
    rage_paragraph = ("What the fuck did you just fucking say about me, you little bitch? I'll have you know I "
                      "graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on "
                      "Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top "
                      "sniper in the entire US armed forces. You are nothing to me but just another target. I will "
                      "wipe you the fuck out with precision the likes of which has never been seen before on this "
                      "Earth, mark my fucking words. You think you can get away with saying that shit to me over the "
                      "Internet? Think again, fucker. As we speak I am contacting my secret network of spies across "
                      "the USA and your IP is being traced right now so you better prepare for the storm, maggot. The "
                      "storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I "
                      "can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with "
                      "my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the "
                      "entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe "
                      "your miserable ass off the face of the continent, you little shit. If only you could have known "
                      "what unholy retribution your little 'clever' comment was about to bring down upon you, maybe "
                      "you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying "
                      "the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're "
                      "fucking dead, kiddo.")

    return rage_paragraph


def commands_command(mention):
    commands = (f"COMMANDS: - - - <@!{mention}>\n\n"
                f"`.register` - Register yourself in the bots systems. You must use .register before you can use the "
                f"majority of the bots functions. \n"
                f"`.store` - Displays the current store information with categories and item descriptions. \n"
                f"`.shop` - Displays a condensed version of the store. \n"
                f"`.ggn-store` - Displays the current GGN store price approximations, as well as specific items. \n"
                f"`.credits` - Calculates your current credit value. \n"
                f"`.directory` - DM's the user a list of names for various important divisions of the 41st. \n"
                f"`.version` - Displays current bot dev info. \n"
                f"`.github` - Sends the link to the bot's git repository. \n"
                f"`.report` - Sends a user-created error report to the bot dev team.")

    return commands


def report_command(mention):
    report_instructions = (f"<@!{mention}>\n\n"
                           f"To report a bug, please use the `.report-send` command. Please specify anything you think"
                           f"would be useful to help the Dev Team fix this problem.\n"
                           f"(Please do not worry about including your name or using a format, as the bot automaticly "
                           f"collects this data for us.) \nHere is an example report:\n"
                           f"```.report-send I was using the .store command when the text suddenly printed in one line"
                           f"with brackets on the end. I do not belive this is how it is supposed to work. Everything "
                           f"else works fine.```")

    return report_instructions


def ggn_store_command(mention):
    credit_emoji = '<:credits:937788738950545464>'
    store_channel = '<#909593785409896538>'

    ggn_store = (f"**Geetsly's Gaming Network Store Conversions:** <@!{mention}> \n"
                 f"(Please note that these are not prices for credit values. These are credit value conversions, "
                 f"meaning that a store item which is 15,000 credits is purchasable with $10.00 USD.) \n\n"
                 f"{credit_emoji} `7,500` - $`5.00` USD \n"
                 f"{credit_emoji} `10,000` - $`7.50` USD \n"
                 f"{credit_emoji} `12,500` - $`10.00` USD \n"
                 f"{credit_emoji} `15,000` - $`10.00` USD \n"
                 f"{credit_emoji} `20,000` - $`15.00` USD \n"
                 f"{credit_emoji} `25,000` - $`20.00` USD \n"
                 f"{credit_emoji} `30,000` - $`25.00` USD \n"
                 f"{credit_emoji} `40,000` - $`30.00` USD \n"
                 f"{credit_emoji} `45,000` - $`30.00` USD \n\n"
                 f"**EXCEPTIONS/SPECIFICS:** \n"
                 f"'Phase-1 In Game' - $`10.00` USD \n"
                 f"'Custom Visor' - $`15.00` USD \n"
                 f"'2003 Helmet' - $`20.00` USD \n"
                 f"Head to {store_channel} for more information. \n"
                 f"Please remember to DM `'Forceps' CC-3432` for any GGN-Store purchases.")

    return ggn_store


def commands_directory(mention):
    directory = (f"DIRECTORY: - - - <@!{mention}>\n\n\n"
                 f"Owner: `CMDR Forceps CC-3432` \n\n"
                 f"Head of Army: `CMDR Forceps CC-3432` \n\n"
                 f"Head of Navy: `CODR Kyoda CC-4221` \n\n"
                 f"SOF Lead(s): [\n`RSGT Bored RC-7690`, \n`RCPT Florence RC-6424` \n]\n\n"
                 f"Regiment CO's: [\n`MJR Adko CC-1258 - Diamond`, \n`MJR Rancor CC-2599 - Krayt`, \n"
                 f"`CPT AlphaDog CC-4676 - Titan` \n]\n\n"
                 f"Heads of Training: [\n`CMDR Forceps CC-3432 - Army`, \n`FCDR Thor CT-3312 - Navy` \n]\n\n"
                 f"Art Team Lead(s): [\n`QTR Marr CT-4154`, \n`QTR Idaho CT-2289`, \n`RLT Numbers RC-1903` \n]\n\n"
                 f"Logistics Lead(s): [\n`MJR Adko CC-1258`, \n`CPT AlphaDog CC-4676` \n]\n\n"
                 f"Media Team Lead(s): `CPT AlphaDog CC-4676` \n\n"
                 f"Development Team Lead(s): `CODR Kyoda CC-4221` \n\n"
                 f"For any remaining questions, please notify `CMDR Forceps CC-3432` or `CODR Kyoda CC-4221`.")

    return directory


def pings():
    pings = "<@&954526344971157544> <@&922002555192631356> <@&851041781978365962> <@&850843079417659402>"

    return pings
