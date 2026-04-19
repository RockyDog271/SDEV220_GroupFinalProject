import os
import json
import asyncio
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
statA = 0
statB = 0

def get_json(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())

@bot.event
async def on_ready():
    print(f"Successfully logged in as {bot.user}")
    if not APIcheck.is_running():
        APIcheck.start()


@tasks.loop(minutes = 15)
async def APIcheck():
    channel = (bot.get_channel(CHANNEL_ID))
    global statA
    global statB

    if channel is None:
        channel = await bot.fetch_channel(CHANNEL_ID)
    
    try:
        Backend = get_json(BACKEND_URL)
        # First Backend check, status returned ONLINE, if not then marks as OFFLINE
        if Backend.get("status") == ("ONLINE"):
            await channel.send(":green_circle: Backend Server **ONLINE**")
            StatA = 0
        else:
            await channel.send(":yellow_circle: Backend Server **OFFLINE**")
            StatA += 1
        await asyncio.sleep(0.5) # here to make it feel more "real"
        
        # If OFFLINE for 3+ times, send additional notif
        if StatA >= 3:
            await channel.send(":red_circle: Backend Server **OFFLINE** for extended period of time")
        await asyncio.sleep(0.5) # here to make it feel more "real"

        #if Backend.get("status") == (""):
        #    await channel.send(":orange: Backend Server sas successfully updated recently")
        if Backend.get("info") == ("DEV"):
            await channel.send(":blue_circle: Backend Server is **ONLINE** but is in DEVELOPMENT mode")
        await asyncio.sleep(0.5) # here to make it feel more "real"
        if Backend.get("info") == ("MAINT"):
            await channel.send(":purple_circle: Backend Server is **ONLINE** but is in MAINTENANCE mode")
        await asyncio.sleep(0.5) # here to make it feel more "real"

        # Delay 5s before running through Frontend code (makes it feel more "real")
        await asyncio.sleep(5)

        Frontend = get_json(FRONTEND_URL)
        if Frontend.get("status") == ("ONLINE"):
            await channel.send(":green_circle:  Frontend Server **ONLINE**")
            StatB = 0
        else:
            await channel.send(":yellow_circle:  Frontend Server **OFFLINE**")
            StatB += 1
        await asyncio.sleep(0.5) # here to make it feel more "real"
        
        # If OFFLINE for 3+ times, send additional notif
        if StatB >= 3:
            await channel.send(":red_circle:  Frontend Server **OFFLINE** for extended period of time")
        await asyncio.sleep(0.5) # here to make it feel more "real"
        
        if Frontend.get("info") == ("DEV"):
            await channel.send(":blue_circle: Frontend Server is **ONLINE** but is in DEVELOPMENT mode")
        await asyncio.sleep(0.5) # here to make it feel more "real"
        if Frontend.get("info") == ("MAINT"):
            await channel.send(":purple_circle:  Frontend Server is **ONLINE** but is in MAINTENANCE mode")
        await asyncio.sleep(0.5) # here to make it feel more "real"

    except Exception as AH:
        await channel.send(f"API check failed: {AH}")

@APIcheck.before_loop
async def before_check():
    await bot.wait_until_ready()

bot.run(DISCORD_TOKEN)

# This is old documentation, it may not be accurate
# -   -   -   -   -   -   -   -   -   -   -   -   -
# 🟢 = Server is online and accepting requests
# 🟡 = Server has not responded to last 3 request
# 🔴 = Server is has not responded to more than 3 requests
# 🟠 = Server is Online, but has been updated in past hour
# 🔵 = Server is Online, but in DEV mode
# 🟣 = Server is Online, but is about to be updated