import discord
from helpers import get_leveling_info

async def grind(ctx, arg=None):
    if arg is None:
        await ctx.send("Usage: /grind [level]")
    else:
        try:
            level = int(arg)
            info = get_leveling_info(level)
            await ctx.send(info)
        except ValueError:
            await ctx.send("Please provide a valid level number.")
