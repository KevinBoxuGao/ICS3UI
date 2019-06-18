from tkinter import *
from time import *
from random import *
tk = Tk()
screen = Canvas( tk, width=1400, height=800, background = "sky blue" )
screen.pack()

sky = screen.create_rectangle(0, 0, 1400, 600, outline="lightblue", fill="lightblue")
ground = screen.create_rectangle(0, 600, 1400, 800, outline="brown", fill="brown")
sun = screen.create_oval(100, 100, 200, 200, fill="yellow", outline="yellow")
for i in range(50):
    x = randint(200,450)
    y = randint(100,200)
    screen.create_oval(x,y,x+70,y+70, fill="white", outline="white")

cannon = screen.create_polygon(100, 600, 150, 600, 170, 570, 150, 550, fill="grey", outline="grey")
balloonDrawings = []
x = []
y= []
startingFrame = []
numBalloons = 40
numFrames = 500
r = 10
frameGap = numFrames//numBalloons

for i in range(numBalloons):
    x.append(0)
    y.append(0)
    balloonDrawings.append(0)
    startingFrame.append(i*frameGap)

for f in range(numFrames):
    for i in range(numBalloons):
        if f >= startingFrame[i]:
            t = f - startingFrame[i]
            x[i] = 9*t + 170
            y[i] = 0.1*t**2 - 12*t + 550
            balloonDrawings[i] = screen.create_oval(x[i]-r, y[i]-r, x[i]+r, y[i]+r, fill="red") 

    screen.update()
    sleep(0.03)
    for i in range(numBalloons):
        screen.delete(balloonDrawings[i])

screen.mainloop()