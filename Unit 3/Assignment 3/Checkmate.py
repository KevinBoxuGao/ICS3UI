from tkinter import *

tk = Tk()
screen = Canvas(tk, width=1600, height=800, background="white")
screen.pack()


def create_ring(top,center, width, height):
    screen.create_polygon(center-width/2, top, center+width/2, top, center+width/2, top+height, center-width/2, top+height, fill=color, outline=outline, smooth=True)

#drawing individual parts
def create_crown(top,center,height1, height2, width):
    screen.create_arc(center-width/3, top, center+width/3, top + 2*height1, start=0, extent=180, fill=color, outline=outline)
    screen.create_oval(center-width/8, top-width/6, center+width/8, top, fill=color, outline=outline)
    screen.create_polygon(center-width/2, top+height1, center+width/2, top+height1, center+width/3, top+height1+height2, center-width/3, top+height1+height2, fill=color, outline=outline)

    screen.create_polygon(center-width/2, top+height1, center+width/2 ,top+height1, center+width/2.4, top+height1 - 10, center-width/2.4 ,top+height1 - 10, fill=color, outline=outline)

def create_cross(top, center, height, width):
    screen.create_rectangle(center-width/2, top, center+width/2, top+height, fill=color, outline=outline)
    screen.create_rectangle(center-40, top+40+width/2, center+40, top+40-width/2, fill=color, outline=outline)
    screen.create_rectangle(center-width/2, top+30, center+width/2, top+50, fill=color, outline=color)

def create_pedestal(top, center, height, width):   
    screen.create_rectangle(center-10, top, center+10, top+height, fill=color, outline=outline)
    screen.create_oval(center-width/2, top, center+width/2, top+height, fill=color, outline=outline)

def create_head(top, center, height1, height2, width):
    screen.create_arc(center-width/2, top, center+width/2, top + 2*height1, start=0, extent=180, fill=color, outline=outline)
    screen.create_polygon(center-width/2, top+height1, center+width/2, top+height1, center+width/3, top+height1+height2, center-width/3, top+height1+height2, fill=color, outline=outline)

def create_neck(top, center, height, ringwidth, neckwidth):
    create_ring(top, center, ringwidth, height/6)
    screen.create_rectangle(center-neckwidth/2, top+height/6, center+neckwidth/2, top+2*height/6, fill=color, outline=outline)
    create_ring(top+2*height/6, center, ringwidth, height/6)
    screen.create_rectangle(center-neckwidth/2, top+3*height/6, center+neckwidth/2, top+4*height/6, fill=color, outline=outline)
    create_ring(top+4*height/6, center, ringwidth, 2*height/6)

def create_body(top,center,height):
    width = height/3
    screen.create_rectangle(center-width/2, top, center+width/2, top+(3/4)*height, fill=color, outline=outline)
    screen.create_polygon(center-width/2, top+(3/4)*height, center+width/2, top+(3/4)*height, center+width, top+height, center-width, top+height, fill=color, outline=outline)

def create_base(top,center,width,height):
    screen.create_rectangle(center-width/2, top, center+width/2, top+height, fill=color, outline=outline)

#background and ground
screen.create_rectangle(0,500,1600,800, fill="white", outline="white")
screen.create_rectangle(0,0,1600,500, fill="white", outline="white")
screen.create_line(0,500,1600,500)

i=0
j=0
for x in range(0,1600,200):
    i=i+1 
    for y in range(500,800,100):
        j=j+1
        if j % 2 == 1:
            color = "#2e0000"
        else:
            color = "#c8bc90"
        screen.create_rectangle(x,y, x+200, y+100, fill=color)


#create chess pieces


#white king
center = 1100
top = 50

color = "white"
outline= "black"

create_cross(top, center, 80, 20)
create_pedestal(top + 80, center, 20, 35)
create_head(top + 100, center, 10, 80, 120)
create_neck(top + 190, center, 50, 105, 80)
create_body(top+ 240, center, 240)
create_base(top+480, center, 160, 30)


#white queen
center = 1300
top = 150


create_crown(top+70, center, 40, 80, 120)
create_neck(top + 190, center, 50, 105, 80)
create_body(top+ 240, center, 240)
create_base(top+480, center, 160, 30)



#black king
center = 1500
top = 150
color = "black"
outline="white"

create_cross(top, center, 80, 20)
create_pedestal(top + 80, center, 20, 35)
create_head(top + 100, center, 10, 80, 120)
create_neck(top + 190, center, 50, 105, 80)
create_body(top+ 240, center, 240)
create_base(top+480, center, 160, 30)

screen.mainloop()