from tkinter import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="white")
screen.pack()

x1 = 375
y1 = 375

x2 = 425
y2 = 425

for i in range(10):
    screen.create_rectangle(x1,y1,x2,y2,outline="red")
    x1 = x1-25
    y1 = y1-25
    x2 = x2+25
    y2 = y2+25

screen.update()
