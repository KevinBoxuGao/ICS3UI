marks = int(input("How many marks do you want to enter? "))
total = 0
for i in range(marks):
    mark = int(input("enter one of your marks: "))
    total = total + mark
print(total/marks)
