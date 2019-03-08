from tkinter import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="yellow")
screen.pack()

y2 = 0
for i in range(11):
    screen.create_line(400,400,800,y2, fill="red", width = 2)
    y2 = y2+80

x2 = 0
for i in range(11):
    screen.create_line(400,400,x2,800, fill="red", width = 2)
    x2 = x2+80

y1 = 0
for i in range(11):
    screen.create_line(400,400,0,y1, fill="red", width = 2)
    y1 = y1+80

x1 = 0
for i in range(11):
    screen.create_line(400,400,x1,0, fill="red", width = 2)
    x1 = x1+80
