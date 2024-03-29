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
from utils.data import getJSON

config = getJSON("config.json")

footer = config.footembed
start_time = time.monotonic()


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="randomroulette",
        description="Pings a random user in the server!",
    )
    @commands.cooldown(1, 1800, commands.BucketType.user)
    @commands.guild_only()
    async def randomroulette(self, ctx):
        message_author = ctx.author

        print("{} issued .randomroulette".format(message_author))

        try:
            await ctx.send(
                choice(
                    tuple(
                        member.mention for member in ctx.guild.members if not member.bot
                    )
                )
            )
        except IndexError:
            await ctx.send("You are the only human member on it!")

    @commands.command(aliases=["ratedank"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def dankrate(self, ctx, *, message):
        color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
        message_author = ctx.author
        message_channel = ctx.channel

        aaaaa = random.randint(1, 101)
        print("{} issued .dankrate 💸".format(message_author))

        message2 = message
        message = message.lower()

        if (
            message == "dank memer"
            or message == "tacoz"
            or message == "tacobot"
            or message == "<@!566193825874182164>"
            or message == "<@!389388825274613771>"
        ):
            embedVar = discord.Embed(
                title="<:monkaS:664097071950856206> Dank r8 Machine",
                description=f"{message2} is so insane and is {aaaaa*1000}% dank (epic) <:monkaS:664097071950856206>",
                color=color,
            )
        else:
            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="<:monkaS:664097071950856206> Dank r8 Machine",
                    description=f"you broke the dank machine >:( :fire:\n{message} is {aaaaa}% dank",
                    color=15105570,
                )
            else:
                embedVar = discord.Embed(
                    title="<:monkaS:664097071950856206> Dank r8 Machine",
                    description=f"{message2} is {aaaaa}% dank",
                    color=color,
                )
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)

    @commands.command(aliases=["epicgamer", "rateepicgamer"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def epicgamerrate(self, ctx, *, message):
        color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
        message_author = ctx.author
        message_channel = ctx.channel

        aaaaa = random.randint(1, 101)
        print("{} issued .epicgamerrate".format(message_author))

        if (
            message == "epic gamer"
            or message == "tacoz"
            or message == "tacobot"
            or message == "<@!566193825874182164>"
            or message == "<@!389388825274613771>"
        ):
            embedVar = discord.Embed(
                title="<:stevedab:745555779666444319> epic gamer r8 Machine",
                description=f"{message} is so insane and is {aaaaa*1000}% epic gamer <:stevedab:745555779666444319>",
                color=color,
            )
        else:
            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="<:stevedab:745555779666444319> epic gamer r8 Machine",
                    description=f"{message} broke the epic gamer machine with {message}'s epic gamerness >:( :fire:\nyou are {aaaaa}% epic gamer",
                    color=15105570,
                )
            else:
                embedVar = discord.Embed(
                    title="<:stevedab:745555779666444319> epic gamer r8 Machine",
                    description=f"{message} is {aaaaa}% epic gamer 😎",
                    color=color,
                )
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)

    @commands.command(aliases=["thot"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def thotrate(self, ctx, *, message):
        color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)

        message_author = ctx.author
        message_channel = ctx.channel

        aaaaa = random.randint(1, 101)
        print("{} issued .thotrate".format(message_author))

        if aaaaa == 101:
            embedVar = discord.Embed(
                title="<:stevedab:745555779666444319>epic gamer r8 Machine",
                description=f"{message} broke the thot machine with {message}'s thotness\nyou are {aaaaa}% thot",
                color=15105570,
            )
        else:
            embedVar = discord.Embed(
                title="<:stevedab:745555779666444319> thot r8 Machine",
                description=f"{message} is {aaaaa}% thot",
                color=color,
            )
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)

    @commands.command(aliases=["bigbrain", "ratebigbrain"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def bigbrainrate(self, ctx, *, message):
        message_author = ctx.author
        message_channel = ctx.channel

        color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)

        aaaaa = random.randint(1, 101)
        print("{} issued .bigbrainrate 🧠".format(message_author))

        if (
            message == "epic gamer"
            or message == "tacoz"
            or message == "tacobot"
            or message == "<@!566193825874182164>"
            or message == "<@!389388825274613771>"
        ):
            embedVar = discord.Embed(
                title="big brain r8 Machine",
                description=f"{message} is so insane and has {aaaaa*1000}iq (big brain ultra) :brain:",
                color=color,
            )
        else:
            if aaaaa == 101:
                embedVar = discord.Embed(
                    title="big brain r8 Machine",
                    description=f"{message} broke the big brain machine with {message}'s iq>:( :fire:\nyou have {aaaaa}iq. big brainnnn!",
                    color=15105570,
                )
            else:
                embedVar = discord.Embed(
                    title="big brain r8 Machine",
                    description=f"{message} is {aaaaa}% big brain",
                    color=color,
                )
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)

    @commands.command(aliases=["8ball"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def eightball(self, ctx, *, message):
        message_author = ctx.author
        message_channel = ctx.channel

        color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)

        print("{} issued .8ball 🎱".format(message_author))

        choices = [
            "hell na",
            "wtf no way",
            "you are so ugly the ball broke. ask again later",
            "Once you grow a braincell, yes",
            "i don't care lol",
            "better not tell you now >:)",
            "Only thing I can predict is you're stupid",
            "Concentrate and ask again.",
            "Don't count on it. Can you count?",
            "It is certain!",
            "It is decidely so.",
            "Most likely",
            "no, just like the amount of brain cells you have",
            "My (totally accurate) sources say no",
            "Outlook not so good",
            "Outlook good",
            "Reply hazy, try again",
            "Signs point to a YES!",
            "Very doubtful",
            "without a doubt",
            "yep (笑)",
            "yes, or no?",
            "yes - definitely, yep, i think so, maybe, no",
            "you may rely on it i guess",
            "Yes.................",
            "No",
            "Take a wild guess...",
            "Very doubtful",
            "Sure why not (笑)",
            "Without a doubt",
            "Most likely",
            "Might be possible",
            "You'll be the judge",
            "no... (╯°□°）╯︵ ┻━┻",
            "no... baka",
            "red is the impostor! wait... this is the 8ball command?!??!?!",
        ]

        aaaaa = random.choice(choices)

        embedVar = discord.Embed(
            title="the magic 8ball",
            description=f"{message_author}: {message}\n🎱8ball: {aaaaa}",
            color=color,
        )
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)

    @commands.command(aliases=["partyblob", "partyman", "partyfrog"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def party(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .party 🥳".format(message_author))
        a = message.replace(" ", "<a:party_blob:763630778352402452>")

        if len(a) < 2000:
            await ctx.send(a)
        else:
            await ctx.send(
                f":angry: Break the bot again and I will break your knees. Characters over Limit, {len(a)}/2000 "
            )

    @commands.command(aliases=["fancy"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def fancytext(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .fancytext 𝔦𝔰𝔰𝔲𝔢𝔡 .𝔣𝔞𝔫𝔠𝔶𝔱𝔢𝔵𝔱".format(message_author))
        # 𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷 𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ
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

    @commands.command(aliases=["hackertext"])
    @commands.cooldown(1, 2, commands.BucketType.user)
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

    @commands.command(aliases=["mockery"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def mock(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .mock 🎱".format(message_author))
        a = "".join(choice((str.upper, str.lower))(c) for c in message)
        await ctx.send(a)

    @commands.command(aliases=["emoji"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def emojify(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .emojify".format(message_author))
        # 𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷 𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ
        a = message.upper()
        a = a.replace(" ", "  ")
        a = a.replace("", " ")
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
        a = a.replace("1", ":one:")
        a = a.replace("2", ":two:")
        a = a.replace("3", ":three:")
        a = a.replace("4", ":four:")
        a = a.replace("5", ":five:")
        a = a.replace("6", ":six:")
        a = a.replace("7", ":seven:")
        a = a.replace("8", ":eight:")
        a = a.replace("9", ":nine:")
        try:
            if len(a) < 2000:
                await ctx.send(a)
            else:
                await ctx.send(
                    f"Break the bot again and I will break your knees. Characters over Limit, {len(a)}/2000 "
                )
        except:
            await ctx.send("Something went wrong! Try again.")

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def reverse(self, ctx, *, text: str):
        print("{} issued .reverse 🔁".format(ctx.author))
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")

    @commands.command(aliases=["haxer", "hacker"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def hack(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .hack 👩‍💻".format(message_author))

        emailchoices = [
            "Tacob0tBeztB0t",
            "dankNeszz",
            "dankratedankrate",
            "pogw12369420",
            "DabeztB0tIzTac0B0t",
            "69c00lkiddo69",
            f"da{message}69",
            f"{message}420",
            "c00lzman360",
        ]
        mailend = ["@pogmail.com", "@gmail.com", "@coldmail.com"]
        passwordchoices = [
            "haxor1998",
            "tacobotbestb0t",
            "password1",
            "password123",
            "boopbooppoo",
            "c0olpaszw0rd320",
            "123456",
            "123456789",
            "qwerty",
            "password",
            "qwerty",
            "111111",
            "12345678",
            "abc123",
            "1234567",
            "agent007",
            "super123",
        ]

        email = random.choice(emailchoices)
        mail = random.choice(mailend)
        email = email + mail
        password = random.choice(passwordchoices)

        hackmsg = [
            f"[▗] Hacking {message}",
            f"[▗] Virus injected, emotes stolen",
            f"[▖] Finding discord login... (2fa bypassed)",
            f"[▖] Finding most common word...",
            f"[▝] Injecting trojan virus into discriminator",
            "[▝] Finding IP address",
            f"Email: {email}\nPassword: {password}",
            '[▗] Last DM: "i think it\'s smaller than most"',
            "[▗] Finding discord login... (2fa bypassed)",
            "[▖] Setting up Epic Store account..",
            "[▘] Reporting account to discord for breaking TOS...",
            "[▖] Finding most common word...",
            "[▖] Selling data to the Government...",
        ]

        message = await ctx.send("Initiating Hacking")

        for i in range(0, 8):
            await asyncio.sleep(1)
            jjj = random.choice(hackmsg)
            await message.edit(content=jjj)

    @commands.command(aliases=["owoify", "owofy"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def owo(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .owo UwU".format(message_author))
        uwu = OwO()
        a = uwu.whatsthis(message)
        await ctx.send(a)

    @commands.command(aliases=["clapp"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def clap(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .clap 👏".format(message_author))
        a = message.replace(" ", "👏")
        await ctx.send("👏" + a + "👏")

    @commands.command(aliases=["roasty", "roastytoasty", "destroy", "destruction100"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def roast(self, ctx):
        message_author = ctx.author
        print("{} issued .roast 🔥".format(message_author))
        roasts = [
            "You’re my favorite person besides every other person I’ve ever met.",
            "Did your parents have any children that lived?",
            "I envy people who have never met you.",
            "Maybe if you eat all that makeup you will be beautiful on the inside.",
            "You’re kinda like Rapunzel except instead of letting down your hair, you let down everyone in your life.",
            "You’re impossible to underestimate.",
            "You’re not the dumbest person on the planet, but you sure better hope he doesn’t die.",
            "If you were an inanimate object, you’d be a participation trophy.",
            "I’m sorry your dad beat you instead of cancer.",
            "Take my lowest priority and put yourself beneath it.",
            "You are a pizza burn on the roof of the world’s mouth.",
            "Does your ass ever get jealous of the shit that comes out of your mouth?",
            "People like you are the reason God doesn’t talk to us anymore.",
            "You’re so dense, light bends around you.",
            "Your mother may have told you that you could be anything you wanted, but a douchebag wasn’t what she meant.",
            "You are so ugly that when you were born, the doctor slapped your mother.",
            "I’d love to stay and chat but I’d rather have type-2 diabetes.",
            "I bet you swim with a T-shirt on.",
            "I hope your wife brings a date to your funeral.",
            "If you were a potato you’d be a stupid potato.",
            "Your face looks like it was set on fire and put out with chains.",
            "Your mother may have told you that you could be anything you wanted, but a douchebag wasn’t what she meant.",
            "You are so ugly that when you were born, the doctor slapped your mother.",
            "You look like two pounds of shit in a one-pound bag.",
            "If I wanted to commit suicide I’d climb to your ego and jump to your IQ.",
            "You make me wish I had more middle fingers.",
            "If genius skips a generation, your children will be brilliant.",
            "Everyone that has ever said they love you was wrong.",
            "You have the charm and charisma of a burning orphanage.",
            "If there was a single intelligent thought in your head it would have died from loneliness.",
            "I don’t have the time or the crayons to explain this to you.",
            "The only difference between you and Hitler is Hitler knew when to kill himself.",
            "You’re dumber than I tell people.",
            "Your face is so oily that I’m surprised America hasn’t invaded yet.",
            "I can explain it to you, but I can’t understand it for you.",
            "You’re not as dumb as you look.",
            "This is why everyone talks about you as soon as you leave the room.",
            "You’ve got a great body. Too bad there’s no workout routine for a face.",
            "Don’t make me have to smack the extra chromosome out of you.",
            "If you were any dumber, someone would have to water you twice a week.",
            "You’re the reason God created the middle finger.",
            "You’re a grey sprinkle on a rainbow cupcake.",
            "If your brain was dynamite, there wouldn’t be enough to blow your hat off.",
            "You are more disappointing than an unsalted pretzel.",
            "Light travels faster than sound which is why you seemed bright until you spoke.",
            "You're so annoying, you make your Happy Meal cry.",
            "Your secrets are always safe with me. I never even listen when you tell me them.",
            "I’ll never forget the first time we met. But I’ll keep trying.",
            "I forgot the world revolves around you. My apologies, how silly of me.",
            "Hold still. I’m trying to imagine you with personality.",
            "Your face makes onions cry.",
            "I’m not insulting you, I’m describing you.",
            "If you’re going to be two-faced, at least make one of them pretty.",
            "OH MY GOD! IT SPEAKS!",
            "You are so full of shit, the toilet’s jealous.",
            "The last time I saw a face like yours I fed it a banana.",
            "I refuse to have a battle of wits with an unarmed person.",
            "I get so emotional when you're not around. That emotion is happiness.",
            "You must be the arithmetic man -- you add trouble, subtract pleasure, divide attention, and multiply ignorance.",
        ]
        randomroast = random.choice(roasts)
        await ctx.send(randomroast)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def spoiler(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .spoiler".format(message_author))
        a = message.replace("", "||||")
        a = a[2:-2]
        if len(a) > 2000:
            await ctx.send(
                f"Break the bot again and I will break your knees. Characters over Limit, {len(a)}/2000 "
            )
        else:
            await ctx.send(a)

    @commands.command(aliases=["renaicirculation"])
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def renai(self, ctx):
        message_author = ctx.author
        print("{} issued .renai".format(message_author))

        lyrics = [
            "Se no!",
            "Demo sonnan ja dame",
            "Mou sonnan ja hora",
            "Kokoro wa shinka suru yo",
            "Motto motto",
            "**",
            "Kotoba ni sureba kiechau kankei nara",
            "Kotoba o keseba ii ya tte",
            "Omotteta osoreteta",
            "Dakedo are? nanka chigau kamo...",
            "Senri no michi mo ippo kara!",
            "Ishi no you ni katai sonna ishi de",
            "Chiri mo tsumoreba Yamato Nadeshiko?",
            "'shi' nuki de iya shinu ki de!",
            "**",
            "Fuwafuwari fuwafuwaru",
            "Anata ga namae o yobu",
            "Sore dake de",
            "Chuu e ukabu",
            "Fuwafuwaru fuwafuwari",
            "Anata ga waratte iru",
            "Sore dake de",
            "Egao ni naru",
            "**",
            "Kami-sama arigatou",
            "Unmei no itazura demo",
            "Meguriaeta koto ga",
            "Shiawase na no",
            "**",
            "Demo sonnan ja dame",
            "Mou sonnan ja hora",
            "Kokoro wa shinka suru yo",
            "Motto motto",
            "Sou sonnan ja ya da",
            "Nee sonnan ja mada",
            "Zutto zutto",
            "Watashi no koto mitete ne",
            "**",
            "Watashi no naka no anata hodo",
            "Anata no naka no watashi no sonzai wa",
            "Madamada ookikunai koto mo",
            "Wakatteru keredo",
            "Ima kono onaji shunkan",
            "Kyouyuu shiteru jikkan",
            "Chiri mo tsumoreba Yamato Nadeshiko!",
            "Ryakushite? chiri-tsumo Yamato Nadeko!",
            "**",
            "Kurakurari kurakuraru",
            "Anata o miagetara",
            "Sore dake de",
            "Mabushisugite",
            "Kurakuraru kurakurari",
            "Anata o omotte iru",
            "Sore dake de",
            "Tokete shimau",
            "**",
            "Kami-sama arigatou",
            "Unmei no itazura demo",
            "Meguriaeta koto ga",
            "Shiawase na no",
            "**",
            "KO I SU RU KI SE TSU WA YO KU BA RI Circulation",
            "KO I SU RU KI MO CHI WA YO KU BA RI Circulation",
            "KO I SU RU HI TO MI WA YO KU BA RI Circulation",
            "KO I SU RU O TO ME WA YO KU BA RI Circulation",
            "**",
            "Fuwafuwari fuwafuwaru",
            "Anata ga namae o yobu",
            "Sore dake de",
            "Chuu e ukabu",
            "Fuwafuwaru fuwafuwari",
            "Anata ga waratte iru",
            "Sore dake de",
            "Egao ni naru",
            "**",
            "Kami-sama arigatou",
            "Unmei no itazura demo",
            "Meguriaeta koto ga",
            "Shiawase na no",
            "**",
            "Demo sonnan ja dame",
            "Mou sonnan ja hora",
            "Kokoro wa shinka suru yo",
            "Motto motto",
            "Sou sonnan ja ya da",
            "Nee sonnan ja mada",
            "Watashi no koto mitete ne",
            "Zutto zutto",
        ]

        msg2 = "**Renai Circulation**"
        msg = await ctx.send(msg2)

        for lyric in lyrics:
            await asyncio.sleep(2)
            e = msg2
            msg2 = f"{e}\n{lyric}"
            await msg.edit(content=msg2)

    @commands.command(aliases=["useless_web"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def uselessweb(self, ctx):
        message_author = ctx.author
        print("{} issued .uselessweb ❓".format(message_author))
        webs = [
            "https://coronavirus-ninja.com/",
            "https://theuselessweb.site/lookadeadfly/",
            "https://theuselessweb.site/drunkronswanson/",
            "https://theuselessweb.site/talktomyass/",
            "https://theuselessweb.site/icantsleep/",
            "https://theuselessweb.site/hmpg/",
            "https://theuselessweb.site/broof/",
            "https://theuselessweb.site/screaminggoatpiano/",
            "https://theuselessweb.site/shamebell/",
            "https://theuselessweb.site/8bitdance/",
            "https://theuselessweb.site/coloursquares/",
            "https://theuselessweb.site/secretsfornicotine/",
            "https://theuselessweb.site/crapola/",
            "https://theuselessweb.site/salmonofcapistrano/",
            "https://theuselessweb.site/More-cowbell/",
            "https://theuselessweb.site/buzzybuzz/",
            "https://theuselessweb.site/buildshruggie/",
            "https://theuselessweb.site/plspetdoge/",
            "https://theuselessweb.site/oppositeofpoop/",
            "https://theuselessweb.site/boohbah-zone/",
            "https://theuselessweb.site/instantostrich/",
            "https://theuselessweb.site/geodude/",
            "https://theuselessweb.site/cuteroulette/",
            "https://theuselessweb.site/infinitefrogs/",
            "https://theuselessweb.site/agitatedchicken/",
            "https://theuselessweb.site/wwwdotcom/",
            "https://theuselessweb.site/ducksarethebest.com/"
            "https://theuselessweb.site/grandpanoclothes.com/",
            "https://theuselessweb.site/poop.bike/",
            "https://theuselessweb.site/whatdoineed/",
            "https://theuselessweb.site/thanksobama/",
            "https://theuselessweb.site/retrolamp/",
            "https://theuselessweb.site/dumbcalculator/",
            "https://theuselessweb.site/interactive-triangualation/",
            "https://theuselessweb.site/Successful%20Troll/",
            "https://theuselessweb.site/Danzorz/",
            "https://theuselessweb.site/Flight%20of%20the%20Hamsters/",
            "https://theuselessweb.site/Know%20Your%20Destiny/",
            "https://theuselessweb.site/Virtual%20Stapler/",
            "https://theuselessweb.site/Game%20music/",
            "https://theuselessweb.site/tunnelsnakes/",
            "https://theuselessweb.site/annoyingdog/",
            "https://theuselessweb.site/blueballmachine/",
            "https://theuselessweb.site/roadblocks/",
            "https://theuselessweb.site/kittencannon/",
            "https://theuselessweb.site/blankwindows/",
            "https://theuselessweb.site/faceofdisapproval/",
            "https://theuselessweb.site/isittimeforanap/",
            "https://theuselessweb.site/whitenoisemachine.com/",
            "https://theuselessweb.site/tacospin/",
            "https://theuselessweb.site/omglasergunspewpewpew/",
            "https://theuselessweb.site/toastybutton/",
            "https://theuselessweb.site/pleasewait/",
            "https://theuselessweb.site/wafflecat/",
            "https://theuselessweb.site/minionstranslator/",
            "https://theuselessweb.site/fallingguy/",
            "https://theuselessweb.site/flyguy/",
            "https://theuselessweb.site/patience-is-a-virtue/",
            "https://theuselessweb.site/whitetrash/",
            "https://theuselessweb.site/pixelsfighting/",
            "https://theuselessweb.site/isitwhite/",
            "https://theuselessweb.site/onemillionlols/",
            "https://theuselessweb.site/chihuahuaspin/",
            "https://theuselessweb.site/ismycomputeron/",
            "https://theuselessweb.site/iamawesome/",
            "https://theuselessweb.site/electricboogiewoogie/",
            "https://theuselessweb.site/willthefuturebeawesome/",
            "https://theuselessweb.site/unicodesnowmanforyou/",
            "https://theuselessweb.site/tencentsinfo/",
            "https://theuselessweb.site/leekspin.com/",
            "https://theuselessweb.site/ninjaflex/",
            "https://theuselessweb.site/imaninja/",
            "https://theuselessweb.site/ouaismaisbon/",
            "https://theuselessweb.site/hasthelargehadroncolliderdestroyedtheworldyet.com/",
            "https://theuselessweb.site/please-like/",
            "https://theuselessweb.site/fallingfalling/",
            "https://theuselessweb.site/randomcolour.com/",
            "https://theuselessweb.site/r33b.net/",
            "https://theuselessweb.site/crouton/",
            "https://theuselessweb.site/dottedlines/",
            "https://theuselessweb.site/thebestdinosaur/",
            "https://theuselessweb.site/www.everydayim.com/",
            "https://theuselessweb.site/www.sanger.dk/",
            "https://theuselessweb.site/bees/",
            "https://theuselessweb.site/cant-not-tweet-this.com/",
            "https://theuselessweb.site/tiling/",
            "https://theuselessweb.site/thatsthefinger/",
            "https://theuselessweb.site/tr-8r/",
            "https://theuselessweb.site/hemansings/",
            "https://theuselessweb.site/fanfare/",
            "https://theuselessweb.site/puppytwister/",
            "https://theuselessweb.site/youareanidiot/",
            "https://theuselessweb.site/solitaire/",
            "https://theuselessweb.site/exactcenteroftheinternet/",
            "https://theuselessweb.site/deepblackhole/",
            "https://theuselessweb.site/skulltrumpet/",
            "https://theuselessweb.site/puppytummy/",
            "https://theuselessweb.site/randomselectioninrandomimage/",
            "https://theuselessweb.site/riddlydiddly/",
            "https://theuselessweb.site/BecauseWhy/",
            "https://theuselessweb.site/walama/",
            "https://theuselessweb.site/dramabutton/",
            "https://theuselessweb.site/hereistoday/",
            "https://theuselessweb.site/spaceis.cool/",
            "https://theuselessweb.site/khaaan/",
            "https://theuselessweb.site/nooooooooooooooo/",
            "https://theuselessweb.site/hiyoooo/",
            "https://theuselessweb.site/shtuff/",
            "https://theuselessweb.site/tomsdog/",
            "https://theuselessweb.site/leglesslegolegolas/",
            "https://theuselessweb.site/lifeisnotfair/",
            "https://theuselessweb.site/something/",
            "https://theuselessweb.site/randomdoh/",
            "https://theuselessweb.site/comingupmilhouse/",
            "https://theuselessweb.site/purple/",
            "https://theuselessweb.site/stagnationmeansdecline/",
            "https://theuselessweb.site/wewillattack/",
            "https://theuselessweb.site/pleasetouchme/",
            "https://theuselessweb.site/iamveryverysorry/",
            "https://theuselessweb.site/everythingyouseeisinthepast/",
            "https://theuselessweb.site/nosquito/",
            "https://theuselessweb.site/vaiavanti/",
            "https://theuselessweb.site/futurephysics/",
            "https://theuselessweb.site/popcornpainting/",
            "https://theuselessweb.site/coldvoid/",
            "https://theuselessweb.site/invisiblecursor/",
            "https://theuselessweb.site/tinycursor/",
            "https://theuselessweb.site/aestheticecho/",
            "https://theuselessweb.site/beefchickenpork/",
            "https://theuselessweb.site/annoyingcursor/",
            "https://theuselessweb.site/hotdoom/",
            "https://theuselessweb.site/fromthedarkpast/",
            "https://theuselessweb.site/closedshut/",
            "https://theuselessweb.site/nekromisantrop/",
            "https://theuselessweb.site/thepersistenceofsadness/",
            "https://theuselessweb.site/tothewater/",
            "https://theuselessweb.site/flaminglog/",
            "https://theuselessweb.site/yesforsure.com/",
            "https://theuselessweb.site/inceptionbutton/",
            "https://theuselessweb.site/niceonedad/",
            "https://theuselessweb.site/nootnoot/",
            "https://theuselessweb.site/youhaveautism/",
            "https://theuselessweb.site/ffffidget/",
            "https://theuselessweb.site/howbigismypotato/",
            "https://theuselessweb.site/feedderpy/",
            "https://theuselessweb.site/exotic-butters/",
            "https://theuselessweb.site/marvelous-breadfish/",
            "https://theuselessweb.site/thebigdog.club/",
            "https://theuselessweb.site/sealspin/",
            "https://theuselessweb.site/thispeanutlookslikeaduck/",
            "https://theuselessweb.site/hardcoreprawnlawn/",
            "https://theuselessweb.site/uppertolowercase/",
            "https://theuselessweb.site/minecraftstal/",
            "https://theuselessweb.site/breakglasstosoundalarm/",
        ]
        await ctx.send("<a:loading:745929307108540446> " + random.choice(webs))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def doot(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .doot".format(message_author))
        a = message.replace(" ", "💀🎺")
        if len(a) > 2000:
            await ctx.send(
                f"Break the bot again and I will break your knees. Characters over Limit, {len(a)}/2000 "
            )
        else:
            await ctx.send(a)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def say(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .say".format(message_author))
        if len(message) > 2000:
            await ctx.send(
                f"Break the bot again and I will break your knees. Characters over Limit, {len(message)}/2000 "
            )
        else:
            await ctx.send(message)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def monch(self, ctx):
        message_author = ctx.author
        print("{} issued .monch".format(message_author))

        try:
            await ctx.send(file=discord.File("images\\Monch.gif"))
        except:
            await ctx.send(
                "https://media.discordapp.net/attachments/729675616420495381/753171581194469465/Monch.gif"
            )

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def kill(self, ctx, user: str):
        possibledeaths = [
            f"``{user}`` died of ligma. what's ligma?",
            f"``{user}`` drank too much tea and died. what a brit.",
            f"``{ctx.author}`` was so cool ``{user}`` died just looking at him.",
            f"``{user}`` slipped on a banana and died. how??",
            f"``{user}`` burnt from ``{ctx.author}``'s epic roast and died, not even going to ask how.",
            f"``{user}`` caught a cold and when taking the medicine, he died of an allergic reaction.",
        ]
        await ctx.send(random.choice(possibledeaths))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ship(self, ctx, user: str, user2: str):
        a = "``"
        if len(user) == 22:
            try:
                user = user.replace("!", "")
                a = ""
            except:
                user = user
        if len(user2) == 22:
            try:
                user2 = user2.replace("!", "")
                a = ""
            except:
                user2 = user2
        lovepercent = random.randint(1, 101)
        rounded = int((round(lovepercent, -1)) / 10)
        shaded = "■" * rounded
        unshaded = (10 - rounded) * "□"
        embedVar = discord.Embed(
            title=f"{shaded}{unshaded}",
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            color=16679378,
        )
        await ctx.send(
            f"**:heartpulse: MATCHMAKING {lovepercent}% :heartpulse:**\n:small_red_triangle: {a+user+a}\n:small_red_triangle_down: {a+user2+a}",
            embed=embedVar,
        )

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ship(self, ctx, user: str, user2: str):
        a = "``"
        if len(user) == 22:
            try:
                user = user.replace("!", "")
                a = ""
            except:
                user = user
        if len(user2) == 22:
            try:
                user2 = user2.replace("!", "")
                a = ""
            except:
                user2 = user2
        lovepercent = random.randint(1, 101)
        rounded = int((round(lovepercent, -1)) / 10)
        shaded = "■" * rounded
        unshaded = (10 - rounded) * "□"
        embedVar = discord.Embed(
            title=f"{shaded}{unshaded}",
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            color=16679378,
        )
        await ctx.send(
            f"**:heartpulse: MATCHMAKING {lovepercent}% :heartpulse:**\n:small_red_triangle: {a+user+a}\n:small_red_triangle_down: {a+user2+a}",
            embed=embedVar,
        )

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def monch(self, ctx):
        message_author = ctx.author
        print("{} issued .monch".format(message_author))

        try:
            await ctx.send(file=discord.File("images\\Monch.gif"))
        except:
            await ctx.send(
                "https://media.discordapp.net/attachments/729675616420495381/753171581194469465/Monch.gif"
            )

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def kill(self, ctx, user: str):
        possibledeaths = [
            f"``{user}`` died of ligma. what's ligma?",
            f"``{user}`` drank too much tea and died. what a brit.",
            f"``{ctx.author}`` was so cool ``{user}`` died just looking at him.",
            f"``{user}`` slipped on a banana and died. how??",
            f"``{user}`` burnt from ``{ctx.author}``'s epic roast and died, not even going to ask how.",
            f"``{user}`` caught a cold and when taking the medicine, he died of an allergic reaction.",
        ]
        await ctx.send(random.choice(possibledeaths))

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ship(self, ctx, user: str, user2: str):
        a = "``"
        if len(user) == 22:
            try:
                user = user.replace("!", "")
                a = ""
            except:
                user = user
        if len(user2) == 22:
            try:
                user2 = user2.replace("!", "")
                a = ""
            except:
                user2 = user2
        lovepercent = random.randint(1, 101)
        rounded = int((round(lovepercent, -1)) / 10)
        shaded = "■" * rounded
        unshaded = (10 - rounded) * "□"
        embedVar = discord.Embed(
            title=f"{shaded}{unshaded}",
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            color=16679378,
        )
        await ctx.send(
            f"**:heartpulse: MATCHMAKING {lovepercent}% :heartpulse:**\n:small_red_triangle: {a+user+a}\n:small_red_triangle_down: {a+user2+a}",
            embed=embedVar,
        )

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ship(self, ctx, user: str, user2: str):
        a = "``"
        if len(user) == 22:
            try:
                user = user.replace("!", "")
                a = ""
            except:
                user = user
        if len(user2) == 22:
            try:
                user2 = user2.replace("!", "")
                a = ""
            except:
                user2 = user2
        lovepercent = random.randint(1, 101)
        rounded = int((round(lovepercent, -1)) / 10)
        shaded = "■" * rounded
        unshaded = (10 - rounded) * "□"
        embedVar = discord.Embed(
            title=f"{shaded}{unshaded}",
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            color=16679378,
        )
        await ctx.send(
            f"**:heartpulse: MATCHMAKING {lovepercent}% :heartpulse:**\n:small_red_triangle: {a+user+a}\n:small_red_triangle_down: {a+user2+a}",
            embed=embedVar,
        )

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def inputtest(self, ctx):
        await ctx.send("say something")
        try:
            await self.bot.wait_for(
                "message", check=lambda msg: msg.author == ctx.author, timeout=30
            )
        except asyncio.TimeoutError:
            await ctx.send("Timeout")
        else:
            await ctx.send("well done. you said something")

        await ctx.send("now say ``tacoz is cool``")
        try:
            await self.bot.wait_for(
                "message",
                check=lambda msg: msg.author == ctx.author
                and msg.content == "tacoz is cool",
                timeout=30,
            )
        except asyncio.TimeoutError:
            await ctx.send("Timeout")
        else:
            await ctx.send("well done. you said ``tacoz is cool``")

        await ctx.send("input test complete!")


def setup(bot):
    bot.add_cog(Fun(bot))
