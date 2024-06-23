import discord

async def send_help_trigger(message):
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
    return 'main_menu'
