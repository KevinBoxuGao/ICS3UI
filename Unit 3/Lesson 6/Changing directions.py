from tkinter import *
from time import *
tk = Tk()
screen = Canvas(tk, width=800, height=800, background="yellow")
screen.pack()

#INITIAL VALUES
x1 = 100
y1 = 400

xSpeed = 11
ySpeed = -2
diameter = 100

#ANIMATION LOOP
while True: 
    x1 = x1 + xSpeed  
    y1 = y1 + ySpeed
    
    x2 = x1 + diameter
    y2 = y1 + diameter

    if x2 >= 800:
        xSpeed = -1 * xSpeed
    elif x1 < 0:
        xSpeed = -1 * xSpeed

    if y2 >= 800:
        ySpeed = -1 * ySpeed
    elif y1 < 0:
        ySpeed = -1 * ySpeed
    ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill="red") 

    #Update, sleep, delete
    screen.update()
    sleep(0.03)
    screen.delete( ball )
