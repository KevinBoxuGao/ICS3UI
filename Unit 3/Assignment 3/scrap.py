from tkinter import *
from math import *

tk = Tk()
screen = Canvas(tk, width=800, height=800, background="white")
screen.pack()

#create grid
spacing = 50
for x in range(0, 1000, spacing): 
    screen.create_line(x, 25, x, 1000, fill="blue")
    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 1000, spacing):
    screen.create_line(25, y, 1000, y, fill="blue")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)

center = 400
top = 100

#cross
screen.create_rectangle(center-10, top, center+10, top+80, fill="red")
screen.create_rectangle(center-40, top+40+10, center+40, top+40-10, fill="red")

a = 60
b = 10
r = (a**2 + b**2)/(2*b)

#head
screen.create_oval(center-25, top+80, center+25, top+80+20, fill="red")
screen.create_arc(center-r, top+100, center+r, top + 100 + 2*r, start=0,extent=180, outline="red")

screen.create_polygon(center-60, top+110, center+60, top+110, center+40, top+190, center-40, top+190, fill="red")
#neck

#body

#base
