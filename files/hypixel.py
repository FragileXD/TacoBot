import discord
import os
import sys
import random
import asyncio
import time
import hypixel
import pypixel
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()
apikey = "INSERT API KEY"
hypixel.setKeys([apikey])


def HyAPI(username):
    username = hypixel.Player(username)
    username.getGuildID()


class Hypixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['alias'])
    async def commandname(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Hypixel(bot))