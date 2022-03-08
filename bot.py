import os
import sys
import time
import datetime

import discord

import assets
import credit_counter
from discord.ext import commands
import discord.ext.commands
from dotenv import load_dotenv

import git_push
import merit_config

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN_TEST = os.getenv('DISCORD_TOKEN_TEST')
GUILD = os.getenv('DISCORD_GUILD')
KYODA_ID = 583386313466708035
FORCEPS_ID = 173202312762884096

client = discord.Client()
bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

bot_version = '1.4.0'
bot_version_date = '3/8/2022 (US EST)'


@bot.event
async def on_ready():
    dev_team_channel = bot.get_channel(939028644175699968)
    bot_command_channel = bot.get_channel(936902313589764146)

    message = (f"{bot.user.name} is live:\n"
               f"`v{bot_version}` - From `{bot_version_date}` \n"
               f"Release - `Alpha`")

    print(f"{bot.user.name} is connected!")
    print('\n\n' + message)
    await dev_team_channel.send(message)
    await bot_command_channel.send(message)


@bot.command(name='troll')
async def troll(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        await ctx.send(f"```{assets.troll_command()}```")


@bot.command(name='bitches')
async def bitches(ctx):
    role_names = [str(r) for r in ctx.author.roles]

    if 'Medal of Valor' in role_names:
        salute_emoji = '<:GreenSalute:906047649982083113>'
        mention = format(f"<@!{ctx.author.id}>")
        await ctx.send(f"congradulations {mention}, you have bitches! {salute_emoji}")
    else:
        mention = format(f"<@!{ctx.author.id}>")
        await ctx.send(f"you have no bitches")


@bot.command(name='drugs')
async def drugs(ctx):
    await ctx.send("deathsticks?")


@bot.command(name='your-mom')
async def your_mom(ctx):
    await ctx.send("is in my bed. your welcome.")


@bot.command(name='no-u')
async def no_u(ctx):
    await ctx.send(assets.rage())


@bot.command(name='add')
@commands.has_role('Economy Admin')
async def add(ctx, user: discord.Member, message):
    role_names = [str(r) for r in user.roles]

    credit_emoji = '<:credits:937788738950545464>'
    var_credit_value = merit_config.add_credits(user.id, int(message))
    role_credit_value = credit_counter.credit_counter(role_names, user.id)
    mention = format(f"<@!{user.id}>")

    await ctx.send(f"Transferred {credit_emoji}`{var_credit_value}` to `user-id: {user.id}`.\n\n"
                   f"{mention} now has {credit_emoji}`{role_credit_value}`.")


@bot.command(name='sub-merits')
async def sub_merits(ctx, user: discord.Member, message):
    if ctx.author.id == KYODA_ID or FORCEPS_ID:
        role_names = [str(r) for r in user.roles]

        credit_emoji = '<:credits:937788738950545464>'
        var_credit_value = merit_config.subtract_merits(user.id, int(message))
        role_credit_value = credit_counter.credit_counter(role_names, user.id)
        mention = format(f"<@!{user.id}>")

        await ctx.send(f"Removed {credit_emoji}`{var_credit_value}` from [ MERITS.TXT ] for `user-id: {user.id}`.\n\n"
                       f"{mention} now has {credit_emoji}`{role_credit_value}`.")
    else:
        await ctx.send("`Not Authorised`")


@bot.command(name='remove')
@commands.has_role('Economy Admin')
async def remove(ctx, user: discord.Member, message):
    role_names = [str(r) for r in user.roles]

    credit_emoji = '<:credits:937788738950545464>'
    var_credit_value = merit_config.remove_credits(user.id, int(message))
    role_credit_value = credit_counter.credit_counter(role_names, user.id)
    mention = format(f"<@!{user.id}>")

    await ctx.send(f"Transferred {credit_emoji}`{var_credit_value}` from `user-id: {user.id}`.\n\n"
                   f"{mention} now has {credit_emoji}`{role_credit_value}`.")


@bot.command(name='sub-demerits')
async def sub_demerits(ctx, user: discord.Member, message):
    if ctx.author.id == KYODA_ID or FORCEPS_ID:
        role_names = [str(r) for r in user.roles]

        credit_emoji = '<:credits:937788738950545464>'
        var_credit_value = merit_config.subtract_demerits(user.id, int(message))
        role_credit_value = credit_counter.credit_counter(role_names, user.id)
        mention = format(f"<@!{user.id}>")

        await ctx.send(f"Removed {credit_emoji}`{var_credit_value}` from [ DEMERITS.TXT ] for `user-id: {user.id}`.\n\n"
                       f"{mention} now has {credit_emoji}`{role_credit_value}`.")
    else:
        await ctx.send("`Not Authorised`")


@bot.command(name='credits')
async def thing_for_roles(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        role_names = [str(r) for r in ctx.author.roles]
        user_id = str(ctx.author.id)

        credit_emoji = '<:credits:937788738950545464>'
        credit_value = credit_counter.credit_counter(role_names, user_id)
        if credit_value == False:
            await ctx.send("You were not detected in the credit logs, or you have no credits. "
                           "Please run `.register` to add yourself to the registry or to check integrity of your user.")
        else:
            if 'Medal of Valor' in role_names:
                salute_emoji = '<:GreenSalute:906047649982083113>'
                mention = format(f"<@!{ctx.author.id}>")
                await ctx.send(f"{mention}, You have {credit_emoji}`{credit_value}`.\n{salute_emoji}")
            else:
                mention = format(f"<@!{ctx.author.id}>")
                await ctx.send(f"{mention}, You have {credit_emoji}`{credit_value}`.")


@bot.command(name='check-credits')
@commands.has_role('Economy Admin')
async def remove(ctx, user: discord.Member):
    role_names = [str(r) for r in user.roles]

    credit_emoji = '<:credits:937788738950545464>'
    credit_value = credit_counter.credit_counter(role_names, user.id)

    if credit_value == False:
        await ctx.send("User was not detected in the credit logs, or has no credits. Please have them run `.register`"
                       " to add yourself to the registry or to check integrity of your user. ")
    else:
        await ctx.send(f"`{user.display_name}` has {credit_emoji}`{credit_value}`.")


# register command order:
# in all three
# in registry, in merit, not demerit
# in registry, not merit, in demerit
# in registry, not merit, not demerit
# not registry, in merit, in demerit
# not registry, not merit, in demerit
# not registry, in merit, not demerit
# not all three


@bot.command(name='register')
async def register(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        user_id = str(ctx.author.id)
        mention = f"<@!{user_id}>"
        channel = bot.get_channel(939028644175699968)
        now = datetime.datetime.now()

        with open("registry.txt", 'r') as f:
            line = f.read()
            if user_id in line:
                print(f"{ctx.author.display_name} - {ctx.author.id} \nis in registry.txt")
                with open("merit.txt", 'r') as f:
                    line = f.read()
                    if user_id in line:
                        print(f"{ctx.author.display_name} - {ctx.author.id} \nis in merit.txt")
                        with open("demerit.txt", 'r') as f:
                            line = f.read()
                            if user_id in line:
                                # in all three
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis in demerit.txt")
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis registered with 0 errors")
                                await ctx.send(f"Registry integrity check for {mention} passed with `0` errors. \n"
                                               f"(You are already in the registry)")
                            if user_id not in line:
                                # in registry, in merit, not demerit
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis not in demerit.txt")
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis registered with 1 error")
                                await ctx.send(f"`ERROR` - - - {mention}\n"
                                               f"Registry integrity check for {mention} failed with `1` error. "
                                               f"[ MERIT.txt ]\nPlease do not use .report, an error report has been "
                                               f"automatically generated.")

                                report_message = (f"@here \n\n"
                                                  f"`{ctx.author.display_name} - {ctx.author.id}`\n"
                                                  f"`{now.month}/{now.day}/{now.year}` in channel "
                                                  f"'#{ctx.message.channel}'\n{ctx.author.display_name} "
                                                  f"reported a malfunction in the file: [ MERIT.TXT ].\n"
                                                  f"Specifics: `The user id was detected in registry.txt as "
                                                  f"well as demerit.txt but was not detected in merit.txt.`")
                                report_log = (f"{ctx.author.display_name} - {ctx.author.id}\n"
                                              f"{now.month}/{now.day}/{now.year} in channel "
                                              f"'#{ctx.message.channel}' \n{ctx.author.display_name} "
                                              f"reported a malfunction in the file: [ MERIT.TXT ].\n"
                                              f"Specifics: The user id was detected in registry.txt as "
                                              f"well as demerit.txt but was not detected in merit.txt.")
                                await channel.send(report_message)
                                print(report_log)
                                with open("reports.txt", "a") as report_file:
                                    report_file.write(f"{report_log}\n---------------\n")
                    if user_id not in line:
                        print(f"{ctx.author.display_name} - {ctx.author.id} \nis not in merit.txt")
                        with open("demerit.txt", 'r') as f:
                            line = f.read()
                            if user_id in line:
                                # in registry, not merit, in demerit
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis in demerit.txt")
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis registered with 1 error")
                                await ctx.send(f"`ERROR` - - - {mention}\n"
                                               f"Registry integrity check for {mention} failed with `1` error. "
                                               f"[ DEMERIT.txt ]\nPlease do not use .report, an error report has been "
                                               f"automatically generated.")

                                report_message = (f"@here \n\n"
                                                  f"`{ctx.author.display_name} - {ctx.author.id}`\n"
                                                  f"`{now.month}/{now.day}/{now.year}` in channel "
                                                  f"'#{ctx.message.channel}'\n{ctx.author.display_name} "
                                                  f"reported a malfunction in the file: [ DEMERIT.TXT ].\n"
                                                  f"Specifics: `The user id was detected in registry.txt as "
                                                  f"well as demerit.txt but was not detected in merit.txt.`")
                                report_log = (f"{ctx.author.display_name} - {ctx.author.id}\n"
                                              f"{now.month}/{now.day}/{now.year} in channel "
                                              f"'#{ctx.message.channel}' \n{ctx.author.display_name} "
                                              f"reported a malfunction in the file: [ DEMERIT.TXT ].\n"
                                              f"Specifics: The user id was detected in registry.txt as "
                                              f"well as demerit.txt but was not detected in merit.txt.")
                                await channel.send(report_message)
                                print(report_log)
                                with open("reports.txt", "a") as report_file:
                                    report_file.write(f"{report_log}\n---------------\n")
                            if user_id not in line:
                                # in registry, not merit, not demerit
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis not in demerit.txt")
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis registered with 2 errors")
                                await ctx.send(f"`ERROR` - - - {mention}\n"
                                               f"Registry integrity check for {mention} failed with `2` errors. "
                                               f"[ MERIT.txt ], [ DEMERIT.txt ]\nPlease do not use .report, an error "
                                               f"report has been automatically generated.")

                                report_message = (f"@here \n\n"
                                                  f"`{ctx.author.display_name} - {ctx.author.id}`\n"
                                                  f"`{now.month}/{now.day}/{now.year}` in channel "
                                                  f"'#{ctx.message.channel}'\n{ctx.author.display_name} "
                                                  f"reported a malfunction in the file: [ MERIT.TXT ], [ DEMERIT.TXT ].\n"
                                                  f"Specifics: `The user id was detected in registry.txt, "
                                                  f"but was not detected in merit.txt. or demerit.txt.`")
                                report_log = (f"{ctx.author.display_name} - {ctx.author.id}\n"
                                              f"{now.month}/{now.day}/{now.year} in channel "
                                              f"'#{ctx.message.channel}' \n{ctx.author.display_name} "
                                              f"reported a malfunction in the file: [ MERIT.TXT ].\n"
                                              f"Specifics: The user id was detected in registry.txt, "
                                              f"but was not detected in merit.txt. or demerit.txt.")
                                await channel.send(report_message)
                                print(report_log)
                                with open("reports.txt", "a") as report_file:
                                    report_file.write(f"{report_log}\n---------------\n")
            if user_id not in line:
                print(f"{ctx.author.display_name} - {ctx.author.id} \nis not in registry.txt")
                with open("merit.txt", 'r') as f:
                    line = f.read()
                    if user_id in line:
                        print(f"{ctx.author.display_name} - {ctx.author.id} \nis in merit.txt")
                        with open("demerit.txt", 'r') as f:
                            line = f.read()
                            if user_id in line:
                                # not registry, in merit, in demerit
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis in in demerit.txt")
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis registered with 2 errors")
                                await ctx.send(f"`ERROR` - - - {mention}\n"
                                               f"Registry integrity check for {mention} failed with `2` errors. "
                                               f"[ MERIT.txt ], [ DEMERIT.txt ]\nPlease do not use .report, an error "
                                               f"report has been automatically generated.")

                                report_message = (f"@here \n\n"
                                                  f"`{ctx.author.display_name} - {ctx.author.id}`\n"
                                                  f"`{now.month}/{now.day}/{now.year}` in channel "
                                                  f"'#{ctx.message.channel}'\n{ctx.author.display_name} "
                                                  f"reported a malfunction in the file: [ MERIT.TXT ].\n"
                                                  f"Specifics: `The user id was not detected in registry.txt, "
                                                  f"but was detected in merit.txt. and demerit.txt.`")
                                report_log = (f"{ctx.author.display_name} - {ctx.author.id}\n"
                                              f"{now.month}/{now.day}/{now.year} in channel "
                                              f"'#{ctx.message.channel}' \n{ctx.author.display_name} "
                                              f"reported a malfunction in the file: [ MERIT.TXT ].\n"
                                              f"Specifics: The user id was not detected in registry.txt, "
                                              f"but was detected in merit.txt. and demerit.txt.")
                                await channel.send(report_message)
                                print(report_log)
                                with open("reports.txt", "a") as report_file:
                                    report_file.write(f"{report_log}\n---------------\n")
                            if user_id not in line:
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis not in demerit.txt")
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis registered with 1 error")
                                await ctx.send(f"`ERROR` - - - {mention}\n"
                                               f"Registry integrity check for {mention} failed with `1` error. "
                                               f"[ MERIT.txt ]\nPlease do not use .report, an error report has been "
                                               f"automatically generated.")

                                report_message = (f"@here \n\n"
                                                  f"`{ctx.author.display_name} - {ctx.author.id}`\n"
                                                  f"`{now.month}/{now.day}/{now.year}` in channel "
                                                  f"'#{ctx.message.channel}'\n{ctx.author.display_name} "
                                                  f"reported a malfunction in the file: [ MERIT.TXT ].\n"
                                                  f"Specifics: `The user id was not detected in registry.txt as "
                                                  f"well as demerit.txt but was detected in merit.txt.`")
                                report_log = (f"{ctx.author.display_name} - {ctx.author.id}\n"
                                              f"{now.month}/{now.day}/{now.year} in channel "
                                              f"'#{ctx.message.channel}' \n{ctx.author.display_name} "
                                              f"reported a malfunction in the file: [ MERIT.TXT ].\n"
                                              f"Specifics: The user id was not detected in registry.txt as "
                                              f"well as demerit.txt but was detected in merit.txt.")
                                await channel.send(report_message)
                                print(report_log)
                                with open("reports.txt", "a") as report_file:
                                    report_file.write(f"{report_log}\n---------------\n")
                    if user_id not in line:
                        print(f"{ctx.author.display_name} - {ctx.author.id} \nis not in merit.txt")
                        with open("demerit.txt", 'r') as f:
                            line = f.read()
                            if user_id in line:
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis in demerit.txt")
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis registered with 1 error")
                                await ctx.send(f"`ERROR` - - - {mention}\n"
                                               f"Registry integrity check for {mention} failed with `1` error. "
                                               f"[ DEMERIT.txt ]\nPlease do not use .report, an error report has been "
                                               f"automatically generated.")

                                report_message = (f"@here \n\n"
                                                  f"`{ctx.author.display_name} - {ctx.author.id}`\n"
                                                  f"`{now.month}/{now.day}/{now.year}` in channel "
                                                  f"'#{ctx.message.channel}'\n{ctx.author.display_name} "
                                                  f"reported a malfunction in the file: [ DEMERIT.TXT ].\n"
                                                  f"Specifics: `The user id was not detected in registry.txt as "
                                                  f"well as merit.txt but was detected in demerit.txt.`")
                                report_log = (f"{ctx.author.display_name} - {ctx.author.id}\n"
                                              f"{now.month}/{now.day}/{now.year} in channel "
                                              f"'#{ctx.message.channel}' \n{ctx.author.display_name} "
                                              f"reported a malfunction in the file: [ DEMERIT.TXT ].\n"
                                              f"Specifics: The user id was not detected in registry.txt as "
                                              f"well as merit.txt but was detected in demerit.txt.")
                                await channel.send(report_message)
                                print(report_log)
                                with open("reports.txt", "a") as report_file:
                                    report_file.write(f"{report_log}\n---------------\n")
                            if user_id not in line:
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis not in demerit.txt")
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nis not registered")

                                with open("registry.txt", 'a') as f:
                                    f.write(user_id + '\n')
                                    print(
                                        f"{ctx.author.display_name} - {ctx.author.id} \nhas been added to registry.txt")
                                with open("merit.txt", 'a') as f:
                                    f.write(user_id + '\n' + '0\n')
                                    print(f"{ctx.author.display_name} - {ctx.author.id} \nhas been added to merit.txt")
                                with open("demerit.txt", 'a') as f:
                                    f.write(user_id + '\n' + '0\n')
                                    print(f"{ctx.author.display_name} - {ctx.author.id} has been added to registry.txt")
                                print(
                                    f"{ctx.author.display_name} - {ctx.author.id} \nhas been  registered with 0 errors")
                                await ctx.send(f"{mention} has been added to the registry with `0` errors.")
    await bot.process_commands()


@bot.command(name='store')
async def store(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        await ctx.send(assets.store_command(format(ctx.author.id)))


@bot.command(name='shop')
async def shop(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        await ctx.send(assets.shop_command(format(ctx.author.id)))


@bot.command(name='ggn-store')
async def ggn_store(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        await ctx.send(assets.ggn_store_command(format(ctx.author.id)))


@bot.command(name='github')
async def github(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        await ctx.send("https://github.com/G41st/41st-utility-bot \n"
                       "If you are interested in helping out with the bot, be sure to DM Kyoda!")


@bot.command(name='fuck')
async def fuck(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        await ctx.send("you")


@bot.command(name='help')
async def command_help(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        await ctx.send(assets.commands_command(ctx.author.id))


@bot.command(name='commands')
async def command_commands(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        await ctx.send(assets.commands_command(ctx.author.id))


@bot.command(name='directory')
async def command_help(ctx):
    channel = await ctx.author.create_dm()
    await channel.send(assets.commands_directory(ctx.author.id))
    await ctx.send(f"<@!{ctx.author.id}> - Directory sent in DM's.")


@bot.command(name='version')
async def version(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        role_names = [str(r) for r in ctx.author.roles]

        version = (f"`v{bot_version}` - From `{bot_version_date}` \n"
                   f"Release - `Alpha`")

        if 'Medal of Valor' in role_names:
            salute_emoji = '<:GreenSalute:906047649982083113>'
            mention = format(f"<@!{ctx.author.id}>")
            await ctx.send(f"{version}\n\n"
                           f"{mention}\n{salute_emoji}")
        else:
            mention = format(f"<@!{ctx.author.id}>")
            await ctx.send(f"{version}\n\n"
                           f"{mention}")


@bot.command(name='report')
async def report(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        await ctx.send(assets.report_command(ctx.author.id))


@bot.command(name='report-send')
async def report_send(ctx, message):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        now = datetime.datetime.now()

        channel = bot.get_channel(939028644175699968)

        report_message = (f"NEW REPORT - - - @here \n\n"
                          f"```{ctx.author.display_name} - {ctx.author.id}\n"
                          f"{now.month}/{now.day}/{now.year} in channel '#{ctx.message.channel}' \n"
                          f"{ctx.author.display_name} said:\n '{ctx.message.content}'```\n")

        report_log = (f"{ctx.author.display_name} - {ctx.author.id}\n"
                      f"{now.month}/{now.day}/{now.year} in channel '#{ctx.message.channel}' \n"
                      f"     {ctx.author.display_name} said:\n'{ctx.message.content}'")

        with open("reports.txt", "a") as report_file:
            report_file.write(f"{report_log}\n---------------\n")

        await channel.send(report_message)


@bot.command(name='git-push')
async def shutdown(ctx):
    if ctx.author.id == KYODA_ID or FORCEPS_ID:
        await ctx.send("```41st://<utilities> ~ $```")
        await ctx.send("`Pushing to Git`")
        time.sleep(1)

        git_push.upload()

        ctx.send("all databases have been pushed and are backed up.")
    else:
        await ctx.send("`Not Authorised`")


@bot.command(name='restart')
async def shutdown(ctx):
    if ctx.author.id == KYODA_ID or FORCEPS_ID:
        await ctx.send("```41st://<utilities> ~ $```")
        await ctx.send("`Pushing to Git`")
        time.sleep(1)

        git_push.upload()

        await ctx.send("`All databases have been pushed and are backed up.`")

        await ctx.send("`Shutdown in 5`")
        time.sleep(1)
        await ctx.send("`4`")
        time.sleep(1)
        await ctx.send("`3`")
        time.sleep(1)
        await ctx.send("`2`")
        time.sleep(1)
        await ctx.send("`1`")
        time.sleep(1)
        await ctx.send("https://www.youtube.com/watch?v=Gb2jGy76v0Y")
        sys.exit()
    else:
        await ctx.send("`Not Authorised`")


@bot.command(name='kill')
async def shutdown(ctx):
    if ctx.author.id == KYODA_ID or FORCEPS_ID:
        await ctx.send("```41st://<utilities> ~ $``` \n `HARD-SHUTDOWN`")
        time.sleep(1)
        sys.exit()
    else:
        await ctx.send("`Not Authorised`")


def main():
    while True:
        bot.run(TOKEN)
