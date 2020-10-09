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

footer = config.footembed
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
            embed1.set_footer(text=footer)
            await ctx.send(embed=embed1)
        except pymongo.errors.DuplicateKeyError:
            embed1 = discord.Embed(
                title="Error!",
                description=f"Sorry {ctx.author.mention} your already registered!",
                color=color,
            )
            embed1.set_footer(text=footer)
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
            embed1.add_field(
                name="Total:", value=f"{(int(bank)+int(purse))}", inline=True
            )
            if bank + purse == 420 or purse == 420 or bank == 420:
                embed1.set_footer(text=f"thats the weed number!11! {footer}")
            elif bank + purse == 69 or purse == 69 or bank == 69:
                embed1.set_footer(text=f"thats the hecking funny number!11! {footer}")
            elif bank + purse == 666 or purse == 666 or bank == 666:
                embed1.set_footer(text=f"spooky | {footer}")
            else:
                embed1.set_footer(text=footer)
            await ctx.send(embed=embed1)
        else:
            await ctx.send("No Account Detected... Creating Account")
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
                embed1.set_footer(text=footer)
                await ctx.send(embed=embed1)
            except pymongo.errors.DuplicateKeyError:
                embed1 = discord.Embed(
                    title="Error!",
                    description=f"Sorry {ctx.author.mention} your already registered!",
                    color=color,
                )
                embed1.set_footer(text=footer)
                await ctx.send(embed=embed1)
                return

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

        for result in user:
            bank = result["bank"]
            maxbank = result["maxbank"]
            purse = result["purse"]
            if bank > maxbank:
                collection.update_one({"_id": ctx.author.id}, {"$set": {"bank": bank}})

            balancecheck(ctx.author.id)

            try:
                if maxbank == bank:
                    await ctx.send(f"{ctx.author.mention} your bank is full!")
                elif amount.lower() == "all":
                    if maxbank - bank > 0:
                        deposit = maxbank - bank
                    collection.update_one(
                        {"_id": ctx.author.id},
                        {"$set": {"bank": bank + deposit}},
                    )
                    collection.update_one(
                        {"_id": ctx.author.id},
                        {"$set": {"purse": purse - deposit}},
                    )
                    await ctx.send(f"{ctx.author.mention} deposited ${deposit}")
                elif maxbank >= bank + int(amount):
                    deposit = int(amount)
                    collection.update_one(
                        {"_id": ctx.author.id}, {"$set": {"bank": bank + deposit}}
                    )
                    collection.update_one(
                        {"_id": ctx.author.id}, {"$set": {"purse": purse - deposit}}
                    )
                    await ctx.send(f"{ctx.author.mention} deposited ${deposit}")
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
                    await ctx.send(f"{ctx.author.mention} deposited ${deposit}")
                else:
                    deposit = maxbank - bank
                    if purse < deposit:
                        await ctx.send(
                            "<a:aquacry:763693175171973140> you don't have enough money lmao"
                        )
                    else:
                        collection.update_one(
                            {"_id": ctx.author.id},
                            {"$set": {"bank": bank + deposit}},
                        )
                        collection.update_one(
                            {"_id": ctx.author.id},
                            {"$set": {"purse": purse - deposit}},
                        )
                        await ctx.send(f"{ctx.author.mention} deposited ${deposit}")
            except ValueError:
                await ctx.send("input a number or just say ``all`` dummy")
            else:
                await ctx.send("No Account Detected... Creating Account")
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
                    embed1.set_footer(text=footer)
                    await ctx.send(embed=embed1)
                except pymongo.errors.DuplicateKeyError:
                    embed1 = discord.Embed(
                        title="Error!",
                        description=f"Sorry {ctx.author.mention} your already registered!",
                        color=color,
                    )
                    embed1.set_footer(text=footer)
                    await ctx.send(embed=embed1)
                    return

    @commands.command(
        name="withdraw",
        description="Withdraw money into your bank",
        aliases=["with"],
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def withdraw(self, ctx, amount: str):
        # color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
        db = cluster["coins"]
        collection = db["coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)

        for result in user:
            bank = result["bank"]
            # maxbank = result["maxbank"]
            purse = result["purse"]

            balancecheck(ctx.author.id)

            try:
                if amount.lower() == "all":
                    withdraw = bank
                    collection.update_one(
                        {"_id": ctx.author.id}, {"$set": {"bank": bank - withdraw}}
                    )
                    collection.update_one(
                        {"_id": ctx.author.id},
                        {"$set": {"purse": purse + withdraw}},
                    )
                    await ctx.send(f"{ctx.author.mention} Withdrawn ${withdraw}.")
                elif int(amount) <= bank:
                    withdraw = int(amount)
                    collection.update_one(
                        {"_id": ctx.author.id}, {"$set": {"bank": bank - withdraw}}
                    )
                    collection.update_one(
                        {"_id": ctx.author.id},
                        {"$set": {f"purse": purse + withdraw}},
                    )
                    await ctx.send(f"{ctx.author.mention} Withdrawn ${withdraw}.")
                else:
                    await ctx.send(
                        "<a:aquacry:763693175171973140> you dont have the money lmao"
                    )
            except ValueError:
                await ctx.send("input a number or just say ``all`` dummy")
            else:
                await ctx.send("No Account Detected... Creating Account")
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
                    embed1.set_footer(text=footer)
                    await ctx.send(embed=embed1)
                except pymongo.errors.DuplicateKeyError:
                    embed1 = discord.Embed(
                        title="Error!",
                        description=f"Sorry {ctx.author.mention} your already registered!",
                        color=color,
                    )
                    embed1.set_footer(text=footer)
                    await ctx.send(embed=embed1)
                    return

    @commands.command(name="beg", description="Beg for money", aliases=["begger"])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def beg(self, ctx):
        # color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
        db = cluster["coins"]
        collection = db["coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)
        people = [
            "Donald Trump",
            "Obama",
            "TacoBot",
            "Tacoz",
            "<:shrek:763697330352029696> Shrek",
            "your mom",
            "Rick Astley",
            "Doge",
        ]
        prompts = [
            "<:02smug:763689785364709376> you're too smelly go away",
            "bruh no",
            "...",
            ":yucky: :vomitblegh: :disgusztfaze69420: :bruhwhy: ew no",
            "go work or something",
            "no <:1975_RukaBleh:763694703182348289>",
            "in your dreams",
            "<:SataniaThumbsUp:763689835986026506> i only give money to hookers",
            "<:akkoShrug:763689780063240204> i already gave away everything to the last guy who asked",
            ":knife: \\*stabs you* jk, unless? :flushed:",
        ]

        for result in user:
            purse = result["purse"]

            balancecheck(ctx.author.id)

            income = random.randint(1, 1000000001)
            if income != 1000000000:
                income = random.randint(1, 101)
                if income > 60:
                    income = random.randint(1, 250)
                    await ctx.send(
                        f"{random.choice(people)} gave {ctx.author.mention} ${income}."
                    )
                    collection.update_one(
                        {"_id": ctx.author.id},
                        {"$set": {"purse": purse + income}},
                    )
                else:
                    await ctx.send(f"{random.choice(people)}: {random.choice(prompts)}")
            else:
                income = random.randint(1000, 100000000)
                collection.update_one(
                    {"_id": ctx.author.id},
                    {"$set": {"purse": purse + income}},
                )
                await ctx.send(
                    f"a rich {random.choice(people)} came and gave {ctx.author.mention} a jackpot worth ${income}."
                )
        else:
            await ctx.send("No Account Detected... Creating Account")
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
                embed1.set_footer(text=footer)
                await ctx.send(embed=embed1)
            except pymongo.errors.DuplicateKeyError:
                embed1 = discord.Embed(
                    title="Error!",
                    description=f"Sorry {ctx.author.mention} your already registered!",
                    color=color,
                )
                embed1.set_footer(text=footer)
                await ctx.send(embed=embed1)
                return


def setup(bot):
    bot.add_cog(Economy(bot))
