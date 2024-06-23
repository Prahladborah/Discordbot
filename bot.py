import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from events import on_ready, on_message
from commands import grind

# Load environment variables from .env file (useful for local development)
load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Check if the token is loaded correctly
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable is not set")

# Define the bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Register event handlers
bot.event(on_ready)
bot.event(on_message)

# Register commands
bot.command(name='grind')(grind)

# Run the bot
bot.run(TOKEN)
