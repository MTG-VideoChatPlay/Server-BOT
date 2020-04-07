import discord
from discord.ext import commands
import random
import math
import operator

token = "Njk2NTUyMDE1MjU3NjY1NTQ3.XoxRWQ.Wa3XrgecusPqWQ7jlMhcdXi0WtU"
bot = commands.Bot(command_prefix='*',activity=discord.Game(name="Prefix is *"))

bot.player = []
bot.players_pod1 = []
bot.players_pod1_score = [0, 0, 0, 0, 0, 0, 0, 0]
bot.players_pod2 = []
bot.players_pod2_score = [0, 0, 0, 0, 0, 0, 0, 0]
bot.players_pod3 = []
bot.players_pod3_score = [0, 0, 0, 0, 0, 0, 0, 0]
bot.playersdict = {}

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def register(ctx, *person):
    bot.player = list(person)


@bot.command()
async def generatepods(ctx, numberofpods):
    random.shuffle(bot.player)
    x = math.ceil(len(bot.player)/int(numberofpods))
    a = 0
    for i in bot.player:
        if a < x:
            bot.players_pod1.append(bot.player[a])
        if x <= a < (2*x):
            bot.players_pod2.append(bot.player[a])
        if (2*x) <= a < (3*x):
            bot.players_pod3.append(bot.player[a])
        a += 1
    await ctx.send("Registered: \nPod 1: " + str(bot.players_pod1) + "\nPod 2: " + str(bot.players_pod2) + "\nPod 3: " + str(bot.players_pod3))


@bot.command()
async def generatetables(ctx, pod):
    if int(pod) == 1:
        random.shuffle(bot.players_pod1)
        table1 = bot.players_pod1[0] + " " + bot.players_pod1[1]
        table2 = bot.players_pod1[2] + " " + bot.players_pod1[3]
        table3 = bot.players_pod1[4] + " " + bot.players_pod1[5]
        table4 = bot.players_pod1[6] + " " + bot.players_pod1[7]
        await ctx.send("Your tables for pod 1 are:\n" + table1 + "\n" + table2 + "\n" + table3 + "\n" + table4 + "\n")
    if int(pod) == 2:
        random.shuffle(bot.players_pod2)
        table5 = bot.players_pod1[0] + " " + bot.players_pod1[1]
        table6 = bot.players_pod1[2] + " " + bot.players_pod1[3]
        table7 = bot.players_pod1[4] + " " + bot.players_pod1[5]
        table8 = bot.players_pod1[6] + " " + bot.players_pod1[7]
        await ctx.send("Your tables for pod 2 are:\n " + table5 + "\n" + table6 + "\n" + table7 + "\n" + table8 + "\n")
    if int(pod) == 3:
        random.shuffle(bot.players_pod3)
        table9 = bot.players_pod1[0] + " " + bot.players_pod1[1]
        table10 = bot.players_pod1[2] + " " + bot.players_pod1[3]
        table11 = bot.players_pod1[4] + " " + bot.players_pod1[5]
        table12 = bot.players_pod1[6] + " " + bot.players_pod1[7]
        await ctx.send("Your tables for pod 3 are:\n" + table9 + "\n" + table10 + "\n" + table11 + "\n" + table12 + "\n")


@bot.command()
async def gameover(ctx, pod, table, score):
    if int(pod) == 1:
        score.split("-")
        bot.players_pod1_score[(int(table)*2)-2] = int(bot.players_pod1_score[(int(table)*2)-2]) + int(score[0])
        bot.players_pod1_score[(int(table)*2)-1] = int(bot.players_pod1_score[(int(table)*2)-1]) + int(score[2])
    if int(pod) == 2:
        score.split("-")
        bot.players_pod2_score[(int(table)*2)-2] = int(bot.players_pod2_score[(int(table)*2)-2]) + int(score[0])
        bot.players_pod2_score[(int(table)*2)-1] = int(bot.players_pod2_score[(int(table)*2)-1]) + int(score[2])
    if int(pod) == 3:
        score.split("-")
        bot.players_pod3_score[(int(table)*2)-2] = int(bot.players_pod3_score[(int(table)*2)-2]) + int(score[0])
        bot.players_pod3_score[(int(table)*2)-1] = int(bot.players_pod3_score[(int(table)*2)-1]) + int(score[2])


@bot.command()
async def results(ctx, pod):
    a = 0
    for player in bot.players_pod1:
        bot.playersdict[player] = bot.players_pod1_score[a]
        a += 1
    sorted_playerdict = dict(sorted(bot.playersdict.items(), key=operator.itemgetter(1), reverse=True))
    await ctx.send(sorted_playerdict)

@bot.command()
async def endtourney(ctx):
    bot.player = []
    bot.players_pod1 = []
    bot.players_pod2 = []
    bot.players_pod3 = []
    await ctx.send("Success!")


bot.run(token)

