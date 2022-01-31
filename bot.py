# bot.py
import os
import time
import sys
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

full_id_250 = ["<Role id=935533280181252137 name='level 250'>"]
full_id_500 = ["<Role id=935533364197355570 name='level 500'>", "<Role id=935533530409205781 name='other medal 1'>"]
full_id_750 = ["<Role id=935533407822315531 name='level 750'>", "<Role id=935533610889527348 name='other medal 2'>"]
full_id_1000 = ["<Role id=935533475249946644 name='level 1000'>"]

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

@bot.command(name='shutdown')
async def shutdown(ctx):
    await ctx.send("```41st://<utilities> ~ Shutdown in 5```")
    time.sleep(1)
    await ctx.send("```41st://<utilities> ~ Shutdown in 4```")
    time.sleep(1)
    await ctx.send("```41st://<utilities> ~ Shutdown in 3```")
    time.sleep(1)
    await ctx.send("```41st://<utilities> ~ Shutdown in 2```")
    time.sleep(1)
    await ctx.send("```41st://<utilities> ~ Shutdown in 1```")
    time.sleep(1)
    await ctx.send("o7")
    sys.exit()

@bot.command(name='hard-shutdown')
async def shutdown(ctx):
    await ctx.send("```41st://<utilities> ~ HARD-SHUTDOWN```")
    time.sleep(1)
    sys.exit()

@bot.command(name='credits')
async def thing_for_roles(ctx):

    global value1, value2, value3, value4

    print(ctx.author.roles)

    role_names = [role.name for discord.RoleTags in ctx.author.roles]
    role_ids_pre = [str(r) for r in ctx.author.roles]
    role_ids = " "

    for i in role_ids_pre:
        role_ids += str(i) + " "

    print(role_names)
    print(role_ids)
    print(role_ids_pre)

    check_250 = any(item in role_ids_pre for item in names_250)
    check_500 = any(item in role_ids_pre for item in names_500)
    check_750 = any(item in role_ids_pre for item in names_750)
    check_1000 = any(item in role_ids_pre for item in names_1000)

    x_thing = [2, 3, 4, 5, 6, 7]
    count = 0
    for element in x_thing:
        count += 1



    return

    for i in role_ids_pre:
        if check_250 is True:
            await ctx.send("The list {} contains some elements of the list {}".format(role_ids_pre, check_250))
        elif check_500 is True:
            await ctx.send("The list {} contains some elements of the list {}".format(role_ids_pre, check_500))
        elif check_750 is True:
            await ctx.send("The list {} contains some elements of the list {}".format(role_ids_pre, check_750))
        elif check_1000 is True:
            await ctx.send("The list {} contains some elements of the list {}".format(role_ids_pre, check_1000))
        else:
            await ctx.send(f"No, {role_names} doesn't have any elements of the role value lists.")

    if names_250 in str(role_ids):
        value1 = 250
    elif names_500 in str(role_ids):
        value2 = 500
    elif names_750 in str(role_ids):
        value3 = 750
    elif names_1000 in str(role_ids):
        value4 = 1000
    else:
        await ctx.send("fuck")
        return

    value = value1 + value2 + value3 + value4

    await ctx.send(f"you are worth {value} credits")
    await ctx.send("fuck you")

def main():
    bot.run(TOKEN)
