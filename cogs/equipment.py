import discord
from discord.ext import commands

class Equipment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.state == 'main_menu' and 'equipment' in message.content.lower():
            embed = discord.Embed(
                title='Equipment',
                description='Here are some topics I can help you with:',
                color=discord.Color.blue()
            )
            embed.add_field(name='1) Weapons', value='Different types of weapons.')
            embed.add_field(name='2) Armor', value='Various types of armor.')
            embed.add_field(name='3) Accessories', value='Additional items for stats.')
            await message.channel.send(embed=embed)
            self.bot.state = 'equipment'

        elif self.bot.state == 'equipment':
            if 'weapons' in message.content.lower():
                embed = discord.Embed(
                    title='Weapons',
                    description='Here is some information on different types of weapons:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Swords', value='Different types of swords and their uses.')
                embed.add_field(name='2) Bows', value='Different types of bows and their uses.')
                embed.add_field(name='3) Staffs', value='Different types of staffs and their uses.')
                await message.channel.send(embed=embed)
                self.bot.state = 'equipment_weapons'

            elif 'armor' in message.content.lower():
                embed = discord.Embed(
                    title='Armor',
                    description='Here is some information on different types of armor:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Light Armor', value='Benefits of light armor.')
                embed.add_field(name='2) Heavy Armor', value='Benefits of heavy armor.')
                await message.channel.send(embed=embed)
                self.bot.state = 'equipment_armor'

            elif 'additionals' in message.content.lower():
                embed = discord.Embed(
                    title='Accessories',
                    description='Here is some information on accessories:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Rings', value='Different types of rings and their effects.')
                embed.add_field(name='2) Amulets', value='Different types of amulets and their effects.')
                await message.channel.send(embed=embed)
                self.bot.state = 'equipment_accessories'

async def setup(bot):
    await bot.add_cog(Equipment(bot))
