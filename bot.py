number_of_pods=input("how many pods")
number_of_pods=int(number_of_pods)
players = []
players_pod1 = []
players_pod2 = []
players_pod3 = []
if number_of_pods==1:
    print("lets get your players registered")
    pod1_player_1=input("what is player 1's name")
    pod1_player_2=input("what is player 2's name")
    pod1_player_3=input("what is player 3's name")
    pod1_player_4=input("what is player 4's name")
    pod1_player_5=input("what is player 5's name")
    pod1_player_6=input("what is player 6's name")
    pod1_player_7=input("what is player 7's name")
    pod1_player_8=input("what is player 8's name")
    pod1_players=[pod1_player_1, pod1_player_2, pod1_player_3, pod1_player_4, pod1_player_5, pod1_player_6, pod1_player_7, pod1_player_8]
    players_correct=input("so, just to confirm, the players are " + pod1_player_1 + " " + pod1_player_2 + " " + pod1_player_3 + " " + pod1_player_4 + " " + pod1_player_5 + " " +  pod1_player_6 + " " + pod1_player_7 + " " + pod1_player_8)
    players_correct=str(players_correct)
    if players_correct=="y":
        players_pod1 = [pod1_player_1, pod1_player_2, pod1_player_3, pod1_player_3, pod1_player_4, pod1_player_5, pod1_player_6, pod1_player_7, pod1_player_8]
        players = players + players_pod1
        print("registered!")
    while players_correct=="n":
            print("lets try again1")
            print("lets get your players registered")
            pod1_player_1 = input("what is player 1's name")
            pod1_player_2 = input("what is player 2's name")
            pod1_player_3 = input("what is player 3's name")
            pod1_player_4 = input("what is player 4's name")
            pod1_player_5 = input("what is player 5's name")
            pod1_player_6 = input("what is player 6's name")
            pod1_player_7 = input("what is player 7's name")
            pod1_player_8 = input("what is player 8's name")
            pod1_players = [pod1_player_1, pod1_player_2, pod1_player_3, pod1_player_4, pod1_player_5, pod1_player_6,
                            pod1_player_7, pod1_player_8]
            players_correct = input(
                "so, just to confirm, the players are " + pod1_player_1 + " " + pod1_player_2 + " " + pod1_player_3 + " " + pod1_player_4 + " " + pod1_player_5 + " " + pod1_player_6 + " " + pod1_player_7 + " " + pod1_player_8)
            players_correct = str(players_correct)
            if players_correct == "y":
                players_pod1 = [pod1_player_1, pod1_player_2, pod1_player_3, pod1_player_3, pod1_player_4,
                                pod1_player_5, pod1_player_6, pod1_player_7, pod1_player_8]
                players = players + players_pod1
                print("registered!")
            else:
                print("please try again")
