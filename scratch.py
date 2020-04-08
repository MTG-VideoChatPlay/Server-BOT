import discord
from discord.ext import commands
import operator
token = "Njk2NTUyMDE1MjU3NjY1NTQ3.Xo0k8w.yhi_3g-cQfnO769PLW_ZP8Gta_Y"
bot = commands.Bot(command_prefix='*', activity=discord.Game(name="Prefix is *"))



@bot.command()
async def results(ctx, pod):
    a = 0
    if int(pod) == 1:
        for player in bot.players_pod1:
            bot.playersdictpod1[player] = bot.players_pod1_score[a] + bot.playersdictpod1[player]
            a += 1
        bot.sorted_playerdictpod1 = dict(sorted(bot.playersdictpod1.items(), key=operator.itemgetter(1), reverse=True))
        await ctx.send(bot.sorted_playerdictpod1)
    """if int(pod) == 2:
        for player in bot.players_pod2:
            bot.playersdictpod2[player] = bot.players_pod2_score[a]
            a += 1
        bot.sorted_playerdictpod2 = dict(sorted(bot.playersdictpod2.items(), key=operator.itemgetter(1), reverse=True))
        await ctx.send(bot.sorted_playerdictpod2)
    if int(pod) == 3:
        for player in bot.players_pod3:
            bot.playersdictpod3[player] = bot.players_pod3_score[a]
            a += 1
        bot.sorted_playerdictpod3 = dict(sorted(bot.playersdictpod3.items(), key=operator.itemgetter(1), reverse=True))
        await ctx.send(bot.sorted_playerdictpod3)"""


bot.run(token)