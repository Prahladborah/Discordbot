import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Check if the token is loaded correctly
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable is not set")

# Define the bot with intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)
        self.state = 'main_menu'
        
    async def setup_hook(self):
        await self.load_extension('cogs.builds')
        await self.load_extension('cogs.blacksmithing')
        await self.load_extension('cogs.synthesis')
        await self.load_extension('cogs.equipment')
        await self.load_extension('events')
        
    async def on_ready(self):
        print(f'Logged in as {self.user}')

# Create the bot instance
bot = MyBot(command_prefix='/', intents=intents)

# Register commands
@bot.command(name='grind')
async def grind_command(ctx, level: int):
    await grind(ctx, level)

# Run the bot
bot.run(TOKEN)
