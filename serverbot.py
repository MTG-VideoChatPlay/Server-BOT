import discord
from discord.ext import commands
import random
import math
import operator
import json
from collections import Counter
import asyncio

token = "Njk2NTUyMDE1MjU3NjY1NTQ3.Xo6WTQ.MDzN2d8fbDPvk1BMwrL4z5PvHwA"
bot = commands.Bot(command_prefix='*', activity=discord.Game(name="Prefix is *"))

bot.player = []
bot.players_pod1_score = [0, 0, 0, 0, 0, 0, 0, 0]
bot.players_pod2_score = [0, 0, 0, 0, 0, 0, 0, 0]
bot.players_pod3_score = [0, 0, 0, 0, 0, 0, 0, 0]
bot.playerspod1 = {}
bot.playerspod2 = {}
bot.playerspod3 = {}
bot.leaderboardpod1 = {}
bot.leaderboardpod2 = {}
bot.leaderboardpod3 = {}
bot.leaderboard = {}


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def register(ctx, *person):
    bot.player = list(person)
    await ctx.send("Registered " + str(len(person)) + " players!")

# WORKS PERFECTLY
@bot.command()
async def generatepods(ctx, numberofpods=1):
    random.shuffle(bot.player)
    x = math.ceil(len(bot.player)/int(numberofpods))
    a = 0
    for i in bot.player:
        if a < x:
            bot.playerspod1.update({bot.player[a]:0})
        if x <= a < (2*x):
            bot.playerspod2.update({bot.player[a]:0})
        if (2*x) <= a < (3*x):
            bot.playerspod3.update({bot.player[a]:0})
        a += 1
    await ctx.send("Registered: \nPod 1: " + str(bot.playerspod1) + "\nPod 2: " + str(bot.playerspod2) + "\nPod 3: " + str(bot.playerspod3))
    if len(bot.playerspod1) % 2 == 1:
        bot.playerspod1.update({"NO PLAY": 0})
    if len(bot.playerspod2) % 2 == 1:
        bot.playerspod2.update({"NO PLAY": 0})
    if len(bot.playerspod3) % 2 == 1:
        bot.playerspod3.update({"NO PLAY": 0})


@bot.command()
async def generatetables(ctx, pod=1):
    tables_pod1 = [0, 0, 0, 0]
    tables_pod2 = [0, 0, 0, 0]
    tables_pod3 = [0, 0, 0, 0]

    if int(pod) == 1:
        for i in range(0, int(len(bot.playerspod1)/2)):
            tables_pod1[i-1] = list(bot.playerspod1.keys())[i*2-2] + " - " + list(bot.playerspod1.keys())[i*2-1]
        await ctx.send("Your tables for pod 1 are:\n" + str(tables_pod1[0]) + "\n" + str(tables_pod1[1]) + "\n" + str(tables_pod1[2]) + "\n" + str(tables_pod1[3]) + "\n")
    if int(pod) == 2:
        for i in range(0, int(len(bot.playerspod2)/2)):
            tables_pod2[i-1] = list(bot.playerspod2.keys())[i*2-2] + " - " + list(bot.playerspod2.keys())[i*2-1]
        await ctx.send("Your tables for pod 1 are:\n" + str(tables_pod2[0]) + "\n" + str(tables_pod2[1]) + "\n" + str(tables_pod2[2]) + "\n" + str(tables_pod2[3]) + "\n")
    if int(pod) == 3:
        for i in range(0, int(len(bot.playerspod3)/2)):
            tables_pod3[i-1] = list(bot.playerspod3.keys())[i*2-2] + " - " + list(bot.playerspod3.keys())[i*2-1]
        await ctx.send("Your tables for pod 1 are:\n" + str(tables_pod3[0]) + "\n" + str(tables_pod3[1]) + "\n" + str(tables_pod3[2]) + "\n" + str(tables_pod3[3]) + "\n")


# fix ties
@bot.command()
async def gameover(ctx, pod, table, score):
    score.split("-")
    if int(pod) == 1:
        if int(score[0]) > int(score[2]):
            bot.players_pod1_score[(int(table)*2)-2] = int(bot.players_pod1_score[(int(table)*2)-2]) + 3
        if int(score[0]) < int(score[2]):
            bot.players_pod1_score[(int(table)*2)-1] = int(bot.players_pod1_score[(int(table)*2)-1]) + 3
        if int(score[0]) == int(score[2]):
            bot.players_pod1_score[(int(table)*2)-2] = int(bot.players_pod1_score[(int(table)*2)-2]) + 1
            bot.players_pod1_score[(int(table)*2)-1] = int(bot.players_pod1_score[(int(table)*2)-1]) + 1
    if int(pod) == 2:
        if int(score[0]) > int(score[2]):
            bot.players_pod2_score[(int(table)*2)-2] = int(bot.players_pod2_score[(int(table)*2)-2]) + 3
        if int(score[0]) < int(score[2]):
            bot.players_pod2_score[(int(table)*2)-1] = int(bot.players_pod2_score[(int(table)*2)-1]) + 3
        if int(score[0]) == int(score[2]):
            bot.players_pod2_score[(int(table)*2)-2] = int(bot.players_pod2_score[(int(table)*2)-2]) + 1
            bot.players_pod2_score[(int(table)*2)-1] = int(bot.players_pod2_score[(int(table)*2)-1]) + 1
    if int(pod) == 3:
        if int(score[0]) > int(score[2]):
            bot.players_pod3_score[(int(table)*2)-2] = int(bot.players_pod3_score[(int(table)*2)-2]) + 3
        if int(score[0]) < int(score[2]):
            bot.players_pod3_score[(int(table)*2)-1] = int(bot.players_pod3_score[(int(table)*2)-1]) + 3
        if int(score[0]) == int(score[2]):
            bot.players_pod3_score[(int(table)*2)-2] = int(bot.players_pod3_score[(int(table)*2)-2]) + 1
            bot.players_pod3_score[(int(table)*2)-1] = int(bot.players_pod3_score[(int(table)*2)-1]) + 1


