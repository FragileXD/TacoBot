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


def balancecheck(userid):
    db = cluster["coins"]
    collection = db["coins"]
    try:
        post = {
            "_id": userid,
            "bank": 0,
            "maxbank": 100,
            "purse": 0,
        }
        collection.insert_one(post)
    except pymongo.errors.DuplicateKeyError:
        query = {"_id": userid}
        user = collection.find(query)
        for result in user:
            bank = result["bank"]
            maxbank = result["maxbank"]
            purse = result["purse"]
            withdraw = maxbank - bank
            if bank > maxbank:
                collection.update_one({"_id": userid}, {"$set": {"bank": bank}})
                collection.update_one(
                    {"_id": userid}, {"$set": {"purse": purse + withdraw}}
                )


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
            bank = result["bank"]
            maxbank = result["maxbank"]
            purse = result["purse"]

            balancecheck(ctx.author.id)

            embed1 = discord.Embed(
                title=f"{ctx.author}'s balance",
                color=color,
            )
            embed1.add_field(name="Purse:", value=purse, inline=True)
            embed1.add_field(name="Bank:", value=f"{bank}/{maxbank}", inline=True)
            await ctx.send(embed=embed1)

    @commands.command(
        name="deposit",
        description="Deposit money into your bank",
        aliases=["dep"],
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def deposit(self, ctx, amount: str):
        # color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
        db = cluster["coins"]
        collection = db["coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)

        balancecheck(ctx.author.id)

        for result in user:
            bank = result["bank"]
            maxbank = result["maxbank"]
            purse = result["purse"]
            if bank > maxbank:
                collection.update_one({"_id": ctx.author.id}, {"$set": {"bank": bank}})

            if bank < 0 or purse < 0:
                await ctx.send("you are in debt, how is this even possible???")
                if purse < 0 and bank > 0 and 0 - bank > purse:
                    await ctx.send(
                        "since your purse is negative, i will put it back to 0 by taking away funds from your bank. this is what you get for cheating the system lmao"
                    )
                    withdraw = -purse
                    collection.update_one(
                        {"_id": ctx.author.id}, {"$set": {"bank": bank - withdraw}}
                    )
                    collection.update_one(
                        {"_id": ctx.author.id}, {"$set": {"purse": purse + withdraw}}
                    )
            else:
                try:
                    if maxbank >= bank + int(amount):
                        deposit = int(amount)
                        collection.update_one(
                            {"_id": ctx.author.id}, {"$set": {"bank": bank + deposit}}
                        )
                        collection.update_one(
                            {"_id": ctx.author.id}, {"$set": {"purse": purse - deposit}}
                        )
                    elif amount.lower() == "all":
                        if maxbank - bank > purse:
                            deposit = purse
                            collection.update_one(
                                {"_id": ctx.author.id},
                                {"$set": {"bank": bank + deposit}},
                            )
                            collection.update_one(
                                {"_id": ctx.author.id},
                                {"$set": {"purse": purse - deposit}},
                            )
                        elif purse >= maxbank - bank:
                            deposit = maxbank - bank
                            collection.update_one(
                                {"_id": ctx.author.id},
                                {"$set": {"bank": bank + deposit}},
                            )
                            collection.update_one(
                                {"_id": ctx.author.id},
                                {"$set": {"purse": purse - deposit}},
                            )
                    else:
                        deposit = maxbank - bank
                        if purse < deposit:
                            await ctx.send("you don't have enough money lmao")
                        else:
                            collection.update_one(
                                {"_id": ctx.author.id},
                                {"$set": {"bank": bank + deposit}},
                            )
                            collection.update_one(
                                {"_id": ctx.author.id},
                                {"$set": {"purse": purse - deposit}},
                            )
                except ValueError:
                    await ctx.send("input a number or just say ``all`` dummy")

    @deposit.error
    async def deposit_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Input something after the command")
        else:
            raise (error)


def setup(bot):
    bot.add_cog(Economy(bot))