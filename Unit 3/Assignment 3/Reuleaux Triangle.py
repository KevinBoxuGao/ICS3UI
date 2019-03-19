from tkinter import *
from math import *


tk = Tk()
screen = Canvas(tk, width=800, height=800, background="black")
screen.pack()

x1 = 200
y1 = 200
x2 = x1 + 600
y2 = y1 + 600

hDistance = sqrt(3)*150

screen.create_arc(x1,y1,x2,y2, fill="red", start=150, extent=60, outline="red")
screen.create_arc(x1-hDistance,y1+150,x2-hDistance,y2+150, fill="red", start=30, extent=60, outline="red")
screen.create_arc(x1-hDistance,y1-150,x2-hDistance,y2-150, fill="red", start=270, extent=60, outline="red")

