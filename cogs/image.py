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


def getMeme(self, subreddit, amount: int = None, time: str = None):
    r = praw.Reddit(client_id=self.client_id,
                    client_secret=self.client_secret,
                    user_agent=self.user_agent)

    subreddit = subreddit.replace("r/", "")

    all_submissions = r.subreddit(subreddit)
    posts = []

    if not amount:
        amount = 50
    if not time:
        time = 'month'

    info = (f"Searching {subreddit} (Amount:{str(amount)})")

    for submission in r.subreddit(subreddit).top(time, limit=amount):
        if submission and not submission.stickied:
            posts.append(submission)

    post = posts[random.randint(1, amount) - 1]
    while post.over_18:
        warning = ("Post rated nsfw")
        post = posts[random.randint(1, amount) - 1]
    return {"title": post.title, "url": post.url, "upvotes": post.score}


class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['subreddit', 'reddit', 'memes', 'dankmemes'])
    async def meme(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .meme 😎".format(message_author))

        for submission in reddit.subreddit('all').hot(limit=25):
            print(submission.title)

    @meme.error
    async def meme_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)


def setup(bot):
    bot.add_cog(Image(bot))