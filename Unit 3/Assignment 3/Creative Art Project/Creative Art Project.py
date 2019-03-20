from tkinter import *

#color reference
very_dark_grey = "#191919"


tk = Tk()
screen = Canvas(tk, width=1440, height=1024+50, background="white")
screen.pack()

#create grid
#spacing = 50
#for x in range(0, 1440, spacing): 
#    screen.create_line(x, 25, x, 1440, fill="blue")
#    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N)

#for y in range(0, 1024, spacing):
#    screen.create_line(25, y, 1000, y, fill="blue")
#    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)


screen.create_rectangle(3,3,1440,1024,width="3", outline = very_dark_grey)
screen.create_rectangle(3,1024,1440,1024+50, width="3", outline = very_dark_grey, fill=very_dark_grey)

screen.create_rectangle(6,6,1440-3,1024-3, width="10", outline="red")

#PhotoImage(file="dell_logo.png")

screen.mainloop()
