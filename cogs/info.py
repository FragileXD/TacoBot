import discord
import os
import sys
import random
import time
import math
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta
from utils.data import getJSON

config = getJSON("config.json")

footer = config.footembed
start_time = time.monotonic()


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="help",
        description="The help command",
        aliases=["commands", "command", "hewwlp"],
        usage="cog",
    )
    async def help_command(self, ctx, cog="all"):
        """ Replaces Default Command"""
        color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)

        emojiCategory = {
            "Utility": ":tools:",
            "Info": ":question:",
            "Fun": ":smile:",
            "Moderation": ":shield:",
            "Minecraft": "<:minecrafticon0:762895015579222066>",
            "Hypixel": "<:Hypixel:745240325064228884>",
            "Memey": "<:Reddit:745241144207867997>",
            "Animals": ":dog:",
            "Economy": ":money_mouth:",
        }

        if cog == "all":
            cogls = []
            for file in os.listdir("cogs"):
                if file.endswith(".py"):
                    name = file[:-3].title()
                    cogls.append(str(name))

            help_embed = discord.Embed(title="TacoBot Command Categories", color=color)
            for scog in cogls:
                try:
                    emoji = emojiCategory[scog]
                    help_embed.add_field(
                        name=f"{emoji} {scog}",
                        value=f"```css\n{ctx.prefix}help {scog}```",
                    )
                except:
                    help_embed.add_field(
                        name=scog, value=f"```css\n{ctx.prefix}help {scog}```"
                    )

            help_embed.set_footer(text="use '.' or '>' before each command | " + footer)
        else:
            cogA = cog.lower()
            emojiCategory = {
                "Utility": ":tools:",
                "Info": ":question:",
                "Fun": ":smile:",
                "Moderation": ":shield:",
                "Minecraft": "<:minecrafticon0:762895015579222066>",
                "Hypixel": "<:Hypixel:745240325064228884>",
                "Memey": "<:Reddit:745241144207867997>",
                "Animals": ":dog:",
                "Economy": ":money_mouth:",
            }

            cogs = [c for c in self.bot.cogs.keys()]

            lower_cogs = [c.lower() for c in cogs]

            all_commands = {}
            for cog in cogs:
                all_commands[cog] = self.bot.get_cog(
                    cogs[lower_cogs.index(cog.lower())]
                ).get_commands()

            for cog in all_commands:
                for c in all_commands[cog]:
                    pass  # print(c)

            all_commandsData = [c for cog in all_commands for c in all_commands[cog]]
            all_commandsName = [
                c.name for cog in all_commands for c in all_commands[cog]
            ]

            if cogA in lower_cogs:
                help_embed = discord.Embed(
                    title=f"{emojiCategory[cogA.title()]} {cogA.title()} Commands",
                    color=3066993,
                )
                commands_list = self.bot.get_cog(
                    cogs[lower_cogs.index(cogA)]
                ).get_commands()
                help_text = ""

                for command in commands_list:
                    help_text += (
                        f"```css\n{command.name} [{' '.join(command.aliases)}]\n```"
                    )
                help_embed.description = help_text

            elif cogA in all_commandsName:
                command = all_commandsData[all_commandsName.index(cogA)]
                help_embed = discord.Embed(
                    title=f"Information about {ctx.prefix}{command.name}", color=3066993
                )
                help_embed.add_field(
                    name="**Description**\n",
                    value=f"{command.description}\n",
                    inline=False,
                )
                help_embed.add_field(
                    name="**Aliases**\n",
                    value=f"`{' '.join(command.aliases)}`",
                    inline=False,
                )

            else:
                await ctx.send("Invalid command/category specified.")
                return

        await ctx.send(embed=help_embed)

    @commands.command(
        name="ping",
        description="Gets the response time of the bot",
        aliases=["lag", "responsetime", "pingo"],
    )
    async def ping(self, ctx):
        print("{} issued .ping 🏓".format(ctx.author))
        """ Pong! """
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("🏓 Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

    @commands.command(
        name="invite",
        description="Gets the an invite link for the bot",
        aliases=["botinvite", "addbot", "botinv"],
    )
    async def botinvite(self, ctx):
        invite_embed = discord.Embed(title="Invite me to your Server!", color=3066993)
        print("{} issued .invite 😉".format(ctx.author))
        invite_embed.add_field(
            name=f"Invite!",
            value=f"[Click to Invite Me!](https://discord.com/api/oauth2/authorize?client_id=566193825874182164&permissions=8&scope=bot)",
        )
        invite_embed.set_footer(text=footer)
        await ctx.send(embed=invite_embed)

    @commands.command(
        name="support",
        description="Gets the support server invite",
        aliases=["server", "supportserver", "helpserver", "helpinvite", "devserver"],
    )
    async def serverinvite(self, ctx):
        print("{} issued .serverinvite".format(ctx.author))
        invite_embed = discord.Embed(
            title="Official Tacoz & TacoBOT Development server!",
            description=f"https://discord.io/Tacoz",
            color=3066993,
        )
        invite_embed.set_footer(text=footer)
        await ctx.send(embed=invite_embed)

    @commands.command
    async def joined(self, ctx, member: discord.Member):
        await ctx.send("{0.name} joined in {0.joined_at}".format(member))


"""
    @commands.command(
        name='source',
        description='Gets the source code link',
        aliases=['sourcecode']
    )
    async def sourceCode(self, ctx):
        source_embed = discord.Embed(
            title='Here is my Source Code!',
            description=f"https://github.com/NotTacoz/TacoBot",
            color=3066993
        )
        source_embed.set_footer(text=footer)
        await ctx.send(embed=source_embed)
"""


def setup(bot):
    bot.add_cog(Info(bot))
