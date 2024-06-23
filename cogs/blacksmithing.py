import discord
from discord.ext import commands

class Blacksmithing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.state == 'main_menu' and 'blacksmithing' in message.content.lower():
            embed = discord.Embed(
                title='Blacksmithing',
                description='Here are some topics I can help you with:',
                color=discord.Color.blue()
            )
            embed.add_field(name='1) Forging', value='Craft weapons and armor.')
            embed.add_field(name='2) Materials', value='Find materials for crafting.')
            await message.channel.send(embed=embed)
            self.bot.state = 'blacksmithing'

        elif self.bot.state == 'blacksmithing':
            # Handle blacksmithing topics
            pass

async def setup(bot):
    await bot.add_cog(Blacksmithing(bot))
