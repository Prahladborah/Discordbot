import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import random

# Load environment variables from .env file (useful for local development)
load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Debugging statement
print(f"Token: {TOKEN[:5]}...")  # Ensure this prints the actual token (or part of it for security reasons)

# Check if the token is loaded correctly
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable is not set")
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Import event handlers and commands
from events import on_ready, on_message
from commands import grind

# Register events and commands
bot.event(on_ready)
bot.event(on_message)
bot.command(name='grind')(grind)
# Run the bot
bot.run(TOKEN)
