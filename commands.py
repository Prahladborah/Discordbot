import discord
from helpers import get_leveling_info

async def grind(ctx, level: int = None):
    if level is None:
        await ctx.send("Usage: /grind [level]")
    else:
        try:
            info = get_leveling_info(level)
            await ctx.send(info)
        except ValueError:
            await ctx.send("Please provide a valid level number.")
