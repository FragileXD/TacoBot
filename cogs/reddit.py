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


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pog'])
    async def commandname2(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Reddit(bot))