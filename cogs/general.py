import discord
import os
import sys
import random
import time
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['hi'])
    async def hello(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel
        print("{} issued .hello 👋".format(message_author))
        await message_channel.send(
            "<a:party_blob:743099804279898143> Hello, {}! 👋".format(
                message_author.name))

    @commands.command(aliases=['timeonline', 'timeup'])
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

    @commands.command(aliases=['getprofilepic', 'getprofilepicture'])
    async def getpfp(self, ctx):
        await ctx.send("Command is not finished.")


def setup(bot):
    bot.add_cog(General(bot))
