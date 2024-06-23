import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
from responses import send_greeting_response, send_potato_response, send_baka_response
from help_triggers import send_help_trigger
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

# Define initial extensions
initial_extensions = ['cogs.builds', 'cogs.blacksmithing', 'cogs.synthesis', 'cogs.equipment']

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

    async def on_message(self, message):
        if message.author.bot:
            return

        content = message.content.lower()

        # Check for greetings and send a response
        await send_greeting_response(message, content)

        # Check for "potato guide" or "potato bot" and send a response
        await send_potato_response(message, content)

        # Check for "baka bot" and send a response
        await send_baka_response(message, content)

        # Initial trigger for help
        if any(x in content for x in ['is anyone here who can help me', 'i need help', 'someone help me', 'hey guide','elite guide','hey elite']):
            self.state = await send_help_trigger(message)
        else:
            await self.process_commands(message)

# Create the bot instance
bot = MyBot(command_prefix='/', intents=intents)

# Register commands
@bot.command(name='grind')
async def grind_command(ctx):
    await grind(ctx)

# Run the bot
bot.run(TOKEN)
