import discord
from discord.ext import commands
import random
import math
import operator
import json
from collections import Counter

token = "Njk2NTUyMDE1MjU3NjY1NTQ3.Xo0k8w.yhi_3g-cQfnO769PLW_ZP8Gta_Y"
bot = commands.Bot(command_prefix='*', activity=discord.Game(name="Prefix is *"))

bot.player = []
bot.players_pod1_score = [0, 0, 0, 0, 0, 0, 0, 0]
bot.players_pod2_score = [0, 0, 0, 0, 0, 0, 0, 0]
bot.players_pod3_score = [0, 0, 0, 0, 0, 0, 0, 0]
bot.playersdictpod1 = {}
bot.playersdictpod2 = {}
bot.playersdictpod3 = {}
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

#WORKS PERFECTLY
@bot.command()
async def generatepods(ctx, numberofpods):
    random.shuffle(bot.player)
    x = math.ceil(len(bot.player)/int(numberofpods))
    a = 0
    for i in bot.player:
        if a < x:
            bot.playersdictpod1.update({bot.player[a]:0})
        if x <= a < (2*x):
            bot.playersdictpod2.update({bot.player[a]:0})
        if (2*x) <= a < (3*x):
            bot.playersdictpod3.update({bot.player[a]:0})
        a += 1
    await ctx.send("Registered: \nPod 1: " + str(bot.playersdictpod1) + "\nPod 2: " + str(bot.playersdictpod2) + "\nPod 3: " + str(bot.playersdictpod3))


@bot.command()
async def generatetables(ctx, pod, round=1):
    if int(pod) == 1:
        table1 = list(bot.playersdictpod1.keys())[0] + " - " + list(bot.playersdictpod1.keys())[1]
        table2 = list(bot.playersdictpod1.keys())[2] + " - " + list(bot.playersdictpod1.keys())[3]
        table3 = list(bot.playersdictpod1.keys())[4] + " - " + list(bot.playersdictpod1.keys())[5]
        table4 = list(bot.playersdictpod1.keys())[6] + " - " + list(bot.playersdictpod1.keys())[7]
        await ctx.send("Your tables for pod 1 are:\n" + table1 + "\n" + table2 + "\n" + table3 + "\n" + table4 + "\n")
    if int(pod) == 2:
        table5 = list(bot.playersdictpod2.keys())[0] + " " + list(bot.playersdictpod1.keys())[1]
        table6 = list(bot.playersdictpod2.keys())[2] + " " + list(bot.playersdictpod1.keys())[3]
        table7 = list(bot.playersdictpod2.keys())[4] + " " + list(bot.playersdictpod1.keys())[5]
        table8 = list(bot.playersdictpod2.keys())[6] + " " + list(bot.playersdictpod1.keys())[7]
        await ctx.send("Your tables for pod 2 are:\n " + table5 + "\n" + table6 + "\n" + table7 + "\n" + table8 + "\n")
    if int(pod) == 3:
        table9 = list(bot.playersdictpod3.keys())[0] + " " + list(bot.playersdictpod3.keys())[1]
        table10 = list(bot.playersdictpod3.keys())[2] + " " + list(bot.playersdictpod3.keys())[3]
        table11 = list(bot.playersdictpod3.keys())[4] + " " + list(bot.playersdictpod3.keys())[5]
        table12 = list(bot.playersdictpod3.keys())[6] + " " + list(bot.playersdictpod3.keys())[7]
        await ctx.send("Your tables for pod 3 are:\n" + table9 + "\n" + table10 + "\n" + table11 + "\n" + table12 + "\n")


