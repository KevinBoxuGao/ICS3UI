from tkinter import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=600, background="black")
screen.pack()

for i in range(500):
    x = randint(0,600)
    y = randint(0,600)
    size = randint(1,3)
    screen.create_oval(x, y, x + size, y + size, fill="white")

screen.update()
screen.mainloop()