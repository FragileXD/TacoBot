import discord
import os
import sys
import urllib
import random
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot

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
async def hello(self, ctx):
    message_author = ctx.author
    message_channel = ctx.channel
    print("{} issued .hello 👋".format(message_author))
    await message_channel.send("Hello, {}! 👋".format(message_author.name))


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


@client.command()
@commands.guild_only()
async def randomroulette(self, ctx):
    message_author = ctx.author
    message_channel = ctx.channel

    try:
        print(choice(tuple(member.mention for member in ctx.guild.members if not member.bot)))
    except IndexError:
        await ctx.send("You are the only human member on it!")


@client.command(aliases=['ratedank'])
async def dankrate(self, ctx, *, message):
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
async def dankrate_error(self, ctx, error):
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
async def bigbrainrate(self, ctx, *, message):
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
            embedVar = discord.Embed(title="big brain r8 Machine", description=f"you are {aaaaa}% big brain", color=3066993)
        embedVar.set_footer(text=footer)
        return await ctx.send(embed=embedVar)
    else:
        raise(error)

@client.command(aliases=['8ball'])
async def eightball(self, ctx, *, message):
    message_author = ctx.author
    message_channel = ctx.channel

    print("{} issued .8ball 🎱".format(message_author))
    aaaaa = random.choice("hell na", "wtf no way", "you are so ugly the ball broke. ask again later", "Ah I see, yes", "better not tell you now >:)", "Cannot predict now", "Concentrate and ask again.", "Don't count on it", "It is certain!", "It is decidely so.", "Most likely", "My reply is no lol", "My (totally accurate) sources say no", "Outlook not so good", "Outlook good", "Reply hazy, try again", "Signs point to a YES!", "Very doubtful", "without a doubt", "yep", "yes", "yes - definitely", "you may rely on it")

    embedVar = discord.Embed(
        title="the magic 8ball",
        description=f"{message_author}: {message}\n🎱8ball: {aaaaa}",
        color=3066993)
    embedVar.set_footer(text=footer)
    await message_channel.send(embed=embedVar)


@eightball.error
async def eightball_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        message_author = ctx.author
        aaaaa = random.randint(1, 101)
        print("{} issued .eightball 🎱".format(message_author))

        aaaaa = random.choice("hell na", "wtf no way", "you are so ugly the ball broke. ask again later", "Ah I see, yes", "better not tell you now >:)", "Cannot predict now", "Concentrate and ask again.", "Don't count on it", "It is certain!", "It is decidely so.",
                            "Most likely", "My reply is no lol", "My (totally accurate) sources say no", "Outlook not so good", "Outlook good", "Reply hazy, try again", "Signs point to a YES!", "Very doubtful", "without a doubt", "yep", "yes", "yes - definitely", "you may rely on it")
        embedVar = discord.Embed(
            title="the magic 8ball",
            description=f"{message_author}: {message}\n🎱8ball: {aaaaa}",
            color=3066993)
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)
    else:
        raise(error)
    

@client.command(
    name='meme',
    description='Sends a random meme',
    aliases=['memes', 'randomeme', 'subreddit']
)
async def meme(self, ctx, subreddit: str = None, amount: int = None, time: str = None):
    if not time:
        time = 'month'
    possibletime = ['day', 'week', 'month','year']
    time = time.replace("ly", "")
    if not time in possibletime:
        return
    if not subreddit:
        if not amount:
            async with ctx.typing():
                meme = self.API_Handler.getMeme("dankmemes")
                e = discord.Embed(colour=0x2ECC71)
                e.title = f"{meme['title']}"
                e.set_image(url=meme['url'])
                e.set_footer(
                    text=f"👍 {meme['upvotes']} | Made with ❤️ by Tacoz!")
                await ctx.send(embed=e)
                return
        elif amount:
            async with ctx.typing():
                meme = self.API_Handler.getMeme("dankmemes", amount, time)
                e = discord.Embed(colour=0x2ECC71)
                e.title = f"{meme['title']}"
                e.set_image(url=meme['url'])
                e.set_footer(
                    text=f"👍 {meme['upvotes']} | Made with ❤️ by Tacoz!")
                await ctx.send(embed=e)
                return
    elif subreddit:
        if amount:
            async with ctx.typing():
                meme = self.API_Handler.getMeme(subreddit, amount, time)
                e = discord.Embed(colour=0x2ECC71)
                e.title = f"{meme['title']}"
                e.set_image(url=meme['url'])
                e.set_footer(
                    text=f"👍 {meme['upvotes']} | Made with ❤️ by Tacoz!")
                await ctx.send(embed=e)
                return
        else:
            async with ctx.typing():
                amount = 50
                meme = self.API_Handler.getMeme(subreddit, amount, time)
                e = discord.Embed(colour=0x2ECC71)
                e.title = f"{meme['title']}"
                e.set_image(url=meme['url'])
                e.set_footer(
                    text=f"👍 {meme['upvotes']} | Made with ❤️ by Tacoz!")
                await ctx.send(embed=e)
                return

client.run(TOKEN)