# fix ties
@bot.command()
async def gameover(ctx, pod, table, score):
    score.split("-")
    if int(pod) == 1:
        if score[0] > score[1]:
            bot.players_pod1_score[(int(table)*2)-2] = int(bot.players_pod1_score[(int(table)*2)-2]) + 3
        elif score[0] < score[1]:
            bot.players_pod1_score[(int(table)*2)-1] = int(bot.players_pod1_score[(int(table)*2)-1]) + 3
        elif score[0] == score[1]:
            bot.players_pod1_score[(int(table)*2)-2] = int(bot.players_pod1_score[(int(table)*2)-2]) + 1
            bot.players_pod1_score[(int(table)*2)-1] = int(bot.players_pod1_score[(int(table)*2)-1]) + 1
    if int(pod) == 2:
        if score[0] > score[1]:
            bot.players_pod2_score[(int(table)*2)-2] = int(bot.players_pod2_score[(int(table)*2)-2]) + 3
        elif score[0] < score[1]:
            bot.players_pod2_score[(int(table)*2)-1] = int(bot.players_pod2_score[(int(table)*2)-1]) + 3
        elif score[0] == score[1]:
            bot.players_pod2_score[(int(table)*2)-2] = int(bot.players_pod2_score[(int(table)*2)-2]) + 1
            bot.players_pod2_score[(int(table)*2)-1] = int(bot.players_pod2_score[(int(table)*2)-1]) + 1
    if int(pod) == 3:
        if score[0] > score[1]:
            bot.players_pod3_score[(int(table)*2)-2] = int(bot.players_pod3_score[(int(table)*2)-2]) + 3
        elif score[0] < score[1]:
            bot.players_pod3_score[(int(table)*2)-1] = int(bot.players_pod3_score[(int(table)*2)-1]) + 3
        elif score[0] == score[1]:
            bot.players_pod3_score[(int(table)*2)-2] = int(bot.players_pod3_score[(int(table)*2)-2]) + 1
            bot.players_pod3_score[(int(table)*2)-1] = int(bot.players_pod3_score[(int(table)*2)-1]) + 1


@bot.command()
async def results(ctx, pod):
    a = 0
    if int(pod) == 1:
        for player in bot.playersdictpod1:
            bot.playersdictpod1[player] = bot.players_pod1_score[a] + bot.playersdictpod1[player]
            a += 1
        bot.sorted_playerdictpod1 = dict(sorted(bot.playersdictpod1.items(), key=operator.itemgetter(1), reverse=True))
        await ctx.send(bot.sorted_playerdictpod1)
    if int(pod) == 2:
        for player in bot.playersdictpod2:
            bot.playersdictpod2[player] = bot.players_pod2_score[a]
            a += 1
        bot.sorted_playerdictpod2 = dict(sorted(bot.playersdictpod2.items(), key=operator.itemgetter(1), reverse=True))
        await ctx.send(bot.sorted_playerdictpod2)
    if int(pod) == 3:
        for player in bot.playersdictpod3:
            bot.playersdictpod3[player] = bot.players_pod3_score[a]
            a += 1
        bot.sorted_playerdictpod3 = dict(sorted(bot.playersdictpod3.items(), key=operator.itemgetter(1), reverse=True))
        await ctx.send(bot.sorted_playerdictpod3)


@bot.command()
async def endtourney(ctx):
    bot.player = []
    bot.players_pod1_score = [0, 0, 0, 0, 0, 0, 0, 0]
    bot.players_pod2_score = [0, 0, 0, 0, 0, 0, 0, 0]
    bot.players_pod3_score = [0, 0, 0, 0, 0, 0, 0, 0]
    bot.playersdictpod1 = {}
    bot.playersdictpod2 = {}
    bot.playersdictpod3 = {}
    bot.leaderboardpod1 = {}
    bot.leaderboardpod2 = {}
    bot.leaderboardpod3 = {}
    bot.leaderboard = {}
    await ctx.send("Success!")


@bot.command()
async def generateleaderboard(ctx, pod):
    if int(pod) == 1:
        bot.leaderboardpod1 = "Leaderboard For Event\n-----------------------------\n"
        for i in bot.sorted_playerdict_pod1:
            bot.leaderboardpod1.join(i + "  ---  " + bot.sorted_playerdict_pod1[i] + "\n")
        await ctx.send(bot.leaderboardpod1)
    elif int(pod) == 2:
        bot.leaderboardpod2 = "Leaderboard For Event\n-----------------------------\n"
        for i in bot.sorted_playerdict_pod2:
            bot.leaderboardpod2.join(i + "  ---  " + bot.sorted_playerdict_pod2[i])
        await ctx.send(bot.leaderboardpod2)
    elif int(pod) == 3:
        bot.leaderboardpod3 = "Leaderboard For Event\n-----------------------------\n"
        for i in bot.sorted_playerdict_pod3:
            bot.leaderboardpod3.join(i + "  ---  " + bot.sorted_playerdict_pod3[i])
        await ctx.send(bot.leaderboardpod3)

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
