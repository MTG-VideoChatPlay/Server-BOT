import discord
from discord.ext import commands
import random
import math

token = "Njk2NTUyMDE1MjU3NjY1NTQ3.Xov-MA.7U-mVcnCwXcFLrR8MWPWLDHBQ20"
bot = commands.Bot(command_prefix='*')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def register(ctx, *person):
    bot.player = list(person)


@bot.command()
async def generatepods(ctx, numberofpods):
    bot.players_pod1 = []
    bot.players_pod2 = []
    bot.players_pod3 = []
    random.shuffle(bot.player)
    x = math.ceil(len(bot.player)/int(numberofpods))
    a = 0
    for i in bot.player:
        if a < x:
            bot.players_pod1.append(bot.player[a])
        if (x) <= a < (2*x):
            bot.players_pod2.append(bot.player[a])
        if (2*x) <= a < (3*x):
            bot.players_pod3.append(bot.player[a])
        a += 1

    await ctx.send("Registered: \nPod 1: " + str(bot.players_pod1) + "\nPod 2: " + str(bot.players_pod2) + "\nPod 3: " + str(bot.players_pod3))


@bot.command()
async def endtourney(ctx):
    bot.player = []
    bot.players_pod1 = []
    bot.players_pod2 = []
    bot.players_pod3 = []


bot.run(token)

