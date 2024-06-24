import os
import discord
import yaml
import asyncio

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

# Run the bot
bot.run(TOKEN)
