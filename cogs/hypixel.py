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
apikey = "***REMOVED***"


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


class Hypixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['alias'])
    async def commandname(self, ctx, *, message):
        pass


def setup(bot):
    bot.add_cog(Hypixel(bot))