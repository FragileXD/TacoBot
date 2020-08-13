import discord
import os
import sys
import random
import time
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @Bot.command()
    @commands.guild_only()
    async def randomroulette(self, ctx):
        message_author = ctx.author

        print("{} issued .randomroulette".format(message_author))

        try:
            await ctx.send(
                choice(
                    tuple(member.mention for member in ctx.guild.members
                          if not member.bot)))
        except IndexError:
            await ctx.send("You are the only human member on it!")

    @Bot.command(aliases=['ratedank'])
    async def dankrate(self, ctx, *, message):
        message_author = ctx.author
        message_channel = ctx.channel

        aaaaa = random.randint(1, 101)
        print("{} issued .dankrate 💸".format(message_author))

        if message == "megalovania" or message == "tacoz" or message == "TacoBot":
            embedVar = discord.Embed(
                title="Dank r8 Machine",
                description=
                f"{message} is so insane and is {aaaaa*1000}% dank (epic) :sunglasses:",
                color=3066993)
        else:
            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="Dank r8 Machine",
                    description=
                    f"you broke the dank machine >:( :fire:\n{message} is {aaaaa}% dank",
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
                embedVar = discord.Embed(
                    title="Dank r8 Machine",
                    description=
                    f"you broke the dank machine >:( :fire:\nyou are {aaaaa}% dank",
                    color=15105570)
            else:
                embedVar = discord.Embed(title="Dank r8 Machine",
                                         description=f"you are {aaaaa}% dank",
                                         color=3066993)
            embedVar.set_footer(text=footer)
            return await ctx.send(embed=embedVar)
        else:
            raise (error)

    @Bot.command(aliases=['epicgamer', 'rateepicgamer'])
    async def epicgamerrate(self, ctx, *, message):
        message_author = ctx.author
        message_channel = ctx.channel

        aaaaa = random.randint(1, 101)
        print("{} issued .epicgamerrate 😎".format(message_author))

        if message == "megalovania" or message == "tacoz" or message == "TacoBot":
            embedVar = discord.Embed(
                title="epic gamer r8 Machine",
                description=
                f"{message} is so insane and has {aaaaa*1000}iq (big brain ultra) :sunglasses:",
                color=3066993)
        else:
            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="epic gamer r8 Machine",
                    description=
                    f"{message} broke the epic gamer machine with {message}'s epic gamerness >:( :fire:\nyou are {aaaaa}% epic gamer",
                    color=15105570)
            else:
                embedVar = discord.Embed(
                    title="epic gamer r8 Machine",
                    description=f"{message} is {aaaaa}% epic gamer 😎",
                    color=3066993)
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)

    @epicgamerrate.error
    async def epicgamerrate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            message_author = ctx.author
            aaaaa = random.randint(1, 101)
            print("{} issued .epicgamerrate 🧠".format(message_author))

            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="epic gamer r8 Machine",
                    description=
                    f"you broke the epic gamer machine with your epic gamerness >:( :fire:\nyou are {aaaaa}% epic gamer",
                    color=15105570)
            else:
                embedVar = discord.Embed(
                    title="epic gamer r8 Machine",
                    description=f"you are {aaaaa}% epic gamer 😎",
                    color=3066993)
            embedVar.set_footer(text=footer)
            return await ctx.send(embed=embedVar)
        else:
            raise (error)

    @Bot.command(aliases=['bigbrain', 'ratebigbrain'])
    async def bigbrainrate(self, ctx, *, message):
        message_author = ctx.author
        message_channel = ctx.channel

        aaaaa = random.randint(1, 101)
        print("{} issued .bigbrainrate 🧠".format(message_author))

        if message == "megalovania" or message == "tacoz" or message == "TacoBot":
            embedVar = discord.Embed(
                title="big brain r8 Machine",
                description=
                f"{message} is so insane and has {aaaaa*1000}iq (big brain ultra) :sunglasses:",
                color=3066993)
        else:
            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="big brain r8 Machine",
                    description=
                    f"{message} broke the big brain machine with {message}'s iq>:( :fire:\nyou are {aaaaa}% big brain",
                    color=15105570)
            else:
                embedVar = discord.Embed(
                    title="big brain r8 Machine",
                    description=f"{message} is {aaaaa}% big brain",
                    color=3066993)
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)

    @bigbrainrate.error
    async def bigbrainrate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            message_author = ctx.author
            aaaaa = random.randint(1, 101)
            print("{} issued .bigbrainrate 🧠".format(message_author))

            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="big brain r8 Machine",
                    description=
                    f"you broke the big brain machine with your iq>:( :fire:\nyou are {aaaaa}% big brain",
                    color=15105570)
            else:
                embedVar = discord.Embed(
                    title="big brain r8 Machine",
                    description=f"you are {aaaaa}% big brain",
                    color=3066993)
            embedVar.set_footer(text=footer)
            return await ctx.send(embed=embedVar)
        else:
            raise (error)

    @Bot.command(aliases=['8ball'])
    async def eightball(self, ctx, *, message):
        message_author = ctx.author
        message_channel = ctx.channel

        print("{} issued .8ball 🎱".format(message_author))

        choices = [
            "hell na", "wtf no way",
            "you are so ugly the ball broke. ask again later", "Ah I see, yes",
            "better not tell you now >:)",
            "Only thing I can predict is you're stupid",
            "Concentrate and ask again.", "Don't count on it",
            "It is certain!", "It is decidely so.", "Most likely",
            "My reply is no lol", "My (totally accurate) sources say no",
            "Outlook not so good", "Outlook good", "Reply hazy, try again",
            "Signs point to a YES!", "Very doubtful", "without a doubt", "yep",
            "yes", "yes - definitely", "you may rely on it"
        ]

        aaaaa = random.choice(choices)

        embedVar = discord.Embed(
            title="the magic 8ball",
            description=f"{message_author}: {message}\n🎱8ball: {aaaaa}",
            color=3066993)
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)

    @eightball.error
    async def eightball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)

    @Bot.command(aliases=['partyblob', "partyman", "partyfrog"])
    async def party(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .party 🥳".format(message_author))
        a = message.replace(" ", "<a:party_blob:743099804279898143>")
        await ctx.send(a)

    @party.error
    async def party_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)

    @Bot.command(aliases=['fancy'])
    async def fancytext(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .fancytext 𝔦𝔰𝔰𝔲𝔢𝔡 .𝔣𝔞𝔫𝔠𝔶𝔱𝔢𝔵𝔱".format(message_author))
        #𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷 𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ
        a = message.replace("a", "𝔞")
        a = a.replace("b", "𝔟")
        a = a.replace("c", "𝔠")
        a = a.replace("d", "𝔡")
        a = a.replace("e", "𝔢")
        a = a.replace("f", "𝔣")
        a = a.replace("g", "𝔤")
        a = a.replace("h", "𝔥")
        a = a.replace("i", "𝔦")
        a = a.replace("j", "𝔧")
        a = a.replace("k", "𝔨")
        a = a.replace("l", "𝔩")
        a = a.replace("m", "𝔪")
        a = a.replace("n", "𝔫")
        a = a.replace("o", "𝔬")
        a = a.replace("p", "𝔭")
        a = a.replace("q", "𝔮")
        a = a.replace("r", "𝔯")
        a = a.replace("s", "𝔰")
        a = a.replace("t", "𝔱")
        a = a.replace("u", "𝔲")
        a = a.replace("v", "𝔳")
        a = a.replace("w", "𝔴")
        a = a.replace("x", "𝔵")
        a = a.replace("y", "𝔶")
        a = a.replace("z", "𝔷")
        a = a.replace("A", "𝔄")
        a = a.replace("B", "𝔅")
        a = a.replace("C", "ℭ")
        a = a.replace("D", "𝔇")
        a = a.replace("E", "𝔈")
        a = a.replace("F", "𝔉")
        a = a.replace("G", "𝔊")
        a = a.replace("H", "ℌ")
        a = a.replace("I", "ℑ")
        a = a.replace("J", "𝔍")
        a = a.replace("K", "𝔎")
        a = a.replace("L", "𝔏")
        a = a.replace("M", "𝔐")
        a = a.replace("N", "𝔑")
        a = a.replace("O", "𝔒")
        a = a.replace("P", "𝔓")
        a = a.replace("Q", "𝔔")
        a = a.replace("R", "ℜ")
        a = a.replace("S", "𝔖")
        a = a.replace("T", "𝔗")
        a = a.replace("U", "𝔘")
        a = a.replace("V", "𝔙")
        a = a.replace("W", "𝔚")
        a = a.replace("X", "𝔛")
        a = a.replace("Y", "𝔜")
        a = a.replace("Z", "ℨ")
        await ctx.send(a)

    @fancytext.error
    async def fancytext_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)

    @Bot.command(aliases=['haxer', "hacker", "hackertext"])
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

    @Bot.command(aliases=['mockery'])
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


