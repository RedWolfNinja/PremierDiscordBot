import discord
import os
from schedule import *
from datetime import date

intents = discord.Intents.default()
intents.message_content = True

api_key = os.getenv('PREMIER_BOT_API_KEY')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/gametoday'):
        await message.channel.send(f"**{gameType[date.today().weekday()]}** today at: **{premierSchedule[date.today().weekday()]}**")

client.run(api_key)

