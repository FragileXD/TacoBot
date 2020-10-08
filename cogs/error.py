import discord
import traceback
import random
from concurrent.futures._base import TimeoutError
from discord.ext import commands
from random import choice


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def send(self, ctx, msg):
        try:
            color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
            await ctx.send(embed=discord.Embed(color=color, description=msg))
        except discord.errors.Forbidden:
            pass
        except Exception:
            try:
                color = int("{:06x}".format(random.randint(0, 0xFFFFFF)), 16)
                await ctx.send(embed=discord.Embed(color=color, description=msg))
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
                ctx, "<a:Aqua_panic:763690124805537842> Hold on! You can't use multiple of that command at once!"
            )
            return

        if isinstance(e, commands.CommandOnCooldown):
            if round(e.retry_after, 2) <= 0:
                await ctx.reinvoke()

            descs = [
                "Didn't your parents tell you that [patience is a virtue](http://www.patience-is-a-virtue.org/)? Calm down and wait another {0} seconds.",
                "Hey, you need to wait another {0} seconds before doing that again.",
                "Hrmmm, looks like you need to wait another {0} seconds before doing that again.",
                ":yawning_face: YAWNNNN! You need to wait another {0} seconds before trying again"
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
                ctx, "<:02smug:763689785364709376> Nice try, but you don't have the permissions to do that."
            )
            return

        if isinstance(e, commands.CheckAnyFailure):
            if "MissingPermissions" in str(
                e.errors
            ):  # yes I know this is jank but it works so shhhh
                await self.send(
                    ctx, "<:AwOo:763689785218695209> Nice try, but you don't have the permissions to do that."
                )
                return

        if isinstance(e, commands.BotMissingPermissions):
            await self.send(
                ctx, "You didn't give me proper the permissions to do that!"
            )
            return

        if "NoStatError" in str(e):
            await self.send(
                ctx, "<a:Aqua_panic:763690124805537842> No stats available!"
            )
            return
        else:
            print(e)
            return e

        try:
            if isinstance(e, TimeoutError) or isinstance(e.original, TimeoutError):
                self.bot.get_cog("Cache").failed += 1
                await self.send(
                    ctx,
                     a:Aqua_panic:763690124805537842>For some reason, the Hypixel API took too long to respond. Please try again later.",
                )
        except Exception:
            pass


def setup(bot):
    bot.add_cog(Errors(bot))