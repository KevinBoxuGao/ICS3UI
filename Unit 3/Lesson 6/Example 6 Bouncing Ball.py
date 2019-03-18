########################################
# Purpose: To show how to incorporate gravity into your animations
# Programmer:  Mr. Schattman
# Last modified:  May 6, 2017
########################################

from tkinter import *
from time import *
from math import *
tk = Tk()
screen = Canvas(tk, width=1000,height=800, background="green")
screen.pack()


#PARAMETERS
yGround = 300
ballWidth = 10
xStart = 100
xSpeed = 0.001                               #Try changing this
ySpeed = 1                              #Try changing this
gravityStrength = 0.2             #Try changing this
heightAboveGround = 300  #Try changing this


#CALCULATED VALUES - DON'T CHANGE THESE
initialUpwardSpeedAfterImpact = sqrt( 2 * gravityStrength * (heightAboveGround-ballWidth) + ySpeed**2 )  #A formula from physics
yStart = yGround - heightAboveGround
x1 = xStart
x2 = x1 + ballWidth
y1 = yStart
y2 = y1 + ballWidth
t = 0  #time in seconds.  This gets set back to 0 every time the ball hits the ground
f = 0  #Frame counter.  This grows forever.


#BACKGROUND SCENERY
ground = screen.create_line(0, yGround, 1000, yGround, fill="black", width=10)
cliff = screen.create_rectangle(0,yStart+ballWidth, xStart+ballWidth, yStart+ballWidth, fill="black")
ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill="red",  outline="black")
screen.update()
sleep(2)
screen.delete(ball)


#ANIMATION LOOP

while x1 <= 1000: #Animate until the ball leaves the screen
    f = f + 1 
    t = t + 1 
    
    x1 =  xSpeed*f**2 + xStart
    y1 = (gravityStrength/2) * t**2 - ySpeed * t + yStart
    
    x2 = x1 + ballWidth
    y2 = y1 + ballWidth

    if y2 > yGround:   #if the bottom edge of the ball hits the ground...
        t = 0   #reset the clock
        yStart = yGround - ballWidth
        y1 = yStart
        y2 = y1 + ballWidth
        ySpeed = initialUpwardSpeedAfterImpact 

    ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill="red",  outline="black")

    screen.update()
    sleep(0.02)
    #screen.delete(ball)

