import os
import sys
import time
import datetime
import assets
import credit_counter
from discord.ext import commands
import discord.ext.commands
from dotenv import load_dotenv
import merit_config
import git_push

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN_TEST = os.getenv('DISCORD_TOKEN_TEST')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='.')
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f"{bot.user.name} is connected!\n")


@bot.command(name='troll')
async def troll(ctx):
    await ctx.send(f"```{assets.troll_command()}```")


@bot.command(name='add')
@commands.has_role('Dev Team Lead')
async def add(ctx, user: discord.Member, message):
    role_names = [str(r) for r in user.roles]

    credit_emoji = '<:credits:937788738950545464>'
    var_credit_value = merit_config.add_credits(user.id, int(message))
    role_credit_value = credit_counter.credit_counter(role_names, user.id)
    mention = format(f"<@!{user.id}>")

    await ctx.send(f"Transferred {credit_emoji}`{var_credit_value}` to `user-id: {user.id}`.\n\n"
                   f"{mention} now has {credit_emoji}`{role_credit_value}`.")


@add.error
async def add_error(ctx, message):
    mention = format(f"<@!{ctx.author.id}>")
    await ctx.send(f"ERROR: *CODE_1* - {mention} \n\n`You are missing an argument!`")


@bot.command(name='sub-merits')
@commands.has_role('Dev Team Lead')
async def sub_merits(ctx, user: discord.Member, message):
    role_names = [str(r) for r in user.roles]

    credit_emoji = '<:credits:937788738950545464>'
    var_credit_value = merit_config.subtract_merits(user.id, int(message))
    role_credit_value = credit_counter.credit_counter(role_names, user.id)
    mention = format(f"<@!{user.id}>")

    await ctx.send(f"Removed {credit_emoji}`{var_credit_value}` from [ MERITS.TXT ] for `user-id: {user.id}`.\n\n"
                   f"{mention} now has {credit_emoji}`{role_credit_value}`.")


@sub_merits.error
async def sub_merits_err(ctx, message):
    mention = format(f"<@!{ctx.author.id}>")
    await ctx.send(f"ERROR: *CODE_1* - {mention} \n\n`You are missing an argument!`")


@bot.command(name='remove')
@commands.has_role('Dev Team Lead')
async def remove(ctx, user: discord.Member, message):
    role_names = [str(r) for r in user.roles]

    credit_emoji = '<:credits:937788738950545464>'
    var_credit_value = merit_config.remove_credits(user.id, int(message))
    role_credit_value = credit_counter.credit_counter(role_names, user.id)
    mention = format(f"<@!{user.id}>")

    await ctx.send(f"Transferred {credit_emoji}`{var_credit_value}` from `user-id: {user.id}`.\n\n"
                   f"{mention} now has {credit_emoji}`{role_credit_value}`.")


@remove.error
async def remove_error(ctx, message):
    mention = format(f"<@!{ctx.author.id}>")

    await ctx.send(f"ERROR: *CODE_1* - {mention} \n\n`You are missing an argument!`")


@bot.command(name='sub-demerits')
@commands.has_role('Dev Team Lead')
async def sub_demerits(ctx, user: discord.Member, message):
    role_names = [str(r) for r in user.roles]

    credit_emoji = '<:credits:937788738950545464>'
    var_credit_value = merit_config.subtract_demerits(user.id, int(message))
    role_credit_value = credit_counter.credit_counter(role_names, user.id)
    mention = format(f"<@!{user.id}>")

    await ctx.send(f"Removed {credit_emoji}`{var_credit_value}` from [ DEMERITS.TXT ] for `user-id: {user.id}`.\n\n"
                   f"{mention} now has {credit_emoji}`{role_credit_value}`.")


@sub_merits.error
async def sub_merits_err(ctx, message):
    mention = format(f"<@!{ctx.author.id}>")
    await ctx.send(f"ERROR: *CODE_1* - {mention} \n\n`You are missing an argument!`")


