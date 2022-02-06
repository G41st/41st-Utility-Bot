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
KYODA_ID = 583386313466708035

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
async def sub_merits(ctx, user: discord.Member, message):
    if ctx.author.id == KYODA_ID:
        role_names = [str(r) for r in user.roles]

        credit_emoji = '<:credits:937788738950545464>'
        var_credit_value = merit_config.subtract_merits(user.id, int(message))
        role_credit_value = credit_counter.credit_counter(role_names, user.id)
        mention = format(f"<@!{user.id}>")

        await ctx.send(f"Removed {credit_emoji}`{var_credit_value}` from [ MERITS.TXT ] for `user-id: {user.id}`.\n\n"
                       f"{mention} now has {credit_emoji}`{role_credit_value}`.")
    else:
        await ctx.send("`Not Authorised`")


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
async def sub_demerits(ctx, user: discord.Member, message):
    if ctx.author.id == KYODA_ID:
        role_names = [str(r) for r in user.roles]

        credit_emoji = '<:credits:937788738950545464>'
        var_credit_value = merit_config.subtract_demerits(user.id, int(message))
        role_credit_value = credit_counter.credit_counter(role_names, user.id)
        mention = format(f"<@!{user.id}>")

        await ctx.send(f"Removed {credit_emoji}`{var_credit_value}` from [ DEMERITS.TXT ] for `user-id: {user.id}`.\n\n"
                       f"{mention} now has {credit_emoji}`{role_credit_value}`.")
    else:
        await ctx.send("`Not Authorised`")


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
    if credit_value == False:
        await ctx.send("You were not detected in the credit logs. Please run `.register` to add yourself to the registry "
                 "or to check integrity of your user. ")
    else:
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
    user_id = str(ctx.author.id)
    mention = f"<@!{user_id}>"
    channel = bot.get_channel(938290721302134855)
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
                            print(f"{ctx.author.display_name} - {ctx.author.id} \nis in demerit.txt")
                            print(f"{ctx.author.display_name} - {ctx.author.id} \nis registered with 0 errors")
                            await ctx.send(f"Registry integrity check for {mention} passed with `0` errors. \n"
                                           f"(You are already in the registry)")
        if user_id not in line:
            print(f"{ctx.author.display_name} - {ctx.author.id} \nis not in registry.txt")
            with open("merit.txt", 'r') as f:
                line = f.read()
                if user_id not in line:
                    print(f"{ctx.author.display_name} - {ctx.author.id} \nis not in merit.txt")
                    with open("demerit.txt", 'r') as f:
                        line = f.read()
                        if user_id not in line:
                            print(f"{ctx.author.display_name} - {ctx.author.id} \nis not in demerit.txt")
                            print(f"{ctx.author.display_name} - {ctx.author.id} \nis not registered")

                            with open("registry.txt", 'a') as f:
                                f.write(user_id + '\n' + '0\n')
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nhas been added to registry.txt")
                            with open("merit.txt", 'a') as f:
                                f.write(user_id + '\n' + '0\n')
                                print(f"{ctx.author.display_name} - {ctx.author.id} \nhas been added to merit.txt")
                            with open("demerit.txt", 'a') as f:
                                f.write(user_id + '\n' + '0\n')
                                print(f"{ctx.author.display_name} - {ctx.author.id} has been added to registry.txt")
                            print(f"{ctx.author.display_name} - {ctx.author.id} \nhas been  registered with 0 errors")
                            await ctx.send(f"{mention} has been added to the registry with `0` errors.")


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
async def fuck(ctx):
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
async def shutdown(ctx):
    if ctx.author.id == KYODA_ID:
        await ctx.send("```41st://<utilities> ~ $```")
        await ctx.send("`Pushing to Git`")
        time.sleep(1)

        git_push.upload("merit.txt", "merit.txt", "main")
        git_push.upload("demerit.txt", "demerit.txt", "main")
        git_push.upload("registry.txt", "registry.txt", "main")
        git_push.upload("reports.txt", "reports.txt", "main")

        ctx.send("all databases have been pushed and are backed up.")
    else:
        await ctx.send("`Not Authorised`")


@bot.command(name='restart')
async def shutdown(ctx):
    if ctx.author.id == KYODA_ID:
        await ctx.send("```41st://<utilities> ~ $```")
        await ctx.send("`Pushing to Git`")
        time.sleep(1)

        git_push.upload("merit.txt", "merit.txt", "main")
        git_push.upload("demerit.txt", "demerit.txt", "main")
        git_push.upload("registry.txt", "registry.txt", "main")
        git_push.upload("reports.txt", "reports.txt", "main")

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
    else:
        await ctx.send("`Not Authorised`")


@bot.command(name='kill')
async def shutdown(ctx):
    if ctx.author.id == KYODA_ID:
        await ctx.send("```41st://<utilities> ~ $``` \n `HARD-SHUTDOWN`")
        time.sleep(1)
        sys.exit()
    else:
        await ctx.send("`Not Authorised`")


def main():
    bot.run(TOKEN_TEST)

    now = datetime.datetime.now()

    while 23 == now.hour:
        if 59 == now.minute:
            git_push.upload("merit.txt", "merit.txt", "main")
            git_push.upload("demerit.txt", "demerit.txt", "main")
            git_push.upload("registry.txt", "registry.txt", "main")
            git_push.upload("reports.txt", "reports.txt", "main")
