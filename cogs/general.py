import os
import discord

from discord.ext import commands
from datetime import datetime


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


    


    @client.command(aliases=['haxer', "hacker", "hackertext"])
    async def leetify(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .leetify 👩‍💻".format(message_author))
        a = message.replace("A", "4")
        a = a.replace("a", "4")
        a = a.replace("B", "8")
        a = a.replace("b", "8")
        a = a.replace("E", "3")
        a = a.replace("e", "3")
        a = a.replace("G", "6")
        a = a.replace("g", "6")
        a = a.replace("I", "1")
        a = a.replace("i", "1")
        a = a.replace("O", "0")
        a = a.replace("o", "0")
        a = a.replace("S", "5")
        a = a.replace("s", "5")
        a = a.replace("T", "7")
        a = a.replace("t", "7")
        await ctx.send(a)


    @leetify.error
    async def leetify_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)


    @client.command(aliases=['mockery'])
    async def mock(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .mock 🎱".format(message_author))
        a = (''.join(choice((str.upper, str.lower))(c) for c in message))
        await ctx.send(a)


    @mock.error
    async def mock_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)


    @client.command(aliases=['up time'])
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