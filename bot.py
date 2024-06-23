import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import random

# Load environment variables from .env file (useful for local development)
load_dotenv()

# Get the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Debugging statement
print(f"Token: {TOKEN[:5]}...")  # Ensure this prints the actual token (or part of it for security reasons)

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

# Additional help functionality
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    # Greeting responses
    greetings = ['hello everyone', 'hi everyone', 'hello', 'hi']
    responses = [
        'Hello! Welcome back!',
        'Greetings!',
        'Welcome back, master!',
        'Hi there! How can I assist you today?',
        'Hello! How are you doing?',
        'Hey! Nice to see you!'
    ]

    # Humorous responses for "potato guide"
    potato_responses = [
        "Don't call me potato, you potato baka!",
        "Who are you calling a potato? Take that back, potato-head!",
        "Potato guide? I'm not a potato, I'm a fully grown spud, thank you very much!",
        "Excuse me? I'm not a potato, I'm a bot with a superior intellect, thank you.",
        "Did you just call me a potato? That's a low blow, my friend!"
    ]

    if any(greeting in content for greeting in greetings):
        response = random.choice(responses)
        await message.channel.send(response)

    elif 'potato guide' in content:
        response = random.choice(potato_responses)
        await message.channel.send(response)

    # Initial trigger for help
    elif any(x in content for x in ['is anyone here who can help me', 'i need help', 'someone help me']):
        embed = discord.Embed(
            title=f'How can I help you, {message.author.name}?',
            description='I can give you information regarding:',
            color=discord.Color.blue()
        )
        embed.add_field(name='1. Builds', value='Learn about different builds.')
        embed.add_field(name='2. Blacksmithing', value='Information on weapon forging, armor crafting, etc.')
        embed.add_field(name='3. Synthesis', value='Material and attribute synthesis, enchantments.')
        embed.add_field(name='4. Equipment', value='Information on various types of equipment.')
        await message.channel.send(embed=embed)

        # State variable to track user's current state
        global state
        state = 'main_menu'

    else:
        # Handle responses based on the current state
        if state == 'main_menu':
            if 'builds' in content:
                embed = discord.Embed(
                    title='Builds',
                    description='Choose one build from my database:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) 0HS Build', value='1-handed sword and sub weapons.')
                embed.add_field(name='2) 2HS Build', value='2-handed sword builds.')
                embed.add_field(name='3) Archer Build', value='Bow builds.')
                embed.add_field(name='4) Bow Gun Build', value='Bow gun builds.')
                embed.add_field(name='5) Mage Build', value='Staff builds.')
                embed.add_field(name='6) Halberd Build', value='Halberd builds.')
                embed.add_field(name='7) Katana Build', value='Katana builds.')
                embed.add_field(name='8) Dual Sword Build', value='Dual sword builds.')
                embed.add_field(name='9) Hybrid Build', value='Combination of different weapons and skills.')
                await message.channel.send(embed=embed)
                state = 'builds'

            elif 'blacksmithing' in content:
                embed = discord.Embed(
                    title='Blacksmithing',
                    description='Here are some topics I can help you with:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Forging', value='Craft weapons and armor.')
                embed.add_field(name='2) Materials', value='Find materials for crafting.')
                await message.channel.send(embed=embed)
                state = 'blacksmithing'

            elif 'synthesis' in content:
                embed = discord.Embed(
                    title='Synthesis',
                    description='Here are some topics I can help you with:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Material Synthesis', value='Combine materials.')
                embed.add_field(name='2) Attribute Synthesis', value='Transfer attributes.')
                embed.add_field(name='3) Enchantments', value='Add magical properties to items.')
                await message.channel.send(embed=embed)
                state = 'synthesis'

            elif 'equipment' in content:
                embed = discord.Embed(
                    title='Equipment',
                    description='Here are some topics I can help you with:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Weapons', value='Different types of weapons.')
                embed.add_field(name='2) Armor', value='Various types of armor.')
                embed.add_field(name='3) Accessories', value='Additional items for stats.')
                await message.channel.send(embed=embed)
                state = 'equipment'

        elif state == 'builds':
            build_options = {
                '0hs': '0HS Build: 1-handed sword and sub weapons.',
                '2hs': '2HS Build: 2-handed sword builds.',
                'archer': 'Archer Build: Bow builds.',
                'bow gun': 'Bow Gun Build: Bow gun builds.',
                'mage': 'Mage Build: Staff builds.',
                'halberd': 'Halberd Build: Halberd builds.',
                'katana': 'Katana Build: Katana builds.',
                'dual sword': 'Dual Sword Build: Dual sword builds.',
                'hybrid': 'Hybrid Build: Combination of different weapons and skills.'
            }
            for build, description in build_options.items():
                if build in content:
                    await message.channel.send(description)
                    state = 'main_menu'
                    break

        elif state == 'blacksmithing':
            # Handle blacksmithing topics
            pass
        elif state == 'synthesis':
            # Handle synthesis topics
            pass
        elif state == 'equipment':
            # Handle equipment topics
            pass

# Run the bot
bot.run(TOKEN)
