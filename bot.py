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
print(f"Token: DISCORD_TOKEN")  # Ensure this prints the actual token (or part of it for security reasons)

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

    await bot.process_commands(message)  # Ensure commands are still processed

    content = message.content.lower()

     # Greeting responses
    if 'good morning' in content:
        await message.channel.send(f"Good morning, {message.author.name}!")
    elif 'good afternoon' in content:
        await message.channel.send(f"Good afternoon, {message.author.name}!")
    elif 'good evening' in content:
        await message.channel.send(f"Good evening, {message.author.name}!")
    elif 'good night' in content:
        await message.channel.send(f"Good night, {message.author.name}!")

    # Initial trigger for help
    if any(x in content for x in ['is anyone here who can help me', 'i need help', 'someone help me',]):
        embed = discord.Embed(
            title=f'How can I help you, {message.author.name}?',
            description='I can give you information regarding:',
            color=discord.Color.blue()
        )
        embed.add_field(name='1. Builds', value='Learn about different builds.')
        embed.add_field(name='2. Blacksmithing', value='Information on weapon forging, armor crafting, etc.')
        embed.add_field(name='3. Synthesis', value='Material and attribute synthesis, enchantments.')
        embed.add_field(name='4. Equipment', value='Information on various types of equipment.')
        await message.reply(embed=embed)

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
                await message.reply(embed=embed)
                state = 'builds'

            elif 'blacksmithing' in content:
                embed = discord.Embed(
                    title='Blacksmithing',
                    description='Here are some topics I can help you with:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1. Weapon Forging', value='Create powerful weapons.')
                embed.add_field(name='2. Armor Crafting', value='Improve your defenses.')
                embed.add_field(name='3. Material Gathering', value='Tips for gathering materials.')
                embed.add_field(name='4. Enhancements', value='Improve your equipment.')
                await message.reply(embed=embed)
                state = 'blacksmithing'

            elif 'synthesis' in content:
                embed = discord.Embed(
                    title='Synthesis',
                    description='Here are some topics I can help you with:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1. Material Synthesis', value='Create materials for crafting.')
                embed.add_field(name='2. Attribute Synthesis', value='Enhance your equipment attributes.')
                embed.add_field(name='3. Crafting Accessories', value='Craft accessories with various bonuses.')
                embed.add_field(name='4. Enchantments', value='Add special effects to your equipment.')
                await message.reply(embed=embed)
                state = 'synthesis'

            # Add handling for other options here (e.g., 'equipment')

        elif state == 'builds':
            # Handle builds submenu
            if '1' in content or '0hs build' in content:
                embed = discord.Embed(
                    title='0HS Build',
                    description='This is a type of build where the primary weapon is a 1-handed sword followed by sub weapons.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Popular 1-handed sword builds', value='[Link to video]')
                await message.reply(embed=embed)

            elif '2' in content or '2hs build' in content:
                embed = discord.Embed(
                    title='2HS Build',
                    description='This is a type of build where the primary weapon is a 2-handed sword.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Popular 2-handed sword builds', value='[Link to video]')
                await message.reply(embed=embed)

            elif '3' in content or 'archer build' in content:
                embed = discord.Embed(
                    title='Archer Build',
                    description='This is a type of build where the primary weapon is a bow.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Popular archer builds', value='[Link to video]')
                await message.reply(embed=embed)

            elif '4' in content or 'bow gun build' in content:
                embed = discord.Embed(
                    title='Bow Gun Build',
                    description='This is a type of build where the primary weapon is a bow gun.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Popular bow gun builds', value='[Link to video]')
                await message.reply(embed=embed)

            elif '5' in content or 'mage build' in content:
                embed = discord.Embed(
                    title='Mage Build',
                    description='This is a type of build where the primary weapon is a staff.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Popular mage builds', value='[Link to video]')
                await message.reply(embed=embed)

            elif '6' in content or 'halberd build' in content:
                embed = discord.Embed(
                    title='Halberd Build',
                    description='This is a type of build where the primary weapon is a halberd.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Popular halberd builds', value='[Link to video]')
                await message.reply(embed=embed)

            elif '7' in content or 'katana build' in content:
                embed = discord.Embed(
                    title='Katana Build',
                    description='This is a type of build where the primary weapon is a katana.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Popular katana builds', value='[Link to video]')
                await message.reply(embed=embed)

            elif '8' in content or 'dual sword build' in content:
                embed = discord.Embed(
                    title='Dual Sword Build',
                    description='This is a type of build where the primary weapons are dual swords.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Popular dual sword builds', value='[Link to video]')
                await message.reply(embed=embed)

            elif '9' in content or 'hybrid build' in content:
                embed = discord.Embed(
                    title='Hybrid Build',
                    description='This is a hybrid build where you combine different weapons and skills.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Popular hybrid builds', value='[Link to video]')
                await message.reply(embed=embed)

            # After handling, reset state to main_menu
            state = 'main_menu'

        elif state == 'blacksmithing':
            # Handle blacksmithing submenu
            if 'weapon forging' in content or '1' in content:
                embed = discord.Embed(
                    title='Weapon Forging',
                    description='Weapon forging allows you to create powerful weapons.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Tips for weapon forging', value='[Link to guide]')
                await message.reply(embed=embed)

            elif 'armor crafting' in content or '2' in content:
                embed = discord.Embed(
                    title='Armor Crafting',
                    description='Armor crafting is essential for improving your defenses.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Tips for armor crafting', value='[Link to guide]')
                await message.reply(embed=embed)

            elif 'material gathering' in content or '3' in content:
                embed = discord.Embed(
                    title='Material Gathering',
                    description='Gathering materials is crucial for blacksmithing.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Tips for material gathering', value='[Link to guide]')
                await message.reply(embed=embed)

            elif 'enhancements' in content or '4' in content:
                embed = discord.Embed(
                    title='Enhancements',
                    description='Enhancements can greatly improve your equipment.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Tips for enhancements', value='[Link to guide]')
                await message.reply(embed=embed)

            # After handling, reset state to main_menu
            state = 'main_menu'

        elif state == 'synthesis':
            # Handle synthesis submenu
            if 'material synthesis' in content or '1' in content:
                embed = discord.Embed(
                    title='Material Synthesis',
                    description='Material synthesis allows you to create materials for crafting.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Tips for material synthesis', value='[Link to guide]')
                await message.reply(embed=embed)

            elif 'attribute synthesis' in content or '2' in content:
                embed = discord.Embed(
                    title='Attribute Synthesis',
                    description='Attribute synthesis allows you to enhance your equipment attributes.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Tips for attribute synthesis', value='[Link to guide]')
                await message.reply(embed=embed)

            elif 'crafting accessories' in content or '3' in content:
                embed = discord.Embed(
                    title='Crafting Accessories',
                    description='Craft accessories with various bonuses.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Tips for crafting accessories', value='[Link to guide]')
                await message.reply(embed=embed)

            elif 'enchantments' in content or '4' in content:
                embed = discord.Embed(
                    title='Enchantments',
                    description='Add special effects to your equipment.',
                    color=discord.Color.blue()
                )
                embed.add_field(name='Tips for enchantments', value='[Link to guide]')
                await message.reply(embed=embed)

            # After handling, reset state to main_menu
            state = 'main_menu'
    

bot.run(TOKEN)
