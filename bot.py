import discord
from discord.ext import commands
import yaml

# Load configuration from config.yml
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

TOKEN = config['discord']['TOKEN']  # Replace with actual token

print(f"Using token: {TOKEN}")  # Debugging: Check the token value

bot = commands.Bot(command_prefix=config['bot']['prefix'])

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(TOKEN)

