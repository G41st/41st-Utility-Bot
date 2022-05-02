import os
import sys
import time
import datetime

import discord
from discord.ext.commands import Bot
from discord import Intents
import assets
import register_command
import role_counter
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
BOT_OPERATOR_ROLE = "Technical Commander"


def startup(START):
    global LAUNCH
    global bot

    if START == TOKEN:
        intents = Intents.all()
        bot = Bot(intents=intents, command_prefix='.')
        bot.remove_command('help')
        LAUNCH = TOKEN

    if START == TOKEN_TEST:
        intents = Intents.all()
        bot = Bot(intents=intents, command_prefix='..')
        bot.remove_command('help')
        LAUNCH = TOKEN_TEST


startup(TOKEN_TEST)
bot_version = '2.0.0'
bot_version_date = '4/24/2022 (US EST)'


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


def credit_counter(role_names, discord_id):
    role_total = role_counter.credit_counter(role_names)
    merit_total = merit_config.merit_reader(discord_id)
    demerit_total = merit_config.demerit_reader(discord_id)

    merit_sum = role_total + merit_total
    total = merit_sum - demerit_total

    if role_total == False:
        return False
    else:
        return total


@bot.command(name='add')
@commands.has_role('Economy Admin')
async def add(ctx, user: discord.Member, message):
    role_names = [str(r) for r in user.roles]

    credit_emoji = '<:credits:937788738950545464>'
    var_credit_value = merit_config.add_credits(user.id, int(message))
    role_credit_value = credit_counter(role_names, user.id)
    mention = format(f"<@!{user.id}>")

    await ctx.send(f"Transferred {credit_emoji}`{var_credit_value}` to `user-id: {user.id}`.\n\n"
                   f"{mention} now has {credit_emoji}`{role_credit_value}`.")


@bot.command(name='sub-merits')
async def sub_merits(ctx, user: discord.Member, message):
    if ctx.author.id == KYODA_ID or FORCEPS_ID:
        role_names = [str(r) for r in user.roles]

        credit_emoji = '<:credits:937788738950545464>'
        var_credit_value = merit_config.subtract_merits(user.id, int(message))
        role_credit_value = credit_counter(role_names, user.id)
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
    role_credit_value = credit_counter(role_names, user.id)
    mention = format(f"<@!{user.id}>")

    await ctx.send(f"Transferred {credit_emoji}`{var_credit_value}` from `user-id: {user.id}`.\n\n"
                   f"{mention} now has {credit_emoji}`{role_credit_value}`.")


@bot.command(name='sub-demerits')
async def sub_demerits(ctx, user: discord.Member, message):
    if ctx.author.id == KYODA_ID or FORCEPS_ID:
        role_names = [str(r) for r in user.roles]

        credit_emoji = '<:credits:937788738950545464>'
        var_credit_value = merit_config.subtract_demerits(user.id, int(message))
        role_credit_value = credit_counter(role_names, user.id)
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
        credit_value = credit_counter(role_names, user_id)
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
    credit_value = credit_counter(role_names, user.id)

    if credit_value == False:
        await ctx.send("User was not detected in the credit logs, or has no credits. Please have them run `.register`"
                       " to add yourself to the registry or to check integrity of your user. ")
    else:
        await ctx.send(f"`{user.display_name}` has {credit_emoji}`{credit_value}`.")


