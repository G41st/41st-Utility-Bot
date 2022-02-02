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

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f"{bot.user.name} is connected!\n")
    print(f'{guild.name}(id: {guild.id})')


@bot.command(name='hello')
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send("hola")
    await message.channel.send(str(message.content))


@bot.command(name='troll')
async def troll(ctx):
    await ctx.send(f"```{assets.troll_command()}```")


@bot.command(name='add')
@commands.has_role('Dev Team Lead')
async def add(ctx, user: discord.Member, message):
    role_names = [str(r) for r in user.roles]

    credit_emoji = '<:credits:937788738950545464>'
    role_credit_value = credit_counter.credit_counter(role_names)
    var_credit_value = message
    credit_value = (int(role_credit_value) + int(var_credit_value))
    mention = format(f"<@!{user.id}>")

    await ctx.send(f"Transfered {credit_emoji}`{var_credit_value}` to `user-id: {user.id}`.\n\n"
                   f"{mention} now has {credit_emoji}`{credit_value}`.")

@add.error
async def add_error(ctx, message):
    mention = format(f"<@!{ctx.author.id}>")

    await ctx.send(f"ERROR: *CODE_1* - {mention} \n\n`You are missing an argument!`")


@bot.command(name='remove')
@commands.has_role('Dev Team Lead')
async def remove(ctx, user: discord.Member, message):
    role_names = [str(r) for r in user.roles]

    credit_emoji = '<:credits:937788738950545464>'
    role_credit_value = credit_counter.credit_counter(role_names)
    var_credit_value = message
    credit_value = (int(role_credit_value) - int(var_credit_value))
    mention = format(f"<@!{user.id}>")

    await ctx.send(f"Transfered {credit_emoji}`{var_credit_value}` from `user-id: {user.id}`.\n\n"
                   f"{mention} now has {credit_emoji}`{credit_value}`.")

@remove.error
async def remove_error(ctx, message):
    mention = format(f"<@!{ctx.author.id}>")

    await ctx.send(f"ERROR: *CODE_1* - {mention} \n\n`You are missing an argument!`")

@bot.command(name='credits')
async def thing_for_roles(ctx):
    role_names = [str(r) for r in ctx.author.roles]

    credit_emoji = '<:credits:937788738950545464>'
    credit_value = credit_counter.credit_counter(role_names)
    mention = format(f"<@!{ctx.author.id}>")

    await ctx.send(f"{mention}, You have {credit_emoji}`{credit_value}`.")


@bot.command(name='store')
async def store(ctx):
    await ctx.send(assets.store_command(format(ctx.author.id)))


@bot.command(name='shop')
async def shop(ctx):
    await ctx.send(assets.shop_command(format(ctx.author.id)))


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
