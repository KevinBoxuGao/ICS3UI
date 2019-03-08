from tkinter import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800,)
screen.pack()

screen.create_line(400,400,400,0, width=2)
screen.create_line(400,400,0,400, width=2)
screen.create_line(400,400,400,800, width=2)
screen.create_line(400,400,800,400, width=2)

y1 = 0
x2 = 440
for i in range(10):
    screen.create_line(400,y1,x2,400,width=2)
    y1 = y1 + 40
    x2 = x2 + 40

y1 = 0
x2 = 4400
for i in range(10):
    screen.create_line(400,y1,x2,400,width=2)
    y1 = y1 + 40
    x2 = x2 - 40

