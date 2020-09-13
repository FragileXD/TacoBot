import discord
import os
import sys
import random
import asyncio
import time
import requests
import math
import locale
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

footer = "『 TacoBot ✦ Tacoz 』"
start_time = time.monotonic()
apikey = "a54ce218-4fd5-4798-9b4b-6c74efac3456"
locale.setlocale(locale.LC_ALL, "en_US")


class Hypixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["generalhelp"])
    @commands.cooldown(1, 5, commands.BucketType.user)
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
            networkLevel = (math.sqrt(networkExp + 15312.5) - 125 / math.sqrt(2)) / (
                25 * math.sqrt(2)
            )
            networkLevel = round(networkLevel, 2)
            name = data["player"]["displayname"]
            full = f"[{rank}] {name}"
            firstloginunix = data["player"]["firstLogin"]
            firstlogin = time.strftime(
                "%Y-%m-%d %H:%M", time.localtime(int(firstloginunix) / 1000.0)
            )
            try:
                lastloginunix = data["player"]["lastLogin"]
                lastlogin = time.strftime(
                    "%Y-%m-%d %H:%M", time.localtime(int(lastloginunix) / 1000.0)
                )
            except:
                pass
            pastusernames = ", ".join(data["player"]["knownAliases"])
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
                    full = f"[{rank}] {name}"

            try:
                friends = requests.get(
                    f"https://api.hypixel.net/friends?key={apikey}&uuid={uuid}"
                ).json()
                friendlen = len(list(friends["records"]))
            except:
                friends = 0

        if data["success"] == False:
            embedVar = discord.Embed(
                title=":no_entry_sign: Something went wrong", color=13381166
            )
            error = data["cause"]
            embedVar.add_field(name="Error", value=f"``{error}``", inline=True)
            embedVar.set_footer(text=footer)
            await ctx.send(embed=embedVar)
        elif data["player"] == None:
            embedVar = discord.Embed(
                title=":no_entry_sign: Something went wrong", color=13381166
            )
            error = data["cause"]
            embedVar.add_field(
                name="Error", value=f"``❌ The player is probably banned``", inline=True
            )
            embedVar.set_footer(text=footer)
            await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(
                title=f"{full}",
                url=f"http://hypixel.net/player/{message}",
                color=15105570,
            )
            embedVar.set_author(name="Hypixel Stats - General [BETA]")
            embedVar.add_field(name="UUID", value=f"``{uuid}``", inline=True)
            embedVar.add_field(
                name="Network Level", value=f"``{networkLevel}``", inline=True
            )
            embedVar.add_field(
                name="Network Exp", value=f"``{networkExp}``", inline=True
            )
            embedVar.add_field(name="Karma", value=f"``{karma}``", inline=True)
            embedVar.add_field(name="Friends", value=f"``{friendlen}``", inline=True)
            embedVar.add_field(
                name="Achivement Points", value=f"``{achievementPoints}``", inline=True
            )
            try:
                embedVar.add_field(
                    name="First • Last Login",
                    value=f"``{firstlogin} • {lastlogin} (EDT)``",
                    inline=True,
                )
            except:
                embedVar.add_field(
                    name="First Login", value=f"``{firstlogin} (EDT)``", inline=True
                )
            embedVar.add_field(
                name="Past usernames", value=f"``{pastusernames}``", inline=True
            )

            embedVar.set_thumbnail(
                url=f"https://crafatar.com/avatars/{uuid}?default=MHF_Steve&overlay"
            )  # alternatives: https://crafatar.com/avatars/uuid https://crafatar.com/renders/head/uuid https://crafatar.com/renders/body/uuid
            embedVar.set_footer(text=footer)
            await ctx.send(embed=embedVar)

    @general.error
    async def general_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)

    @commands.command(aliases=["watchdog", "banstats", "hypixelban"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def watchdogstats(self, ctx):
        watchdog = requests.get(
            f"https://api.hypixel.net/watchdogstats?key={apikey}"
        ).json()
        lastminute = watchdog["watchdog_lastMinute"]
        watchdogtotal = watchdog["watchdog_total"]
        watchdogdaily = watchdog["watchdog_rollingDaily"]
        staffdaily = watchdog["staff_rollingDaily"]
        stafftotal = watchdog["staff_total"]
        embedVar = discord.Embed(title=f"Hypixel Ban Stats", color=15105570)
        embedVar.add_field(
            name="Watchdog Bans",
            value=f"Last Minute - `{lastminute}`\nToday - `{watchdogdaily}`\nTotal - `{watchdogtotal}`",
            inline=True,
        )
        embedVar.add_field(
            name="Staff Bans",
            value=f"Today - `{staffdaily}`\nTotal - `{stafftotal}`",
            inline=True,
        )

        embedVar.set_thumbnail(
            url=f"https://render.namemc.com/skin/3d/body.png?skin=2d1f536e7e659774&model=classic&width=175&height=350"
        )
        embedVar.set_footer(text=footer)
        await ctx.send(embed=embedVar)

    @commands.command(
        aliases=["bedwarshelp", "bedwarsstats", "bedwarstats", "bedwarstat"]
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bedwars(self, ctx, msg: str):
        msg = msg.lower()
        data = requests.get(
            f"https://api.hypixel.net/player?key={apikey}&name={msg}"
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
            bwdata = data["player"]["stats"]["Bedwars"]
            bwlevel = data["player"]["achievements"]["bedwars_level"]
            bwcoins = bwdata["coins"]
            bwwinstreak = bwdata["winstreak"]
            bwwins = bwdata["wins_bedwars"]
            bwlosses = bwdata["losses_bedwars"]
            bwwinlossratio = round(bwwins / bwlosses, 2)
            bwkills = bwdata["kills_bedwars"]
            bwdeaths = bwdata["deaths_bedwars"]
            bwkdr = round(bwkills / bwdeaths, 2)
            try:
                bwfinalkills = bwdata["final_kills_bedwars"]
            except:
                bwfinalkills = 0
            try:
                bwfinaldeaths = bwdata["final_deaths_bedwars"]
            except:
                bwfinaldeaths = 0
            try:
                bwbedlost = bwdata["beds_lost_bedwars"]
            except:
                bwbedlost = 0
            try:
                bwbedbreak = bwdata["beds_broken_bedwars"]
            except:
                bwbedbreak = 0
            try:
                bblr = bwbedbreak / bwbedlost
            except:
                bblr = 0
            try:
                gamesplayed = bwdata["games_played_bedwars"]
            except:
                gamesplayed = 0
            try:
                finalspergame = bwfinalkills / gamesplayed
            except:
                finalspergame = 0
            try:
                bedspergame = bwbedbreak / gamesplayed
            except:
                bedspergame = 0
            try:
                bwfkdr = round(bwfinalkills / bwfinaldeaths, 2)
            except:
                bwfkdr = 0

            try:
                bwwinstreak1 = bwdata["eight_one_winstreak"]
            except:
                bwwinstreak1 = "N/A"
            try:
                bwwins1 = bwdata["eight_one_wins_bedwars"]
            except:
                bwwins1 = 0
            try:
                bwlosses1 = bwdata["eight_one_losses_bedwars"]
            except:
                bwlosses1 = 0
            try:
                bwkills1 = bwdata["eight_one_kills_bedwars"]
            except:
                bwkills1 = 0
            try:
                bwdeaths1 = bwdata["eight_one_deaths_bedwars"]
            except:
                bwdeaths1 = 0
            try:
                bwkdr1 = round(bwkills1 / bwdeaths1, 2)
            except:
                bwkdr1 = 0
            try:
                bwfinalkills1 = bwdata["eight_one_final_kills_bedwars"]
            except:
                bwfinalkills1 = 0
            try:
                bwfinaldeaths1 = bwdata["eight_one_final_deaths_bedwars"]
            except:
                bwfinaldeaths1 = 0
            try:
                bwfkdr1 = round(bwfinalkills1 / bwfinaldeaths1, 2)
            except:
                bwfkdr1 = 0
            try:
                bwbedlost1 = bwdata["eight_one_beds_lost_bedwars"]
            except:
                bwbedlost1 = 0
            try:
                bwbedbreak1 = bwdata["eight_one_beds_broken_bedwars"]
            except:
                bwbedbreak1 = 0
            try:
                gamesplayed1 = bwdata["eight_one_games_played_bedwars"]
            except:
                gamesplayed1 = 0
            try:
                bblr1 = bwbedbreak1 / bwbedlost1
            except:
                bblr1 = 0
            try:
                finalspergame1 = bwfinalkills1 / gamesplayed1
            except:
                finalspergame1 = 0
            try:
                bedspergame1 = bwbedbreak1 / gamesplayed1
            except:
                bedspergame1 = 0
            try:
                bwwinlossratio1 = round(bwwins1 / bwlosses1, 2)
            except:
                bwwinlossratio1 = 0

            try:
                bwwinstreak2 = bwdata["eight_two_winstreak"]
            except:
                bwwinstreak2 = 0
            try:
                bwwins2 = bwdata["eight_two_wins_bedwars"]
            except:
                bwwins2 = 0
            try:
                bwlosses2 = bwdata["eight_two_losses_bedwars"]
            except:
                bwlosses2 = 0
            try:
                bwwinlossratio2 = round(bwwins2 / bwlosses2, 2)
            except:
                bwwinlossratio2 = 0
            try:
                bwkills2 = bwdata["eight_two_kills_bedwars"]
            except:
                bwkills2 = 0
            try:
                bwdeaths2 = bwdata["eight_two_deaths_bedwars"]
            except:
                bwdeaths2 = 0
            try:
                bwkdr2 = round(bwkills2 / bwdeaths2, 2)
            except:
                bwkdr2 = 0
            try:
                bwfinalkills2 = bwdata["eight_two_final_kills_bedwars"]
            except:
                bwdeaths2 = 0
            try:
                bwfinaldeaths2 = bwdata["eight_two_final_deaths_bedwars"]
            except:
                bwfinaldeaths2 = 0
            try:
                bwfkdr2 = round(bwfinalkills2 / bwfinaldeaths2, 2)
            except:
                bwfkdr2 = 0
            try:
                bwbedlost2 = bwdata["eight_two_beds_lost_bedwars"]
            except:
                bwbedlost2 = 0
            try:
                bwbedbreak2 = bwdata["eight_two_beds_broken_bedwars"]
            except:
                bwbedbreak2 = 0
            try:
                bblr2 = bwbedbreak2 / bwbedlost2
            except:
                bblr2 = 0
            try:
                gamesplayed2 = bwdata["eight_two_games_played_bedwars"]
            except:
                gamesplayed2 = 0
            try:
                finalspergame2 = bwfinalkills2 / gamesplayed2
            except:
                finalspergame2 = 0
            try:
                bedspergame2 = bwbedbreak2 / gamesplayed2
            except:
                bedspergame2 = 0

            try:
                bwwinstreak3 = bwdata["four_three_winstreak"]
            except:
                bwwinstreak3 = 0
            try:
                bwwins3 = bwdata["four_three_wins_bedwars"]
            except:
                bwwins3 = 0
            try:
                bwlosses3 = bwdata["four_three_losses_bedwars"]
            except:
                bwlosses3 = 0
            try:
                bwwinlossratio3 = round(bwwins3 / bwlosses3, 2)
            except:
                bwwinlossratio3 = 0
            try:
                bwkills3 = bwdata["four_three_kills_bedwars"]
            except:
                bwkills3 = 0
            try:
                bwdeaths3 = bwdata["four_three_deaths_bedwars"]
            except:
                bwdeaths3 = 0
            try:
                bwkdr3 = round(bwkills3 / bwdeaths3, 2)
            except:
                bwkdr3 = 0
            try:
                bwfinalkills3 = bwdata["four_three_final_kills_bedwars"]
            except:
                bwfinalkills3 = 0
            try:
                bwfinaldeaths3 = bwdata["four_three_final_deaths_bedwars"]
            except:
                bwfinaldeaths3 = 0
            try:
                bwfkdr3 = round(bwfinalkills3 / bwfinaldeaths3, 2)
            except:
                bwfkdr3 = 0
            try:
                bwbedlost3 = bwdata["four_three_beds_lost_bedwars"]
            except:
                bwbedlost3 = 0
            try:
                bwbedbreak3 = bwdata["four_three_beds_broken_bedwars"]
            except:
                bwbedbreak3 = 0
            try:
                bblr3 = bwbedbreak3 / bwbedlost3
            except:
                bblr3 = 0
            try:
                gamesplayed3 = bwdata["four_three_games_played_bedwars"]
            except:
                gamesplayed3 = 0
            try:
                finalspergame3 = bwfinalkills3 / gamesplayed3
            except:
                finalspergame3 = 0
            try:
                bedspergame3 = bwbedbreak3 / gamesplayed3
            except:
                bedspergame3 = 0

            try:
                bwwinstreak4 = bwdata["four_four_winstreak"]
            except:
                bwwinstreak4 = 0
            try:
                bwwins4 = bwdata["four_four_wins_bedwars"]
            except:
                bwwins4 = 0
            try:
                bwlosses4 = bwdata["four_four_losses_bedwars"]
            except:
                bwlosses4 = 0
            try:
                bwwinlossratio4 = round(bwwins4 / bwlosses4, 2)
            except:
                bwwinlossratio4 = 0
            try:
                bwkills4 = bwdata["four_four_kills_bedwars"]
            except:
                bwkills4 = 0
            try:
                bwdeaths4 = bwdata["four_four_deaths_bedwars"]
            except:
                bwdeaths4 = 0
            try:
                bwkdr4 = round(bwkills4 / bwdeaths4, 2)
            except:
                bwkdr4 = 0
            try:
                bwfinalkills4 = bwdata["four_four_final_kills_bedwars"]
            except:
                bwfinalkills4 = 0
            try:
                bwfinaldeaths4 = bwdata["four_four_final_deaths_bedwars"]
            except:
                bwfinaldeaths4 = 0
            try:
                bwfkdr4 = round(bwfinalkills4 / bwfinaldeaths4, 2)
            except:
                bwfkdr4 = 0
            try:
                bwbedlost4 = bwdata["four_four_beds_lost_bedwars"]
            except:
                bwbedlost4 = 0
            try:
                bwbedbreak4 = bwdata["four_four_beds_broken_bedwars"]
            except:
                bwbedbreak4 = 0
            try:
                bblr4 = bwbedbreak4 / bwbedlost4
            except:
                bblr4 = 0
            try:
                gamesplayed4 = bwdata["four_four_games_played_bedwars"]
            except:
                gamesplayed4 = 0
            try:
                finalspergame4 = bwfinalkills4 / gamesplayed4
            except:
                finalspergame4 = 0
            try:
                bedspergame4 = bwbedbreak4 / gamesplayed4
            except:
                bedspergame4 = 0

            try:
                bwwinstreak4v4 = bwdata["two_four_winstreak"]
            except:
                bwwinstreak4v4 = 0
            try:
                bwwins4v4 = bwdata["two_four_wins_bedwars"]
            except:
                bwwins4v4 = 0
            try:
                bwlosses4v4 = bwdata["two_four_losses_bedwars"]
            except:
                bwlosses4v4 = 0
            try:
                bwwinlossratio4v4 = round(bwwins4v4 / bwlosses4v4, 2)
            except:
                bwwinlossratio4v4 = 0
            try:
                bwkills4v4 = bwdata["two_four_kills_bedwars"]
            except:
                bwkills4v4 = 0
            try:
                bwdeaths4v4 = bwdata["two_four_deaths_bedwars"]
            except:
                bwdeaths4v4 = 0
            try:
                bwkdr4v4 = round(bwkills4v4 / bwdeaths4v4, 2)
            except:
                bwkdr4v4 = 0
            try:
                bwfinalkills4v4 = bwdata["two_four_final_kills_bedwars"]
            except:
                bwfinalkills4v4 = 0
            try:
                bwfinaldeaths4v4 = bwdata["two_four_final_deaths_bedwars"]
            except:
                bwfinaldeaths4v4 = 0
            try:
                bwfkdr4v4 = round(bwfinalkills4v4 / bwfinaldeaths4v4, 2)
            except:
                bwfkdr4v4 = 0
            try:
                bwbedlost4v4 = bwdata["two_four_beds_lost_bedwars"]
            except:
                bwbedlost4v4 = 0
            try:
                bwbedbreak4v4 = bwdata["two_four_beds_broken_bedwars"]
            except:
                bwbedbreak4v4 = 0
            try:
                bblr4v4 = bwbedbreak4v4 / bwbedlost4v4
            except:
                bblr4v4 = 0
            try:
                gamesplayed4v4 = bwdata["two_four_games_played_bedwars"]
            except:
                gamesplayed4v4 = 0
            try:
                finalspergame4v4 = bwfinalkills4v4 / gamesplayed4v4
            except:
                finalspergame4v4 = 0
            try:
                bedspergame4v4 = bwbedbreak4v4 / gamesplayed4v4
            except:
                bedspergame4v4 = 0

            bblr = round(bblr, 2)
            bblr1 = round(bblr1, 2)
            bblr2 = round(bblr2, 2)
            bblr3 = round(bblr3, 2)
            bblr4 = round(bblr4, 2)
            bblr4v4 = round(bblr4v4, 2)

            finalspergame = round(finalspergame, 2)
            finalspergame1 = round(finalspergame1, 2)
            finalspergame2 = round(finalspergame2, 2)
            finalspergame3 = round(finalspergame3, 2)
            finalspergame4 = round(finalspergame4, 2)
            finalspergame4v4 = round(finalspergame4v4, 2)

            bedspergame = round(bedspergame, 2)
            bedspergame1 = round(bedspergame1, 2)
            bedspergame2 = round(bedspergame2, 2)
            bedspergame3 = round(bedspergame3, 2)
            bedspergame4 = round(bedspergame4, 2)
            bedspergame4v4 = round(bedspergame4v4, 2)

        if data["success"] == False:
            embedVar = discord.Embed(
                title=":no_entry_sign: Something went wrong", color=13381166
            )
            error = data["cause"]
            embedVar.add_field(name="Error", value=f"``{error}``", inline=True)
            embedVar.set_footer(text=footer)
            await ctx.send(embed=embedVar)
        elif data["player"] == None:
            embedVar = discord.Embed(
                title=":no_entry_sign: Something went wrong", color=13381166
            )
            error = data["cause"]
            embedVar.add_field(
                name="Error", value=f"``❌ The player is probably banned``", inline=True
            )
            embedVar.set_footer(text=footer)
            await ctx.send(embed=embedVar)
        else:
            displayname = data["player"]["displayname"]
            full = f"[{rank}] {displayname}"
            uuid = data["player"]["uuid"]

            embedVar = discord.Embed(
                title=f"{full}",
                color=15105570,
                url=f"https://hypixel.net/player/{msg}",
            )
            embedVar.set_author(
                name="Overall Bedwars Stats",
                icon_url="https://statsify.net/img/assets/hypixel/bedwars.png",
            )
            embedVar.add_field(name="Stars", value=f"``{bwlevel}☆``", inline=True)
            try:
                embedVar.add_field(name="Coins", value=f"``{bwcoins:,}``", inline=True)
            except:
                embedVar.add_field(name="Coins", value=f"``{bwcoins}``", inline=True)
            try:
                embedVar.add_field(
                    name="Winstreak", value=f"``{bwwinstreak:,}``", inline=True
                )
            except:
                embedVar.add_field(
                    name="Winstreak", value=f"``{bwwinstreak}``", inline=True
                )
            embedVar.add_field(name="Wins", value=f"``{bwwins}``", inline=True)
            try:
                embedVar.add_field(
                    name="Losses", value=f"``{bwlosses:,}``", inline=True
                )
            except:
                embedVar.add_field(name="Losses", value=f"``{bwlosses}``", inline=True)
            try:
                embedVar.add_field(
                    name="Win Loss Ratio", value=f"``{bwwinlossratio:,}``", inline=True
                )
            except:
                embedVar.add_field(
                    name="Win Loss Ratio", value=f"``{bwwinlossratio}``", inline=True
                )
            try:
                embedVar.add_field(name="Kills", value=f"``{bwkills:,}``", inline=True)
            except:
                embedVar.add_field(name="Kills", value=f"``{bwkills}``", inline=True)
            try:
                embedVar.add_field(
                    name="Deaths", value=f"``{bwdeaths:,}``", inline=True
                )
            except:
                embedVar.add_field(name="Deaths", value=f"``{bwdeaths}``", inline=True)
            embedVar.add_field(name="KDR", value=f"``{bwkdr}``", inline=True)
            try:
                embedVar.add_field(
                    name="Final Kills", value=f"``{bwfinalkills:,}``", inline=True
                )
            except:
                embedVar.add_field(
                    name="Final Kills", value=f"``{bwfinalkills}``", inline=True
                )
            try:
                embedVar.add_field(
                    name="Final Deaths", value=f"``{bwfinaldeaths:,}``", inline=True
                )
            except:
                embedVar.add_field(
                    name="Final Deaths", value=f"``{bwfinaldeaths}``", inline=True
                )
            try:
                embedVar.add_field(
                    name="Final KDR", value=f"``{bwfkdr:,}``", inline=True
                )
            except:
                embedVar.add_field(name="Final KDR", value=f"``{bwfkdr}``", inline=True)
            try:
                embedVar.add_field(
                    name="Beds Lost", value=f"``{bwbedlost:,}``", inline=True
                )
            except:
                embedVar.add_field(
                    name="Beds Lost", value=f"``{bwbedlost}``", inline=True
                )
            try:
                embedVar.add_field(
                    name="Beds Broken", value=f"``{bwbedbreak:,}``", inline=True
                )
            except:
                embedVar.add_field(
                    name="Beds Broken", value=f"``{bwbedbreak}``", inline=True
                )
            try:
                embedVar.add_field(name="BBLR", value=f"``{bblr:,}``", inline=True)
            except:
                embedVar.add_field(name="BBLR", value=f"``{bblr}``", inline=True)
            try:
                embedVar.add_field(
                    name="Finals/Game", value=f"``{finalspergame:,}``", inline=True
                )
            except:
                embedVar.add_field(
                    name="Finals/Game", value=f"``{finalspergame}``", inline=True
                )
            try:
                embedVar.add_field(
                    name="Beds/Game", value=f"``{bedspergame:,}``", inline=True
                )
            except:
                embedVar.add_field(
                    name="Beds/Game", value=f"``{bedspergame}``", inline=True
                )
            try:
                embedVar.add_field(
                    name="Games Played", value=f"``{gamesplayed:,}``", inline=True
                )
            except:
                embedVar.add_field(
                    name="Games Played", value=f"``{gamesplayed}``", inline=True
                )

            solo = discord.Embed(
                title=f"{full}",
                color=15105570,
                url=f"https://hypixel.net/player/{msg}",
            )
            solo.set_author(
                name="Overall Bedwars Stats",
                icon_url="https://statsify.net/img/assets/hypixel/bedwars.png",
            )
            solo.add_field(name="Stars", value=f"``{bwlevel}☆``", inline=True)
            try:
                solo.add_field(name="Coins", value=f"``{bwcoins:,}``", inline=True)
            except:
                solo.add_field(name="Coins", value=f"``{bwcoins}``", inline=True)
            try:
                solo.add_field(
                    name="Winstreak", value=f"``{bwwinstreak:,}``", inline=True
                )
            except:
                solo.add_field(
                    name="Winstreak", value=f"``{bwwinstreak}``", inline=True
                )
            solo.add_field(name="Wins", value=f"``{bwwins}``", inline=True)
            try:
                solo.add_field(name="Losses", value=f"``{bwlosses:,}``", inline=True)
            except:
                solo.add_field(name="Losses", value=f"``{bwlosses}``", inline=True)
            try:
                solo.add_field(
                    name="Win Loss Ratio", value=f"``{bwwinlossratio:,}``", inline=True
                )
            except:
                solo.add_field(
                    name="Win Loss Ratio", value=f"``{bwwinlossratio}``", inline=True
                )
            try:
                solo.add_field(name="Kills", value=f"``{bwkills:,}``", inline=True)
            except:
                solo.add_field(name="Kills", value=f"``{bwkills}``", inline=True)
            try:
                solo.add_field(name="Deaths", value=f"``{bwdeaths:,}``", inline=True)
            except:
                solo.add_field(name="Deaths", value=f"``{bwdeaths}``", inline=True)
            solo.add_field(name="KDR", value=f"``{bwkdr}``", inline=True)
            try:
                solo.add_field(
                    name="Final Kills", value=f"``{bwfinalkills:,}``", inline=True
                )
            except:
                solo.add_field(
                    name="Final Kills", value=f"``{bwfinalkills}``", inline=True
                )
            try:
                solo.add_field(
                    name="Final Deaths", value=f"``{bwfinaldeaths:,}``", inline=True
                )
            except:
                solo.add_field(
                    name="Final Deaths", value=f"``{bwfinaldeaths}``", inline=True
                )
            try:
                solo.add_field(name="Final KDR", value=f"``{bwfkdr:,}``", inline=True)
            except:
                solo.add_field(name="Final KDR", value=f"``{bwfkdr}``", inline=True)
            try:
                solo.add_field(
                    name="Beds Lost", value=f"``{bwbedlost:,}``", inline=True
                )
            except:
                solo.add_field(name="Beds Lost", value=f"``{bwbedlost}``", inline=True)
            try:
                solo.add_field(
                    name="Beds Broken", value=f"``{bwbedbreak:,}``", inline=True
                )
            except:
                solo.add_field(
                    name="Beds Broken", value=f"``{bwbedbreak}``", inline=True
                )
            try:
                solo.add_field(name="BBLR", value=f"``{bblr:,}``", inline=True)
            except:
                solo.add_field(name="BBLR", value=f"``{bblr}``", inline=True)
            try:
                solo.add_field(
                    name="Finals/Game", value=f"``{finalspergame:,}``", inline=True
                )
            except:
                solo.add_field(
                    name="Finals/Game", value=f"``{finalspergame}``", inline=True
                )
            try:
                solo.add_field(
                    name="Beds/Game", value=f"``{bedspergame:,}``", inline=True
                )
            except:
                solo.add_field(
                    name="Beds/Game", value=f"``{bedspergame}``", inline=True
                )
            try:
                solo.add_field(
                    name="Games Played", value=f"``{gamesplayed:,}``", inline=True
                )
            except:
                solo.add_field(
                    name="Games Played", value=f"``{gamesplayed}``", inline=True
                )

            solo.set_thumbnail(
                url=f"https://crafatar.com/avatars/{uuid}?default=MHF_Steve&overlay"
            )  # alternatives: https://crafatar.com/avatars/uuid https://crafatar.com/renders/head/uuid https://crafatar.com/renders/body/uuid
            solo.set_footer(text=footer)
            doubles.set_thumbnail(
                url=f"https://crafatar.com/avatars/{uuid}?default=MHF_Steve&overlay"
            )  # alternatives: https://crafatar.com/avatars/uuid https://crafatar.com/renders/head/uuid https://crafatar.com/renders/body/uuid
            doubles.set_footer(text=footer)
            threes.set_thumbnail(
                url=f"https://crafatar.com/avatars/{uuid}?default=MHF_Steve&overlay"
            )  # alternatives: https://crafatar.com/avatars/uuid https://crafatar.com/renders/head/uuid https://crafatar.com/renders/body/uuid
            threes.set_footer(text=footer)
            fours.set_thumbnail(
                url=f"https://crafatar.com/avatars/{uuid}?default=MHF_Steve&overlay"
            )  # alternatives: https://crafatar.com/avatars/uuid https://crafatar.com/renders/head/uuid https://crafatar.com/renders/body/uuid
            fours.set_footer(text=footer)
            fours2.set_thumbnail(
                url=f"https://crafatar.com/avatars/{uuid}?default=MHF_Steve&overlay"
            )  # alternatives: https://crafatar.com/avatars/uuid https://crafatar.com/renders/head/uuid https://crafatar.com/renders/body/uuid
            fours2.set_footer(text=footer)
            embedVar.set_thumbnail(
                url=f"https://crafatar.com/avatars/{uuid}?default=MHF_Steve&overlay"
            )  # alternatives: https://crafatar.com/avatars/uuid https://crafatar.com/renders/head/uuid https://crafatar.com/renders/body/uuid
            embedVar.set_footer(text=footer)

            message = await ctx.send(embed=embedVar)
            selected2 = 0

            def checkselection(selected, parameter):
                selected = selected + parameter
                if selected > 5:
                    selected2 = 0
                elif selected < 0:
                    selected2 = 5

            await message.add_reaction("◀")
            await message.add_reaction("▶")
            await message.add_reaction("⏹")

            def check(reaction, user):
                return user == message.author and (
                    str(reaction.emoji) == "◀"
                    or str(reaction.emoji) == "▶"
                    or str(reaction.emoji) == "⏹"
                )

            e = True

            while e == True:
                try:
                    reaction1, user = await self.bot.wait_for(
                        "reaction_add", timeout=60.0, check=check
                    )
                except asyncio.TimeoutError:
                    e = False  # no reaction recieved, e is set to false
                else:
                    if reaction1 == "◀":
                        checkselection(selected2, -1)
                        if selected2 == 0:
                            await message.edit(content=embedVar)
                        elif selected2 == 1:
                            await message.edit(content=solo)
                        elif selected2 == 2:
                            await message.edit(content=doubles)
                        elif selected2 == 3:
                            await message.edit(content=threes)
                        elif selected2 == 4:
                            await message.edit(content=fours)
                        elif selected2 == 5:
                            await message.edit(content=fours2)
                        else:
                            pass
                        await message.remove_reaction("◀", user)
                    elif reaction1 == "▶":
                        checkselection(selected2, +1)
                        if selected2 == 0:
                            await message.edit(content=embedVar)
                        elif selected2 == 1:
                            await message.edit(content=solo)
                        elif selected2 == 2:
                            await message.edit(content=doubles)
                        elif selected2 == 3:
                            await message.edit(content=threes)
                        elif selected2 == 4:
                            await message.edit(content=fours)
                        elif selected2 == 5:
                            await message.edit(content=fours2)
                        else:
                            pass
                        await message.remove_reaction("▶", user)
                    elif reaction1 == "⏹":
                        e = False
                        break

            await message.clear_reactions()

    @bedwars.error
    async def bedwars_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)

        """
    @commands.command(
        aliases=["skywarshelp", "skywarsstats", "skywarstats", "skywar", "skywarstat"]
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def skywars(self, ctx, msg: str):
        msg = msg.lower()
        data = requests.get(
            f"https://api.hypixel.net/player?key={apikey}&name={msg}"
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
            bwdata = data["player"]["stats"]["Bedwars"]
            souls = bwdata["souls"]
            bwlevel = data["player"]["achievements"]["bedwars_level"]
            bwcoins = bwdata["coins"]
            bwwinstreak = bwdata["winstreak"]
            bwwins = bwdata["wins_bedwars"]
            bwlosses = bwdata["losses"]
            bwwinlossratio = round(bwwins / bwlosses, 2)
            bwkills = bwdata["kills_bedwars"]
            bwdeaths = bwdata["deaths_bedwars"]
            bwkdr = round(bwkills / bwdeaths, 2)
            gamesplayed = bwdata["games_played_bedwars"]

            if data["success"] == False:
                embedVar = discord.Embed(
                    title=":no_entry_sign: Something went wrong", color=13381166
                )
                error = data["cause"]
                embedVar.add_field(name="Error", value=f"``{error}``", inline=True)
                embedVar.set_footer(text=footer)
                await ctx.send(embed=embedVar)
            elif data["player"] == None:
                embedVar = discord.Embed(
                    title=":no_entry_sign: Something went wrong", color=13381166
                )
                error = data["cause"]
                embedVar.add_field(
                    name="Error",
                    value=f"``❌ The player is probably banned``",
                    inline=True,
                )
                embedVar.set_footer(text=footer)
                await ctx.send(embed=embedVar)
            else:
                displayname = data["player"]["displayname"]
                full = f"[{rank}] {displayname}"
                uuid = data["player"]["uuid"]
                embedVar = discord.Embed(
                    title=f"{full}",
                    color=15105570,
                    url=f"https://hypixel.net/player/{msg}",
                )
                embedVar.set_author(
                    name="Overall Skywars Stats",
                    icon_url="https://statsify.net/img/assets/hypixel/skywars.png",
                )
                embedVar.add_field(name="Stars", value=f"``{bwlevel}☆``", inline=True)
                embedVar.add_field(name="Coins", value=f"``{bwcoins:,}``", inline=True)
                embedVar.add_field(
                    name="Winstreak", value=f"``{bwwinstreak:,}``", inline=True
                )
                embedVar.add_field(name="Wins", value=f"``{bwwins}``", inline=True)
                embedVar.add_field(
                    name="Losses", value=f"``{bwlosses:,}``", inline=True
                )
                embedVar.add_field(
                    name="Win Loss Ratio", value=f"``{bwwinlossratio:,}``", inline=True
                )
                embedVar.add_field(name="Kills", value=f"``{bwkills:,}``", inline=True)
                embedVar.add_field(
                    name="Deaths", value=f"``{bwdeaths:,}``", inline=True
                )
                embedVar.add_field(name="KD", value=f"``{bwkdr:,}``", inline=True)
                embedVar.add_field(
                    name="Games Played", value=f"``{gamesplayed:,}``", inline=True
                )

                embedVar.set_footer(text=footer)

                message = await ctx.send(embed=embedVar)

    @skywars.error
    async def skywars_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)
            """


def setup(bot):
    bot.add_cog(Hypixel(bot))
