from tkinter import *
from math import *
from time import *
from random import *
root = Tk()
screen = Canvas( root, width=800, height=800, background = "black" )
screen.pack()

x = []
y = []
starDrawings = []

colors = ["white", "yellow", "orange"]
for i in range(500):
    x.append(randint(0,800))
    y.append(randint(0,800))
    starDrawings.append(0)

for i in range(1000):
    for j in range(500):
        starDrawings[j] = screen.create_oval(x[j]-5, y[j]-5, x[j]+5, y[j]+5, fill=colors[j%3])
        if x[j] >= 800:
            x[j] = -1
        x[j] = x[j] + 1

    screen.update()
    sleep(0.01)
    for j in range(500):
        screen.delete(starDrawings[j])