elif number_of_pods==2:
    print("begin pod 1 registration")
    pod1_player_1 = input("what is player 1's name")
    pod1_player_2 = input("what is player 2's name")
    pod1_player_3 = input("what is player 3's name")
    pod1_player_4 = input("what is player 4's name")
    pod1_player_5 = input("what is player 5's name")
    pod1_player_6 = input("what is player 6's name")
    pod1_player_7 = input("what is player 7's name")
    pod1_player_8 = input("what is player 8's name")
    pod1_correct=input("so, just to confirm, the players are " + pod1_player_1 + " " + pod1_player_2 + " " + pod1_player_3 + " " + pod1_player_4 + " " + pod1_player_5 + " " + pod1_player_6 + " " + pod1_player_7 + " " + pod1_player_8)
    pod1_correct=str(pod1_correct)
    if pod1_correct=="y":
        players_pod1 = [pod1_player_1, pod1_player_2, pod1_player_3, pod1_player_3, pod1_player_4, pod1_player_5, pod1_player_6, pod1_player_7, pod1_player_8]
        players = players + players_pod1
        print("registered pod 1")
    while pod1_correct=="n":
        print("please try again")
        print("begin pod 1 registration")
        pod1_player_1 = input("what is player 1's name")
        pod1_player_2 = input("what is player 2's name")
        pod1_player_3 = input("what is player 3's name")
        pod1_player_4 = input("what is player 4's name")
        pod1_player_5 = input("what is player 5's name")
        pod1_player_6 = input("what is player 6's name")
        pod1_player_7 = input("what is player 7's name")
        pod1_player_8 = input("what is player 8's name")
        pod1_correct = input(
            "so, just to confirm, the players are " + pod1_player_1 + " " + pod1_player_2 + " " + pod1_player_3 + " " + pod1_player_4 + " " + pod1_player_5 + " " + pod1_player_6 + " " + pod1_player_7 + " " + pod1_player_8)
        pod1_correct = str(pod1_correct)
        if pod1_correct == "y":
            players_pod1 = [pod1_player_1, pod1_player_2, pod1_player_3, pod1_player_3, pod1_player_4, pod1_player_5,
                            pod1_player_6, pod1_player_7, pod1_player_8]
            players = players + players_pod1
            print("registered pod 1")
        else:
            print("please try again")
    print("now lets register pod 2")
    pod2_player_1 = input("what is player 1's name")
    pod2_player_2 = input("what is player 2's name")
    pod2_player_3 = input("what is player 3's name")
    pod2_player_4 = input("what is player 4's name")
    pod2_player_5 = input("what is player 5's name")
    pod2_player_6 = input("what is player 6's name")
    pod2_player_7 = input("what is player 7's name")
    pod2_player_8 = input("what is player 8's name")
    pod2_correct = input("so, just to confirm, the players in pod 2 are " + pod2_player_1 + " " + pod2_player_2 + " " + pod2_player_3 + " " + pod2_player_4 + " " + pod2_player_5 + " " + pod2_player_6 + " " + pod2_player_7 + " " + pod2_player_8)
    pod2_correct = str(pod2_correct)
    if pod2_correct == "y":
        players_pod2 = [pod2_player_1, pod2_player_2, pod2_player_3, pod2_player_4, pod2_player_5, pod2_player_6,
                        pod2_player_7, pod2_player_8]
        players = players + players_pod2
        print("pod 2 registered")
    while pod2_correct=="n":
        print("lets try again")
        print("now lets register pod 2")
        pod2_player_1 = input("what is player 1's name")
        pod2_player_2 = input("what is player 2's name")
        pod2_player_3 = input("what is player 3's name")
        pod2_player_4 = input("what is player 4's name")
        pod2_player_5 = input("what is player 5's name")
        pod2_player_6 = input("what is player 6's name")
        pod2_player_7 = input("what is player 7's name")
        pod2_player_8 = input("what is player 8's name")
        pod2_correct = input("so, just to confirm, the players in pod 2 are " + pod2_player_1 + " " + pod2_player_2 + " " + pod2_player_3 + " " + pod2_player_4 + " " + pod2_player_5 + " " + pod2_player_6 + " " + pod2_player_7 + " " + pod2_player_8)
        pod2_correct = str(pod2_correct)
        if pod2_correct == "y":
            players_pod2 = [pod2_player_1, pod2_player_2, pod2_player_3, pod2_player_4, pod2_player_5, pod2_player_6,
                            pod2_player_7, pod2_player_8]
            players = players + players_pod2
            print("pod 2 registered")
        else:
            print("please try again")
