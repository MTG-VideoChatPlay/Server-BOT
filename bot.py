import discord
from discord.ext import commands
import random
import math
import operator
import json
from collections import Counter

token = "Njk2NTUyMDE1MjU3NjY1NTQ3.XozjZQ.98EpSLsSfmIyzeQ22jrre_eVulY"
bot = commands.Bot(command_prefix='*', activity=discord.Game(name="Prefix is *"))

bot.player = []
bot.players_pod1 = []
bot.players_pod1_score = [0, 0, 0, 0, 0, 0, 0, 0]
bot.players_pod2 = []
bot.players_pod2_score = [0, 0, 0, 0, 0, 0, 0, 0]
bot.players_pod3 = []
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
async def generatetables(ctx, pod, round=1):
    if int(pod) == 1:
        if int(round) == 1:
            random.shuffle(bot.players_pod1)
        else:
            bot.players_pod1 = list(bot.playersdictpod1)
        table1 = bot.players_pod1[0] + " " + bot.players_pod1[1]
        table2 = bot.players_pod1[2] + " " + bot.players_pod1[3]
        table3 = bot.players_pod1[4] + " " + bot.players_pod1[5]
        table4 = bot.players_pod1[6] + " " + bot.players_pod1[7]
        await ctx.send("Your tables for pod 1 are:\n" + table1 + "\n" + table2 + "\n" + table3 + "\n" + table4 + "\n")
    if int(pod) == 2:
        if int(round) == 1:
            random.shuffle(bot.players_pod1)
        else:
            bot.players_pod2 = list(bot.playersdictpod2)
        random.shuffle(bot.players_pod2)
        table5 = bot.players_pod2[0] + " " + bot.players_pod2[1]
        table6 = bot.players_pod2[2] + " " + bot.players_pod2[3]
        table7 = bot.players_pod2[4] + " " + bot.players_pod2[5]
        table8 = bot.players_pod2[6] + " " + bot.players_pod2[7]
        await ctx.send("Your tables for pod 2 are:\n " + table5 + "\n" + table6 + "\n" + table7 + "\n" + table8 + "\n")
    if int(pod) == 3:
        if int(round) == 1:
            random.shuffle(bot.players_pod3)
        else:
            bot.players_pod3 = list(bot.playersdictpod3)
        random.shuffle(bot.players_pod3)
        table9 = bot.players_pod3[0] + " " + bot.players_pod3[1]
        table10 = bot.players_pod3[2] + " " + bot.players_pod3[3]
        table11 = bot.players_pod3[4] + " " + bot.players_pod3[5]
        table12 = bot.players_pod3[6] + " " + bot.players_pod3[7]
        await ctx.send("Your tables for pod 3 are:\n" + table9 + "\n" + table10 + "\n" + table11 + "\n" + table12 + "\n")


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
    if pod == 1:
        for player in bot.players_pod1:
            bot.playersdictpod1[player] = bot.players_pod1_score[a]
            a += 1
        bot.sorted_playerdictpod1 = dict(sorted(bot.playersdictpod1.items(), key=operator.itemgetter(1), reverse=True))
        await ctx.send(bot.sorted_playerdictpod1)
    if pod == 2:
        for player in bot.players_pod2:
            bot.playersdictpod2[player] = bot.players_pod2_score[a]
            a += 1
        bot.sorted_playerdictpod2 = dict(sorted(bot.playersdictpod2.items(), key=operator.itemgetter(1), reverse=True))
        await ctx.send(bot.sorted_playerdictpod2)
    if pod == 3:
        for player in bot.players_pod3:
            bot.playersdictpod3[player] = bot.players_pod3_score[a]
            a += 1
        bot.sorted_playerdictpod3 = dict(sorted(bot.playersdictpod3.items(), key=operator.itemgetter(1), reverse=True))
        await ctx.send(bot.sorted_playerdictpod3)


@bot.command()
async def endtourney(ctx):
    bot.player = []
    bot.players_pod1 = []
    bot.players_pod2 = []
    bot.players_pod3 = []
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
        d = Counter(bot.leaderboardpod3)
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
