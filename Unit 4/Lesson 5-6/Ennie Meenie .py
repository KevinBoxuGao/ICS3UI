p = ["a", "b", "c", "d", "e"]
phrase = "R e e e e e e e e e e e e e e e e e e e e "
wordArray = phrase.split()


i = 0
while len(p) > 1:
    print(p)
    for j in range(len(wordArray)):
        print(wordArray[j] + " --> "+ p[i])
        if j == len(wordArray)-1:
            print(p[i]+ " is out!")
            print()
            p.remove(p[i])
            i = i - 1
        if i == len(p)-1:
            i = 0
        else:
            i = i+1

print(p[0]+" wins!")
