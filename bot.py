# bot.py
import os
import time
import sys
import assets
import credit_counter
import discord
from discord.ext import commands
import discord.ext.commands
from discord.ext.commands import MissingPermissions
from discord.utils import get
from dotenv import load_dotenv
import merit_config


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
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
    await ctx.send("adding")


@bot.command(name='store')
async def store(ctx):
    await ctx.send(assets.store_command(format(ctx.author.id)))


@bot.command(name='shop')
async def shop(ctx):
    await ctx.send(assets.shop_command(format(ctx.author.id)))


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


@bot.command(name='off')
@commands.has_role('Dev Team Lead')
async def shutdown(ctx):
    await ctx.send("```41st://<utilities> ~ $```")
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
    bot.run(TOKEN)
