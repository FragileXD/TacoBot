import discord
import os
import sys
import random
import asyncio
import time
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

footer = "『 TacoBot ✦ Tacoz 』"
start_time = time.monotonic()


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello", aliases=["hi"])
    async def hello(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel
        print("{} issued .hello 👋".format(message_author))
        await message_channel.send(
            "<a:party_blob:743099804279898143> Hello, {}! 👋".format(message_author.name)
        )

    @commands.command(
        name="uptime",
        description="Shows the amount of time the bot has been online",
        aliases=["timeonline", "timeup"],
    )
    async def uptime(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel
        print("{} issued .uptime ⬆".format(message_author))
        embedVar = discord.Embed(
            title="TacoBot Uptime",
            description=f"TacoBot has been up for `{timedelta(seconds=time.monotonic() - start_time)}`",
            color=3066993,
        )
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)

    @commands.command(
        name="stats",
        description="Shows the general stats for this bot!",
        aliases=["generalstats", "gstats", "stat"],
    )
    async def stats(self, ctx):
        message_author = ctx.author
        print("{} issued .stats ⬆".format(message_author))

        info_msg = discord.Embed(title="General Stats", color=3066993)

        info_msg.add_field(name="Bot Library", value="Discord.py", inline=True)
        info_msg.add_field(name="Command Prefix", value=ctx.prefix, inline=True)
        info_msg.add_field(
            name="Creators", value="Tacoz#1916 - MC IGN: ||NotTacoz||", inline=True
        )

        info_msg.add_field(
            name="Server Count", value=str((len(self.bot.guilds))), inline=True
        )
        info_msg.add_field(name="Shards", value=str(self.bot.shard_count), inline=True)
        info_msg.add_field(
            name="Total Users", value=str(len(self.bot.users)), inline=True
        )

        info_msg.add_field(
            name="DMs Opened", value=str((len(self.bot.private_channels))), inline=True
        )
        info_msg.add_field(
            name="Latency", value=str(round(self.bot.latency * 1000, 2)), inline=True
        )

        # info_msg.add_field(
        # name="Top.gg Page",
        # value="[Click Here](https://top.gg/bot/718523903147900998)",
        # inline=True)
        info_msg.add_field(
            name="Support", value="[Click Here](https://discord.io/Tacoz)", inline=True
        )
        info_msg.add_field(
            name="Invite",
            value="[Click Here](https://discord.com/api/oauth2/authorize?client_id=566193825874182164&permissions=8&scope=bot)",
            inline=True,
        )

        info_msg.set_author(
            name="TacoBot",
            icon_url=str(self.bot.user.avatar_url_as(format="png", size=256)),
        )

        info_msg.set_footer(
            text=(
                f"Uptime: {timedelta(seconds=time.monotonic() - start_time)} | {footer}"
            )
        )
        await ctx.send(embed=info_msg)

    @commands.command(
        name="choose",
        description="For when you wanna settle the score some other way",
        aliases=["chooser"],
    )
    async def choose(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .choose".format(message_author))

        jjj = message.split(" ")
        e = random.choice(jjj)

        embedVar = discord.Embed(
            title="TacoBot Choose",
            description=f"Possible Outcomes: {jjj}",
            color=3066993,
        )
        embedVar.add_field(name="Randomly Chosen Outcome:", value=e, inline=False)
        embedVar.set_footer(text=footer)
        await ctx.send(embed=embedVar)

    @commands.command(aliases=["search"])
    async def google(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .google".format(message_author))
        a = message.replace(" ", "+")
        await ctx.send(f"<:Google:745916595351846962> https://lmgtfy.com/?q={a}")

    @google.error
    async def google_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)

    @commands.command(aliases=["media", "socialmedia"])
    async def socials(self, ctx):
        message_author = ctx.author
        print("{} issued .socials 🐦".format(message_author))

        embedVar = discord.Embed(
            title="<a:party_blob:743099804279898143> Social Media <a:party_blob:743099804279898143>",
            color=3066993,
        )
        embedVar.add_field(
            name="<:twitter:745938625316913234> Twitter:",
            value="https://twitter.com/NotTacoz",
            inline=True,
        )
        embedVar.add_field(
            name="<:youtube:745938625157398548> Youtube:",
            value="https://youtube.com/TacozLmao",
            inline=True,
        )
        embedVar.add_field(
            name="<:discord:745938625522434108> Discord Server:",
            value="https://discord.io/Tacoz",
            inline=True,
        )
        embedVar.set_footer(text=footer)
        await ctx.send(embed=embedVar)


def setup(bot):
    bot.add_cog(Utility(bot))