@bot.command(name='id')
@commands.has_role('Economy Admin')
async def identify(ctx, user: discord.Member):
    role_names = [str(r) for r in user.roles]

    credit_emoji = '<:credits:937788738950545464>'
    credit_value = credit_counter(role_names, user.id)
    credit_value_raw = role_counter.credit_counter(role_names)

    merit_checker = merit_config.merit_reader(user.id)
    demerit_checker = merit_config.demerit_reader(user.id)
    join_date = user.joined_at.strftime("%b %d, %Y")

    shadow_mention = discord.AllowedMentions(users=False)

    if credit_value == False:
        await ctx.send("User was not detected in the credit logs, or has no credits. Please have them run `.register`"
                       " to add yourself to the registry or to check integrity of your user. ")
    else:
        await ctx.send(f"Name: `{user.display_name}`\n"
                       f"ID:`{user.id}`\n"
                       f"Join Date: `{join_date}`\n"
                       f"Credits: {credit_emoji}`{credit_value}`\n"
                       f"Raw Credits: `{credit_value_raw}`\n"
                       f"Merits: `{merit_checker}`\n"
                       f"Demerits: `{demerit_checker}`\n"
                       f"Certifications: \n```\n"
                       f"{assets.certifications('command', role_names)}\n"
                       f"{assets.certifications('sof1', role_names)}\n"
                       f"{assets.certifications('sof2', role_names)}\n"
                       f"{assets.certifications('trooper', role_names)}\n"
                       f"{assets.certifications('pilot', role_names)}\n"
                       f"{assets.certifications('veteran', role_names)}"
                       f"{assets.certifications('valor', role_names)}```\n"
                       f"Shadow Mention: <@!{user.id}>", allowed_mentions=shadow_mention)


@bot.command(name='whoami')
async def who_am_i(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        credit_emoji = '["7]'

        channel = await ctx.author.create_dm()
        role_names = [str(r) for r in ctx.author.roles]
        credit_value = credit_counter(role_names, ctx.author.id)
        credit_value_raw = role_counter.credit_counter(role_names)

        merit_checker = merit_config.merit_reader(ctx.author.id)
        demerit_checker = merit_config.demerit_reader(ctx.author.id)
        join_date = ctx.author.joined_at.strftime("%b %d, %Y")

        if credit_value == False:
            await ctx.send("User was not detected in the credit logs, or has no credits. Please have them run "
                           "`.register` to add yourself to the registry or to check integrity of your user. ")
        else:
            await ctx.send(f"<@!{ctx.author.id}> - User Info sent in DM's.")
            await channel.send(f"Name: `{ctx.author.display_name}`\n"
                               f"ID:`{ctx.author.id}`\n"
                               f"Join Date: `{join_date}`\n"
                               f"Credits: {credit_emoji}`{credit_value}`\n"
                               f"Raw Credits: `{credit_value_raw}`\n"
                               f"Merits: `{merit_checker}`\n"
                               f"Demerits: `{demerit_checker}`\n"
                               f"Certifications: \n```\n"
                               f"{assets.certifications('command', role_names)}"
                               f"{assets.certifications('sof1', role_names)}"
                               f"{assets.certifications('sof2', role_names)}"
                               f"{assets.certifications('trooper', role_names)}"
                               f"{assets.certifications('pilot', role_names)}"
                               f"{assets.certifications('veteran', role_names)}"
                               f"{assets.certifications('valor', role_names)}```\n")


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
        mention = f"<@!{ctx.user.id}>"
        channel = bot.get_channel(939028644175699968)

        database_check = register_command.register(ctx.author.id, ctx.author.display_name)

        if database_check == "00" or "07":
            await ctx.send(register_command.channel_reply(database_check, mention))
        else:
            report_message = \
                register_command.report_message(database_check, ctx.author.id, ctx.author.display_name, ctx.channel.id)
            report_log = \
                register_command.report_log(database_check, ctx.author.id, ctx.author.display_name, ctx.channel.id)

            await ctx.send(register_command.channel_reply(database_check, mention))
            await channel.send(report_message)
            with open("reports.txt", "a") as report_file:
                report_file.write(f"{report_log}\n---------------\n")


@bot.command(name='store')
async def store(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        credit_emoji = '<:credits:937788738950545464>'

        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 69))


@bot.command(name='store-1')
async def store(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        credit_emoji = '<:credits:937788738950545464>'

        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 0))
        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 1))


@bot.command(name='store-2')
async def store(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        credit_emoji = '<:credits:937788738950545464>'

        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 0))
        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 2))


@bot.command(name='store-3')
async def store(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        credit_emoji = '<:credits:937788738950545464>'

        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 0))
        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 3))


@bot.command(name='store-4')
async def store(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        credit_emoji = '<:credits:937788738950545464>'

        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 0))
        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 4))


@bot.command(name='store-5')
async def store(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        credit_emoji = '<:credits:937788738950545464>'

        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 0))
        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 5))


@bot.command(name='store-6')
async def store(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        credit_emoji = '<:credits:937788738950545464>'

        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 0))
        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 6))


