import os
import asyncio
import discord
from discord.ext import commands
import database as db

# Bot setup with required gateway intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"⚓ Berry Broker logged in as {bot.user} (ID: {bot.user.id})")
    print("--------------------------------------------------")

async def main():
    # 1. Initialize SQLite Database Schema
    db.init_db()

    # 2. Load Cogs
    await bot.load_extension("cogs.economy")
    await bot.load_extension("cogs.shop")

    # 3. Start Bot (Set token via environment variable or pass explicitly)
    token = os.getenv("DISCORD_BOT_TOKEN") or "YOUR_DISCORD_BOT_TOKEN_HERE"
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())