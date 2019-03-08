from tkinter import*
import random

myInterface = Tk()
screen = Canvas( myInterface, width=900, height=900, background="white" )
screen.pack()

for i in range(101):
    screen.create_line(random.randint(0,900), random.randint(0,900), random.randint(0,900), random.randint(0,900), fill="orange")


spacing = 50
for x in range(0, 1000, spacing): 
    screen.create_line(x, 25, x, 1000, fill="blue")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 1000, spacing):
    screen.create_line(25, y, 1000, y, fill="blue")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)

screen.update()
