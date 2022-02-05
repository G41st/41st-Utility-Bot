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


@bot.command(name='welcome')
@commands.has_role('Commodore')
async def welcome_event_command(ctx):
    kyoda_mention = f"<@!583386313466708035>"
    forceps_mention = f"<@!173202312762884096>"

    await ctx.send("Hello Sir! Congradulations on Commodore! How are you...")
    time.sleep(3)
    await ctx.send("Wait...")
    time.sleep(3)
    await ctx.send("Sir, you didnt tell me that I was being unveiled. Oh well, here we go:")
    time.sleep(6)
    await ctx.send(f"Hello 41st!\n\n"
                   f"I am CT-1571, but you all will most likely know me by the *custom tailored* 41st Utility Discord "
                   f"Bot! Developed with love and care by {kyoda_mention}, I will be automating tasks throughout the "
                   f"server, to help ease the burden of {forceps_mention}. \n"
                   f"None of my commands are active at the moment, but they will be released soon! For now, just hold "
                   f"on, and ask your questions at the end of the meeting!\n\n"
                   f"Godspeed, my new brothers! \n <:GreenSalute:906047649982083113>")


@bot.command(name='kill')
@commands.has_role('Dev Team Lead')
async def shutdown(ctx):
    await ctx.send("```41st://<utilities> ~ $``` \n `HARD-SHUTDOWN`")
    time.sleep(1)
    sys.exit()


def main():
    bot.run(TOKEN_TEST)
