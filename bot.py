import discord
from discord.ext import commands
import yaml
from level_info import get_leveling_info
from help_triggers import send_help_trigger
from responses import send_potato_response, send_baka_response

with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

TOKEN = config['discord']['TOKEN']
PREFIX = config['bot']['prefix']

intents = discord.Intents.default()
intents.messages = config['intents']['messages']
intents.message_content = config['intents']['message_content']

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if 'where should i level' in content or 'leveling info' in content or 'where i level' in content or 'where to level' in content:
        await grind(message)
        return

    if any(trigger in content for trigger in ['i need help', 'hey elite', 'hey guide', 'hey elite guide', 'someone help me']):
        await send_help_trigger(message)
        return

    await send_potato_response(message, content)
    await send_baka_response(message, content)

    await bot.process_commands(message)

async def grind(message):
    words = message.content.split()
    level = next((int(word) for word in words if word.isdigit()), None)

    if level is None:
        await message.channel.send("Please provide a level number. Example: 'Where should I level at (provide your level)'")
    else:
        try:
            info = get_leveling_info(level)
            await send_level_info_embed(message, info)
        except ValueError:
            await message.channel.send("Please provide a valid level number.")

async def send_level_info_embed(message, info):
    level_range, location, enemy, notes = info

    embed = discord.Embed(title=f'Leveling Info for Level {level_range}', color=discord.Color.blue())
    embed.add_field(name='Location', value=location, inline=True)
    embed.add_field(name='Enemy', value=enemy, inline=True)
    embed.add_field(name='Notes', value=notes if notes else 'No additional notes', inline=False)

    await message.channel.send(embed=embed)

if __name__ == '__main__':
    bot.run(TOKEN)
