import discord
import os
import sys
import random
import asyncio
import time
import praw
import urllib.request
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

footer = "『 TacoBot ✦ Tacoz 』"
start_time = time.monotonic()

reddit = praw.Reddit(client_id="CFOX66IL6PXgRQ",
                     client_secret="sBlyjAFOUcrHKe1KyflDhg0CnsU",
                     user_agent="User Agent",
                     username="***REMOVED***",
                     password="6x*JdQ@5h3t9")


class Animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='animals',
        description='see a multitude of animals from a range of subreddits',
        aliases=['animal'])
    async def animals(self, ctx):
        message_author = ctx.author
        print("{} issued .animals 🐶".format(message_author))

        submissions = []

        try:

            for submission in reddit.subreddit("aww").top("week", limit=50):
                if submission and not submission.stickied and not submission.over_18:
                    submissions.append(submission)
            for submission in reddit.subreddit("Awwducational").top("week",
                                                                    limit=25):
                if submission and not submission.stickied and not submission.over_18:
                    submissions.append(submission)
            for submission in reddit.subreddit("Eyebleach").top("week",
                                                                limit=25):
                if submission and not submission.stickied and not submission.over_18:
                    submissions.append(submission)
            for submission in reddit.subreddit("AnimalsBeingBros").top(
                    "week", limit=25):
                if submission and not submission.stickied and not submission.over_18:
                    submissions.append(submission)

            submission = submissions[random.randint(1, len(submissions)) - 1]
            while submission.url[0:10] == "https://v.r" or submission.url[
                    0:19] == "https://gfycat.com/" or submission.url[
                        -4:-1] + "v" == "gifv":
                submission = submissions[random.randint(1, len(submissions)) -
                                         1]
            else:
                urlvar = (submission.url)

            title = (submission.title)
            upvotes = (submission.score)
            aww = [
                "awwwwwwwwwwww", "I love animals <3", "Absolute Cutie", "🥺🙏",
                "*pet pet*", "owo!"
            ]
            permalink = f"https://reddit.com{submission.permalink}"

            embedVar = discord.Embed(title=title, url=permalink, color=3066993)
            embedVar.set_image(url=urlvar)
            embedVar.set_footer(
                text=(f"👍{upvotes}⬆ | {random.choice(aww)} |{footer}"))

            await ctx.send(embed=embedVar)

        except:
            embedVar = discord.Embed(
                title=":no_entry_sign: Something went wrong", color=13381166)
            embedVar.set_footer(text=(f"{footer}"))

            await ctx.send(embed=embedVar)

    @commands.command(name='aww',
                      description='See some cute random things.',
                      aliases=['cute', 'adorable'])
    async def aww(self, ctx):
        message_author = ctx.author
        print("{} issued .aww 🥺".format(message_author))

        submissions = []

        try:

            for submission in reddit.subreddit("aww").top("week", limit=50):
                if submission and not submission.stickied and not submission.over_18:
                    submissions.append(submission)

            submission = submissions[random.randint(1, len(submissions)) - 1]
            while submission.url[0:10] == "https://v.r" or submission.url[
                    0:19] == "https://gfycat.com/" or submission.url[
                        -4:-1] + "v" == "gifv":
                submission = submissions[random.randint(1, len(submissions)) -
                                         1]
            else:
                urlvar = (submission.url)

            title = (submission.title)
            upvotes = (submission.score)
            aww = ["AWWWWWWWWWWWWWWWW", "pwease can i kweep itw?", "🥺"]
            permalink = f"https://reddit.com{submission.permalink}"

            embedVar = discord.Embed(title=title, url=permalink, color=3066993)
            embedVar.set_image(url=urlvar)
            embedVar.set_footer(
                text=(f"👍{upvotes}⬆ | {random.choice(aww)} |{footer}"))

            await ctx.send(embed=embedVar)
        except:
            embedVar = discord.Embed(
                title=":no_entry_sign: Something went wrong", color=13381166)
            embedVar.set_footer(text=(f"{footer}"))

    @commands.command(name='ducc',
                      description='Gets some duccs 🦆',
                      aliases=['quack', 'quacker', "kwek", 'duck'])
    async def ducc(self, ctx):
        message_author = ctx.author
        print("{} issued .ducc 🦆".format(message_author))

        aww = ["AWWWWWWW", "pwease can i kweep itw?", "🥺"]
        permalink = "https://random-d.uk"
        a = (urllib.request.urlopen("https://random-d.uk/api/random").read())
        b = a[43:-3]
        b = b.decode('utf-8')

        embedVar = discord.Embed(title="Ducc", url=permalink, color=3066993)
        embedVar.set_image(url=b)
        embedVar.set_footer(
            text=(f"Duck from random-d.uk | {random.choice(aww)} |{footer}"))

        await ctx.send(embed=embedVar)


"""
@commands.command(
        name='Command',
        description='Command Description',
        aliases=['alias'])
async def commandname(self, ctx):
    message_author = ctx.author
    print("{} issued .commandname".format(message_author))

    submissions = []

    try:

        for submission in reddit.subreddit("aww").top("week", limit=50):
            if submission and not submission.stickied and not submission.over_18:
                submissions.append(submission)

        submission = submissions[random.randint(1, len(submissions)) - 1]
        while submission.url[0:10] == "https://v.r" or submission.url[
                0:19] == "https://gfycat.com/" or or submission.url[
                        -4:-1] + "v" == "gifv":
            submission = submissions[random.randint(1, len(submissions)) -
                                        1]
        else:
            urlvar = (submission.url)

        title = (submission.title)
        upvotes = (submission.score)
        aww = [
            "quote 1", "quote 2"
        ]
        permalink = f"https://reddit.com{submission.permalink}"

        embedVar = discord.Embed(title=title, url=permalink, color=3066993)
        embedVar.set_image(url=urlvar)
        embedVar.set_footer(
            text=(f"👍{upvotes}⬆ | {random.choice(aww)} |{footer}"))

        await ctx.send(embed=embedVar)
    except:
        embedVar = discord.Embed(
                    title=":no_entry_sign: Something went wrong", color=13381166)
                embedVar.set_footer(text=(f"{footer}"))
"""


def setup(bot):
    bot.add_cog(Animals(bot))