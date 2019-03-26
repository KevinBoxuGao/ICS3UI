raceTimes = [453, 450, 420, 492, 509, 444, 460, 530, 499]

for i in range(len(raceTimes)):
    high = raceTimes[0]
    for j in range(len(raceTimes)):
        if raceTimes[j] > high:
            high = raceTimes[j]

    if i == 0:
        ending="st"
    elif i < 3:
        ending="rd"
    else: 
        ending="th"

    print(str(i + 1) + ending + " place: " + str(high))
    raceTimes.remove(high)