@bot.command(name='store-7')
async def store(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        credit_emoji = '<:credits:937788738950545464>'

        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 0))
        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 7))


@bot.command(name='store-8')
async def store(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        credit_emoji = '<:credits:937788738950545464>'

        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 0))
        await ctx.send(assets.store_command(format(ctx.author.id), credit_emoji, 8))


@bot.command(name='store-all')
async def store(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        credit_emoji = '["7]'

        channel = await ctx.author.create_dm()
        await ctx.send(f"<@!{ctx.author.id}> - Store sent in DM's.")

        await channel.send(assets.store_command(format(ctx.author.id), credit_emoji, 0))
        await channel.send(assets.store_command(format(ctx.author.id), credit_emoji, 1))
        await channel.send(assets.store_command(format(ctx.author.id), credit_emoji, 2))
        await channel.send(assets.store_command(format(ctx.author.id), credit_emoji, 3))
        await channel.send(assets.store_command(format(ctx.author.id), credit_emoji, 4))
        await channel.send(assets.store_command(format(ctx.author.id), credit_emoji, 5))
        await channel.send(assets.store_command(format(ctx.author.id), credit_emoji, 6))
        await channel.send(assets.store_command(format(ctx.author.id), credit_emoji, 7))
        await channel.send(assets.store_command(format(ctx.author.id), credit_emoji, 8))


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


# start troll commands

@bot.command(name='bitches')
async def bitches(ctx):
    role_names = [str(r) for r in ctx.author.roles]

    if 'Medal of Valor' in role_names:
        salute_emoji = '<:GreenSalute:906047649982083113>'
        mention = format(f"<@!{ctx.author.id}>")
        await ctx.send(f"congradulations {mention}, you have bitches! {salute_emoji}")
    else:
        await ctx.send(f"you have no bitches")


@bot.command(name='drugs')
async def drugs(ctx):
    await ctx.send("deathsticks?")


@bot.command(name='shitterbawx')
async def shitterbawx(ctx):
    await ctx.send("pretorien is the better ginger")


@bot.command(name='chatterbox')
async def chatterbox(ctx):
    await ctx.send("you mean shitterbawx?")


@bot.command(name='your-mom')
async def your_mom(ctx):
    await ctx.send("is in my bed. your welcome.")


@bot.command(name='not-scared')
async def not_scared(ctx):
    await ctx.send("`<@!391974737745805322>`")


@bot.command(name='no-u')
async def no_u(ctx):
    await ctx.send(assets.rage())


@bot.command(name='troll')
async def troll(ctx):
    if ctx.channel.id == '936902313589764146' or '939028644175699968':
        await ctx.send(f"```{assets.troll_command()}```")


@bot.command(name='adko')
async def adko(ctx):
    salute_emoji = '<:GreenSalute:906047649982083113>'

    await ctx.send(f"`MJR Adko CC-1258`\n"
                   f"Trained on: `07/12/2021 (US EAST)`\n"
                   f"Stepped down on: `03/20/2022 (US EAST)`\n"
                   f"- 'The road to freedom is paved with blood. (Unknown)' \n"
                   f"Godspeed brother, may Floppa bless you on your journey.\n"
                   f"{salute_emoji}")


@bot.command(name='blue')
async def adko(ctx):
    salute_emoji = '<:GreenSalute:906047649982083113>'

    await ctx.send(f"`CPT Blue CC-1591`\n"
                   f"Trained on: `08/20/2021 (US EAST)`\n"
                   f"Stepped down on: `03/20/2022 (US EAST)`\n"
                   f"- 'A loving, caring, human being. Always there for you if you need him. Like the brother you "
                   f"never got. (2LT Raven)' \n"
                   f"Godspeed brother.\n"
                   f"{salute_emoji}")


# end troll commands

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


@bot.command(name='announcement')
async def shutdown(ctx):
    if ctx.author.id == KYODA_ID or FORCEPS_ID:
        channel = bot.get_channel(851284148915404831)

        with open("announcement.txt", "r") as annoucement:
            message = annoucement.read()

        pings = assets.pings()

        await channel.send(pings + "\n\n" + message)
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
        bot.run(LAUNCH)
