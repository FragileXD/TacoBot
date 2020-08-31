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
apikey = "***REMOVED***"


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
            try:
                rank = data["player"]["prefix"]
                rank = rank.replace("§c", "")
                rank = rank.replace("§e", "")
                rank = rank.replace("§a", "")
                rank = rank.replace("§b", "")
                rank = rank.replace("§9", "")
                rank = rank.replace("§d", "")
                rank = rank.replace("§4", "")
                rank = rank.replace("§7", "")
                rank = rank.replace("§4", "")
                rank = rank.replace("§6", "")
                rank = rank.replace("§2", "")
                rank = rank.replace("§3", "")
                rank = rank.replace("§1", "")
                rank = rank.replace("§5", "")
                rank = rank.replace("§8", "")
                rank = rank.replace("§0", "")
                rank = rank.replace("§1", "")
                rank = rank.replace("§m", "")
                rank = rank.replace("§n", "")
                rank = rank.replace("§o", "")
                rank = rank.replace("§k", "")
                rank = rank.replace("§r", "")
                rank = rank.replace("[", "")
                rank = rank.replace("]", "")
            except:
                try:
                    rank = data["player"]["rank"]
                except:
                    try:
                        rank = data["player"]["monthlyPackageRank"]
                        rank = rank.replace("SUPERSTAR", "MVP++")
                    except:
                        try:
                            rank = data["player"]["packageRank"]
                            rank = rank.replace("_PLUS", "+")
                        except:
                            try:
                                rank = data["player"]["newPackageRank"]
                                rank = rank.replace("_PLUS", "+")
                            except:
                                rank = "NON"
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
            embedVar = discord.Embed(
                title="Hypixel Stats - General [BETA]",
                description=f"{full}",
                url=f"http://hypixel.net/player/{message}",
                color=15105570)
            embedVar.add_field(name="First • Last Login",
                               value=f"``{firstlogin} • {lastlogin}``",
                               inline=True)
            embedVar.add_field(name="Past usernames",
                               value=f"``{pastusernames}``",
                               inline=True)

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