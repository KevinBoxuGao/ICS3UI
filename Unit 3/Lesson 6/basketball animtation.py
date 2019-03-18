from tkinter import *
from time import *
from math import *
tk = Tk()
screen = Canvas(tk, width=1000,height=800, background="white")
screen.pack()

screen.create_rectangle(0,750,1000,1000, fill="green", outline="green")

#values
ballWidth = 20
xStart = 100
xSpeed = 6           
ySpeed = 14               
gravityStrength = 0.2             
initialUpwardSpeedAfterImpact = sqrt( 2 * gravityStrength * (0-ballWidth) + ySpeed**2 )  #A formula from physics
yStart = 750
x1 = xStart
x2 = x1 + ballWidth
y1 = yStart
y2 = y1 + ballWidth

for i in range(1,126):

    
    x1 =  xSpeed*i + xStart
    y1 = (gravityStrength/2) * i**2 - ySpeed * i + yStart
    
    x2 = x1 + ballWidth
    y2 = y1 + ballWidth

    ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill="orange",  outline="black")

    screen.update()
    sleep(0.02)
    #screen.delete(ball)
