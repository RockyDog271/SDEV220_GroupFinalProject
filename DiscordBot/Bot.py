import os
import json
import discord
import urllib.request
from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
BACKEND_URL = os.getenv("BACKEND_URL")
FRONTEND_URL = os.getenv("FRONTEND_URL")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='>', intents = intents)

def get_json(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())

@bot.event
async def on_ready():
    print(f"Successfully logged in as {bot.user}")
    if not APIcheck.is_running():
        APIcheck.start()


# Hello World command for testing
@tasks.loop(minutes = 15)
async def APIcheck():
    channel = (bot.get_channel(CHANNEL_ID))
    if channel is None:
        channel = await bot.fetch_channel(CHANNEL_ID)
    
    try:
        Backend = get_json(BACKEND_URL)
        Frontend = get_json(FRONTEND_URL)

        if Backend.get("status") == ("good"):
            await channel.send(":green_circle: Backend server **ONLINE**")
        else:
            await channel.send(":red_circle: Backend server **OFFLINE**")
            
        if Frontend.get("status") == ("good"):
            await channel.send(":green_circle: Frontend server **ONLINE**")
        else:
            await channel.send(":red_circle: Frontend server **OFFLINE**")

    except Exception as AH:
        await channel.send(f"API check failed: {AH}")

@APIcheck.before_loop
async def before_check():
    await bot.wait_until_ready()

bot.run(DISCORD_TOKEN)