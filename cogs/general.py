import discord
import os
import sys
import random
import time
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

start_time = time.monotonic()

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command(aliases=['hi'])
    async def hello(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel
        print("{} issued .hello 👋".format(message_author))
        await message_channel.send(
            "<a:party_blob:743099804279898143> Hello, {}! 👋".format(
                message_author.name))

    @client.command(aliases=['pingo'])
    async def ping(self, ctx):
        message_author = ctx.author
        print("{} issued .ping 🏓".format(message_author))
        await ctx.send(f'🏓 Pong! {round(client.latency * 1000)}ms')

    @client.command(aliases=['botinv'])
    async def invite(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel

        print("{} issued .invite 😉".format(message_author))

        await ctx.send("Check Your Dm's :wink:")
        await message_author.send(
            'https://discord.com/api/oauth2/authorize?client_id=566193825874182164&permissions=8&scope=bot'
        )


    @client.command(aliases=['timeonline', 'timeup'])
    async def uptime(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel
        print("{} issued .uptime ⬆".format(message_author))
        embedVar = discord.Embed(
            title="TacoBot Uptime",
            description=f"TacoBot has been up for `{timedelta(seconds=time.monotonic() - start_time)}`",
            color=3066993)
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)


def setup(bot):
    bot.add_cog(General(bot))
