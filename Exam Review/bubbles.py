from tkinter import *
from random import *
from time import *

root = Tk()
screen = Canvas(root, width=800, height=800, background="white")
screen.pack()

size = []
speed = []
x = []
y = []
bubbles = []

for i in range(200):
    size.append(randint(2,6))
    speed.append(randint(1,10))
    x.append(randint(0,800))
    y.append(randint(0,800))
    bubbles.append(0)

for i in range(500):
    for j in range(200):
        y[j] = y[j] - speed[j]
        bubbles[j] = screen.create_oval(x[j]-size[j],y[j]-size[j],x[j]+size[j],y[j]+size[j], outline="blue")
        speed[j] = speed[j] + 0.25
    screen.update()
    sleep(0.03)
    for j in range(200):
        screen.delete(bubbles[j])
        
