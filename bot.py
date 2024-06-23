import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from events import MyBot
from commands import grind

# Load environment variables from .env file (useful for local development)
load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Debugging statement
print(f"Token: {TOKEN[:5]}...")  # Ensure this prints the actual token (or part of it for security reasons)

# Check if the token is loaded correctly
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable is not set")

# Define the bot with intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = MyBot(command_prefix='/', intents=intents)

# Register commands
bot.command(name='grind')(grind)

# Run the bot
bot.run(TOKEN)
