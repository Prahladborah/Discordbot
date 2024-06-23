import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from tabulate import tabulate

# Load environment variables from .env file (useful for local development)
load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Debugging statement
print(f"Token:DISCORD_TOKEN")  # Ensure this prints the actual token (or part of it for security reasons)

# Check if the token is loaded correctly
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable is not set")

# Define leveling information
leveling_info = [
    (range(1, 34), "Nisel Mountain:Mountainside", "Shell Mask", "keep grinding till you reach 34 to 36"),
    (range(34, 50), "Ancient Empress Tomb: Area 1", "Bone Dragonewt", "Level there till at least 50 or 56"),
    (range(50, 60), "Land Of Chaos", "'Hidden boss: Forestia' (normal/hard)", "Level there till 60"),
    (range(60, 69), "Land Of Chaos", "'Hidden boss: Forestia' (Nightmare)", "Level there till 69"),
    (range(70, 80), "Land Under Cultivation:Hill", "Masked Warrior (Hard)", "Level there till 74-76"),
    (range(80, 90), "Land Under Cultivation:Hill", "Masked Warrior (Nightmare)", "Level there till 90-94"),
    (range(90, 100), "Gravel Terrace:Jade Raptor (Nightmare) or Polde Ice Valley", "Don-Yeti", "Level till 100-104"),
    (range(100, 110), "Land Under Cultivation:Hill", "Masked Warrior (Ultimate)", "Level there till 110"),
    (range(110, 117), "Spring of Rebirth: Top", "Cerberus (Nightmare)", "Level there till 117"),
    (range(117, 130), "Magic Waste Site: Deepest Part", "Scrader (Ultimate)", "Level there till 130-132"),
    (range(130, 140), "Spring of Rebirth: Top", "Cerberus (Ultimate)", "Level there till 140"),
    (range(140, 148), "Dark Castle: Area 2", "Memecoleous (Ultimate)", "Level there till 148..Ask friends to help its a hellish boss if you are a rookie"),
    (range(148, 153), "Plastida: Deepest Part", "Imitator (Ultimate)", ""),
    (range(154, 158), "Small Demi Machina Factory Core", "Tyrant Machina (Ultimate)", ""),
    (range(158, 164), "Large Demi Machina Factory: Deepest Part", "Mozto Machina (Ultimate)", ""),
    (range(164, 175), "Ultimea Palace: Throne", "Venena Coenubia (Nightmare)", "Level there till 175-176"),
    (range(176, 184), "Droma Square", "Ultimate Machina (Ultimate)", "Level there till 184"),
    (range(184, 198), "Ultimea Palace: Throne", "Venena Coenubia (Ultimate)", "Level there till 194-198"),
    (range(198, 208), "Dark Dragon Shrine: Near the Top", "Finstern the Dark Dragon (Ultimate)", "Level there till 208"),
    (range(208, 220), "Labilans Sector: Square", "Kuzto (Ultimate)", "Level there till 220"),
    (range(220, 230), "Recetacula Sector: Depot Rooftop", "Gravicep (Ultimate) or better to do main quest", "Level there till 230"),
    (range(230, 245), "Arche Valley: Depths", "Arachnidemon (Ultimate)", "Better suggestion: do mq till 250"),
    (range(245, 260), "Operation Zone: Cockpit Area", "Trickster Dragon Mimyugon (Nightmare)", ""),
    (range(260, 285), "NO info", "", "DO mq till 285"),
    (range(285, 295), "Boss colon", "", ""),
    (range(295, 300), "Boss colon", "", ""),
]

# Helper function to get leveling information
def get_leveling_info(level):
    for level_range, location, monster, additional_info in leveling_info:
        if level in level_range:
            return [level, location, monster, additional_info]
    return None

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
        info = get_leveling_info(level)
        if info:
            embed = discord.Embed(title=f"Leveling Information for Level {info[0]}", color=discord.Color.green())
            embed.add_field(name="Location", value=info[1], inline=False)
            embed.add_field(name="Monster", value=info[2], inline=False)
            embed.add_field(name="Additional Info", value=info[3], inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Level out of range. Please provide a valid level.")
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond! Please try again.")

bot.run(TOKEN)
