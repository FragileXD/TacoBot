import discord
import os
import sys
import random
import asyncio
import time
import pymongo
from pymongo import MongoClient
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta
from utils.data import getJSON

config = getJSON("config.json")

cluster = MongoClient(config.mongoclient)

footer = "『 TacoBot ✦ Tacoz 』"
start_time = time.monotonic()


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="start", description="Start your economical adventure!", aliases=["create"]
    )
    async def start(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Economy(bot))