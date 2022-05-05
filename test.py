import os
import sys
import time
import datetime

import discord
from discord.ext.commands import Bot
from discord import Intents
import discord.ui
import assets
import register_command
import role_analyze
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
embed_color = 0x144202


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


@bot.command(name='test')
async def suggestion_command(ctx):
    button1 = discord.ui.Button(label="hello", style=discord.ButtonStyle.green)
    button2 = discord.ui.Button(label="goodbye", style=discord.ButtonStyle.danger)

    select = discord.ui.Select(
        min_values=2,
        max_values=3,
        placeholder="Enter Tags",
        options=[
            discord.SelectOption(
                label="Army",
                description="Anything relating to Regiments, or ground game modes."
            ),
            discord.SelectOption(
                label="Navy",
                description="Anything relating to Wings or Space Gamemodes."
            ),
            discord.SelectOption(
                label="Logistics",
                description="Logistics"
            )
        ],
        row=2
    )

    async def select_callback(interaction):
        await interaction.response.send_message(view=view2)

    async def button1_callback(interaction):
        await interaction.response.send_message(f"You chose: {select.values}, {button1.label}")

    async def button2_callback(interaction):
        await interaction.response.send_message(f"You chose: {select.values}, {button2.label}")

    view1 = discord.ui.View()
    view2 = discord.ui.View()

    view1.add_item(select)
    view2.add_item(button1)
    view2.add_item(button2)
    select.callback = select_callback
    button1.callback = button1_callback
    button2.callback = button2_callback


    await ctx.send("hello", view=view1)


@bot.command(name='create-suggestion')
async def create_suggestion(ctx):
    channel = await ctx.author.create_dm()
    await ctx.send("dms lmao")


    async def button1_callback(interaction):
        await interaction.response.send_message("Ok. Thank you for your suggestion.")

    async def button2_callback(interaction):
        await interaction.response.send_message("Ok. Canceled. Please rerun the command to try again.")

    async def select_callback(interaction):
        await interaction.response.send_message("enter your suggestion:")
        suggestion_body_raw = await bot.wait_for('message')
        suggestion_body = suggestion_body_raw.content
        await channel.send(suggestion_body)
        await channel.send("here is a summary of your suggestion:")
        await channel.send(f"Title: **{suggestion_title}**\n"
                           f"Tags: {select.values}\n"
                           f"Description: \n```\n{suggestion_body}```")
        await channel.send("are you sure you want to post it?", view=view2)

    button1 = discord.ui.Button(label="Upload", style=discord.ButtonStyle.green)
    button2 = discord.ui.Button(label="Cancel", style=discord.ButtonStyle.danger)

    select = discord.ui.Select(
        max_values=4,
        placeholder="Tags",
        options=[
            discord.SelectOption(
                label="Army", description="Anything relating to Regiments, or ground game modes."),
            discord.SelectOption(
                label="Navy", description="Anything relating to Wings or Ship game modes."),
            discord.SelectOption(
                label="Logistics", description="Anything relating to raid logs, attendance, etc."),
            discord.SelectOption(
                label="High Command Improvement", description="Any suggestions/recommendations/ideas for members of "
                                                              "high command that you wish to be public.")
        ]
    )

    view1 = discord.ui.View()
    view2 = discord.ui.View()
    view1.add_item(select)
    view2.add_item(button1)
    view2.add_item(button2)

    await channel.send("What is the title of your suggestion?")
    suggestion_title_raw = await bot.wait_for('message')
    suggestion_title = suggestion_title_raw.content
    await channel.send(view=view1)

    select.callback = select_callback
    button1.callback = button1_callback
    button2.callback = button2_callback



    parent_folder = os.getcwd()
    subfolder = 'suggestions'



    await channel.send(suggestion_title)
    print(suggestion_title)

    with open(f"{parent_folder}/{subfolder}/suggestion_number.txt", "r") as suggestion_number_file:
        old_ticket_number = int(suggestion_number_file.read())
        new_ticket_number = old_ticket_number + 1
        print(new_ticket_number)

#    with open(f"{parent_folder}/{subfolder}/{new_ticket_number}.txt", "w") as new_ticket_file:
 #       pass



def main():
    while True:
        bot.run(LAUNCH)


main()
