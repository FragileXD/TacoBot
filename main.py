import discord
import math
import time
import os
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from random import choice

TOKEN = 'NTY2MTkzODI1ODc0MTgyMTY0.XLBbFw.o0yHAbU7R2yq5GnpdO7P7pzJyRY'
PREFIX = (".", ">")
client = commands.Bot(command_prefix=PREFIX)

colors = {
  'DEFAULT': 0x000000,
  'WHITE': 0xFFFFFF,
  'AQUA': 0x1ABC9C,
  'GREEN': 0x2ECC71,
  'BLUE': 0x3498DB,
  'PURPLE': 0x9B59B6,
  'LUMINOUS_VIVID_PINK': 0xE91E63,
  'GOLD': 0xF1C40F,
  'ORANGE': 0xE67E22,
  'RED': 0xE74C3C,
  'GREY': 0x95A5A6,
  'NAVY': 0x34495E,
  'DARK_AQUA': 0x11806A,
  'DARK_GREEN': 0x1F8B4C,
  'DARK_BLUE': 0x206694,
  'DARK_PURPLE': 0x71368A,
  'DARK_VIVID_PINK': 0xAD1457,
  'DARK_GOLD': 0xC27C0E,
  'DARK_ORANGE': 0xA84300,
  'DARK_RED': 0x992D22,
  'DARK_GREY': 0x979C9F,
  'DARKER_GREY': 0x7F8C8D,
  'LIGHT_GREY': 0xBCC0C0,
  'DARK_NAVY': 0x2C3E50,
  'BLURPLE': 0x7289DA,
  'GREYPLE': 0x99AAB5,
  'DARK_BUT_NOT_BLACK': 0x2C2F33,
  'NOT_QUITE_BLACK': 0x23272A
}

class Testing(commands.Cog):
    @client.event
    async def on_ready(self):
        activity = discord.Game(
            name=".help | http://youtube.com/tacozlmao", type=1)
        await client.change_presence(status=discord.Status.idle, activity=activity)
        print(f"{client.user.name} is Launched")
        print(client.user.id)
        print('-------------')


    @client.command()
    async def hello(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel
        print("{} issued .hello 👋".format(message_author))
        await message_channel.send("Hello, {}! 👋".format(message_author.name))


    @client.command()
    async def ping(self, ctx):
        message_author = ctx.author
        print("{} issued .ping 🏓".format(message_author))
        await ctx.send(f'🏓 Pong! {round(client.latency * 1000)}ms')


    @client.command()
    async def invite(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel

        print("{} issued .invite 😉".format(message_author))

        await ctx.send("Check Your Dm's :wink:")
        await message_author.send(
            'https://discord.com/api/oauth2/authorize?client_id=566193825874182164&permissions=8&scope=bot'
        )


    @client.command()
    @commands.guild_only()
    async def randomroulette(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel

        try:
            print(
                choice(
                    tuple(member.mention for member in ctx.guild.members
                        if not member.bot)))
        except IndexError:
            await ctx.send("You are the only human member on it!")


    @client.command()
    async def dankrate(self, ctx, *, message):
        message_author = ctx.author
        message_channel = ctx.channel

        aaaaa = random.randint(1, 101)
        print("{} issued .dankrate 💸".format(message_author))

        if message == "megalovania" or message == "tacoz" or message == "<@***REMOVED***>" or message == "TacoBot":
            embedVar = discord.Embed(
                title="Dank r8 Machine",
                description=f"{message} is so insane and is {aaaaa*1000}% dank (epic) :sunglasses:",
                color=3066993)
        else:
            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="Dank r8 Machine",
                    description=f"you broke the dank machine >:( :fire:\n{message} is {aaaaa}% dank",
                    color=15105570)
            else:
                embedVar = discord.Embed(
                    title="Dank r8 Machine",
                    description=f"{message} is {aaaaa}% dank",
                    color=3066993)
        await message_channel.send(embed=embedVar)


    @dankrate.error
    async def dankrate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            message_author = ctx.author
            aaaaa = random.randint(1, 101)
            print("{} issued .dankrate 💸".format(message_author))

            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="Dank r8 Machine",
                    description=f"you broke the dank machine >:( :fire:\nyou are {aaaaa}% dank",
                    color=15105570)
            else:
                embedVar = discord.Embed(
                    title="Dank r8 Machine",
                    description=f"you are {aaaaa}% dank",
                    color=3066993)
            return await ctx.send(embed=embedVar)
        else:
            raise (error)


    @client.command()
    async def bigbrainrate(self, ctx, *, message):
        message_author = ctx.author
        message_channel = ctx.channel

        aaaaa = random.randint(1, 101)
        print("{} issued .bigbrainrate 🧠".format(message_author))

        if message == "megalovania" or message == "tacoz" or message == "<@***REMOVED***>" or message == "TacoBot":
            embedVar = discord.Embed(
                title="big brain r8 Machine",
                description=f"{message} is so insane and has {aaaaa*1000}iq (big brain ultra) :sunglasses:",
                color=3066993)
        else:
            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="big brain r8 Machine",
                    description=f"{message} broke the big brain machine with {message}'s iq>:( :fire:\nyou are {aaaaa}% big brain",
                    color=15105570)
            else:
                embedVar = discord.Embed(
                    title="big brain r8 Machine",
                    description=f"{message} is {aaaaa}% big brain",
                    color=3066993)
        await message_channel.send(embed=embedVar)


    @bigbrainrate.error
    async def dankrate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            message_author = ctx.author
            aaaaa = random.randint(1, 101)
            print("{} issued .bigbrainrate 🧠".format(message_author))

            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="big brain r8 Machine",
                    description=f"you broke the big brain machine with your iq>:( :fire:\nyou are {aaaaa}% big brain",
                    color=15105570)
            else:
                embedVar = discord.Embed(
                    title="big brain r8 Machine",
                    description=f"you are {aaaaa}% big brain",
                    color=3066993)
            return await ctx.send(embed=embedVar)
        else:
            raise (error)


def setup(client):
    client.add_cog(Testing(client))
    client.run(TOKEN)

