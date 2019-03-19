from tkinter import *
from random import *

tk = Tk()
screen = Canvas(tk, width=1000, height=1000, background="black")
screen.pack()

for y in range(100,900,100):
    for x in range(100,900,100):
        if(x + y)%200 == 100: 
            color = "blue"
        else:
            color = "yellow"

        for i in range(100):
            width = randint(2,5)
            x1 = randint(x,x+100-width)
            y1 = randint(y,y+100-width)
            screen.create_rectangle(x1, y1, x1+width, y1+width, fill=color, outline=color)

screen.update()