@bot.command(name='credits')
async def thing_for_roles(ctx):
    role_names = [str(r) for r in ctx.author.roles]
    user_id = str(ctx.author.id)

    credit_emoji = '<:credits:937788738950545464>'
    credit_value = credit_counter.credit_counter(role_names, user_id)
    mention = format(f"<@!{ctx.author.id}>")

    await ctx.send(f"{mention}, You have {credit_emoji}`{credit_value}`.")


@bot.command(name='check-credits')
@commands.has_role('Dev Team Lead')
async def remove(ctx, user: discord.Member):
    role_names = [str(r) for r in user.roles]

    credit_emoji = '<:credits:937788738950545464>'
    credit_value = credit_counter.credit_counter(role_names, user.id)

    await ctx.send(f"`{user.display_name}` has {credit_emoji}`{credit_value}`.")


@bot.command(name='register')
async def register(ctx):
    user_id = ctx.author.id
    mention = f"<@!{user_id}>"
    channel = bot.get_channel(938290721302134855)
    now = datetime.datetime.now()

    with open("registry.txt", 'r') as f:
        for number, line in enumerate(f):
            if user_id not in line:
                with open("merit.txt", 'r') as f:
                    for number, line in enumerate(f):
                        if user_id not in line:
                            with open("demerit.txt", 'r') as f:
                                for number, line in enumerate(f):
                                    if user_id not in line:
                                        with open("registry.txt", 'e') as f:
                                            f.write(user_id + '\n')
                                        with open("merit.txt", "e") as f:
                                            f.write(f"{user_id}\n0\n")
                                        with open("demerit.txt", "e") as f:
                                            f.write(f"{user_id}\n0\n")
            if user_id in line:
                with open("merit.txt", 'r') as f:
                    for number, line in enumerate(f):
                        if user_id not in line:
                            with open("demerit.txt", 'r') as f:
                                for number, line in enumerate(f):
                                    if user_id not in line:
                                        # in registry but not anywhere else
                                        await ctx.send(f"`ERROR` - - - {mention}\n"
                                                       f"Error discovered within registry, alerting Dev Team.\n"
                                                       f"Please do not use .report, an error report has been "
                                                       f"automatically generated.")

                                        report_message = (f"`{ctx.author.display_name} - {ctx.author.id}`\n"
                                                          f"`{now.month}/{now.day}/{now.year}` in channel "
                                                          f"'#{ctx.message.channel}'\n{ctx.author.display_name} "
                                                          f"reported a malfunction in the file: [ MERIT.TXT ], "
                                                          f"[ DEMERIT.TXT ].\n"
                                                          f"Specifics: `The user id was detected in registry.txt but "
                                                          f"was not detected in any of the corresponding files.`")
                                        report_log = (f"{ctx.author.display_name} - {ctx.author.id}\n"
                                                      f"{now.month}/{now.day}/{now.year} in channel "
                                                      f"'#{ctx.message.channel}' \n{ctx.author.display_name} "
                                                      f"reported a malfunction in the file: [ MERIT.TXT ], "
                                                      f"[ DEMERIT.TXT ].\n"
                                                      f"Specifics: The user id was detected in registry.txt but "
                                                      f"was not detected in any of the corresponding files.")
                                        await channel.send(report_message)
                                        with open("reports.txt", "a") as report_file:
                                            report_file.write(f"{report_log}\n---------------\n")
                                    if user_id in line:
                                        # in registry and demerit, but not merit
                                        await ctx.send(f"`ERROR` - - - {mention}\n"
                                                       f"Error discovered within registry, alerting Dev Team.\n"
                                                       f"Please do not use .report, an error report has been "
                                                       f"automatically generated.")

                                        report_message = (f"`{ctx.author.display_name} - {ctx.author.id}`\n"
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
                                        with open("reports.txt", "a") as report_file:
                                            report_file.write(f"{report_log}\n---------------\n")
                        if user_id in line:
                            with open("demerit.txt", 'r') as f:
                                for number, line in enumerate(f):
                                    if user_id not in line:
                                        # in registry and merit, but not demerit
                                        await ctx.send(f"`ERROR` - - - {mention}\n"
                                                       f"Error discovered within registry, alerting Dev Team.\n"
                                                       f"Please do not use .report, an error report has been "
                                                       f"automatically generated.")

                                        report_message = (f"`{ctx.author.display_name} - {ctx.author.id}`\n"
                                                          f"`{now.month}/{now.day}/{now.year}` in channel "
                                                          f"'#{ctx.message.channel}'\n{ctx.author.display_name} "
                                                          f"reported a malfunction in the file: [ DEMERIT.TXT ].\n"
                                                          f"Specifics: `The user id was detected in registry.txt as "
                                                          f"well as merit.txt but was not detected in demerit.txt.`")
                                        report_log = (f"{ctx.author.display_name} - {ctx.author.id}\n"
                                                      f"{now.month}/{now.day}/{now.year} in channel "
                                                      f"'#{ctx.message.channel}' \n{ctx.author.display_name} "
                                                      f"reported a malfunction in the file: [ DEMERIT.TXT ].\n"
                                                      f"Specifics: The user id was detected in registry.txt as "
                                                      f"well as merit.txt but was not detected in demerit.txt.")
                                        await channel.send(report_message)
                                        with open("reports.txt", "a") as report_file:
                                            report_file.write(f"{report_log}\n---------------\n")
            if user_id not in line:
                with open("merit.txt", 'r') as f:
                    for number, line in enumerate(f):
                        if user_id in line:
                            with open("demerit.txt", 'r') as f:
                                for number, line in enumerate(f):
                                    if user_id in line:
                                        # in merit and demerit but not in registry
                                        await ctx.send(f"`ERROR` - - - {mention}\n"
                                                       f"Error discovered within registry, alerting Dev Team.\n"
                                                       f"Please do not use .report, an error report has been "
                                                       f"automatically generated.")

                                        report_message = (f"`{ctx.author.display_name} - {ctx.author.id}`\n"
                                                          f"`{now.month}/{now.day}/{now.year}` in channel "
                                                          f"'#{ctx.message.channel}'\n{ctx.author.display_name} "
                                                          f"reported a malfunction in the file: [ MERIT.TXT ], "
                                                          f"[ DEMERIT.TXT ].\n"
                                                          f"Specifics: `The user id was not detected in registry.txt "
                                                          f"but was detected in merit and demerit files.`")
                                        report_log = (f"{ctx.author.display_name} - {ctx.author.id}\n"
                                                      f"{now.month}/{now.day}/{now.year} in channel "
                                                      f"'#{ctx.message.channel}' \n{ctx.author.display_name} "
                                                      f"reported a malfunction in the file: [ MERIT.TXT ], "
                                                      f"[ DEMERIT.TXT ].\n"
                                                      f"Specifics: The user id was not detected in registry.txt "
                                                      f"but was detected in merit and demerit files.")
                                        await channel.send(report_message)
                                        with open("reports.txt", "a") as report_file:
                                            report_file.write(f"{report_log}\n---------------\n")
                                    if user_id not in line:
                                        # not in registry and demerit, but in merit
                                        await ctx.send(f"`ERROR` - - - {mention}\n"
                                                       f"Error discovered within registry, alerting Dev Team.\n"
                                                       f"Please do not use .report, an error report has been "
                                                       f"automatically generated.")

                                        report_message = (f"`{ctx.author.display_name} - {ctx.author.id}`\n"
                                                          f"`{now.month}/{now.day}/{now.year}` in channel "
                                                          f"'#{ctx.message.channel}'\n{ctx.author.display_name} "
                                                          f"reported a malfunction in the file: [ MERIT.TXT ].\n"
                                                          f"Specifics: `The user id was not detected in the registry as"
                                                          f" well as demerit.txt but was detected in merit.txt.`")
                                        report_log = (f"{ctx.author.display_name} - {ctx.author.id}\n"
                                                      f"{now.month}/{now.day}/{now.year} in channel "
                                                      f"'#{ctx.message.channel}' \n{ctx.author.display_name} "
                                                      f"reported a malfunction in the file: [ MERIT.TXT ].\n"
                                                      f"Specifics: The user id was not detected in the registry as"
                                                      f" well as demerit.txt but was detected in merit.txt.")
                                        await channel.send(report_message)
                                        with open("reports.txt", "a") as report_file:
                                            report_file.write(f"{report_log}\n---------------\n")
                        if user_id in line:
                            with open("demerit.txt", 'r') as f:
                                for number, line in enumerate(f):
                                    if user_id in line:
                                        # not in registry and demerit, but in merit
                                        await ctx.send(f"`ERROR` - - - {mention}\n"
                                                       f"Error discovered within registry, alerting Dev Team.\n"
                                                       f"Please do not use .report, an error report has been "
                                                       f"automatically generated.")

                                        report_message = (f"`{ctx.author.display_name} - {ctx.author.id}`\n"
                                                          f"`{now.month}/{now.day}/{now.year}` in channel "
                                                          f"'#{ctx.message.channel}'\n{ctx.author.display_name} "
                                                          f"reported a malfunction in the file: [ DEMERIT.TXT ].\n"
                                                          f"Specifics: `The user id was not detected in the registry as"
                                                          f" well as merit.txt but was detected in demerit.txt.`")
                                        report_log = (f"{ctx.author.display_name} - {ctx.author.id}\n"
                                                      f"{now.month}/{now.day}/{now.year} in channel "
                                                      f"'#{ctx.message.channel}' \n{ctx.author.display_name} "
                                                      f"reported a malfunction in the file: [ DEMERIT.TXT ].\n"
                                                      f"Specifics: The user id was not detected in the registry as"
                                                      f" well as merit.txt but was detected in demerit.txt.")
                                        await channel.send(report_message)
                                        with open("reports.txt", "a") as report_file:
                                            report_file.write(f"{report_log}\n---------------\n")


@bot.command(name='store')
async def store(ctx):
    await ctx.send(assets.store_command(format(ctx.author.id)))


@bot.command(name='shop')
async def shop(ctx):
    await ctx.send(assets.shop_command(format(ctx.author.id)))


@bot.command(name='github')
async def github(ctx):
    await ctx.send("https://github.com/G41st/41st-utility-bot \nIf you are interested in helping out with the bot,"
                   "be sure to DM Kyoda!")


@bot.command(name='fuck')
@commands.has_role('Dev Team Lead')
async def shutdown(ctx):
    await ctx.send("you")


@bot.command(name='help')
async def command_help(ctx):
    await ctx.send(assets.commands_command(ctx.author.id))


@bot.command(name='report')
async def report(ctx):
    await ctx.send(assets.report_command(ctx.author.id))


@bot.command(name='report-send')
async def report_send(ctx, message):
    now = datetime.datetime.now()

    channel = bot.get_channel(938290721302134855)

    report_message = (f"NEW REPORT - - - <@&937785771673391184> \n\n"
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
@commands.has_role('Dev Team Lead')
async def shutdown(ctx):
    await ctx.send("```41st://<utilities> ~ $```")
    await ctx.send("`Pushing to Git`")
    time.sleep(1)

    git_push.upload("merit.txt", "merit.txt", "main")
    git_push.upload("demerit.txt", "demerit.txt", "main")
    git_push.upload("registry.txt", "registry.txt", "main")

    ctx.send("all databases have been pushed and are backed up.")


@bot.command(name='restart')
@commands.has_role('Dev Team Lead')
async def shutdown(ctx):
    await ctx.send("```41st://<utilities> ~ $```")
    await ctx.send("`Pushing to Git`")
    time.sleep(1)

    git_push.upload("merit.txt", "merit.txt", "main")
    git_push.upload("demerit.txt", "demerit.txt", "main")
    git_push.upload("registry.txt", "registry.txt", "main")

    ctx.send("all databases have been pushed and are backed up.")

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
    await ctx.send("o7")
    sys.exit()


@bot.command(name='kill')
@commands.has_role('Dev Team Lead')
async def shutdown(ctx):
    await ctx.send("```41st://<utilities> ~ $``` \n `HARD-SHUTDOWN`")
    time.sleep(1)
    sys.exit()


def main():
    bot.run(TOKEN_TEST)

    now = datetime.datetime.now()

    while 23 == now.hour:
        if 59 == now.minute:
            git_push.upload("merit.txt", "merit.txt", "main")
            git_push.upload("demerit.txt", "demerit.txt", "main")
            git_push.upload("registry.txt", "registry.txt", "main")
