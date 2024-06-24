import discord
from discord.ext import commands
from responses import send_greeting_response, send_potato_response, send_baka_response
from help_triggers import send_help_trigger

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
        else:
            await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(Events(bot))
