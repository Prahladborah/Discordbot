import discord
from helpers import get_leveling_info

async def grind(ctx, arg=None):
    if arg is None:
        await ctx.send("Usage: /grind [level]")
    else:
        try:
            level = int(arg)
            info = get_leveling_info(level)
            if info:
                await ctx.send(info)
            else:
                await ctx.send("Leveling information not found for the specified level.")
        except ValueError:
            await ctx.send("Invalid level. Please provide a valid number.")
