import discord
from discord.ext import commands
from level_info import get_leveling_info
from help_triggers import send_help_trigger
from responses import send_potato_response, send_baka_response

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        content = message.content.lower()

        # Add the trigger for the grind function
        if 'where should i level' in content or 'leveling info' in content or 'where i level' in content or 'where to level' in content:
            await self.grind(message)
            return

        # Add help trigger
        if any(trigger in content for trigger in ['i need help', 'hey elite', 'hey guide', 'hey elite guide', 'someone help me']):
            await send_help_trigger(message)
            return

        # Add potato response
        await send_potato_response(message, content)

        # Add baka response
        await send_baka_response(message, content)

        # Process other messages
        await self.bot.process_commands(message)

    async def grind(self, message):
        # Extract the level from the message
        words = message.content.split()
        level = next((int(word) for word in words if word.isdigit()), None)

        if level is None:
            await message.channel.send("Please provide a level number. Example: 'Where should I level at (provide your level)'")
        else:
            try:
                info = get_leveling_info(level)
                await self.send_level_info_embed(message, info)
            except ValueError:
                await message.channel.send("Please provide a valid level number.")

    async def send_level_info_embed(self, message, info):
        # Extract information for embedding
        level_range, location, enemy, notes = info

        embed = discord.Embed(title=f'Leveling Info for Level {level_range}', color=discord.Color.blue())
        embed.add_field(name='Location', value=location, inline=True)
        embed.add_field(name='Enemy', value=enemy, inline=True)
        embed.add_field(name='Notes', value=notes if notes else 'No additional notes', inline=False)

        await message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Events(bot))
