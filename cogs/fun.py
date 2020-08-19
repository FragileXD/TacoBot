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
from owotext import OwO

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='randomroulette',
        description='Pings a random user in the server!',
    )
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

    @commands.command(aliases=['ratedank'])
    async def dankrate(self, ctx, *, message):
        message_author = ctx.author
        message_channel = ctx.channel

        aaaaa = random.randint(1, 101)
        print("{} issued .dankrate 💸".format(message_author))

        message2 = message
        message = message.lower()

        if message == "dank memer" or message == "tacoz" or message == "tacobot" or message == "<@!566193825874182164>" or message == "<@!389388825274613771>":
            embedVar = discord.Embed(
                title="<:monkaS:664097071950856206> Dank r8 Machine",
                description=
                f"{message2} is so insane and is {aaaaa*1000}% dank (epic) <:monkaS:664097071950856206>",
                color=3066993)
        else:
            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="<:monkaS:664097071950856206> Dank r8 Machine",
                    description=
                    f"you broke the dank machine >:( :fire:\n{message} is {aaaaa}% dank",
                    color=15105570)
            else:
                embedVar = discord.Embed(
                    title="<:monkaS:664097071950856206> Dank r8 Machine",
                    description=f"{message2} is {aaaaa}% dank",
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
                    title="<:monkaS:664097071950856206> Dank r8 Machine",
                    description=
                    f"you broke the dank machine >:( :fire:\nyou are {aaaaa}% dank",
                    color=15105570)
            else:
                embedVar = discord.Embed(
                    title="<:monkaS:664097071950856206> Dank r8 Machine",
                    description=f"you are {aaaaa}% dank",
                    color=3066993)
            embedVar.set_footer(text=footer)
            return await ctx.send(embed=embedVar)
        else:
            raise (error)

    @commands.command(aliases=['epicgamer', 'rateepicgamer'])
    async def epicgamerrate(self, ctx, *, message):
        message_author = ctx.author
        message_channel = ctx.channel

        aaaaa = random.randint(1, 101)
        print("{} issued .epicgamerrate 😎".format(message_author))

        if message == "epic gamer" or message == "tacoz" or message == "tacobot" or message == "<@!566193825874182164>" or message == "<@!389388825274613771>":
            embedVar = discord.Embed(
                title="epic gamer r8 Machine",
                description=
                f"{message} is so insane and is {aaaaa*1000}% epic gamer <:monkaS:664097071950856206>",
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

    @commands.command(aliases=['bigbrain', 'ratebigbrain'])
    async def bigbrainrate(self, ctx, *, message):
        message_author = ctx.author
        message_channel = ctx.channel

        aaaaa = random.randint(1, 101)
        print("{} issued .bigbrainrate 🧠".format(message_author))

        if message == "epic gamer" or message == "tacoz" or message == "tacobot" or message == "<@!566193825874182164>" or message == "<@!389388825274613771>":
            embedVar = discord.Embed(
                title="big brain r8 Machine",
                description=
                f"{message} is so insane and has {aaaaa*1000}iq (big brain ultra) :brain:",
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

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, message):
        message_author = ctx.author
        message_channel = ctx.channel

        print("{} issued .8ball 🎱".format(message_author))

        choices = [
            "hell na", "wtf no way",
            "you are so ugly the ball broke. ask again later",
            "Once you grow a braincell, yes", "i don't care lol",
            "better not tell you now >:)",
            "Only thing I can predict is you're stupid",
            "Concentrate and ask again.", "Don't count on it. Can you count?",
            "It is certain!", "It is decidely so.", "Most likely",
            "no, just like the amount of brain cells you have",
            "My (totally accurate) sources say no", "Outlook not so good",
            "Outlook good", "Reply hazy, try again", "Signs point to a YES!",
            "Very doubtful", "without a doubt", "yep", "yes",
            "yes - definitely", "you may rely on it", 'Yes', 'No',
            'Take a wild guess...', 'Very doubtful', 'Sure', 'Without a doubt',
            'Most likely', 'Might be possible', "You'll be the judge",
            'no... (╯°□°）╯︵ ┻━┻', 'no... baka'
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

    @commands.command(aliases=['partyblob', "partyman", "partyfrog"])
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

    @commands.command(aliases=['fancy'])
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

    @commands.command(aliases=["hackertext"])
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

    @commands.command(aliases=['mockery'])
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

    @commands.command(aliases=['emoji'])
    async def emojify(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .emojify".format(message_author))
        #𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷 𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ
        a = message.upper()
        a = a.replace("A", ":regional_indicator_a:")
        a = a.replace("B", ":regional_indicator_b:")
        a = a.replace("C", ":regional_indicator_c:")
        a = a.replace("D", ":regional_indicator_d:")
        a = a.replace("E", ":regional_indicator_e:")
        a = a.replace("F", ":regional_indicator_f:")
        a = a.replace("G", ":regional_indicator_g:")
        a = a.replace("H", ":regional_indicator_h:")
        a = a.replace("I", ":regional_indicator_i:")
        a = a.replace("J", ":regional_indicator_j:")
        a = a.replace("K", ":regional_indicator_k:")
        a = a.replace("L", ":regional_indicator_l:")
        a = a.replace("M", ":regional_indicator_m:")
        a = a.replace("N", ":regional_indicator_n:")
        a = a.replace("O", ":regional_indicator_o:")
        a = a.replace("P", ":regional_indicator_p:")
        a = a.replace("Q", ":regional_indicator_q:")
        a = a.replace("R", ":regional_indicator_r:")
        a = a.replace("S", ":regional_indicator_s:")
        a = a.replace("T", ":regional_indicator_t:")
        a = a.replace("U", ":regional_indicator_u:")
        a = a.replace("V", ":regional_indicator_v:")
        a = a.replace("W", ":regional_indicator_w:")
        a = a.replace("X", ":regional_indicator_x:")
        a = a.replace("Y", ":regional_indicator_y:")
        a = a.replace("Z", ":regional_indicator_z:")
        try:
            if len(a) < 2000:
                await ctx.send(a)
            else:
                await ctx.send("The message went above 2000 characters")
        except:
            await ctx.send("Something went wrong! Try again.")

    @emojify.error
    async def emojify_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)

    @commands.command()
    async def reverse(self, ctx, *, text: str):
        print("{} issued .reverse 🔁".format(ctx.author))
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")

    @reverse.error
    async def reverse_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)

    @commands.command(aliases=['haxer', 'hacker'])
    async def hack(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .hack 👩‍💻".format(message_author))

        emailchoices = [
            "Tacob0tBeztB0t", "dankNeszz", "dankratedankrate", "pogw12369420",
            "DabeztB0tIzTac0B0t", "69c00lkiddo69", f"da{message}69",
            f"{message}420", "c00lzman360"
        ]
        mailend = ["@pogmail.com", "@gmail.com", "@coldmail.com"]
        passwordchoices = [
            "haxor1998", "tacobotbestb0t", "password1", "password123",
            "boopbooppoo", "c0olpaszw0rd320", "123456", "123456789", "qwerty",
            "password", "qwerty", "111111", "12345678", "abc123", "1234567",
            "agent007", "super123"
        ]

        email = random.choice(emailchoices)
        mail = random.choice(mailend)
        email = email + mail
        password = random.choice(passwordchoices)

        hackmsg = [
            f"[▗] Hacking {message}", f"[▗] Virus injected, emotes stolen",
            f"[▖] Finding discord login... (2fa bypassed)",
            f"[▖] Finding most common word...",
            f"[▝] Injecting trojan virus into discriminator",
            "[▝] Finding IP address", f"Email: {email}\nPassword: {password}",
            "[▗] Last DM: \"i think it's smaller than most\"",
            "[▗] Finding discord login... (2fa bypassed)",
            "[▖] Setting up Epic Store account..",
            "[▘] Reporting account to discord for breaking TOS...",
            "[▖] Finding most common word...",
            "[▖] Selling data to the Government..."
        ]

        message = await ctx.send("Initiating Hacking")

        for i in range(0, 8):
            await asyncio.sleep(1)
            jjj = random.choice(hackmsg)
            await message.edit(content=jjj)

    @hack.error
    async def hack_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            message_author = ctx.author
            print("{} issued .hack 👩‍💻".format(message_author))

            emailchoices = [
                "Tacob0tBeztB0t", "dankNeszz", "dankratedankrate",
                "pogw12369420", "DabeztB0tIzTac0B0t", "69c00lkiddo69",
                f"da{message}69", f"{message}420", "c00lzman360"
            ]
            mailend = ["@pogmail.com", "@gmail.com", "@coldmail.com"]
            passwordchoices = [
                "haxor1998", "tacobotbestb0t", "password1", "password123",
                "boopbooppoo", "c0olpaszw0rd320", "123456", "123456789",
                "qwerty", "password", "qwerty", "111111", "12345678", "abc123",
                "1234567", "agent007", "super123"
            ]

            email = random.choice(emailchoices)
            mail = random.choice(mailend)
            email = email + mail
            password = random.choice(passwordchoices)

            hackmsg = [
                f"[▗] Hacking into who knows what",
                f"[▗] Virus injected, emotes stolen",
                f"[▖] Finding discord login... (2fa bypassed)",
                f"[▖] Finding most common word...",
                f"[▝] Injecting trojan virus into discriminator",
                "[▝] Finding IP address",
                f"Email: {email}\nPassword: {password}",
                "[▗] Last DM: \"i think it's smaller than most\"",
                "[▗] Finding discord login... (2fa bypassed)",
                "[▖] Setting up Epic Store account..",
                "[▘] Reporting account to discord for breaking TOS...",
                "[▖] Finding most common word...",
                "[▖] Selling data to the Government..."
            ]

            message = await ctx.send("Initiating Hacking")

            for i in range(0, 8):
                await asyncio.sleep(1)
                jjj = random.choice(hackmsg)
                await message.edit(content=jjj)
        else:
            raise (error)

    @commands.command(aliases=['owoify', 'owofy'])
    async def owo(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .owo UwU".format(message_author))
        uwu = OwO()
        a = (uwu.whatsthis(message))
        await ctx.send(a)

    @owo.error
    async def owo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)

    @commands.command(aliases=['clapp'])
    async def clap(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .clap 👏".format(message_author))
        a = message.replace(" ", "👏")
        await ctx.send("👏" + a + "👏")

    @clap.error
    async def clap_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)

    @commands.command(aliases=[
        'roasty', 'roastytoasty', 'destroy', 'destruction100', 'kill'
    ])
    async def roast(self, ctx):
        message_author = ctx.author
        print("{} issued .roast 🔥".format(message_author))
        roasts = [
            "You’re my favorite person besides every other person I’ve ever met.",
            'Did your parents have any children that lived?',
            'I envy people who have never met you.',
            'Maybe if you eat all that makeup you will be beautiful on the inside.',
            'You’re kinda like Rapunzel except instead of letting down your hair, you let down everyone in your life.',
            'You’re impossible to underestimate.',
            'You’re not the dumbest person on the planet, but you sure better hope he doesn’t die.',
            'If you were an inanimate object, you’d be a participation trophy.',
            'I’m sorry your dad beat you instead of cancer.',
            'Take my lowest priority and put yourself beneath it.',
            'You are a pizza burn on the roof of the world’s mouth.',
            'Does your ass ever get jealous of the shit that comes out of your mouth?',
            'People like you are the reason God doesn’t talk to us anymore.',
            'You’re so dense, light bends around you.',
            'Your mother may have told you that you could be anything you wanted, but a douchebag wasn’t what she meant.',
            'You are so ugly that when you were born, the doctor slapped your mother.',
            'I’d love to stay and chat but I’d rather have type-2 diabetes.',
            'I bet you swim with a T-shirt on.',
            'I hope your wife brings a date to your funeral.',
            'If you were a potato you’d be a stupid potato.',
            'Your face looks like it was set on fire and put out with chains.',
            'Your mother may have told you that you could be anything you wanted, but a douchebag wasn’t what she meant.',
            'You are so ugly that when you were born, the doctor slapped your mother.',
            'You look like two pounds of shit in a one-pound bag.',
            'If I wanted to commit suicide I’d climb to your ego and jump to your IQ.',
            'You make me wish I had more middle fingers.',
            'If genius skips a generation, your children will be brilliant.',
            'Everyone that has ever said they love you was wrong.',
            'You have the charm and charisma of a burning orphanage.',
            'If there was a single intelligent thought in your head it would have died from loneliness.',
            'I don’t have the time or the crayons to explain this to you.',
            'The only difference between you and Hitler is Hitler knew when to kill himself.',
            'You’re dumber than I tell people.',
            'Your face is so oily that I’m surprised America hasn’t invaded yet.',
            'I can explain it to you, but I can’t understand it for you.',
            'You’re not as dumb as you look.',
            'This is why everyone talks about you as soon as you leave the room.',
            'You’ve got a great body. Too bad there’s no workout routine for a face.',
            'Don’t make me have to smack the extra chromosome out of you.',
            'If you were any dumber, someone would have to water you twice a week.'
        ]
        randomroast = random.choice(roasts)
        await ctx.send(randomroast)

    @commands.command()
    async def spoiler(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .spoiler".format(message_author))
        a = message.replace("", "||||")
        a = a[2:-2]
        ctx.send(a)

    @spoiler.error
    async def spoiler_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)


def setup(bot):
    bot.add_cog(Fun(bot))
