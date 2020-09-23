import discord
import traceback
from aiopypixel.exceptions.exceptions import *
from concurrent.futures._base import TimeoutError
from discord.ext import commands
from random import choice


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def send(self, ctx, msg):
        try:
            await ctx.send(
                embed=discord.Embed(
                    color=await self.bot.cc(ctx.author.id), description=msg
                )
            )
        except discord.errors.Forbidden:
            pass
        except Exception:
            try:
                await ctx.send(
                    embed=discord.Embed(color=await self.bot.cc(), description=msg)
                )
            except discord.errors.Forbidden:
                pass

    @commands.Cog.listener()
    async def on_command_error(self, ctx, e):

        # Commands to ignore
        for _type in [
            commands.CommandNotFound,
            commands.NotOwner,
            commands.CheckFailure,
            discord.errors.Forbidden,
        ]:
            if isinstance(e, _type):
                return

        if isinstance(e, commands.MaxConcurrencyReached):
            await self.send(
                ctx, "Hold on! You can't use multiple of that command at once!"
            )
            return

        if isinstance(e, commands.CommandOnCooldown):
            if await self.bot.get_cog("Database").is_premium(ctx.author.id):
                e.retry_after -= (2 / 5) * e.cooldown.per

            if round(e.retry_after, 2) <= 0:
                await ctx.reinvoke()

            descs = [
                "Didn't your parents tell you that [patience is a virtue](http://www.patience-is-a-virtue.org/)? Calm down and wait another {0} seconds.",
                "Hey, you need to wait another {0} seconds before doing that again.",
                "Hrmmm, looks like you need to wait another {0} seconds before doing that again.",
                "Don't you know [patience is a virtue](http://www.patience-is-a-virtue.org/)? Wait another {0} seconds.",
            ]

            await self.send(ctx, choice(descs).format(round(e.retry_after, 2)))
            return

        if isinstance(e, commands.errors.MissingRequiredArgument):
            await self.send(ctx, "Looks like you're forgetting to put something in!")
            return

        if isinstance(e, commands.BadArgument):
            await self.send(ctx, "Looks like you typed something wrong.")
            return

        if isinstance(e, commands.errors.NoPrivateMessage):
            await self.send(ctx, "This command can't be used in private chat channels.")
            return

        if isinstance(e, commands.MissingPermissions):
            await self.send(
                ctx, "Nice try, but you don't have the permissions to do that."
            )
            return

        if isinstance(e, commands.CheckAnyFailure):
            if "MissingPermissions" in str(
                e.errors
            ):  # yes I know this is jank but it works so shhhh
                await self.send(
                    ctx, "Nice try, but you don't have the permissions to do that."
                )
                return

        if isinstance(e, commands.BotMissingPermissions):
            await self.send(
                ctx, "You didn't give me proper the permissions to do that!"
            )
            return

        if "NoStatError" in str(e):
            await self.send(ctx, "No stats available!")
            return

        try:
            if isinstance(e, TimeoutError) or isinstance(e.original, TimeoutError):
                self.bot.get_cog("Cache").failed += 1
                await self.send(
                    ctx,
                    "For some reason, the Hypixel API took too long to respond. Please try again later.",
                )
        except Exception:
            pass

        if isinstance(e.original, HypixelAPIError):
            self.bot.get_cog("Cache").failed += 1
            await self.send(
                ctx,
                "For some reason, the Hypixel API is not working properly. Please try again later.",
            )

        if isinstance(e.original, RateLimitError):
            await self.send(
                ctx,
                f"Uh oh, something took way too long, try again! If this message persists, "
                f"please contact us on the [support server](https://discord.gg/{self.bot.guild_invite_code}), thank you!",
            )
            return

        if isinstance(e, InvalidPlayerError):
            await self.send(ctx, f'Player "`{e.player}`" is invalid or doesn\'t exist!')
            return

        if isinstance(e.original, InvalidPlayerError):
            await self.send(
                ctx, f'Player "`{e.original.player}`" is invalid or doesn\'t exist!'
            )
            return

        if isinstance(e.original, InvalidGuildError):
            await self.send(ctx, "That guild is invalid or doesn't exist!")
            return

        if isinstance(e.original, NullPlayerError):
            await self.send(
                ctx,
                "That player hasn't joined Hypixel before! (They don't have any stats!)",
            )
            return


def setup(bot):
    bot.add_cog(Errors(bot))