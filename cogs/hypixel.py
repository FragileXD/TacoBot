import discord
import os
import sys
import random
import asyncio
import time
import hypixel
import requests
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()
apikey = "a54ce218-4fd5-4798-9b4b-6c74efac3456"


def General(username):
    data = requests.get(
        f"https://api.hypixel.net/player?key={apikey}&name={username}").json()
    if "rank" in data["player"] and data["player"]["rank"] != "NORMAL":
        rank = data["player"]["rank"]
    elif "newPackageRank" in data["player"]:
        rank = data["player"]["newPackageRank"]
    elif "packageRank" in data["player"]:
        rank = data["player"]["packageRank"]
    else:
        rank = "Non"
    name = data["player"]["displayname"]
    full = f"[{rank},{name}]"
    firstlogin = time.strftime(
        "%D %H:%M",
        time.localtime(int(data["player"]["firstLogin"].strip()[0:9])))
    lastlogin = time.strftime(
        "%D %H:%M",
        time.localtime(int(data["player"]["lastLogin"].strip()[0:9])))
    pastusernames = ','.join(data["player"]["knownAliases"])


class Hypixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['alias'])
    async def general(self, ctx, *, message):
        pass
        @meme.error
    async def meme_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            message_author = ctx.author
            print("{} issued .meme 😎".format(message_author))

           
        else:
            raise (error)


def setup(bot):
    bot.add_cog(Hypixel(bot))