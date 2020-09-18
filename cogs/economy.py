import discord
import os
import sys
import random
import asyncio
import time
import pymongo
from pymongo import MongoClient
from random import choice
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, Bot
from datetime import timedelta
from utils.data import getJSON

config = getJSON("config.json")

cluster = MongoClient(config.mongoclient)
# db = cluster["coins"]
# collection = db["coins"]

footer = "『 TacoBot ✦ Tacoz 』"
start_time = time.monotonic()


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="start", description="Start your economical adventure!", aliases=["create"]
    )
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def start(self, ctx):
        color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
        try:
            db = cluster["coins"]
            collection = db["coins"]
            post = {
                "_id": ctx.author.id,
                "bank": 0,
                "maxbank": 100,
                "purse": 0,
            }
            collection.insert_one(post)
            embed1 = discord.Embed(
                title=":white_check_mark: Success!",
                description=f"{ctx.author.mention} your have been registered!",
                color=color,
            )
            await ctx.send(embed=embed1)
        except pymongo.errors.DuplicateKeyError:
            embed1 = discord.Embed(
                title="Error!",
                description=f"Sorry {ctx.author.mention} your already registered!",
                color=color,
            )
            await ctx.send(embed=embed1)
            return

    @commands.command(
        name="bal",
        description="View your balance",
        aliases=["balance", "bank", "purse"],
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def bal(self, ctx):
        color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
        db = cluster["coins"]
        collection = db["coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)
        for result in user:
            userbal = result["bank"]
            maxbank = result["maxbank"]
            purse = result["purse"]
            if userbal > maxbank:
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"bank": userbal}}
                )
            embed1 = discord.Embed(
                title=f"{ctx.author}'s balance",
                color=color,
            )
            embed1.add_field(name="Purse:", value=purse, inline=True)
            embed1.add_field(name="Bank:", value=f"{userbal}/{maxbank}", inline=True)
            await ctx.send(embed=embed1)

    @commands.command(
        name="deposit",
        description="Deposit money into your bank",
        aliases=["dep"],
    )
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def deposit(self, ctx):
        color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
        db = cluster["coins"]
        collection = db["coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)

        for result in user:
            userbal = result["bank"]
            maxbank = result["maxbank"]
            purse = result["purse"]
            if userbal > maxbank:
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"bank": userbal}}
                )

            if userbal < 0:
                await ctx.send("you are in debt, how is this even possible???")
            else:
                if maxbank >= bank:
                    deposit = maxbank - bank


def setup(bot):
    bot.add_cog(Economy(bot))