elif number_of_pods==3:
    print("begin pod 1 registration")
    pod1_player_1 = input("what is player 1's name")
    pod1_player_2 = input("what is player 2's name")
    pod1_player_3 = input("what is player 3's name")
    pod1_player_4 = input("what is player 4's name")
    pod1_player_5 = input("what is player 5's name")
    pod1_player_6 = input("what is player 6's name")
    pod1_player_7 = input("what is player 7's name")
    pod1_player_8 = input("what is player 8's name")
    pod1_correct = input(
        "so, just to confirm, the players are " + pod1_player_1 + " " + pod1_player_2 + " " + pod1_player_3 + " " + pod1_player_4 + " " + pod1_player_5 + " " + pod1_player_6 + " " + pod1_player_7 + " " + pod1_player_8)
    pod1_correct = str(pod1_correct)
    if pod1_correct == "y":
        players_pod1 = [pod1_player_1, pod1_player_2, pod1_player_3, pod1_player_3, pod1_player_4, pod1_player_5, pod1_player_6, pod1_player_7, pod1_player_8]
        players = players + players_pod1
        print("registered pod 1")
    while pod1_correct == "n":
        print("please try again")
        print("begin pod 1 registration")
        pod1_player_1 = input("what is player 1's name")
        pod1_player_2 = input("what is player 2's name")
        pod1_player_3 = input("what is player 3's name")
        pod1_player_4 = input("what is player 4's name")
        pod1_player_5 = input("what is player 5's name")
        pod1_player_6 = input("what is player 6's name")
        pod1_player_7 = input("what is player 7's name")
        pod1_player_8 = input("what is player 8's name")
        pod1_correct = input(
            "so, just to confirm, the players are " + pod1_player_1 + " " + pod1_player_2 + " " + pod1_player_3 + " " + pod1_player_4 + " " + pod1_player_5 + " " + pod1_player_6 + " " + pod1_player_7 + " " + pod1_player_8)
        pod1_correct = str(pod1_correct)
        if players_correct == "y":
            players_pod1 = [pod1_player_1, pod1_player_2, pod1_player_3, pod1_player_3, pod1_player_4, pod1_player_5,
                            pod1_player_6, pod1_player_7, pod1_player_8]
            players = players + players_pod1
            print("registered pod 1")
            print("registered so far " + players)
        else:
            print("please try again")
    print("now lets register pod 2")
    pod2_player_1 = input("what is player 1's name")
    pod2_player_2 = input("what is player 2's name")
    pod2_player_3 = input("what is player 3's name")
    pod2_player_4 = input("what is player 4's name")
    pod2_player_5 = input("what is player 5's name")
    pod2_player_6 = input("what is player 6's name")
    pod2_player_7 = input("what is player 7's name")
    pod2_player_8 = input("what is player 8's name")
    pod2_correct = input(
        "so, just to confirm, the players in pod 2 are " + pod2_player_1 + " " + pod2_player_2 + " " + pod2_player_3 + " " + pod2_player_4 + " " + pod2_player_5 + " " + pod2_player_6 + " " + pod2_player_7 + " " + pod2_player_8)
    pod2_correct = str(pod2_correct)
    if pod2_correct == "y":
        players_pod2 = [pod2_player_1, pod2_player_2, pod2_player_3, pod2_player_4, pod2_player_5, pod2_player_6,
                        pod2_player_7, pod2_player_8]
        players = players + players_pod2
        print("pod 2 registered")
    while pod2_correct == "n":
        print("lets try again")
        print("now lets register pod 2")
        pod2_player_1 = input("what is player 1's name")
        pod2_player_2 = input("what is player 2's name")
        pod2_player_3 = input("what is player 3's name")
        pod2_player_4 = input("what is player 4's name")
        pod2_player_5 = input("what is player 5's name")
        pod2_player_6 = input("what is player 6's name")
        pod2_player_7 = input("what is player 7's name")
        pod2_player_8 = input("what is player 8's name")
        pod2_correct = input("so, just to confirm, the players in pod 2 are " + pod2_player_1 + " " + pod2_player_2 + " " + pod2_player_3 + " " + pod2_player_4 + " " + pod2_player_5 + " " + pod2_player_6 + " " + pod2_player_7 + " " + pod2_player_8)
        pod2_correct = str(pod2_correct)
        if pod2_correct == "y":
            players_pod2 = [pod2_player_1, pod2_player_2, pod2_player_3, pod2_player_4, pod2_player_5, pod2_player_6,
                            pod2_player_7, pod2_player_8]
            players = players + players_pod2
            print("pod 2 registered")
            print("registered so far" + players)
        else:
            print("please try again")
    print("now, lets register pod 3")
    pod3_player_1 = input("what is player 1's name")
    pod3_player_2 = input("what is player 2's name")
    pod3_player_3 = input("what is player 3's name")
    pod3_player_4 = input("what is player 4's name")
    pod3_player_5 = input("what is player 5's name")
    pod3_player_6 = input("what is player 6's name")
    pod3_player_7 = input("what is player 7's name")
    pod3_player_8 = input("what is player 8's name")
    pod3_correct = input("so, just to confirm, the players in pod 2 are " + pod3_player_1 + " " + pod3_player_2 + " " + pod3_player_3 + " " + pod3_player_4 + " " + pod3_player_5 + " " + pod3_player_6 + " " + pod3_player_7 + " " + pod3_player_8)
    pod3_correct = str(pod3_correct)
    if pod3_correct=="y":
        players_pod3 = [pod3_player_1, pod3_player_2, pod3_player_3, pod3_player_4, pod3_player_5, pod3_player_6, pod3_player_7, pod3_player_8]
        players = players + players_pod3
        print("pod 3 registered")
    while pod3_correct=="n":
        print("now, lets register pod 3")
        pod3_player_1 = input("what is player 1's name")
        pod3_player_2 = input("what is player 2's name")
        pod3_player_3 = input("what is player 3's name")
        pod3_player_4 = input("what is player 4's name")
        pod3_player_5 = input("what is player 5's name")
        pod3_player_6 = input("what is player 6's name")
        pod3_player_7 = input("what is player 7's name")
        pod3_player_8 = input("what is player 8's name")
        pod3_correct = input("so, just to confirm, the players in pod 2 are " + pod3_player_1 + " " + pod3_player_2 + " " + pod3_player_3 + " " + pod3_player_4 + " " + pod3_player_5 + " " + pod3_player_6 + " " + pod3_player_7 + " " + pod3_player_8)
        pod3_correct = str(pod3_correct)
        if pod3_correct == "y":
            players_pod3 = [pod3_player_1, pod3_player_2, pod3_player_3, pod3_player_4, pod3_player_5, pod3_player_6,
                            pod3_player_7, pod3_player_8]
            players = players + players_pod3
            print("pod 3 registered")
            print("registered so far " + players)
        else:
            print("please try again")
else:
    print("error")

print(players)
print(players_pod1)
print(players_pod2)
print(players_pod3)
