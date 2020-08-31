import discord
import os
import sys
import random
import asyncio
import time
import requests
import math
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
        data = requests.get(
            f"https://api.hypixel.net/player?key={apikey}&name={message.lower()}"
        ).json()
        if data["success"] == True and data["player"] != None:
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
                            rank = data["player"]["newPackageRank"]
                            rank = rank.replace("_PLUS", "+")
                        except:
                            try:
                                rank = data["player"]["packageRank"]
                                rank = rank.replace("_PLUS", "+")
                            except:
                                rank = "NON"
            networkExp = data["player"]["networkExp"]
            uuid = data["player"]["uuid"]
            networkLevel = (math.sqrt(networkExp + 15312.5) -
                            125 / math.sqrt(2)) / (25 * math.sqrt(2))
            networkLevel = round(networkLevel, 2)
            name = data["player"]["displayname"]
            full = f"[{rank}] {name}"
            firstloginunix = data["player"]["firstLogin"]
            firstlogin = time.strftime(
                '%Y-%m-%d %H:%M:%S',
                time.localtime(int(firstloginunix) / 1000.0))
            try:
                lastloginunix = data["player"]["lastLogin"]
                lastlogin = time.strftime(
                    '%Y-%m-%d %H:%M:%S',
                    time.localtime(int(lastloginunix) / 1000.0))
            except:
                pass
            pastusernames = ', '.join(data["player"]["knownAliases"])
            karma = data["player"]["karma"]
            achievementPoints = data["player"]["achievementPoints"]
            guild = requests.get(
                f"https://api.hypixel.net/guild?key={apikey}&player={uuid}"
            ).json()
            if guild["success"] == True:
                try:
                    guildtag = guild["guild"]["tag"]
                    full = f"[{rank}] {name} [{guildtag}]"
                except:
                    full = f"[{rank}] {name} [No Guild Tag]"

            try:
                friends = requests.get(
                    f"https://api.hypixel.net/friends?key={apikey}&uuid={uuid}"
                ).json()
                friendlen = len(list(friends["records"]))
            except:
                friends = 0

        if data["success"] == False:
            embedVar = discord.Embed(
                title=":no_entry_sign: Something went wrong", color=13381166)
            error = data["cause"]
            embedVar.add_field(name="Error", value=f"``{error}``", inline=True)
            embedVar.set_footer(text=footer)
            await ctx.send(embed=embedVar)
        elif data["player"] == None:
            embedVar = discord.Embed(
                title=":no_entry_sign: Something went wrong", color=13381166)
            error = data["cause"]
            embedVar.add_field(name="Error",
                               value=f"``❌ The player is probably banned``",
                               inline=True)
            embedVar.set_footer(text=footer)
            await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(
                title=f"{full}",
                url=f"http://hypixel.net/player/{message}",
                color=15105570)
            embedVar.set_author(name="Hypixel Stats - General [BETA]")
            embedVar.add_field(name="UUID", value=f"``{uuid}``", inline=True)
            embedVar.add_field(name="Network Level",
                               value=f"``{networkLevel}``",
                               inline=True)
            embedVar.add_field(name="Network Exp",
                               value=f"``{networkExp}``",
                               inline=True)
            embedVar.add_field(name="Karma", value=f"``{karma}``", inline=True)
            embedVar.add_field(name="Friends",
                               value=f"``{friendlen}``",
                               inline=True)
            embedVar.add_field(name="Achivement Points",
                               value=f"``{achievementPoints}``",
                               inline=True)
            try:
                embedVar.add_field(name="First • Last Login",
                                   value=f"``{firstlogin} • {lastlogin}``",
                                   inline=True)
            except:
                embedVar.add_field(name="First Login",
                                   value=f"``{firstlogin}``",
                                   inline=True)
            embedVar.add_field(name="Past usernames",
                               value=f"``{pastusernames}``",
                               inline=True)

            embedVar.set_thumbnail(
                url=f"https://crafatar.com/avatars/{uuid}"
            )  #alternatives: https://crafatar.com/avatars/uuid https://crafatar.com/renders/head/uuid https://crafatar.com/renders/body/uuid
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