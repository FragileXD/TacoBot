import discord
import os
import sys
import random
import asyncio
import time
import praw
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()

reddit = praw.Reddit(client_id="CFOX66IL6PXgRQ",
                     client_secret="sBlyjAFOUcrHKe1KyflDhg0CnsU",
                     user_agent="User Agent",
                     username="TacozRedditBot",
                     password="6x*JdQ@5h3t9")


class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='meme',
                      description='Sends a random meme',
                      aliases=['subreddit', 'reddit', 'memes', 'dankmemes'])
    async def meme(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .meme 😎".format(message_author))

        subreddit = message.replace("r/", "")
        title = []
        url = []
        upvotes = []

        for submission in reddit.subreddit(subreddit).hot(limit=69):
            title.append(submission.title)
            url.append(submission.url)
            upvotes.append(submission.score)

        abc = random.choice(title)
        indexed = title.index(abc)
        title = abc
        urlvar = url[indexed]
        upvotes = upvotes[indexed]

        embedVar = discord.Embed(title=title, url=urlvar, color=3066993)
        embedVar.set_image(url=urlvar)
        embedVar.set_footer(text=(f"👍{upvotes}⬆ | {footer}"))

    @meme.error
    async def meme_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)


def setup(bot):
    bot.add_cog(Image(bot))