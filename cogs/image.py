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

    @commands.command(name='meme',
                      description='Sends a random meme',
                      aliases=['subreddit', 'reddit', 'memes', 'dankmemes'])
    async def meme(self, ctx, *, message:
        message_author = ctx.author
        print("{} issued .meme 😎".format(message_author))

        subreddit = message.replace("r/", "")
        title = []
        url = []
        upvotes = []
        
        for submission in reddit.subreddit(subreddit).hot(limit=69):
            print(submission.title)
            title.append(submission.title)
            url.append(submission.url)
            upvotes.append(post.score)
            
        abc = random.choice(title)
        indexed = title.index(abc)
        title = abc
        url = url[indexed]
        upvotes = url[indexed]
        
        

    @meme.error
    async def meme_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)


def setup(bot):
    bot.add_cog(Image(bot))