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


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', aliases=['hi'])
    async def hello(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel
        print("{} issued .hello 👋".format(message_author))
        await message_channel.send(
            "<a:party_blob:743099804279898143> Hello, {}! 👋".format(
                message_author.name))

    @commands.command(
        name='uptime',
        description='Shows the amount of time the bot has been online',
        aliases=['timeonline', 'timeup'])
    async def uptime(self, ctx):
        message_author = ctx.author
        message_channel = ctx.channel
        print("{} issued .uptime ⬆".format(message_author))
        embedVar = discord.Embed(
            title="TacoBot Uptime",
            description=
            f"TacoBot has been up for `{timedelta(seconds=time.monotonic() - start_time)}`",
            color=3066993)
        embedVar.set_footer(text=footer)
        await message_channel.send(embed=embedVar)

    @commands.command(
        name='choose',
        description='For when you wanna settle the score some other way',
        aliases=['chooser'])
    async def choose(self, ctx, *, message):
        message_author = ctx.author
        print("{} issued .choose".format(message_author))

        jjj = message.split(" ")
        e = random.choice(jjj)

        embedVar = discord.Embed(title="TacoBot Choose",
                                 description=f"Possible Outcomes: {jjj}",
                                 color=3066993)
        embedVar.add_field(name="Randomly Chosen Outcome:",
                           value=e,
                           inline=False)
        embedVar.set_footer(text=footer)
        await ctx.send(embed=embedVar)

    @commands.group(name='encode',
                    description='Encodes the input',
                    aliases=['encrypt'])
    async def encode(self, ctx):
        if ctx.invoked_subcommand is None:
            e = discord.Embed(title='Encode Command',
                              description=f"Encodes the given input",
                              color=0x2ECC71)
            e.add_field(name="Usage",
                        value=f"`?encode <encoding_type> <input>`")
            e.add_field(
                name="Avaliable encoding types",
                value=
                f"`base16 base32 base64 base85 hex binary url rot13 rot47 `")
            e.set_footer(text=footer)
            await ctx.send(embed=e)

        @encode.command(name="base64", aliases=["b64"])
        async def encode_base64(self,
                                ctx,
                                *,
                                input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = base64.b64encode(input.encode('UTF-8')).decode('utf-8')
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @encode.command(name="base32", aliases=["b32"])
        async def encode_base32(self,
                                ctx,
                                *,
                                input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = base64.b32encode(input.encode('UTF-8')).decode('utf-8')
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @encode.command(name="base16", aliases=["b16"])
        async def encode_base16(self,
                                ctx,
                                *,
                                input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = base64.b16encode(input.encode('UTF-8')).decode('utf-8')
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @encode.command(name="base85", aliases=["b85"])
        async def encode_base85(self,
                                ctx,
                                *,
                                input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = base64.b85encode(input.encode('UTF-8')).decode('utf-8')
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @encode.command(name="hex", aliases=[])
        async def encode_hex(self,
                             ctx,
                             *,
                             input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = (input.encode('UTF-8').hex())  #.decode('utf-8')
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @encode.command(name="url", aliases=[])
        async def encode_url(self,
                             ctx,
                             *,
                             input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = requote_uri(str(input))
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @encode.command(name="rot13", aliases=['r13'])
        async def encode_rot13(self,
                               ctx,
                               *,
                               input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = codecs.encode(str(input), "rot-13")
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        #https://github.com/VoxelPixel
        @encode.command(name="rot47", aliases=['r47'])
        async def encode_rot47(self,
                               ctx,
                               *,
                               input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            message = str(input)
            key = 47
            encryp_text = ""

            for i in range(len(message)):
                temp = ord(message[i]) + key
                if ord(message[i]) == 32:
                    encryp_text += " "
                elif temp > 126:
                    temp -= 94
                    encryp_text += chr(temp)
                else:
                    encryp_text += chr(temp)

            result = encryp_text

            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @encode.command(name="binary", aliases=['bin'])
        async def encode_binary(self,
                                ctx,
                                *,
                                input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = ''.join(format(ord(c), '08b') for c in str(input))
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @commands.group(name='decode',
                        description='Decode the input',
                        aliases=['decrypt'])
        async def decode(self, ctx):
            if ctx.invoked_subcommand is None:
                e = discord.Embed(title='Decode Command',
                                  description=f"Decodes the given input",
                                  color=0x2ECC71)
                e.add_field(name="Usage",
                            value=f"`?decode <decoding_type> <input>`")
                e.add_field(
                    name="Avaliable decoding types",
                    value=
                    f"`base16 base32 base64 base85 hex binary url rot13 rot47 `"
                )
                e.set_footer(text=footer)
                await ctx.send(embed=e)

        @decode.command(name="base64", aliases=["b64"])
        async def decode_base64(self,
                                ctx,
                                *,
                                input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = base64.b64decode(input.encode('UTF-8')).decode('utf-8')
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @decode.command(name="base16", aliases=["b16"])
        async def decode_base16(self,
                                ctx,
                                *,
                                input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = base64.b16decode(input.encode('UTF-8')).decode('utf-8')
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @decode.command(name="base32", aliases=["b32"])
        async def decode_base32(self,
                                ctx,
                                *,
                                input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = base64.b32decode(input.encode('UTF-8')).decode('utf-8')
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @decode.command(name="base85", aliases=["b85"])
        async def decode_base85(self,
                                ctx,
                                *,
                                input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = base64.b85decode(input.encode('UTF-8')).decode('utf-8')
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @decode.command(name="rot13", aliases=['r13'])
        async def decode_rot13(self,
                               ctx,
                               *,
                               input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = codecs.encode(str(input), "rot-13")
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @decode.command(name="hex", aliases=[])
        async def decode_hex(self,
                             ctx,
                             *,
                             input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = (binascii.unhexlify(
                input.encode('UTF-8'))).decode('utf-8')
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @decode.command(name="url", aliases=[])
        async def decode_url(self,
                             ctx,
                             *,
                             input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = unquote(str(input))
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @decode.command(name="rot47", aliases=['r47'])
        async def decode_rot47(self,
                               ctx,
                               *,
                               input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            message = str(input)
            key = 47
            decryp_text = ""

            for i in range(len(message)):
                temp = ord(message[i]) - key
                if ord(message[i]) == 32:
                    decryp_text += " "
                elif temp < 32:
                    temp += 94
                    decryp_text += chr(temp)
                else:
                    decryp_text += chr(temp)

            result = decryp_text

            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)

        @decode.command(name="binary", aliases=['bin'])
        async def decode_binary(self,
                                ctx,
                                *,
                                input: commands.clean_content = None):
            if not input:
                e = discord.Embed(
                    description=":no_entry_sign: You must give an input string",
                    colour=0xE74C3C)
                await ctx.send(embed=e)
                return

            e = discord.Embed(title="Result", colour=0x2ECC71)

            result = self.decode_binary_string(str(input).replace(" ", ""))
            e.add_field(name="Input", value=f"`{input}`")
            e.add_field(name="Output", value=f"`{result}`")
            e.set_footer(text=footer)

            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Utility(bot))
