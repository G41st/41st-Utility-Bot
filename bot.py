# bot.py
import os
import random
import overides
import discord
from discord.ext import commands
import discord.ext.commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client()

bot = commands.Bot(command_prefix='---')


@bot.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f"{bot.user.name} is connected!\n")
    print(f"{guild} is live.")


@bot.command(name='hello')
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send("hola")


bot.run(TOKEN)
