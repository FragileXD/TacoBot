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


class Memey(commands.Cog):
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

        for submission in reddit.subreddit(subreddit).top("week", limit=50):
            if submission and not submission.stickied and not submission.over_18:
                submissions.append(submission)

        submission = submissions[random.randint(1, 50) - 1]

        try:
            while submission.url[0:10] == "https://v.r" or submission.url[
                    0:19] == "https://gfycat.com/" or submission.url[
                        -4:-1] + "v" == "gifv":
                submission = submissions[random.randint(1, len(submissions)) -
                                         1]
            else:
                urlvar = (submission.url)
                print(urlvar)

        except:
            try:
                body = submission.body
                urlvar = ""
                print(urlvar)
            except:
                urlvar = ""
                body = ""

        title = (submission.title)
        upvotes = (submission.score)
        permalink = f"https://reddit.com{submission.permalink}"

        embedVar = discord.Embed(title=title, url=permalink, color=3066993)
        if urlvar != "":
            embedVar.set_image(url=urlvar)
        elif urlvar == "":
            if body == "":
                pass
            else:
                embedVar.add_field(name="", value=f"{body}", inline=False)
        embedVar.set_footer(text=(f"👍{upvotes}⬆ | {footer}"))

        await ctx.send(embed=embedVar)
        """
        except:
            embedVar = discord.Embed(
                title=":no_entry_sign: Something went wrong", color=13381166)
            embedVar.set_footer(text=(f"{footer}"))

            await ctx.send(embed=embedVar)
        """

    @meme.error
    async def meme_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            message_author = ctx.author
            print("{} issued .meme 😎".format(message_author))

            submissions = []

            try:
                for submission in reddit.subreddit("dankmemes").top("week",
                                                                    limit=200):
                    if submission and not submission.stickied and not submission.over_18:
                        submissions.append(submission)
                for submission in reddit.subreddit("memes").top("week",
                                                                limit=100):
                    if submission and not submission.stickied and not submission.over_18:
                        submissions.append(submission)

                submission = submissions[random.randint(1, 50) - 1]

                while submission.url[0:10] == "https://v.r" or submission.url[
                        0:19] == "https://gfycat.com/" or submission.url[
                            -4:-1] + "v" == "gifv":
                    submission = submissions[
                        random.randint(1, len(submissions)) - 1]
                else:
                    urlvar = (submission.url)

                title = (submission.title)
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

    @commands.command(name='4chan',
                      description='Sends a 4chan image (from reddit)',
                      aliases=['4chan'])
    async def fourchan(self, ctx, error):
        message_author = ctx.author
        print("{} issued .4chan 🍀".format(message_author))

        submissions = []

        try:
            for submission in reddit.subreddit("4chan").top("week", limit=150):
                if submission and not submission.stickied and not submission.over_18:
                    submissions.append(submission)

            submission = submissions[random.randint(1, 50) - 1]

            while submission.url[0:10] == "https://v.r" or submission.url[
                    0:19] == "https://gfycat.com/" or submission.url[
                        -4:-1] + "v" == "gifv":
                submission = submissions[random.randint(1, len(submissions)) -
                                         1]
            else:
                urlvar = (submission.url)

            title = (submission.title)
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

    @commands.command(name='animeme',
                      description='Sends an Animeme',
                      aliases=['animemes'])
    async def animeme(self, ctx, error):
        message_author = ctx.author
        print("{} issued .Animeme owo".format(message_author))

        submissions = []

        try:
            for submission in reddit.subreddit("goodanimemes").top("week",
                                                                   limit=100):
                if submission and not submission.stickied and not submission.over_18:
                    submissions.append(submission)

            submission = submissions[random.randint(1, 50) - 1]

            while submission.url[0:10] == "https://v.r" or submission.url[
                    0:19] == "https://gfycat.com/" or submission.url[
                        -4:-1] + "v" == "gifv":
                submission = submissions[random.randint(1, len(submissions)) -
                                         1]
            else:
                urlvar = (submission.url)

            title = (submission.title)
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

    @commands.command(name='🔄 antiantijoke',
                      description='not not even funny',
                      aliases=['antiantijokes'])
    async def antiantijoke(self, ctx, error):
        message_author = ctx.author
        print("{} issued .antiantijoke 🐔".format(message_author))

        submissions = []

        try:
            for submission in reddit.subreddit("AntiAntiJokes").top("week",
                                                                    limit=75):
                if submission and not submission.stickied and not submission.over_18:
                    submissions.append(submission)

            submission = submissions[random.randint(1, 50) - 1]

            while submission.url[0:10] == "https://v.r" or submission.url[
                    0:19] == "https://gfycat.com/" or submission.url[
                        -4:-1] + "v" == "gifv":
                submission = submissions[random.randint(1, len(submissions)) -
                                         1]
            else:
                urlvar = (submission.url)

            title = (submission.title)
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

    @commands.command(name='🔄 antijoke',
                      description='not even funny',
                      aliases=['antijokes'])
    async def antijoke(self, ctx, error):
        message_author = ctx.author
        print("{} issued .antijoke 🐔".format(message_author))

        submissions = []

        try:
            for submission in reddit.subreddit("AntiJokes").top("week",
                                                                limit=125):
                if submission and not submission.stickied and not submission.over_18:
                    submissions.append(submission)

            submission = submissions[random.randint(1, 50) - 1]

            while submission.url[0:10] == "https://v.r" or submission.url[
                    0:19] == "https://gfycat.com/" or submission.url[
                        -4:-1] + "v" == "gifv":
                submission = submissions[random.randint(1, len(submissions)) -
                                         1]
            else:
                urlvar = (submission.url)

            title = (submission.title)
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

    @commands.command(name='Prequel',
                      description='The force is with the prequel memes',
                      aliases=['prequelmemes'])
    async def prequel(self, ctx, error):
        message_author = ctx.author
        print("{} issued .prequel 🌟".format(message_author))

        submissions = []

        try:
            for submission in reddit.subreddit("PrequelMemes").top("week",
                                                                   limit=125):
                if submission and not submission.stickied and not submission.over_18:
                    submissions.append(submission)

            submission = submissions[random.randint(1, 50) - 1]

            while submission.url[0:10] == "https://v.r" or submission.url[
                    0:19] == "https://gfycat.com/" or submission.url[
                        -4:-1] + "v" == "gifv":
                submission = submissions[random.randint(1, len(submissions)) -
                                         1]
            else:
                urlvar = (submission.url)

            title = (submission.title)
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


def setup(bot):
    bot.add_cog(Memey(bot))