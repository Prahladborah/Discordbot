import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file (useful for local development)
load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Check if the token is loaded correctly
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable is not set")

# Define leveling information
leveling_info = {
    range(1, 34): ("Nisel Mountain: Mountainside", "Shell Mask", "Earth"),
    range(34, 50): ("Ancient Empress Tomb: Area 1", "Bone Dragonewt", "Dark"),
    range(50, 60): ("Land Of Chaos: Hidden boss", "Forestia (normal/hard)", "Wind"),
    range(60, 69): ("Land Of Chaos: Hidden boss", "Forestia (Nightmare)", "Wind"),
    range(70, 80): ("Land Under Cultivation: Hill", "Masked Warrior (Hard)", "Earth"),
    range(80, 90): ("Land Under Cultivation: Hill", "Masked Warrior (Nightmare)", "Earth"),
    range(90, 100): ("Gravel Terrace", "Jade Raptor (Nightmare) or Polde Ice Valley: Don-Yeti", "Water"),
    range(100, 110): ("Land Under Cultivation: Hill", "Masked Warrior (Ultimate)", "Earth"),
    range(110, 117): ("Spring of Rebirth: Top", "Cerberus (Nightmare)", "Fire"),
    range(117, 130): ("Magic Waste Site: Deepest Part", "Scrader (Ultimate)", "Dark"),
    range(130, 140): ("Spring of Rebirth: Top", "Cerberus (Ultimate)", "Fire"),
    range(140, 148): ("Dark Castle: Area 2", "Memecoleous (Ultimate)", "Dark"),
    range(148, 153): ("Plastida: Deepest Part", "Imitator (Ultimate)", "Water"),
    range(154, 158): ("Small Demi Machina Factory Core", "Tyrant Machina (Ultimate)", "Neutral"),
    range(158, 164): ("Large Demi Machina Factory: Deepest Part", "Mozto Machina (Ultimate)", "Neutral"),
    range(164, 175): ("Ultimea Palace: Throne", "Venena Coenubia (Nightmare)", "Dark"),
    range(176, 184): ("Droma Square", "Ultimate Machina (Ultimate)", "Neutral"),
    range(184, 198): ("Ultimea Palace: Throne", "Venena Coenubia (Ultimate)", "Dark"),
    range(198, 208): ("Dark Dragon Shrine: Near the Top", "Finstern the Dark Dragon (Ultimate)", "Dark"),
    range(208, 220): ("Labilans Sector: Square", "Kuzto (Ultimate)", "Dark"),
    range(220, 230): ("Recetacula Sector: Depot Rooftop", "Gravicep (Ultimate)", "Dark"),
    range(230, 245): ("Arche Valley: Depths", "Arachnidemon (Ultimate)", "Dark"),
    range(245, 260): ("Operation Zone: Cockpit Area", "Trickster Dragon Mimyugon (Nightmare)", "Dark"),
    range(260, 285): ("No info", "Do main quest", "N/A"),
    range(285, 295): ("Boss colon", "Boss colon", "N/A"),
    range(295, 300): ("Boss colon", "Boss colon", "N/A"),
}

# Helper function to get leveling information
def get_leveling_info(level):
    for level_range, info in leveling_info.items():
        if level in level_range:
            return info
    return ("Level out of range", "Please provide a valid level", "N/A")

# Define the bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='grind')
async def grind(ctx):
    await ctx.send("Please provide your current level:")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit()

    try:
        msg = await bot.wait_for('message', check=check, timeout=10)
        level = int(msg.content)
        place, monster, element = get_leveling_info(level)
        
        # Create a thread for the response
        thread = await ctx.message.create_thread(name=f"Grinding Info for Level {level}")
        
        embed = discord.Embed(title=f"Grinding Info for Level {level}", color=discord.Color.blue())
        embed.add_field(name="Level", value=f"{level}", inline=True)
        embed.add_field(name="Place", value=f"{place}", inline=True)
        embed.add_field(name="Monster", value=f"{monster}", inline=True)
        embed.add_field(name="Element", value=f"{element}", inline=True)
        
        await thread.send(embed=embed)
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond! Please try again.")

bot.run(TOKEN)
