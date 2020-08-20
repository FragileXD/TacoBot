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


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', aliases=['hi'])
    async def hello(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel
        print("{} issued .hello 👋".format(message_author))
        await message_channel.send(
            "<a:party_blob:743099804279898143> Hello, {}! 👋".format(
                message_author.name))

    @commands.command(
        name='uptime',
        description='Shows the amount of time the bot has been online',
        aliases=['timeonline', 'timeup'])
    async def uptime(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel
        print("{} issued .uptime ⬆".format(message_author))
        embedVar = discord.Embed(
            title="TacoBot Uptime",
            description=
            f"TacoBot has been up for `{timedelta(seconds=time.monotonic() - start_time)}`",
            color=3066993)
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)

    @commands.command(name='stats',
                      description='Shows the general stats for this bot!',
                      aliases=['generalstats', 'gstats'])
    async def stats(self, ctx):
        message_author = ctx.author
        print("{} issued .stats ⬆".format(message_author))

    @commands.command(
        name='choose',
        description='For when you wanna settle the score some other way',
        aliases=['chooser'])
    async def choose(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .choose".format(message_author))

        jjj = message.split(" ")
        e = random.choice(jjj)

        embedVar = discord.Embed(title="TacoBot Choose",
                                 description=f"Possible Outcomes: {jjj}",
                                 color=3066993)
        embedVar.add_field(name="Randomly Chosen Outcome:",
                           value=e,
                           inline=False)
        embedVar.set_footer(text=footer)
        await ctx.send(embed=embedVar)

    @commands.command(aliases=['search'])
    async def google(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .google".format(message_author))
        a = message.replace(" ", "+")
        await ctx.send(
            f"<:Google:745916595351846962> https://lmgtfy.com/?q={a}")

    @google.error
    async def google_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)


def setup(bot):
    bot.add_cog(Utility(bot))
