from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=900, background="white")

global logoGIF

startX = 80
startY = 900

recycleLogoGIF = PhotoImage(file="imgs/recycling logo.gif")


#wheel1 = screen.create_rectangle(startX-55-8, startY-15, startX-55+8, startY+5, fill="black")
#wheel2 = screen.create_rectangle(startX+55-8, startY-15, startX+55+8, startY+5, fill="black")
#body = screen.create_polygon(startX-70, startY-160, startX+70, startY-160, startX+55, startY, startX-55, startY, fill="green", outline="black")
#lid = screen.create_polygon(startX-70, startY-160, startX+70, startY-160, startX+60, startY-160-10, startX-60, startY-160-10, fill="green", outline="black")
#label = screen.create_text(startX, startY-50, text="PLASTIC", font = "Roboto 16", anchor=CENTER, fill="white")
#logo = screen.create_image(startX, startY-100, anchor="center", image=logoGIF)
#lidOpen = screen.create_polygon(startX-70, startY-160, startX-70, startY-160-140, startX-70-10, startY-160-140+10, startX-70-10, startY-160-140-10+130, fill="green", outline="black")

wheel1 = screen.create_rectangle(startX-63, startY-15, startX-47, startY+5, fill="black")
wheel2 = screen.create_rectangle(startX+47, startY-15, startX+63, startY+5, fill="black")
body = screen.create_polygon(startX-70, startY-160, startX+70, startY-160, startX+55, startY, startX-55, startY, fill="green", outline="black")
lid = screen.create_polygon(startX-70, startY-160, startX+70, startY-160, startX+60, startY-170, startX-60, startY-170, fill="green", outline="black")
label = screen.create_text(startX, startY-50, text="ORGANIC", font = "Roboto 16", anchor=CENTER, fill="white")
logo = screen.create_image(startX, startY-100, anchor="center", image=recycleLogoGIF)
lidOpen = screen.create_polygon(startX-70, startY-160, startX-70, startY-300, startX-80, startY-290, startX-80, startY-180, fill="green", outline="black")

screen.pack()
screen.mainloop()