@bot.command()
async def results(ctx, pod=1):
    a = 0
    if int(pod) == 1:
        for player in bot.playerspod1:
            bot.playerspod1[player] = bot.players_pod1_score[a] + bot.playerspod1[player]
            a += 1
        bot.sorted_playerspod1 = dict(sorted(bot.playerspod1.items(), key=operator.itemgetter(1), reverse=True))
        await ctx.send(bot.sorted_playerspod1)
    if int(pod) == 2:
        for player in bot.playerspod2:
            bot.playerspod2[player] = bot.players_pod2_score[a]
            a += 1
        bot.sorted_playerspod2 = dict(sorted(bot.playerspod2.items(), key=operator.itemgetter(1), reverse=True))
        await ctx.send(bot.sorted_playerspod2)
    if int(pod) == 3:
        for player in bot.playerspod3:
            bot.playerspod3[player] = bot.players_pod3_score[a]
            a += 1
        bot.sorted_playerspod3 = dict(sorted(bot.playerspod3.items(), key=operator.itemgetter(1), reverse=True))
        await ctx.send(bot.sorted_playerspod3)


@bot.command()
async def endtourney(ctx):
    bot.player = []
    bot.players_pod1_score = [0, 0, 0, 0, 0, 0, 0, 0]
    bot.players_pod2_score = [0, 0, 0, 0, 0, 0, 0, 0]
    bot.players_pod3_score = [0, 0, 0, 0, 0, 0, 0, 0]
    bot.playerspod1 = {}
    bot.playerspod2 = {}
    bot.playerspod3 = {}
    bot.leaderboardpod1 = {}
    bot.leaderboardpod2 = {}
    bot.leaderboardpod3 = {}
    bot.leaderboard = {}
    await ctx.send("Success!")


@bot.command()
async def generateleaderboard(ctx, pod):
    if int(pod) == 1:
        bot.leaderboardpod1 = "Leaderboard For Event\n-----------------------------\n"
        for i in bot.sorted_player_pod1:
            bot.leaderboardpod1.join(i + "  ---  " + bot.sorted_player_pod1[i] + "\n")
        await ctx.send(bot.leaderboardpod1)
    elif int(pod) == 2:
        bot.leaderboardpod2 = "Leaderboard For Event\n-----------------------------\n"
        for i in bot.sorted_player_pod2:
            bot.leaderboardpod2.join(i + "  ---  " + bot.sorted_player_pod2[i])
        await ctx.send(bot.leaderboardpod2)
    elif int(pod) == 3:
        bot.leaderboardpod3 = "Leaderboard For Event\n-----------------------------\n"
        for i in bot.sorted_player_pod3:
            bot.leaderboardpod3.join(i + "  ---  " + bot.sorted_player_pod3[i])
        await ctx.send(bot.leaderboardpod3)

@bot.command()
async def timer(ctx, type="start", time=3000):
    if type == 'start':
        await asyncio.sleep(time - 600)
        await ctx.send("10 minutes left in the round!")
        await asyncio.sleep(300)
        await ctx.send("5 minutes left in the round!")
        await asyncio.sleep(300)
        await ctx.send("5 Rounds before Tie!")

@bot.command()
async def updateleaderboard(ctx, pod):
    with open('leaderboard.json', 'r') as fp:
        oldleaderboard = json.load(fp)
        A = Counter(oldleaderboard)
        B = Counter(bot.leaderboardpod1)
        C = Counter(bot.leaderboardpod2)
        D = Counter(bot.leaderboardpod3)
        newleaderboard = A + B + C + D
        leaderboarddisplay = "Leaderboard For Event\n-----------------------------\n"
        for key in newleaderboard:
            leaderboarddisplay = leaderboarddisplay + str(key) + "  ---  " + str(newleaderboard[key]) + "\n"
        await ctx.send(leaderboarddisplay)
    with open('leaderboard.json', 'w') as fp:
        json.dump(newleaderboard, fp)

    bot.leaderboarddisplay = "Leaderboard For Event\n-----------------------------\n"
    for i in bot.leaderboard:
        bot.leaderboarddisplay.join(str(i) + "  ---  " + str(bot.leaderboard[i] + "\n"))
    await ctx.send(bot.leaderboarddisplay)

    with open('leaderboard.json', 'w') as fp:
        json.dump(bot.leaderboard, fp)

bot.run(token)
