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
                     username="***REMOVED***",
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
        urlvar = []
        upvotes = []
        over18 = []
        descr = []
        for submission in reddit.subreddit(subreddit).hot(limit=30):
            title.append(submission.title)
            urlvar.append(submission.url)
            upvotes.append(submission.score)
            over18.append(submission.over_18)
            descr.append(submission.selftext)

        abc = random.choice(title)
        indexed = title.index(abc)
        title = abc
        urlvar = urlvar[indexed]
        upvotes = upvotes[indexed]
        descr = descr[indexed]
        over18 = over18[indexed]

        embedVar = discord.Embed(title=title, url=urlvar, color=3066993)
        embedVar.add_field(name="Description", value=descr)
        embedVar.set_image(url=urlvar)
        embedVar.set_footer(text=(f"👍{upvotes}⬆ | {footer}"))

        await ctx.send(embed=embedVar)

    @meme.error
    async def meme_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)


def setup(bot):
    bot.add_cog(Image(bot))