@Bot.command(aliases=['emoji'])
async def emojify(self, ctx, *, message):
    message_author = ctx.author
    print("{} issued .emojify".format(message_author))
    #𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷 𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ
    a = lower(message).replace("a", ":regional_indicator_a:")
    a = a.replace("b", ":regional_indicator_b:")
    a = a.replace("c", ":regional_indicator_c:")
    a = a.replace("d", ":regional_indicator_d:")
    a = a.replace("e", ":regional_indicator_e:")
    a = a.replace("f", ":regional_indicator_f:")
    a = a.replace("g", ":regional_indicator_g:")
    a = a.replace("h", ":regional_indicator_h:")
    a = a.replace("i", ":regional_indicator_i:")
    a = a.replace("j", ":regional_indicator_j:")
    a = a.replace("k", ":regional_indicator_k:")
    a = a.replace("l", ":regional_indicator_l:")
    a = a.replace("m", ":regional_indicator_m:")
    a = a.replace("n", ":regional_indicator_n:")
    a = a.replace("o", ":regional_indicator_o:")
    a = a.replace("p", ":regional_indicator_p:")
    a = a.replace("q", ":regional_indicator_q:")
    a = a.replace("r", ":regional_indicator_r:")
    a = a.replace("s", ":regional_indicator_s:")
    a = a.replace("t", ":regional_indicator_t:")
    a = a.replace("u", ":regional_indicator_u:")
    a = a.replace("v", ":regional_indicator_v:")
    a = a.replace("w", ":regional_indicator_w:")
    a = a.replace("x", ":regional_indicator_x:")
    a = a.replace("y", ":regional_indicator_y:")
    a = a.replace("z", ":regional_indicator_z:")
    a = a.replace("1", ":regional_indicator_1:")
    a = a.replace("2", ":regional_indicator_2:")
    a = a.replace("3", ":regional_indicator_3:")
    a = a.replace("4", ":regional_indicator_4:")
    a = a.replace("5", ":regional_indicator_5:")
    a = a.replace("6", ":regional_indicator_6:")
    a = a.replace("7", ":regional_indicator_7:")
    a = a.replace("8", ":regional_indicator_8:")
    a = a.replace("9", ":regional_indicator_9:")
    a = a.replace("0", ":regional_indicator_0:")
    await ctx.send(a)

    @emojify.error
    async def emojify_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)


def setup(bot):
    bot.add_cog(Fun(bot))
