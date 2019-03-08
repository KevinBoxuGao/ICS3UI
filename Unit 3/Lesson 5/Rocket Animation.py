from tkinter import *
from time import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="white")
screen.pack()

x1 = 0
x2 = x1 + 20
x3 = x1 + 300
y1 = 400
y2 = y1 + 80
y3 = (y1 + y2)/2

for f in range(500):
    box = screen.create_rectangle(x1,y1,x2,y2, fill="blue")
    nose = screen.create_polygon(x2,y1,x2,y2,x3,y3, fill="red")
    screen.update()
    sleep(0.03)
    screen.delete(box,nose)
    x1 = x1 + 15
    x2 = x1 + 200
    x3 = x1 + 300
