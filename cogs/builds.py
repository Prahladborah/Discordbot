import discord
from discord.ext import commands

class Builds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.build_options = {
            '0hs': ['https://youtu.be/qE52_rriFBc?si=aOj5kKvi1km1O816', 'https://youtu.be/3-sSrIHGySk?si=p8HH1-x5_bERqt9i', 'https://youtu.be/M03qVi9_vdI?si=qMjCBBBdv2FPE0Gs', 'https://youtu.be/7UvKkEddqk8?si=8Dup1KIP3mw_vJcJ'],
            '2hs': ['https://youtu.be/AAk9a15bFOo?si=NHRe2j0Sx4eUa87b', 'https://youtu.be/p4VovPuXzc8?si=41dabqNw26BIuMyZ', 'https://youtu.be/sryP00c5ynY?si=wnDEHdJVyJbrsRTK'],
            'archer': ['https://youtu.be/aVQRczWLieE?si=AUxCgQVLvUXsQbc7', 'https://youtu.be/tWMCDuVekSA?si=AYdxmcQqueRSlIjB', 'https://youtu.be/79LWLNfubVc?si=s6La3fb0_bygwMy2'],
            'bow gun': ['https://youtu.be/-Tua7wRqNnY?si=4J99TEatTeuu0_-s', 'https://youtu.be/zZx415EGib4?si=iGqUPeyDWIPxm-aQ'],
            'mage': ['https://youtu.be/Ie4PvtBcL_Q?si=za2_Mihzc2zGr1LI', 'https://youtu.be/xpOtObKL_wc?si=YxmwUfyVX5f_tXW0', 'https://youtu.be/mIamA3JQsiM?si=ov5BCGdGf3eJcD95'],
            'halberd': ['https://youtu.be/OANNpTI_w3w?si=uAvPYUibqqfBeK06', 'https://youtu.be/BGcUxg9c4ls?si=ay1h27LzepiJJUYq', 'https://youtu.be/6_Pr9x63ebA?si=x1Hyri0wmeVSoFpU'],
            'katana': ['https://youtu.be/GkKh8mr5Jz4?si=ihxbrq3AkJuHR-m6', 'https://youtu.be/9kDYZ4Oo8z0?si=3f9H-K0uvFNgE4G5'],
            'dual sword': ['https://youtu.be/xmx_C5p2q3k?si=FOzfgfMEG_OSFLrB', 'https://youtu.be/g_SVXeg0dqI?si=VNlmhribceSzYwzl', 'https://youtu.be/x4WpUzTPaLc?si=YTCGRJjkq3SGo-hI'],
            'hybrid': ['https://youtu.be/2IBUC4y-JZs?si=_lhsCEDOFpsKuTAj', 'https://youtu.be/9jPpPz_V_SI?si=PWYB7Vv6aXvd2Fx_']
        }
        self.current_link_index = {key: 0 for key in self.build_options}  # Initialize the index tracker for each build

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.state == 'main_menu' and 'builds' in message.content.lower():
            embed = discord.Embed(
                title='Builds',
                description='Here are some build options:',
                color=discord.Color.blue()
            )
            embed.add_field(name='1) 0HS Build', value='Type "0hs" for the next video link.')
            embed.add_field(name='2) 2HS Build', value='Type "2hs" for the next video link.')
            embed.add_field(name='3) Archer Build', value='Type "archer" for the next video link.')
            embed.add_field(name='4) Bow Gun Build', value='Type "bow gun" for the next video link.')
            embed.add_field(name='5) Mage Build', value='Type "mage" for the next video link.')
            embed.add_field(name='6) Halberd Build', value='Type "halberd" for the next video link.')
            embed.add_field(name='7) Katana Build', value='Type "katana" for the next video link.')
            embed.add_field(name='8) Dual Sword Build', value='Type "dual sword" for the next video link.')
            embed.add_field(name='9) Hybrid Build', value='Type "hybrid" for the next video link.')
            await message.channel.send(embed=embed)
            self.bot.state = 'builds'

        elif self.bot.state == 'builds':
            for build, links in self.build_options.items():
                if build in message.content.lower():
                    current_index = self.current_link_index[build]
                    await message.channel.send(f"{build.capitalize()} Build: {links[current_index]}")
                    self.current_link_index[build] = (current_index + 1) % len(links)
                    self.bot.state = 'main_menu'
                    break

async def setup(bot):
    await bot.add_cog(Builds(bot))
