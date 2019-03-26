temperatures = [25, 27, 30, 28, 22, 29, 33, 31, 30, 27, 27, 19, 18, 17, 16, 12, 18]

#Use a for-loop to find the highest and the lowest temperatures

low = temperatures[0]
high = temperatures[0]

for i in range(len(temperatures)):
    if temperatures[i] < low:
        low = temperatures[i]
    elif temperatures[i] > high:
        high = temperatures[i]

print(low)
print(high)
