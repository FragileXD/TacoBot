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
from utils.data import getJSON
from utils.subredditgrabber import redditgrabber

config = getJSON("config.json")

footer = config.footerembed
start_time = time.monotonic()


class Memey(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.API_Handler = redditgrabber()

    def color(self):
        color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
        return color

    @commands.command(
        name="Reddit",
        description="Grab CONTENT from ANY (Non NSFW) Subreddits",
        aliases=["subreddit", "r/"],
    )
    async def Reddit(self, ctx):
        await ctx.send(not done yet lmao)

    @commands.command(
        name="Memes",
        description="Sends a random meme from r/dankmemes or r/memes",
        aliases=["meme", "dankmemes", "funny", "memesdank", "dankmeme"],
    )
    async def Memes(self, ctx):
        meme1 = self.API_Handler.redditgrabber("memes")
        meme2 = self.API_Handler.redditgrabber("dankmemes")

        if random.choice("1", "2") == "1":
            meme = meme1
        else:
            meme = meme2

        updoots = meme["upvotes"]

        embedVar = discord.Embed(
            title=meme["title"], url=meme["permalink"], color=3066993
        )
        embedVar.set_image(url=meme["urlvar"])
        embedVar.set_footer(text=(f"👍{updoots}⬆ | {footer}"))

        await ctx.send(embed=embedVar)


def setup(bot):
    bot.add_cog(Memey(bot))