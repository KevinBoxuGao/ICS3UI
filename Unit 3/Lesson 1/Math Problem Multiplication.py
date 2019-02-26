from random import *

while True:
    first = randint(0, 15)
    second = randint(0, 15)
    answer = first*second

    guess = input("What is "+str(first)+" times "+str(second)+"? ")

    while guess != str(answer):
        print("O no, try again.")
        guess = input("What is "+str(first)+" times "+str(second)+"? ")
        
    print("Great job, you got it!")

