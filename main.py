import discord
import os
import sys
import random
import time
import json
import praw
import asyncio
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta
from utils.data import getJSON

config = getJSON("config.json")

statusesplay = [
    ".help / >help | http://youtube.com/tacozlmao",
    "with the ban hammer | .help",
    "owo! twype .hewwlp for hwelp maaswter! :3",
    f"with {Bot.users}",
    "with my dog",
    "video games instead of working",
    "breaking the mental stability of tacoz",
]

statuseswatch = [
    "https://youtube.com/tacozlmao",
    "@everyone",
    f"{random.randint(1,10000)} errors",
    f"{str(len(Bot.users))} users",
    f"{str((len(Bot.guilds)))} servers",
    "the world burn",
    "everything 👀",
]

# CONFIG!
PREFIX = (".", ">")
TOKEN = config.token
OWNERID = config.ownerid
footer = "『 TacoBot ✦ Tacoz 』"
client = commands.Bot(command_prefix=PREFIX, owner_id=OWNERID, case_insensitive=True)


@client.event
async def cog_command_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Retry again in {int(error.retry_after/60)}s")


@client.event
async def on_ready():
    print(f"{client.user.name} is Launched")
    print(client.user.id)
    print("--------------")
    print("Servers connected to:")
    for guild in client.guilds:
        print(guild.name)
    print("--------------")
    while True:
        a = random.randint(1, 2)
        if a == 1:
            status = random.choice(statuseswatch)
            activity = discord.Activity(
                type=discord.ActivityType.watching,
                name=status,
            )
        elif a == 2:
            status = random.choice(statusesplay)
            activity = discord.Activity(
                type=discord.ActivityType.playing,
                name=status,
            )
        await client.change_presence(status=discord.Status.idle, activity=activity)
        await asyncio.sleep(random.randint(60, 180))


client.remove_command("help")
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        client.load_extension(f"cogs.{name}")

client.run(TOKEN, bot=True, reconnect=True)
