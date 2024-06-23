import discord
import random
from helpers import get_leveling_info

greetings = ['hello everyone', 'hi everyone', 'hello', 'hi']
responses = [
    'Hello! Welcome back!',
    'Greetings!',
    'Welcome back, master!',
    'Hi there! How can I assist you today?',
    'Hello! How are you doing?',
    'Hey! Nice to see you!',
]

potato_responses = [
    "Don't call me potato, you potato baka!",
    "Who are you calling a potato? Take that back, potato-head!",
    "Potato guide? I'm not a potato, I'm a fully grown spud, thank you very much!",
    "Excuse me? I'm not a potato, I'm a bot with a superior intellect, thank you.",
    "Did you just call me a potato? That's a low blow, my friend!",
    "You're the real spud here!",
    "Potato? I'm a technologically advanced tuber!",
    "Do I look like I belong in a stew?",
    "Hey, no need to hashbrown me!",
    "Who you calling potato, tater tot?",
    "Don't be a small fry",
    "That's Mr. Potato Head to you!",
]

state = 'main_menu'

async def on_ready():
    print(f'Logged in as {bot.user}')

async def on_message(message):
    global state
    if message.author.bot:
        return

    content = message.content.lower()

    if any(greeting in content for greeting in greetings):
        response = random.choice(responses)
        await message.channel.send(response)

    elif 'potato guide' in content:
        response = random.choice(potato_responses)
        await message.channel.send(response)

    elif any(x in content for x in ['is anyone here who can help me', 'i need help', 'someone help me', 'hey guide', 'elite guide', 'hey elite']):
        embed = discord.Embed(
            title=f'How can I help you, {message.author.name}?',
            description='I can give you information regarding:',
            color=discord.Color.blue()
        )
        embed.add_field(name='1. Builds', value='Learn about different builds.')
        embed.add_field(name='2. Blacksmithing', value='Information on weapon forging, armor crafting, etc.')
        embed.add_field(name='3. Synthesis', value='Material and synthesis, enchantments.')
        embed.add_field(name='4. Equipment', value='Information on various types of equipment.')
        await message.channel.send(embed=embed)
        state = 'main_menu'

    else:
        if state == 'main_menu':
            if 'builds' in content:
                embed = discord.Embed(
                    title='Builds',
                    description='Here are some build options:',
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
            if 'forging' in content:
                embed = discord.Embed(
                    title='Forging',
                    description='Here is some information on forging:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Weapons', value='How to forge weapons.')
                embed.add_field(name='2) Armor', value='How to forge armor.')
                await message.channel.send(embed=embed)
                state = 'blacksmithing_forging'
            
            elif 'materials' in content:
                embed = discord.Embed(
                    title='Materials',
                    description='Here is some information on materials:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Common Materials', value='Materials commonly used in crafting.')
                embed.add_field(name='2) Rare Materials', value='Materials that are harder to find.')
                await message.channel.send(embed=embed)
                state = 'blacksmithing_materials'
        
        elif state == 'synthesis':
            if 'material synthesis' in content:
                embed = discord.Embed(
                    title='Material Synthesis',
                    description='Here is some information on material synthesis:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Combining Materials', value='How to combine materials for better results.')
                embed.add_field(name='2) Material Properties', value='Understanding the properties of materials.')
                await message.channel.send(embed=embed)
                state = 'synthesis_material_synthesis'
            
            elif 'attribute synthesis' in content:
                embed = discord.Embed(
                    title='Attribute Synthesis',
                    description='Here is some information on attribute synthesis:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Transferring Attributes', value='How to transfer attributes between items.')
                embed.add_field(name='2) Attribute Effects', value='Understanding the effects of different attributes.')
                await message.channel.send(embed=embed)
                state = 'synthesis_attribute_synthesis'
            
            elif 'enchantments' in content:
                embed = discord.Embed(
                    title='Enchantments',
                    description='Here is some information on enchantments:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Adding Enchantments', value='How to add enchantments to items.')
                embed.add_field(name='2) Enchantment Effects', value='Understanding the effects of enchantments.')
                await message.channel.send(embed=embed)
                state = 'synthesis_enchantments'

        elif state == 'equipment':
            if 'weapons' in content:
                embed = discord.Embed(
                    title='Weapons',
                    description='Here is some information on different types of weapons:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Swords', value='Different types of swords and their uses.')
                embed.add_field(name='2) Bows', value='Different types of bows and their uses.')
                embed.add_field(name='3) Staffs', value='Different types of staffs and their uses.')
                await message.channel.send(embed=embed)
                state = 'equipment_weapons'
            
            elif 'armor' in content:
                embed = discord.Embed(
                    title='Armor',
                    description='Here is some information on different types of armor:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Light Armor', value='Benefits of light armor.')
                embed.add_field(name='2) Heavy Armor', value='Benefits of heavy armor.')
                await message.channel.send(embed=embed)
                state = 'equipment_armor'
            
            elif 'accessories' in content:
                embed = discord.Embed(
                    title='Accessories',
                    description='Here is some information on accessories:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Rings', value='Different types of rings and their effects.')
                embed.add_field(name='2) Amulets', value='Different types of amulets and their effects.')
                await message.channel.send(embed=embed)
                state = 'equipment_accessories'
