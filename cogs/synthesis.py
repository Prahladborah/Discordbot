import discord
from discord.ext import commands

class Synthesis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.state == 'main_menu' and 'synthesis' in message.content.lower():
            embed = discord.Embed(
                title='Synthesis',
                description='Here are some topics I can help you with:',
                color=discord.Color.blue()
            )
            embed.add_field(name='1) Material Synthesis', value='Combine materials.')
            embed.add_field(name='2) Attribute Synthesis', value='Transfer attributes.')
            embed.add_field(name='2) Enchantment Effects', value='Understanding the effects of enchantments.')
            await message.channel.send(embed=embed)
            self.bot.state = 'synthesis_enchantments'

        elif self.bot.state == 'synthesis_enchantments':
            # Handle synthesis topics
            pass

async def setup(bot):
    await bot.add_cog(Synthesis(bot))
