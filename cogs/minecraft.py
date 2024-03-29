import discord
import os
import sys
import random
import aiohttp
import asyncio
import time
import base64
import json
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta
from utils.data import getJSON

config = getJSON("config.json")

footer = config.footembed
start_time = time.monotonic()
apikey = "**REMOVED**"


class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.session = aiohttp.ClientSession()

    @commands.command(name="stealskin", aliases=["skinsteal", "skin"])
    async def skinner(self, ctx, gamertag: str):
        response = await self.session.get(
            f"https://api.mojang.com/users/profiles/minecraft/{gamertag}"
        )
        if response.status == 204:
            await ctx.send(
                embed=discord.Embed(
                    color=3066993, description="That player doesn't exist!"
                )
            )
            return
        uuid = json.loads(await response.text()).get("id")
        if uuid is None:
            await ctx.send(
                embed=discord.Embed(
                    color=3066993, description="That player doesn't exist!"
                )
            )
            return
        response = await self.session.get(
            f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}?unsigned=false"
        )
        content = json.loads(await response.text())
        if "error" in content:
            if content["error"] == "TooManyRequestsException":
                await ctx.send(
                    embed=discord.Embed(
                        color=3066993,
                        description="Oops, we're being ratelimited by the Mojang API, try again later!",
                    )
                )
                return
        if len(content["properties"]) == 0:
            await ctx.send(
                embed=discord.Embed(
                    color=3066993,
                    description="We can't get this person's skin for some reason...",
                )
            )
            return
        undec = base64.b64decode(content["properties"][0]["value"])
        try:
            url = json.loads(undec)["textures"]["SKIN"]["url"]
        except Exception:
            await ctx.send(
                embed=discord.Embed(
                    color=3066993,
                    description="An error occurred while fetching that skin!",
                )
            )
            return
        skin_embed = discord.Embed(
            color=3066993, description=f"{gamertag}'s skin\n[**[Download]**]({url})"
        )
        skin_embed.set_thumbnail(url=url)
        skin_embed.set_image(url=f"https://mc-heads.net/body/{gamertag}")
        await ctx.send(embed=skin_embed)

    @commands.command(name="nametouuid", aliases=["uuid", "getuuid"])
    async def get_uuid(self, ctx, gamertag: str):
        r = await self.session.post(
            "https://api.mojang.com/profiles/minecraft", json=[gamertag]
        )
        j = json.loads(await r.text())  # [0]['id']
        if not j:
            await ctx.send(
                embed=discord.Embed(
                    color=3066993, description="That user could not be found."
                )
            )
            return
        await ctx.send(
            embed=discord.Embed(
                color=3066993, description=f"{gamertag}: ``{j[0]['id']}``"
            )
        )

    @commands.command(name="uuidtoname", aliases=["getgamertag"])
    async def get_gamertag(self, ctx, uuid: str):
        response = await self.session.get(
            f"https://api.mojang.com/user/profiles/{uuid}/names"
        )
        if response.status == 204:
            await ctx.send(
                embed=discord.Embed(
                    color=3066993, description="That player doesn't exist!"
                )
            )
            return
        j = json.loads(await response.text())
        name = j[len(j) - 1]["name"]
        await ctx.send(
            embed=discord.Embed(color=3066993, description=f"{uuid}: ``{name}``")
        )

    @commands.command(name="colorcodes", aliases=["mccolorcodes", "colors", "cc"])
    async def mc_color_codes(self, ctx):
        embed = discord.Embed(
            color=3066993,
            description="Text in Minecraft can be formatted using different codes and\nthe section (``§``) sign.",
        )
        embed.set_author(name="Minecraft Formatting Codes")
        embed.add_field(
            name="Color Codes",
            value="<:red:697541699706028083> **Red** ``§c``\n"
            "<:yellow:697541699743776808> **Yellow** ``§e``\n"
            "<:green:697541699316219967> **Green** ``§a``\n"
            "<:aqua:697541699173613750> **Aqua** ``§b``\n"
            "<:blue:697541699655696787> **Blue** ``§9``\n"
            "<:light_purple:697541699546775612> **Light Purple** ``§d``\n"
            "<:white:697541699785719838> **White** ``§f``\n"
            "<:gray:697541699534061630> **Gray** ``§7``\n",
        )
        embed.add_field(
            name="Color Codes",
            value="<:dark_red:697541699488055426> **Dark Red** ``§4``\n"
            "<:gold:697541699639050382> **Gold** ``§6``\n"
            "<:dark_green:697541699500769420> **Dark Green** ``§2``\n"
            "<:dark_aqua:697541699475472436> **Dark Aqua** ``§3``\n"
            "<:dark_blue:697541699488055437> **Dark Blue** ``§1``\n"
            "<:dark_purple:697541699437592666> **Dark Purple** ``§5``\n"
            "<:dark_gray:697541699471278120> **Dark Gray** ``§8``\n"
            "<:black:697541699496444025> **Black** ``§0``\n",
        )
        embed.add_field(
            name="Formatting Codes",
            value="<:bold:697541699488186419> **Bold** ``§l``\n"
            "<:strikethrough:697541699768942711> ~~Strikethrough~~ ``§m``\n"
            "<:underline:697541699806953583> __Underline__ ``§n``\n"
            "<:italic:697541699152379995> *Italic* ``§o``\n"
            "<:obfuscated:697541699769204736> ||Obfuscated|| ``§k``\n"
            "<:reset:697541699697639446> Reset ``§r``\n",
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Minecraft(bot))
