import discord
import os
import sys
import random
import praw
import requests
import asyncio
import time
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta
from utils.data import getJSON


config = getJSON("config.json")

footer = config.footerembed
start_time = time.monotonic()

reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=config.user_agent,
    username=config.username,
    password=config.password,
)


def is_url_image(image_url, psubmissions):
    image_formats = ("image/png", "image/jpeg", "image/jpg", "image/gif", "image/gifv")
    r = requests.head(image_url)
    if r.headers["content-type"] in image_formats:
        urlvar = image_url
        return urlvar
    else:
        submission = psubmissions[random.randint(1, len(psubmissions)) - 1]
        is_url_image(submission, psubmissions)


def redditgrabber(subreddit, amount=None, time=None):
    description = None
    urlvar = None
    subreddit = subreddit.replace("r/", "")

    submissions = []

    if not amount:
        amount = 50
    if not time:
        time = "month"

    for submission in reddit.subreddit(subreddit).top(time, limit=amount):
        if (
            submission and not submission.stickied and not submission.over_18
        ):  # if submission is NOT pinned or NSFW
            submissions.append(submission)

    submission = submissions[random.randint(1, amount) - 1]

    if not submission.is_self:
        urlvar = is_url_image(submission.url, submissions)
    elif submission.is_self:
        description = submission.selftext

    author = "u/" + str(submission.author)

    if len(description) > 1024:
        description = description[:1020] + " ..."

    return {
        "title": submission.title,
        "url": f"https://reddit.com{submission.permalink}",
        "upvotes": submission.score,
        "imgurl": urlvar,
        "desc": description,
        "comments": submission.num_comments,
        "author": author,
    }


class Memey(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.redditgrabber = redditgrabber

    def color(self):
        color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
        return color

    @commands.command(
        name="reddit",
        description="Grab CONTENT from ANY (Non NSFW) Subreddits",
        aliases=["subreddit", "r/"],
    )
    async def reddit(self, ctx, subreddit: str, amount: str = None, time: str = None):
        async with ctx.typing():
            color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)

            if not time:
                time = "month"
            possibletime = ["day", "week", "month", "year"]
            time = time.replace("ly", "")
            if not time in possibletime:
                return
            if not amount:
                amount = 50
            else:
                try:
                    int(amount)
                    if amount > 1000:
                        amount = 1000
                except:
                    amount = 50

            meme = redditgrabber(subreddit, amount, time)
            print(meme)

            updoots = meme["upvotes"]
            comments = meme["comments"]

            embedVar = discord.Embed(title=meme["title"], url=meme["url"], color=color)
            if meme["imgurl"] != None:
                embedVar.set_image(url=meme["imgurl"])
            elif meme["desc"] != None:
                print("test")
                embedVar.add_field(name=["author"], value=meme["desc"])

            embedVar.set_footer(text=(f"👍{updoots} | 💬{comments} | {footer}"))

            await ctx.send(embed=embedVar)

    @commands.command(
        name="memes",
        description="Sends a random meme from r/dankmemes or r/memes",
        aliases=["meme", "dankmemes", "funny", "memesdank", "dankmeme"],
    )
    async def memes(self, ctx):
        async with ctx.typing():
            meme1 = redditgrabber("memes")
            meme2 = redditgrabber("dankmemes")

            color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)

            list = [1, 2]

            if random.choice(list) == 1:
                meme = meme1
            else:
                meme = meme2

            updoots = meme["upvotes"]
            comments = meme["comments"]

            embedVar = discord.Embed(title=meme["title"], url=meme["url"], color=color)
            embedVar.set_image(url=meme["imgurl"])
            embedVar.set_footer(text=(f"👍{updoots} | 💬{comments} | {footer}"))

            await ctx.send(embed=embedVar)


def setup(bot):
    bot.add_cog(Memey(bot))