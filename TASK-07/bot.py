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

    # 3. Retrieve token strictly from environment variable
    token = os.getenv("DISCORD_BOT_TOKEN")
    
    if not token or token == "your_actual_token_here" or token.startswith("MTI3..."):
        print("\n❌ ERROR: Invalid or missing DISCORD_BOT_TOKEN!")
        print("Please set your real token using: export DISCORD_BOT_TOKEN=\"your_copied_token\"\n")
        return

    # 4. Start the bot
    await bot.start(token.strip())

if __name__ == "__main__":
    asyncio.run(main())