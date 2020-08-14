import discord
import os
import sys
import random
import time
import urllib
import secrets
import asyncio
import aiohttp
import re
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta
from io import BytesIO
#from utils import lists, permissions, http, default, argparser

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()


class Animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def randomimageapi(self, ctx, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except aiohttp.ClientConnectorError:
            return await ctx.send("The API seems to be down...")
        except aiohttp.ContentTypeError:
            return await ctx.send(
                "The API returned an error or didn't return JSON...")

    @Bot.command()
    async def cat(self, ctx):
        """ Posts a random cat """
        await self.randomimageapi(ctx, 'https://api.alexflipnote.dev/cats',
                                  'file')

    @Bot.command()
    async def dog(self, ctx):
        """ Posts a random dog """
        await self.randomimageapi(ctx, 'https://api.alexflipnote.dev/dogs',
                                  'file')

    @Bot.command(aliases=["bird"])
    async def birb(self, ctx):
        """ Posts a random birb """
        await self.randomimageapi(ctx, 'https://api.alexflipnote.dev/birb',
                                  'file')

    @Bot.command()
    async def duck(self, ctx):
        """ Posts a random duck """
        await self.randomimageapi(ctx, 'https://random-d.uk/api/v1/random',
                                  'url')


def setup(bot):
    bot.add_cog(Animals(bot))