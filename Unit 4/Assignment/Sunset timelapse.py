from tkinter import *
from time import *
from random import *

root = Tk()
screen = Canvas( root, width=800, height=800, background = "black" )
screen.pack()

#helper function that converts RGB to Hex
def convertRGB(r, g , b):
    return '#%02x%02x%02x' % (r, g, b)

groundRGB = [124, 252, 0]
skyRGB = [0, 175, 255]

#constant y coordinates
numStars = 500
constY = []
sizes = []
for i in range(numStars):
    diceRoll = randint(1, 100)
    if diceRoll > 90:
        sizes.append(4)
    elif diceRoll > 75:
        sizes.append(3)
    elif diceRoll > 50:
        sizes.append(2)
    else:
        sizes.append(1)
    constY.append(randint(0-20, 600+20))

while True:
    #sun
    radius = 40
    x1 = 400 
    y1 = 600 + radius
    sunSpeed = 4 

    #stars
    
    x = []
    y = []
    stars = []

    for i in range(numStars):
        x.append(randint(0-800, 800-800))
        y.append(constY[i])
        stars.append(0)

    #day to night
    for f in range(255):
        groundColor = convertRGB(groundRGB[0],groundRGB[1],groundRGB[2])
        skyColor = convertRGB(skyRGB[0],skyRGB[1],skyRGB[2])

        if groundRGB[0] > 0:
            groundRGB[0] = groundRGB[0] - 1
        if groundRGB[1] > 30:
            groundRGB[1] = groundRGB[1] - 1

        if skyRGB[1] > 0:
            skyRGB[1] = skyRGB[1] - 1
        if skyRGB[2] > 0:
            skyRGB[2] = skyRGB[2] - 1

        sky = screen.create_rectangle(0, 0, 810, 600, fill=skyColor, outline=skyColor)
        ground = screen.create_rectangle(0, 600, 810, 810, fill=groundColor, outline=groundColor)

        screen.update()
        sleep(0.03)
        screen.delete(sky, ground)

    for f in range(500):
        #overlap ground
        groundColor = convertRGB(groundRGB[0],groundRGB[1],groundRGB[2])
        if groundRGB[0] > 0:
            groundRGB[0] = groundRGB[0] - 1
        if groundRGB[1] > 30:
            groundRGB[1] = groundRGB[1] - 1

        #draw stars when it is night
        for i in range(numStars):

            if x[i] - sizes[i] >= 800 and f < 300:
                x[i] = 0
            else:
                x[i] = x[i] + 4
            if x[i] >= 0:
                y[i] = (1/2500)*(x[i]-400)**2+constY[i] - 20 
        
            stars[i] = screen.create_oval(x[i] - sizes[i], y[i] - sizes[i], x[i] + sizes[i], y[i] + sizes[i], fill="white", outline="white")   

        ground = screen.create_rectangle(0, 600, 810, 810, fill=groundColor, outline=groundColor)

        screen.update()    
        sleep(0.03)
        screen.delete(ground)
        for i in range(numStars):
            screen.delete(stars[i])

            
    #night to day
    for f in range(255):
        groundColor = convertRGB(groundRGB[0],groundRGB[1],groundRGB[2])
        skyColor = convertRGB(skyRGB[0],skyRGB[1],skyRGB[2])

        if f > 128 and groundRGB[0]  < 124:
            groundRGB[0] = groundRGB[0] +1
        if groundRGB[1]  < 252:
            groundRGB[1] = groundRGB[1] +1

        if f > 80 and skyRGB[1]  < 175:
            skyRGB[1] = skyRGB[1] +1
        if skyRGB[2]  < 255:
            skyRGB[2] = skyRGB[2] +1

        sky = screen.create_rectangle(0,0, 800, 600, fill=skyColor, outline=skyColor)

        if f > 255 - ((600+2*radius)/sunSpeed):
            y1 = y1 - sunSpeed
            sun = screen.create_oval(x1-radius, y1-radius, x1+radius, y1+radius, fill="yellow", outline="yellow")
            ground = screen.create_rectangle(0, 600, 800, 800, fill=groundColor, outline=groundColor)
            screen.update()
            sleep(0.03)
            screen.delete(ground, sky, sun)
        else:
            ground = screen.create_rectangle(0, 600, 800, 800, fill=groundColor, outline=groundColor)
            screen.update()
            sleep(0.03)
            screen.delete(ground, sky)

        
