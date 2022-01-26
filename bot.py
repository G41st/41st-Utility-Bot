# bot.py
import os
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
bot = commands.Bot(command_prefix='---')


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


@bot.command(name='bruh')
async def on_message(message):
    if message.author == bot.user:
        return

    if "hello" in message.content:
        await message.channel.send("hello")
        print(message.content)
    else:
        await message.channel.send("fuck you")

@bot.command(name='test')
async def kick(self, message):
    await message.channel.send("bruh moment - ")
    await message.channel.send(str(message.content))


@bot.command(name='role')
@commands.has_permissions(administrator=True) #permissions
async def role(ctx, user : discord.Member, *, role : discord.Role):
  if role.position > ctx.author.top_role.position: #if the role is above users top role it sends error
    return await ctx.send('**:x: | That role is above your top role!**')
  if role in user.roles:
      await user.remove_roles(role) #removes the role if user already has
      await ctx.send(f"Removed {role} from {user.mention}")
  else:
      await user.add_roles(role) #adds role if not already has it
      await ctx.send(f"Added {role} to {user.mention}")

@role.error
async def role_error(ctx, error):
  if isinstance(error, MissingPermissions):
    await ctx.send('**:x: | You do not have permission to use this command!**')

names_250 = ['level 250']
names_500 = ['level 500', 'other medal 1']
names_750 = ['level 750', 'other medal 2']
names_1000 = ['level 1000']

@bot.command(name='value')
async def role(ctx, role : discord.Role):

    if str(role) in names_250:
        value = 250
    elif str(role) in names_500:
        value = 500
    elif str(role) in names_750:
        value = 750
    elif str(role) in names_1000:
        value = 1000
    else:
        ctx.send("this role does not have a value")
        return

    await ctx.send(f"{role} is worth {value} credits")
    await ctx.send("fuck you")

def main():
    bot.run(TOKEN)
