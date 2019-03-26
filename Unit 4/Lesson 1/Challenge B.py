marks = [67, 47, 98, 40, 78, 0, 50, 53, 42, 50, 49, 88, 91, 6, 32]

for i in range(len(marks)):
    if marks[i] <= 0:
        continue
    elif marks[i] <= 34:
        marks[i] = 35
    elif 46 <= marks[i] <= 49:
        marks[i] = 45
    elif marks[i] == 50:
        marks[i] = 51

for m in marks:
    print(m)
