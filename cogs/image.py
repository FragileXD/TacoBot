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

        submissions = []

        try:
            for submission in reddit.subreddit(subreddit).top("week",
                                                              limit=50):
                if submission and not submission.stickied and not submission.over_18:
                    submissions.append(submission)

            submission = submissions[random.randint(1, 50) - 1]

            title = (submission.title)
            urlvar = (submission.url)
            upvotes = (submission.score)
            permalink = f"https://reddit.com{submission.permalink}"

            embedVar = discord.Embed(title=title, url=permalink, color=3066993)
            embedVar.set_image(url=urlvar)
            embedVar.set_footer(text=(f"👍{upvotes}⬆ | {footer}"))

            await ctx.send(embed=embedVar)

        except:
            embedVar = discord.Embed(
                title=":no_entry_sign: Something went wrong", color=13381166)
            embedVar.set_footer(text=(f"{footer}"))

            await ctx.send(embed=embedVar)

    @meme.error
    async def meme_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            message_author = ctx.author
            print("{} issued .meme 😎".format(message_author))

            submissions = []

            try:
                for submission in reddit.subreddit("dankmemes").top("week",
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
        else:
            raise (error)


def setup(bot):
    bot.add_cog(Image(bot))