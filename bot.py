import discord
from discord.ext import commands

token = ""
bot = commands.Bot(command_prefix='*')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def register(ctx, *person):
    await ctx.send("Registered: " + str(list(person)))

bot.run(token)
