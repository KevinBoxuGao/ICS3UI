from math import *
from tkinter import *

tk = Tk()
screen = Canvas(tk, width = 800, height=800,background="black")
screen.pack()

n = 100
r = 350

points = []
gap = 60

deltaTheta = 2*pi/n
theta = 0

for i in range(n):
    x = 400 +r*cos(theta)
    y = 400 - r*sin(theta)

    points.append([x,y])
    
    screen.create_oval(x-2,y-2,x+2,y+2, fill="white")
    theta = theta + deltaTheta

for i in range(n):
    secondPoint = (i+gap)%n
    screen.create_line(points[i][0], points[i][1], points[secondPoint][0], points[secondPoint][1], fill="white")

screen.mainloop()
