import discord
import os
import sys

PREFIX = (".", ">")
TOKEN = "NTY2MTkzODI1ODc0MTgyMTY0.XLBbFw.o0yHAbU7R2yq5GnpdO7P7pzJyRY"
OWNERID = ***REMOVED***
footer = "Made with ❤️ by Tacoz!"

client = commands.Bot(
    command_prefix=PREFIX, owner_id=OWNERID, case_insensitive=True)


@client.event
async def on_ready():
    activity = discord.Game(
        name=".help | http://youtube.com/tacozlmao", type=1)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print(f"{client.user.name} is Launched")
    print(client.user.id)
    print('-------------')

bot.remove_command('help')
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

client.run(TOKEN,  bot=True, reconnect=True)