import os
import discord
import yaml
import asyncio
from discord.ext import commands
from local_ai_chatbot import get_local_ai_response  # Import the local AI chat bot function

# Load configuration from .yml file
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Get the token from environment variable
TOKEN = os.getenv('DISCORD_TOKEN')

# Check if the token is loaded correctly
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable is not set")

# Define the bot with intents
intents = discord.Intents.default()
intents.messages = config['intents']['messages']
intents.message_content = config['intents']['message_content']

class MyBot(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)
        self.state = 'main_menu'
        
    async def setup_hook(self):
        for module in config['modules']:
            await self.load_extension(module)
        
    async def on_ready(self):
        print(f'Logged in as {self.user}')

# Create the bot instance
bot = MyBot(command_prefix=config['bot']['prefix'], intents=intents)

# Register commands
@bot.command(name='grind')
async def grind_command(ctx, level: int):
    await grind(ctx, level)

@bot.command(name='chat')
async def chat_command(ctx, *, prompt: str):
    response = await get_local_ai_response(prompt)
    await ctx.send(response)

# Run the bot
bot.run(TOKEN)
