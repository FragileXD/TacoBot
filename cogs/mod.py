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

footer = "Made with ❤️ by Tacoz!"
start_time = time.monotonic()


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='whois',
                      description='Gets info about a user',
                      aliases=['userinfo', 'user', 'user_info'])
    @commands.guild_only()
    async def whois(self, ctx, user: discord.Member = None):
        if not user:
            e = discord.Embed(
                description=":no_entry_sign: You must specify a user",
                colour=0xE74C3C)
            e.set_footer(text=footer)
            await ctx.send(embed=e)
            return

        show_roles = ', '.join([
            f"<@&{x.id}>"
            for x in sorted(user.roles, key=lambda x: x.position, reverse=True)
            if x.id != ctx.guild.default_role.id
        ]) if len(user.roles) > 1 else 'None'

        userObject = self.bot.get_user(user.id)

        e = discord.Embed(title=f"{user}", colour=0x2ECC71)

        e.add_field(name="Discord Tag", value=f"{str(user)}")
        e.add_field(name="Nickname",
                    value=user.nick if hasattr(user, "nick") else "None")
        e.add_field(name="User ID", value=user.id)
        e.add_field(name="Account Created",
                    value=user.created_at.strftime("%d %B %Y, %H:%M"))
        e.add_field(name="Server Join Data",
                    value=user.joined_at.strftime("%d %B %Y, %H:%M"))
        e.add_field(name="Is Bot?", value=str(userObject.bot))
        e.set_thumbnail(url=user.avatar_url)
        e.set_footer(text=footer)

        e.add_field(name="Roles", value=show_roles, inline=False)

        await ctx.send(embed=e)

    @commands.command(name='getpfp',
                      description='Gets the profile picture of the user',
                      aliases=['getprofilepic'])
    @commands.guild_only()
    async def getpfp(self, ctx, user: discord.Member = None):
        if not user:
            e = discord.Embed(
                description=":no_entry_sign: You must specify a user",
                colour=0xE74C3C)
            e.set_footer(text=footer)
            await ctx.send(embed=e)
            return

        e = discord.Embed(title=f"{user}'s Profile Picture", colour=0x2ECC71)

        e.set_thumbnail(url=user.avatar_url)
        e.set_footer(text=footer)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Moderation(bot))
