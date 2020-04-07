a = 0
b = 0
players_pod1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
players_pod1_score = [1, 2, 0, 1, 2, 3, 1, 2]
while a < 7:
    print(a)
    while b < 7:
        print(b)
        if players_pod1_score[a] > players_pod1_score[b]:
            players_pod1_buffer = players_pod1[a]
            players_pod1_score_buffer = players_pod1_score[a]
            players_pod1[a] = players_pod1[b]
            players_pod1_score[a] = players_pod1_score[b]
            players_pod1[b] = players_pod1_buffer
            players_pod1_score[b] = players_pod1_score_buffer
        elif players_pod1_score[a] < players_pod1_score[b]:
            players_pod1_buffer = players_pod1[b]
            players_pod1_score_buffer = players_pod1_score[b]
            players_pod1[b] = players_pod1[a]
            players_pod1_score[b] = players_pod1_score[a]
            players_pod1[a] = players_pod1_buffer
            players_pod1_score[a] = players_pod1_score_buffer
        b += 1
    a += 1



"""for i in players_pod1:
    print(str(players_pod1[a]) + " " + str(players_pod1_score[a]))
    a += 1"""