L = [92,456,34,7234,24,7,623,5,35]

maxSoFar = L[0]

for i in range(len(L)):
    if L[i] > maxSoFar:
        maxSoFar = L[i]

print(maxSoFar)
