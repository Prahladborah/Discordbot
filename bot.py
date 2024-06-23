import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from responses import send_greeting_response, send_potato_response, send_baka_response
from help_triggers import send_help_trigger
from commands import grind

# Load environment variables from .env file
load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Check if the token is loaded correctly
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable is not set")

# Define initial extensions
initial_extensions = ['cogs.builds', 'cogs.blacksmithing', 'cogs.synthesis', 'cogs.equipment', 'events']

# Define the bot with intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)
        self.state = 'main_menu'
        for extension in initial_extensions:
            self.load_extension(extension)
        
    async def on_ready(self):
        print(f'Logged in as {self.user}')

# Create the bot instance
bot = MyBot(command_prefix='/', intents=intents)

# Register commands
@bot.command(name='grind')
async def grind_command(ctx):
    await grind(ctx)

# Run the bot
bot.run(TOKEN)
