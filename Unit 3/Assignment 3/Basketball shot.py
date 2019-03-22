from tkinter import *
from time import *
from math import *

tk = Tk()
screen = Canvas(tk, width=800, height=800, background="lightblue")
screen.pack()

#background
screen.create_rectangle(0,700,1000,1000, fill="grey", outline="grey")

#ball
ballWidth = 40

xStart = 200
xSpeed = 6

yStart = 400
ySpeed = 14

gravityStrength = 0.4     
initialUpwardSpeedAfterImpact = sqrt( 2 * gravityStrength * (0-ballWidth) + ySpeed**2 )  #A formula from physics

x1 = xStart
x2 = x1 + ballWidth
y1 = yStart
y2 = y1 + ballWidth

#net
i = (ySpeed+ySpeed)/gravityStrength
netx = xSpeed*i + xStart
screen.create_rectangle(netx-ballWidth,yStart, netx+ballWidth+5,yStart+10, fill="grey")

#backboard
screen.create_rectangle(netx+ballWidth+5, yStart-80, netx+ballWidth+20+5, yStart+10, fill="white")

#post
screen.create_rectangle(netx+ballWidth+5, yStart+10, netx+ballWidth+20+5, 800-40, fill="red")

#person jump
#for i in range():

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
