from tkinter import *
from math import *

root = Tk()
screen = Canvas(root, width=800, height=600, background="white")
screen.pack()


y1 = 100
y2 = 500
xStart = 100
width = 50
gap = 150
balls = 5


for i in range(5):
    x = xStart+gap*i
    screen.create_oval(x-width, y1-width, x+width, y1+width, fill="blue")
    screen.create_oval(x-width, y2-width, x+width, y2+width, fill="red")

for i in range(5):
    x1 = xStart+gap*i
    for j in range(5):
        x2 = xStart + gap*j
        screen.create_line(x1, y1, x2, y2)


screen.mainloop()
