from tkinter import *
from time import *
from math import *
from random import *
tk = Tk()
screen = Canvas(tk, width=800, height=800, background="yellow")
screen.pack()

colours = ["blue", "green", "orange", "purple"]

#INITIAL VALUES
x1 = 100
y1 = 400

xSpeed1 = 11
ySpeed1 = -2
diameter1 = 100

x3 = 400
y3 = 500

xSpeed2 = -3
ySpeed2 = 2
diameter2 = 200

color1 = "red"
color2 = "blue"
#ANIMATION LOOP
while True:
    #Circle 1
    x1 = x1 + xSpeed1  
    y1 = y1 + ySpeed1
    
    x2 = x1 + diameter1
    y2 = y1 + diameter1
    #Circle 2
    x3 = x3 + xSpeed2  
    y3 = y3 + ySpeed2
    
    x4 = x3 + diameter2
    y4 = y3 + diameter2

    center1 = [(x1+x2)/2, (y1+y2)/2]
    center2 = [(x3+x4)/2, (y3+y4)/2]

    #Circle 1
    if x2 >= 800:
        xSpeed1 = -1 * xSpeed1
    elif x1 < 0:
        xSpeed1 = -1 * xSpeed1

    if y2 >= 800:
        ySpeed1 = -1 * ySpeed1
    elif y1 < 0:
        ySpeed1 = -1 * ySpeed1
    #Circle 2
    if x4 >= 800:
        xSpeed2 = -1 * xSpeed2
    elif x3 < 0:
        xSpeed2 = -1 * xSpeed2

    if y4 >= 800:
        ySpeed2 = -1 * ySpeed2
    elif y3 < 0:
        ySpeed2 = -1 * ySpeed2
        
    ball1 = screen.create_oval(  x1,  y1,  x2,  y2,  fill=color1) 
    ball2 = screen.create_oval(  x3,  y3,  x4,  y4,  fill=color2)  
    #Update, sleep, delete
    screen.update()
    sleep(0.03)
    screen.delete( ball1,ball2 )

    d = sqrt((center1[0]-center2[0])**2+(center1[1]-center2[1])**2)
    if d < diameter1/2 + diameter2/2:
        xSpeed1 = -1 * xSpeed1
        ySpeed1 = -1 * ySpeed1
        xSpeed2 = -1 * xSpeed2
        ySpeed2 = -1 * ySpeed2

