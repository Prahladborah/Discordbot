import discord
from discord.ext import commands

class Builds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.state == 'main_menu' and 'builds' in message.content.lower():
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
            self.bot.state = 'builds'

        elif self.bot.state == 'builds':
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
                if build in message.content.lower():
                    await message.channel.send(description)
                    self.bot.state = 'main_menu'
                    break

async def setup(bot):
    await bot.add_cog(Builds(bot))
