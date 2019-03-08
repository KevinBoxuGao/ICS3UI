from tkinter import *
from random import*
from time import*
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="skyblue")
screen.pack()

floor = screen.create_rectangle(0, 600, 800, 800, fill="chocolate4")
wall = screen.create_rectangle(0, 0, 800, 600, fill="blanched almond")
window = screen.create_rectangle(400, 250, 660, 400, fill="skyblue", outline="sienna2", width=9)

def distance(coordinate):
    return coordinate+1

#rug
x1 = 50
y1 = 650
x2 = x1 + 500
y2 = y1 + 100
for i in range(5):
    xchange = i*50
    ychange = i*10
    if i%2 == 0:
        screen.create_oval(x1+xchange, y1+ychange, x2-xchange ,y2-ychange, fill="red")
    else:    
        screen.create_oval(x1+xchange, y1+ychange, x2-xchange ,y2-ychange, fill="darkgreen")

x = [randint(409,651) for i in range(250)]
y = [randint(259,391) for i in range(250)]
s = [randint(1,3) for i in range(250)]


for j in range(50):
    for i in range(250):    
        screen.create_oval(x[i],y[i],x[i]+s[i],y[i]+s[i],fill="white",outline="white")
    screen.update()
    sleep(0.1)
    map(distance,y)
    
