from tkinter import *
from time import *
from math import *

myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="white")
screen.pack()

#stoplight
xStart = 360
yStart = 320
diameter1 = 80
colors = ["green","yellow","red"]
screen.create_rectangle(xStart, yStart, xStart + diameter1, yStart + 3*diameter1, fill="black")

#ball
x1 = 100
y1 = 400

xSpeed = 11
ySpeed = -2
diameter2 = 100

color = "red"

#ANIMATION LOOP
for i in range(10000):
        
    x1 = x1 + xSpeed  
    y1 = y1 + ySpeed
    x2 = x1 + diameter2
    y2 = y1 + diameter2
    ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill=color)  
    #Update, sleep, delete

    screen.update()
    sleep(0.03)
    screen.delete(ball)

    if i % 50 == 0:
        j = (i//10) % 3
        print(j)
        light = screen.create_oval(xStart, yStart+j*diameter1, xStart+diameter1, yStart+(j+1)*diameter1, fill=colors[j%3])
        screen.update()
        screen.delete(light)

    #changing directions
    if x2 >= 800:
        xSpeed = -1 * xSpeed
    elif x1 < 0:
        xSpeed = -1 * xSpeed

    if y2 >= 800:
        ySpeed = -1 * ySpeed
    elif y1 < 0:
        ySpeed = -1 * ySpeed



