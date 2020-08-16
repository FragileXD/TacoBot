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

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', aliases=['hi'])
    async def hello(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel
        print("{} issued .hello 👋".format(message_author))
        await message_channel.send(
            "<a:party_blob:743099804279898143> Hello, {}! 👋".format(
                message_author.name))

    @commands.command(
        name='uptime',
        description='Shows the amount of time the bot has been online',
        aliases=['timeonline', 'timeup'])
    async def uptime(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel
        print("{} issued .uptime ⬆".format(message_author))
        embedVar = discord.Embed(
            title="TacoBot Uptime",
            description=
            f"TacoBot has been up for `{timedelta(seconds=time.monotonic() - start_time)}`",
            color=3066993)
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)

    @commands.command(name='choose',
                      description='Choose between some choices',
                      aliases=['chooser'])
    async def choose(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .choose".format(message_author))

        jjj = message.split(" ")
        e = random.choice(jjj)

        embedVar = discord.Embed(title="TacoBot Choose",
                                 description=f"Possible Outcomes: {jjj}",
                                 color=3066993)
        embedVar.add_field(name="Randomly Chosen Outcome:",
                           value=e,
                           inline=False)
        embedVar.set_footer(text=footer)
        await ctx.send(embed=embedVar)


def setup(bot):
    bot.add_cog(Utility(bot))
