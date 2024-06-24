import discord
from helpers import level_info  # Assuming get_leveling_info is defined in helpers.py

async def grind(ctx, level: int = None):
    if level is None:
        await ctx.send("Usage: /grind [level]")
    else:
        try:
            info = get_leveling_info(level)
            await ctx.send(info)
        except ValueError:
            await ctx.send("Please provide a valid level number.")
