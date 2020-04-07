person = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
pod1 = []
pod2 = []
pod3 = []
a = 0
for i in person:
    if a < 8:
        pod1.append(person[a])
    if 7 < a < 15:
        pod2.append(person[a])
    if 15 < a < 23:
        pod3.append(person[a])
    a += 1
print(pod1)
print(pod2)
print(pod3)
