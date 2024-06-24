import discord
from discord.ext import commands
from responses import send_greeting_response, send_potato_response, send_baka_response
from level_info import get_leveling_info

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
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
            self.bot.state = await send_help_trigger(message)
        elif 'where should i level' in content or 'leveling info' in content:
            await self.grind(message)
            return
       
        else:
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
