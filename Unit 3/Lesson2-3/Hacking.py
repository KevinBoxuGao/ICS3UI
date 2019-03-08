from time import *
from random import *

def loading():
    for i in range(3):
        sleep(0.5)
        print(".", end="")

def percentage():

target = input("Who would you like to hack? ")
print("\n"+"initializing", end ="")
loading()

print("\n hacking their mainframes")

print("\n disabling their firewall")

print("\n cracking their passwords")

print("\n ")

print(target+"'s credit card number is "+str(randomint(1000000000000000,9999999999999999)))
print("The three digits on the back are"+str(randomint(100,999)))
