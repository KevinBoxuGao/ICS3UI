from tkinter import *
from time import *
from math import *

tk = Tk()
screen = Canvas(tk, width=800, height=800, background="black")
screen.pack()

#background
screen.create_rectangle(0,750,1000,1000, fill="green", outline="green")

#net
#screen.create_rectangle()
screen.create_rectangle(520, 400, 520+50, 400+10, fill="grey")

#ball
ballWidth = 40

xStart = 100
xSpeed = 6

yStart = 400
ySpeed = 14

gravityStrength = 0.4     
initialUpwardSpeedAfterImpact = sqrt( 2 * gravityStrength * (0-ballWidth) + ySpeed**2 )  #A formula from physics

x1 = xStart
x2 = x1 + ballWidth
y1 = yStart
y2 = y1 + ballWidth

#initial ball arc
for i in range(1,126):
    
    x1 =  xSpeed*i + xStart
    y1 = (gravityStrength/2) * i**2 - ySpeed * i + yStart
    
    x2 = x1 + ballWidth
    y2 = y1 + ballWidth

    ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill="orange",  outline="black")

    screen.update()
    sleep(0.02)
    screen.delete(ball)

    if y1 > yStart:
        print("yes")
        print(x1)
        break

#ball falling down vertically after hit into net
for i in range(1,120):
    y1 = y1 + 10

    x2 = x1 + ballWidth
    y2 = y1 + ballWidth
    
    ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill="orange",  outline="black")
    screen.update()
    sleep(0.02)
    screen.delete(ball)
