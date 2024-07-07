import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Replace this with your Discord user ID and the ID of the channel where you want the bot to post the embeds
YOUR_USER_ID = prahlad9741
TARGET_CHANNEL_ID = 1253610711490498623

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def embed(ctx, title: str, *, content: str):
    if ctx.author.id != YOUR_USER_ID:
        await ctx.send("You are not authorized to use this command.")
        return

    if isinstance(ctx.channel, discord.DMChannel):
        lines = content.split('\n')
        description = '\n'.join(lines[:-1])
        image_url = lines[-1] if lines[-1].startswith('http') else None

        embed = discord.Embed(
            title=title,
            description=description,
            color=0x3498db
        )
        embed.set_author(name="Guild Master", icon_url="https://example.com/icon.png")
        embed.set_footer(text="Footer text here.")
        
        if image_url:
            embed.set_image(url=image_url)

        channel = bot.get_channel(TARGET_CHANNEL_ID)
        if channel:
            await channel.send(embed=embed)
            await ctx.send("Your message has been sent to the specified channel.")
        else:
            await ctx.send("I couldn't find the specified channel.")
    else:
        await ctx.send("Please use this command in a direct message.")

# Accessing Discord token from environment variable
discord_token = os.getenv('DISCORD_TOKEN')
if discord_token is None:
    print("DISCORD_TOKEN environment variable not found.")
else:
    # Replace 'YOUR_TOKEN_HERE' with your bot's token
    bot.run(discord_token)
