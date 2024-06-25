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
                embed.add_field(name='1) Swords', value='this section is under development.')
                embed.add_field(name='2) Bows', value='this section is under development.')
                embed.add_field(name='3) Staffs', value='this section is under development.')
                await message.channel.send(embed=embed)
                self.bot.state = 'equipment_weapons'

            elif 'armor' in message.content.lower():
                embed = discord.Embed(
                    title='Armor',
                    description='Here is some information on different types of armor:',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Light Armor', value="Switching to light armor not only alters your character's appearance but also enhances gameplay with evasion bonuses and increased movement speed, making it ideal for agile, DPS-focused builds using dual-wield daggers or halberds.")
                embed.add_field(name='2) Heavy Armor', value='Heavy armor significantly boosts defense and magic defense, enhances guard recharge speed, but comes with a 50% attack speed reduction and a 10% evasion penalty, impacting overall damage output and dodging capability.')
                await message.channel.send(embed=embed)
                self.bot.state = 'equipment_armor'

            elif 'additionals' in message.content.lower():
                embed = discord.Embed(
                    title='Accessories',
                    description='this section is under development',
                    color=discord.Color.blue()
                )
                embed.add_field(name='1) Rings', value='no info')
                embed.add_field(name='2) Additionals', value='no info')
                await message.channel.send(embed=embed)
                self.bot.state = 'equipment_accessories'

async def setup(bot):
    await bot.add_cog(Equipment(bot))
