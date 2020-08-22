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

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()

class Animals(commands.Cog):  
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='Animals',
                      description='see a multitude of animals from a range of subreddits',
                      aliases=['alias'])
    async def animals(self, ctx):

"""
CODE
message_author = ctx.author
print("{} issued .commandname".format(message_author))

submissions = []

try:
    for submission in reddit.subreddit("subname").top("week",
                                                        limit=50):
        if submission and not submission.stickied and not submission.over_18:
            submissions.append(submission)

    submission = submissions[random.randint(1, 50) - 1]

    title = (submission.title)
    urlvar = (submission.url)
    upvotes = (submission.score)
    permalink = f"https://reddit.com{submission.permalink}"

    embedVar = discord.Embed(title=title,
                                url=permalink,
                                color=3066993)
    embedVar.set_image(url=urlvar)
    embedVar.set_footer(text=(f"👍{upvotes}⬆ | {footer}"))

    await ctx.send(embed=embedVar)

except:
    embedVar = discord.Embed(
        title=":no_entry_sign: Something went wrong",
        color=13381166)
    embedVar.set_footer(text=(f"{footer}"))

    await ctx.send(embed=embedVar)
"""


def setup(bot):
    bot.add_cog(Animals(bot))