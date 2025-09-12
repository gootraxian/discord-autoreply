import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        await message.channel.send("Hello! I don't recieve dms, if you want to message me create a ticket in my discord (https://discord.gg/f7X3sh2PBk), good luck!")

    await bot.process_commands(message)

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
