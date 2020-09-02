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

footer = "『 TacoBot ✦ Tacoz 』"
start_time = time.monotonic()
apikey = "a54ce218-4fd5-4798-9b4b-6c74efac3456"


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
                '%Y-%m-%d %H:%M', time.localtime(int(firstloginunix) / 1000.0))
            try:
                lastloginunix = data["player"]["lastLogin"]
                lastlogin = time.strftime(
                    '%Y-%m-%d %H:%M',
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
                embedVar.add_field(
                    name="First • Last Login",
                    value=f"``{firstlogin} • {lastlogin} (EDT)``",
                    inline=True)
            except:
                embedVar.add_field(name="First Login",
                                   value=f"``{firstlogin} (EDT)``",
                                   inline=True)
            embedVar.add_field(name="Past usernames",
                               value=f"``{pastusernames}``",
                               inline=True)

            embedVar.set_thumbnail(
                url=f"https://crafatar.com/avatars/{uuid}?default=MHF_Steve&overlay"
            )  #alternatives: https://crafatar.com/avatars/uuid https://crafatar.com/renders/head/uuid https://crafatar.com/renders/body/uuid
            embedVar.set_footer(text=footer)
            await ctx.send(embed=embedVar)

    @general.error
    async def general_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)

    @commands.command(aliases=['watchdog', 'banstats', 'hypixelban'])
    async def watchdogstats(self, ctx):
        watchdog = requests.get(
            f"https://api.hypixel.net/watchdogstats?key={apikey}").json()
        lastminute = watchdog["watchdog_lastMinute"]
        watchdogtotal = watchdog["watchdog_total"]
        watchdogdaily = watchdog["watchdog_rollingDaily"]
        staffdaily = watchdog["staff_rollingDaily"]
        stafftotal = watchdog["staff_total"]
        embedVar = discord.Embed(title=f"Hypixel Ban Stats", color=15105570)
        embedVar.add_field(
            name="Watchdog Bans",
            value=
            f"Last Minute - `{lastminute}`\nToday - `{watchdogdaily}`\nTotal - `{watchdogtotal}`",
            inline=True)
        embedVar.add_field(
            name="Staff Bans",
            value=f"Today - `{staffdaily}`\nTotal - `{stafftotal}`",
            inline=True)

        embedVar.set_thumbnail(
            url=
            f"https://render.namemc.com/skin/3d/body.png?skin=2d1f536e7e659774&model=classic&width=175&height=350"
        )
        embedVar.set_footer(text=footer)
        await ctx.send(embed=embedVar)

    @commands.command(
        aliases=['bedwarshelp', 'bedwarsstats', 'bedwarstats', 'bedwarstat'])
    async def bedwars(self, ctx, *, message):
        message = message.lower()
        data = requests.get(
            f"https://api.hypixel.net/player?key={apikey}&name={message}"
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
            bwfinalkills = bwdata["final_kills_bedwars"]
            bwfinaldeaths = bwdata["final_deaths_bedwars"]
            bwfkdr = round(bwfinalkills / bwfinaldeaths, 2)
            bwbedlost = bwdata["beds_lost_bedwars"]
            bwbedbreak = bwdata["beds_broken_bedwars"]
            bblr = bwbedbreak / bwbedlost
            gamesplayed = bwdata["games_played_bedwars"]
            finalspergame = bwfinalkills / gamesplayed
            bedspergame = bwbedbreak / gamesplayed
            
            bwwinstreak1 = bwdata["eight_one_winstreak"]
            bwwins1 = bwdata["eight_one_wins_bedwars"]
            bwlosses1 = bwdata["eight_one_losses_bedwars"]
            bwwinlossratio1 = round(bwwins1 / bwlosses1, 2)
            bwkills1 = bwdata["eight_one_kills_bedwars"]
            bwdeaths1 = bwdata["eight_one_deaths_bedwars"]
            bwkdr1 = round(bwkills1 / bwdeaths1, 2)
            bwfinalkills1 = bwdata["eight_one_final_kills_bedwars"]
            bwfinaldeaths1 = bwdata["eight_one_final_deaths_bedwars"]
            bwfkdr1 = round(bwfinalkills1 / bwfinaldeaths1, 2)
            bwbedlost1 = bwdata["eight_one_beds_lost_bedwars"]
            bwbedbreak1 = bwdata["eight_one_beds_broken_bedwars"]
            bblr1 = bwbedbreak1 / bwbedlost1
            gamesplayed1 = bwdata["eight_one_games_played_bedwars"]
            finalspergame1 = bwfinalkills1 / gamesplayed1
            bedspergame1 = bwbedbreak1 / gamesplayed1
            
            bwwinstreak2 = bwdata["eight_two_winstreak"]
            bwwins2 = bwdata["eight_two_wins_bedwars"]
            bwlosses2 = bwdata["eight_two_losses_bedwars"]
            bwwinlossratio2 = round(bwwins2 / bwlosses2, 2)
            bwkills2 = bwdata["eight_two_kills_bedwars"]
            bwdeaths2 = bwdata["eight_two_deaths_bedwars"]
            bwkdr2 = round(bwkills2 / bwdeaths2, 2)
            bwfinalkills2 = bwdata["eight_two_final_kills_bedwars"]
            bwfinaldeaths2 = bwdata["eight_two_final_deaths_bedwars"]
            bwfkdr2 = round(bwfinalkills2 / bwfinaldeaths2, 2)
            bwbedlost2 = bwdata["eight_two_beds_lost_bedwars"]
            bwbedbreak2 = bwdata["eight_two_beds_broken_bedwars"]
            bblr2 = bwbedbreak2 / bwbedlost2
            gamesplayed2 = bwdata["eight_two_games_played_bedwars"]
            finalspergame2 = bwfinalkills2 / gamesplayed2
            bedspergame2 = bwbedbreak2 / gamesplayed2
            
            bwwinstreak3 = bwdata["four_three_winstreak"]
            bwwins3 = bwdata["four_three_wins_bedwars"]
            bwlosses3 = bwdata["four_three_losses_bedwars"]
            bwwinlossratio3 = round(bwwins3 / bwlosses3, 2)
            bwkills3 = bwdata["four_three_kills_bedwars"]
            bwdeaths3 = bwdata["four_three_deaths_bedwars"]
            bwkdr3 = round(bwkills3 / bwdeaths3, 2)
            bwfinalkills3 = bwdata["four_three_final_kills_bedwars"]
            bwfinaldeaths3 = bwdata["four_three_final_deaths_bedwars"]
            bwfkdr3 = round(bwfinalkills3 / bwfinaldeaths3, 2)
            bwbedlost3 = bwdata["four_three_beds_lost_bedwars"]
            bwbedbreak3 = bwdata["four_three_beds_broken_bedwars"]
            bblr3 = bwbedbreak3 / bwbedlost3
            gamesplayed3 = bwdata["four_three_games_played_bedwars"]
            finalspergame3 = bwfinalkills3 / gamesplayed3
            bedspergame3 = bwbedbreak3 / gamesplayed3
            
            bwwinstreak4 = bwdata["four_four_winstreak"]
            bwwins4 = bwdata["four_four_wins_bedwars"]
            bwlosses4 = bwdata["four_four_losses_bedwars"]
            bwwinlossratio4 = round(bwwins4 / bwlosses4, 2)
            bwkills4 = bwdata["four_four_kills_bedwars"]
            bwdeaths4 = bwdata["four_four_deaths_bedwars"]
            bwkdr4 = round(bwkills4 / bwdeaths4, 2)
            bwfinalkills4 = bwdata["four_four_final_kills_bedwars"]
            bwfinaldeaths4 = bwdata["four_four_final_deaths_bedwars"]
            bwfkdr4 = round(bwfinalkills4 / bwfinaldeaths4, 2)
            bwbedlost4 = bwdata["four_four_beds_lost_bedwars"]
            bwbedbreak4 = bwdata["four_four_beds_broken_bedwars"]
            bblr4 = bwbedbreak4 / bwbedlost4
            gamesplayed = bwdata["four_four_games_played_bedwars"]
            finalspergame4 = bwfinalkills4 / gamesplayed4
            bedspergame4 = bwbedbreak4 / gamesplayed4
            
            bwwinstreak4v4 = bwdata["two_four_winstreak"]
            bwwins4v4 = bwdata["two_four_wins_bedwars"]
            bwlosses4v4 = bwdata["two_four_losses_bedwars"]
            bwwinlossratio4v4 = round(bwwins4v4 / bwlosses4v4, 2)
            bwkills4v4 = bwdata["two_four_kills_bedwars"]
            bwdeaths4v4 = bwdata["two_four_deaths_bedwars"]
            bwkdr4v4 = round(bwkills4v4 / bwdeaths4v4, 2)
            bwfinalkills4v4 = bwdata["two_four_final_kills_bedwars"]
            bwfinaldeaths4v4 = bwdata["two_four_final_deaths_bedwars"]
            bwfkdr4v4 = round(bwfinalkills4v4 / bwfinaldeaths4v4, 2)
            bwbedlost4v4 = bwdata["two_four_beds_lost_bedwars"]
            bwbedbreak4v4 = bwdata["two_four_beds_broken_bedwars"]
            bblr4v4 = bwbedbreak4v4 / bwbedlost4v4
            gamesplayed4v4 = bwdata["two_four_games_played_bedwars"]
            finalspergame4v4 = bwfinalkills4v4 / gamesplayed4v4
            bedspergame4v4 = bwbedbreak4v4 / gamesplayed4v4
            

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
            displayname = data["player"]["displayname"]
            full = f"[{rank}] {displayname}"
            uuid = data["player"]["uuid"]
            embedVar = discord.Embed(
                title=f"{full}",
                color=15105570,
                url=f"https://hypixel.net/player/{message}")
            embedVar.set_author(
                name="Overall Bedwars Stats",
                icon_url="https://statsify.net/img/assets/hypixel/bedwars.png")
            embedVar.add_field(name="Stars",
                               value=f"``{bwlevel}☆``",
                               inline=True)
            embedVar.add_field(name="Coins",
                               value=f"``{bwcoins:,}``",
                               inline=True)
            embedVar.add_field(name="Winstreak",
                               value=f"``{bwwinstreak:,}``",
                               inline=True)
            embedVar.add_field(name="Wins", value=f"``{bwwins}``", inline=True)
            embedVar.add_field(name="Losses",
                               value=f"``{bwlosses:,}``",
                               inline=True)
            embedVar.add_field(name="Win Loss Ratio",
                               value=f"``{bwwinlossratio:,}``",
                               inline=True)
            embedVar.add_field(name="Kills",
                               value=f"``{bwkills:,}``",
                               inline=True)
            embedVar.add_field(name="Deaths",
                               value=f"``{bwdeaths:,}``",
                               inline=True)
            embedVar.add_field(name="KDR", value=f"``{bwkdr}``", inline=True)
            embedVar.add_field(name="Final Kills",
                               value=f"``{bwfinalkills:,}``",
                               inline=True)
            embedVar.add_field(name="Final Deaths",
                               value=f"``{bwfinaldeaths:,}``",
                               inline=True)
            embedVar.add_field(name="Final KDR",
                               value=f"``{bwfkdr:,}``",
                               inline=True)
            embedVar.add_field(name="Beds Lost",
                               value=f"``{bwbedlost:,}``",
                               inline=True)
            embedVar.add_field(name="Beds Broken",
                               value=f"``{bwbedbreak:,}``",
                               inline=True)
            embedVar.add_field(name="BBLR",
                               value=f"``{bwlr:,}``",
                               inline=True)
            embedVar.add_field(name="Finals/Game",
                               value=f"``{finalspergame:,}``",
                               inline=True)
            embedVar.add_field(name="Beds/Game",
                               value=f"``{bedspergame:,}``",
                               inline=True)
            embedVar.add_field(name="Games Played",
                               value=f"``{gamesplayed:,}``",
                               inline=True)
            solo = discord.Embed(
                title=f"{full}",
                color=15105570,
                url=f"https://hypixel.net/player/{message}")
            solo.set_author(
                name="Overall Bedwars Stats",
                icon_url="https://statsify.net/img/assets/hypixel/bedwars.png")
            solo.add_field(name="Stars",
                               value=f"``{bwlevel}☆``",
                               inline=True)
            solo.add_field(name="Coins",
                               value=f"``{bwcoins:,}``",
                               inline=True)
            solo.add_field(name="Winstreak",
                               value=f"``{bwwinstreak1:,}``",
                               inline=True)
            solo.add_field(name="Wins", value=f"``{bwwins1}``", inline=True)
            solo.add_field(name="Losses",
                               value=f"``{bwlosses1:,}``",
                               inline=True)
            solo.add_field(name="Win Loss Ratio",
                               value=f"``{bwwinlossratio1:,}``",
                               inline=True)
            solo.add_field(name="Kills",
                               value=f"``{bwkills1:,}``",
                               inline=True)
            solo.add_field(name="Deaths",
                               value=f"``{bwdeaths1:,}``",
                               inline=True)
            solo.add_field(name="KDR", value=f"``{bwkdr1}``", inline=True)
            solo.add_field(name="Final Kills",
                               value=f"``{bwfinalkills1:,}``",
                               inline=True)
            solo.add_field(name="Final Deaths",
                               value=f"``{bwfinaldeaths1:,}``",
                               inline=True)
            solo.add_field(name="Final KDR",
                               value=f"``{bwfkdr1:,}``",
                               inline=True)
            solo.add_field(name="Beds Lost",
                               value=f"``{bwbedlost1:,}``",
                               inline=True)
            solo.add_field(name="Beds Broken",
                               value=f"``{bwbedbreak1:,}``",
                               inline=True)
            solo.add_field(name="BBLR",
                               value=f"``{bwlr1:,}``",
                               inline=True)
            solo.add_field(name="Finals/Game",
                               value=f"``{finalspergame1:,}``",
                               inline=True)
            solo.add_field(name="Beds/Game",
                               value=f"``{bedspergame1:,}``",
                               inline=True)
            solo.add_field(name="Games Played",
                               value=f"``{gamesplayed1:,}``",
                               inline=True)

            try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await channel.send('👎')
            else:
                await channel.send('👍')
                
            embedVar.set_thumbnail(
                url=
                f"https://crafatar.com/avatars/{uuid}?default=MHF_Steve&overlay"
            )  #alternatives: https://crafatar.com/avatars/uuid https://crafatar.com/renders/head/uuid https://crafatar.com/renders/body/uuid
            embedVar.set_footer(text=footer)
            await ctx.send(embed=embedVar)
    
    @bedwars.error
    async def bedwars_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)
        
    

def setup(bot):
    bot.add_cog(Hypixel(bot))