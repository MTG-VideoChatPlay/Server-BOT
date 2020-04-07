from discord.ext import commands

bot = commands.Bot(command_prefix='*')


@bot.command()
async def add(ctx, num1, num2):
    await ctx.send(num1 + num2)
