from tkinter import *
from time import *
from random import *

root = Tk()
screen = Canvas( root, width=800, height=800, background = "lightgrey" )
screen.pack()

x = []
y = []
rainDrops = []

lengths = []
speeds=[]

for i in range(800):
    x.append(randint(0,800))
    y.append(randint(-400,500))
    lengths.append(randint(10,40))
    speeds.append(randint(25, 50))
    rainDrops.append(0)

while True:
    for j in range(800):
        rainDrops[j] = screen.create_line(x[j], y[j], x[j], y[j]+lengths[j], fill="blue", width="2")
        if y[j] >= 800:
            y[j] = -(lengths[j])
        y[j] = y[j] + speeds[j]      
    
    screen.update()
    sleep(0.03)
    for j in range(800):
        screen.delete(rainDrops[j])
