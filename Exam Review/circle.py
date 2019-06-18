
from tkinter import *
from math import *

root = Tk()
screen = Canvas(root, width=800, height=800, background="black")
screen.pack()

squares = 50
width = 40
radius = 300
deltaTheta = 2*pi/squares
angle = 0

xC = 400
yC = 400

for i in range(50):
    x = xC + radius * cos(angle)
    y = yC - radius * sin(angle)
    screen.create_rectangle(x-width/2,y-width/2,x+width/2,y+width/2,fill="red")
    angle = angle + deltaTheta

screen.mainloop()
