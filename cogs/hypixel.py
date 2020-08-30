import discord
import os
import sys
import random
import asyncio
import time
import requests
import hypixel
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()
apikey = "a54ce218-4fd5-4798-9b4b-6c74efac3456"


class Hypixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['generalhelp'])
    async def general(self, ctx, *, message):
        invalid = False
        try:

            invalid = False
            data = requests.get(
                f"https://api.hypixel.net/player?key={apikey}&name={message.lower()}"
            ).json()
            rank = "NA"
            name = data["player"]["displayname"]
            full = f"[{rank}] {name}"
            firstlogin = time.strftime(
                "%D %H:%M",
                time.localtime(
                    int(str(data["player"]["firstLogin"]).strip()[0:9])))
            lastlogin = time.strftime(
                "%D %H:%M",
                time.localtime(
                    int(str(data["player"]["lastLogin"]).strip()[0:9])))
            pastusernames = ','.join(data["player"]["knownAliases"])
        except:
            invalid = True

        if invalid == True:
            embedVar = discord.Embed(
                title=":no_entry_sign: Something went wrong", color=13381166)
            embedVar.set_footer(text=footer)
            await ctx.send(embed=embedVar)
        elif invalid == False:
            embedVar = discord.Embed(title="Hypixel Stats - General [BETA]",
                                     description=f"{full}",
                                     color=15105570)
            embedVar.add_field(name=":shield: Mod",
                               value=f"`{ctx.prefix}help moderation`",
                               inline=False)

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