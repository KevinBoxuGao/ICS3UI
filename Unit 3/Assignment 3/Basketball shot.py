from tkinter import *
from time import *
from math import *

tk = Tk()
screen = Canvas(tk, width=800, height=800, background="lightblue")
screen.pack()

#background
screen.create_rectangle(0,700,1000,1000, fill="grey", outline="grey")

screen.create_oval(700,100, 700+50,100+50, fill="yellow")

#ball
ballWidth = 40

xStart = 200
xSpeed = 6

yStart = 400
ySpeed = 14

gravityStrength = 0.4     
initialUpwardSpeedAfterImpact = sqrt( 2 * gravityStrength * (0-ballWidth) + ySpeed**2 )  #A formula from physics

x1 = xStart
x2 = x1 + ballWidth
y1 = yStart
y2 = y1 + ballWidth

#net
i = (ySpeed+ySpeed)/gravityStrength
netx = xSpeed*i + xStart
screen.create_rectangle(netx-ballWidth,yStart, netx+ballWidth+5,yStart+10, fill="grey")

#backboard
screen.create_rectangle(netx+ballWidth+5, yStart-80, netx+ballWidth+20+5, yStart+10, fill="white")

#post
screen.create_rectangle(netx+ballWidth+5, yStart+10, netx+ballWidth+20+5, 800-40, fill="red")

#person jump
xStartP = 100
yStartP = 700

legheight = 100
legwidth = 40

bodyheight = 80
bodywidth = 40

headwidth = 40







for i in range(1,126):
    yStartP = (gravityStrength/2) * i**2 - 4 * i + yStartP
    person = [[xStartP, yStartP],[xStartP+legwidth,yStartP-legheight], [xStartP,yStartP-legheight],[xStartP+bodywidth, yStartP-legheight-bodyheight], [xStartP,yStartP-legheight-bodyheight], [xStartP+headwidth, yStartP-legheight-bodyheight-headwidth], [xStartP+(bodywidth/2),yStartP-legheight-bodyheight], [xStartP+(bodywidth/2),yStartP-legheight-bodyheight+20], [xStartP+(bodywidth/2)+bodyheight,yStartP-legheight-bodyheight-10], [xStartP+(bodywidth/2)+bodyheight,yStartP-legheight-bodyheight+20-10]]

    leg = screen.create_rectangle(person[0], person[1], fill="blue")
    body = screen.create_rectangle(person[2], person[3], fill="red")
    head = screen.create_oval(person[4], person[5],fill="tan")
    arm = screen.create_polygon(person[6],person[7],person[9],person[8], fill="red")    
    ball1 = screen.create_oval(person[8][0], person[8][1]+ballWidth, person[8][0]+ballWidth, person[8][1], fill="orange") 

    screen.update()
    sleep(0.02)
    screen.delete(leg, body,head,arm, ball1)

    if person[8][1] + ballWidth <= yStart:
        break   


#initial ball arc
grounded = False

for i in range(1,126):
    x1 =  xSpeed*i + xStart
    y1 = (gravityStrength/2) * i**2 - ySpeed * i + yStart
    
    x2 = x1 + ballWidth
    y2 = y1 + ballWidth

    ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill="orange",  outline="black")

    if grounded == False:
        yStartP = (gravityStrength/2) * i**2 - 0.5 * i + yStartP
        person = [[xStartP, yStartP],[xStartP+legwidth,yStartP-legheight], [xStartP,yStartP-legheight],[xStartP+bodywidth, yStartP-legheight-bodyheight], [xStartP,yStartP-legheight-bodyheight], [xStartP+headwidth, yStartP-legheight-bodyheight-headwidth], [xStartP+(bodywidth/2),yStartP-legheight-bodyheight], [xStartP+(bodywidth/2),yStartP-legheight-bodyheight+20], [xStartP+(bodywidth/2)+bodyheight,yStartP-legheight-bodyheight-10], [xStartP+(bodywidth/2)+bodyheight,yStartP-legheight-bodyheight+20-10]]

        leg = screen.create_rectangle(person[0], person[1], fill="blue")
        body = screen.create_rectangle(person[2], person[3], fill="red")
        head = screen.create_oval(person[4], person[5],fill="tan")
        arm = screen.create_polygon(person[6],person[7],person[9],person[8], fill="red")    

        
        if yStartP >= 700:
            grounded = True

    screen.update()
    sleep(0.02)
        
    screen.delete(ball)
    
    if yStartP <= 700:
        screen.delete(leg, body, arm, head)
     

   

    if y1 > yStart:
        break

#ball falling down vertically after hit into net
for i in range(1,120):
    y1 = y1 + 10

    x2 = x1 + ballWidth
    y2 = y1 + ballWidth
    
    ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill="orange",  outline="black")
    
    screen.update()
    sleep(0.02)
    screen.delete(ball)


screen.mainloop()