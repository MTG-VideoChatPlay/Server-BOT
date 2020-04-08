import json
from collections import Counter
leaderboardpod1 = {
        "a": 3,
        "b": 6,
        "c": 12,
        "d": 9,
        "e": 9,
        "f": 6,
        "g": 3,
        "h": 0,
    }


with open('leaderboard.json', 'r') as fp:
    oldleaderboard = json.load(fp)
    A = Counter(oldleaderboard)
    B = Counter(leaderboardpod1)
    newleaderboard = A + B

    leaderboarddisplay = "Leaderboard For Event\n-----------------------------\n"
    for key in newleaderboard:
        leaderboarddisplay = leaderboarddisplay + str(key) + "  ---  " + str(newleaderboard[key]) + "\n"
    await ctx.send(leaderboarddisplay)
with open('leaderboard.json', 'w') as fp:
    json.dump(newleaderboard, fp)
