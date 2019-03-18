from tkinter import *
from time import *
from math import *

tk = Tk()
screen = Canvas(tk, width=600, height=600, background="black")
screen.pack()

colors = ["purple", "green", "blue", "red"]

#ring coordinates
ringx1 = 0
ringy1 = 0
ringx2 = 600
ringy2 = 600
#draw rings
for i in range(6):
    screen.create_oval(ringx1,ringy1,ringx2,ringy2, outline="white", width=2)
    ringx1 = ringx1 + (600/12)
    ringy1 = ringy1 + (600/12)
    ringx2 = ringx2 - (600/12)
    ringy2 = ringy2 - (600/12)


#initial circle values
x1 = 100
y1 = 100

xSpeed = -3
ySpeed = 2
diameter = 30

color = colors[0]

for frame in range(1000):
    x1 = x1 + xSpeed
    y1 = y1 + ySpeed
    
    x2 = x1 + diameter
    y2 = y1 + diameter

    #check for collision
    if x2 >= 600:
        xSpeed = -1 * xSpeed
    elif x1 < 0:
        xSpeed = -1 * xSpeed

    if y2 >= 600:
        ySpeed = -1 * ySpeed
    elif y1 < 0:
        ySpeed = -1 * ySpeed

    #check for color

    #center values
    circleCenter = [(x1+x2)/2, (y1+y2)/2]
    ringCenter = [300,300]

    #check for distance between center of screen and circle
    d = sqrt((x1+x2)/2- 300)**2+((y1+y2)/2 - 300)**2)

    
    ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill=color) 

    #Update, sleep, delete
    screen.update()
    sleep(0.01)
    screen.delete(ball)
