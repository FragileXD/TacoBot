import discord
import os
import sys
import random
import asyncio
import time
import hypixel
import requests
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()
apikey = "a54ce218-4fd5-4798-9b4b-6c74efac3456"


def Arcade(username):
    data = requests.get(
        f"https://api.hypixel.net/player?key={apikey}&name={username}").json()


class Hypixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['alias'])
    async def commandname(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Hypixel(bot))