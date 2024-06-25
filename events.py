import discord
from discord.ext import commands
from level_info import get_leveling_info  # Make sure this import is correct

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        content = message.content.lower()

        # Add the trigger for the grind function
        if 'where should i level' in content or 'leveling info' in content:
            await self.grind(message)
            return

        # Process other messages
        await self.bot.process_commands(message)

    async def grind(self, message):
        # Extract the level from the message
        words = message.content.split()
        level = None
        for word in words:
            if word.isdigit():
                level = int(word)
                break

        if level is None:
            await message.channel.send("Please provide a level number. Example: 'Where should I level at 50?'")
        else:
            try:
                info = get_leveling_info(level)
                await message.channel.send(info)
            except ValueError:
                await message.channel.send("Please provide a valid level number.")

async def setup(bot):
    await bot.add_cog(Events(bot))
