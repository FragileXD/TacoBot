import discord
import os
import sys
import random
import asyncio
import time
import requests
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()
apikey = "a54ce218-4fd5-4798-9b4b-6c74efac3456"
invalid = False


def General(username):
    global invalid
    invalid = False
    data = requests.get(
        f"https://api.hypixel.net/player?key={apikey}&name={username.lower()}"
    ).json()
    if "rank" in data["player"] and data["player"]["rank"] != "NORMAL":
        General.rank = data["player"]["rank"]
    elif "newPackageRank" in data["player"]:
        General.rank = data["player"]["newPackageRank"]
    elif "packageRank" in data["player"]:
        General.rank = data["player"]["packageRank"]
    else:
        General.rank = "Non"
    General.name = data["player"]["displayname"]
    General.full = f"[{General.rank}] {General.name}"
    General.firstlogin = time.strftime(
        "%D %H:%M",
        time.localtime(int(str(data["player"]["firstLogin"]).strip()[0:9])))
    General.lastlogin = time.strftime(
        "%D %H:%M",
        time.localtime(int(str(data["player"]["lastLogin"]).strip()[0:9])))
    General.pastusernames = ','.join(data["player"]["knownAliases"])


class Hypixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['generalhelp'])
    async def general(self, ctx, *, message):
        General(message)

        if invalid == True:
            embedVar = discord.Embed(
                title=":no_entry_sign: Something went wrong", color=13381166)
            embedVar.set_footer(text=footer)
            await ctx.send(embed=embedVar)
        elif invalid == False:
            embedVar = discord.Embed(title="Hypixel General Stats [BETA]",
                                     description=f"{General.full}",
                                     color=15105570)
            embedVar.add_field(name=":shield: Mod",
                               value=f"`{ctx.prefix}help moderation`")

            embedVar.set_footer(text=footer)
            await ctx.send(embed=embedVar)

    @general.error
    async def general_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)


def setup(bot):
    bot.add_cog(Hypixel(bot))