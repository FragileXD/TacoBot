import discord
import os
import sys
import urllib
import random
import time
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

start_time = time.monotonic()
PREFIX = (".", ">")
TOKEN = "NTY2MTkzODI1ODc0MTgyMTY0.XLBbFw.o0yHAbU7R2yq5GnpdO7P7pzJyRY"
OWNERID = ***REMOVED***
footer ="Made with ❤️ by Tacoz!"

client = commands.Bot(command_prefix=PREFIX, owner_id = OWNERID, case_insensitive=True)


@client.event
async def on_ready():
    activity = discord.Game(
        name=".help | http://youtube.com/tacozlmao", type=1)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print(f"{client.user.name} is Launched")
    print(client.user.id)
    print('-------------')


@client.command(aliases=['hi'])
async def hello(ctx):
    message_author = ctx.author
    message_channel = ctx.channel
    print("{} issued .hello 👋".format(message_author))
    await message_channel.send("Hello, {}! 👋".format(message_author.name))


@client.command(aliases=['pingo'])
async def ping(ctx):
    message_author = ctx.author
    print("{} issued .ping 🏓".format(message_author))
    await ctx.send(f'🏓 Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['botinv'])
async def invite(ctx):
    message_author = ctx.author
    message_channel = ctx.channel

    print("{} issued .invite 😉".format(message_author))

    await ctx.send("Check Your Dm's :wink:")
    await message_author.send(
        'https://discord.com/api/oauth2/authorize?client_id=566193825874182164&permissions=8&scope=bot'
    )


@client.command()
@commands.guild_only()
async def randomroulette(ctx):
    message_author = ctx.author
    message_channel = ctx.channel
    
    print("{} issued .randomroulette".format(message_author))

    try:
        await ctx.send(choice(tuple(member.mention for member in ctx.guild.members if not member.bot)))
    except IndexError:
        await ctx.send("You are the only human member on it!")


@client.command(aliases=['ratedank'])
async def dankrate(ctx, *, message):
    message_author = ctx.author
    message_channel = ctx.channel

    aaaaa = random.randint(1, 101)
    print("{} issued .dankrate 💸".format(message_author))

    if message == "megalovania" or message == "tacoz" or message == "TacoBot":
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
        embedVar.set_footer(text=footer)
    await message_channel.send(embed=embedVar)


@dankrate.error
async def dankrate_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        message_author = ctx.author
        aaaaa = random.randint(1, 101)
        print("{} issued .dankrate 💸".format(message_author))

        if aaaaa == 101:
            embedVar = discord.Embed(title="Dank r8 Machine", description=f"you broke the dank machine >:( :fire:\nyou are {aaaaa}% dank", color=15105570)
        else:
            embedVar = discord.Embed(title="Dank r8 Machine", description=f"you are {aaaaa}% dank", color=3066993)
        embedVar.set_footer(text=footer)
        return await ctx.send(embed=embedVar)
    else:
        raise(error)


@client.command(aliases=['bigbrain', 'ratebigbrain', 'big brain rate'])
async def bigbrainrate(ctx, *, message):
    message_author = ctx.author
    message_channel = ctx.channel

    aaaaa = random.randint(1, 101)
    print("{} issued .bigbrainrate 🧠".format(message_author))

    if message == "megalovania" or message == "tacoz" or message == "TacoBot":
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
    embedVar.set_footer(text=footer)
    await message_channel.send(embed=embedVar)


@bigbrainrate.error
async def bigbrainrate_error(ctx, error):
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
            embedVar = discord.Embed(title="big brain r8 Machine", description=f"you are {aaaaa}% big brain", color=3066993)
        embedVar.set_footer(text=footer)
        return await ctx.send(embed=embedVar)
    else:
        raise(error)

@client.command(aliases=['8ball'])
async def eightball(ctx, *, message):
    message_author = ctx.author
    message_channel = ctx.channel

    print("{} issued .8ball 🎱".format(message_author))
    choices = ["hell na", "wtf no way", "you are so ugly the ball broke. ask again later", "Ah I see, yes", "better not tell you now >:)", "Cannot predict now", "Concentrate and ask again.", "Don't count on it", "It is certain!", "It is decidely so.",
               "Most likely", "My reply is no lol", "My (totally accurate) sources say no", "Outlook not so good", "Outlook good", "Reply hazy, try again", "Signs point to a YES!", "Very doubtful", "without a doubt", "yep", "yes", "yes - definitely", "you may rely on it"]
    aaaaa = random.choice(choices)

    embedVar = discord.Embed(
        title="the magic 8ball",
        description=f"{message_author}: {message}\n🎱8ball: {aaaaa}",
        color=3066993)
    embedVar.set_footer(text=footer)
    await message_channel.send(embed=embedVar)


@eightball.error
async def eightball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please Input something after the command")
    else:
        raise(error)

@client.command(aliases=['haxer',"hacker","hackertext"])
async def leetify(ctx, *, message):
    message_author = ctx.author
    print("{} issued .leetify 👩‍💻".format(message_author))
    a = message.replace("A","4")
    a = a.replace("a","4")
    a = a.replace("B","8")
    a = a.replace("b","8")
    a = a.replace("E","3")
    a = a.replace("e","3")
    a = a.replace("G","6")
    a = a.replace("g","6")
    a = a.replace("I","1")
    a = a.replace("i","1")
    a = a.replace("O","0")
    a = a.replace("o","0")
    a = a.replace("S","5")
    a = a.replace("s","5")
    a = a.replace("T","7")
    a = a.replace("t","7")
    await ctx.send(a)


@leetify.error
async def leetify_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please Input something after the command")
    else:
        raise(error)

@client.command(aliases=['mockery'])
async def mock(ctx, *, message):
    message_author = ctx.author
    print("{} issued .mock 🎱".format(message_author))
    a = (''.join(choice((str.upper, str.lower))(c) for c in message))
    await ctx.send(a)

@mock.error
async def mock_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please Input something after the command")
    else:
        raise(error)
    
@client.command(aliases=['up time'])
async def uptime(ctx):
    message_author = ctx.author
    message_channel = ctx.channel
    print("{} issued .uptime ⬆".format(message_author))
    embedVar = discord.Embed(
        title="TacoBot Uptime",
        description=f"TacoBot has been up for `{timedelta(seconds=time.monotonic() - start_time)}`",
        color=3066993)
    embedVar.set_footer(text=footer)
    await message_channel.send(embed=embedVar)
    
    
    await ctx.send()
        
client.run(TOKEN)
