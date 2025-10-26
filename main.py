import discord
from discord import app_commands
import os
from schedule import *
from datetime import date

intents = discord.Intents.default()
intents.message_content = True

api_key = os.getenv('PREMIER_BOT_API_KEY')

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    try:
        await tree.sync()
    except Exception as e:
        print(e)

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('/gametoday'):
#         await message.channel.send(f"**{gameType[date.today().weekday()]}** today at: **{premierSchedule[date.today().weekday()]}**")


@tree.command(name="gametoday", description="Returns today's game schedule and type (Scrim or Match)")
async def gametoday(interaction: discord.Integration):
    await interaction.response.send_message(f"**{gameType[date.today().weekday()]}** today at: **{premierSchedule[date.today().weekday()]}**")

client.run(api_key)

