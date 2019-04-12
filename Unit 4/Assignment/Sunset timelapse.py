from tkinter import *
from time import *
from random import *

root = Tk()
screen = Canvas( root, width=800, height=800, background = "black" )
screen.pack()

#helper function that converts RGB to Hex
def convertRGB(r, g , b):
    return '#%02x%02x%02x' % (r, g, b)

#starting Values
#ground and sky
groundRGB = [124, 252, 0]
skyRGB = [0, 175, 255]

#clouds
cloudRGB = [255, 255, 255]

numClouds = 3
clouds = []
cloudXStart = [-130-800, 225-800, 600-800]
cloudYStart = [150, 110, 200]
cloudX = []
cloudY = []
cloudSize = []

for i in range(numClouds):
    blobX = []
    blobY = []
    cloudBlobs = []
    blobSize = []

    for j in range(50):
        blobX.append(randint(cloudXStart[i]-100, cloudXStart[i]+100))
        blobY.append(randint(cloudYStart[i]-50, cloudYStart[i]+50))
        blobSize.append(randint(30, 50))
        cloudBlobs.append(0)

    cloudX.append(blobX)
    cloudY.append(blobY)
    clouds.append(cloudBlobs)
    cloudSize.append(blobSize)

#stars
numStars = 500
constY = []
sizes = []
starRGB = [0, 0, 0]

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


#animation driver
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
        x.append(randint(0, 800))
        y.append(constY[i])
        stars.append(0)

    #day to night
    for f in range(255):
        #change ground and sky
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

        #draw clouds
        cloudRGB[0] = cloudRGB[0] - 1
        cloudRGB[1] = cloudRGB[1] - 1
        cloudRGB[2] = cloudRGB[2] - 1
        for i in range(numClouds):
            if cloudXStart[i] - 100 - 50 >= 800:
                cloudXStart[i] = -150
                for j in range(50):
                    cloudX[i][j] = cloudX[i][j] - 800 - 200 - 50 -50             
            
            cloudXStart[i] = cloudXStart[i] + 5
            for j in range(50):
                cloudX[i][j] = cloudX[i][j] + 5
                clouds[i][j] = screen.create_oval(cloudX[i][j] + cloudSize[i][j], cloudY[i][j] + cloudSize[i][j], cloudX[i][j] - cloudSize[i][j], cloudY[i][j] - cloudSize[i][j], fill=convertRGB(cloudRGB[0], cloudRGB[1], cloudRGB[2]), outline=convertRGB(cloudRGB[0], cloudRGB[1], cloudRGB[2]))

        screen.update()
        sleep(0.03)
        screen.delete(sky, ground)

        for i in range(numClouds):
            for j in range(50):
                screen.delete(clouds[i][j])
    
    #draw stars during night
    for f in range(350):
        #overlap ground
        groundColor = convertRGB(groundRGB[0],groundRGB[1],groundRGB[2])
        if groundRGB[0] > 0:
            groundRGB[0] = groundRGB[0] - 1
        if groundRGB[1] > 30:
            groundRGB[1] = groundRGB[1] - 1

        #draw stars 
        #fade stars in
        if f < 51 and starRGB[0] < 255:
            starRGB[0] = starRGB[0] +5
            starRGB[1] = starRGB[1] +5
            starRGB[2] = starRGB[2] +5

        #fade stars out
        if f >= 350 - 51 and starRGB[0] > 0:
            starRGB[0] = starRGB[0] -5
            starRGB[1] = starRGB[1] -5
            starRGB[2] = starRGB[2] -5

        for i in range(numStars):
            if x[i] - sizes[i] >= 800:
                x[i] = 0
            else:
                x[i] = x[i] + 4
            if x[i] >= 0:
                y[i] = (1/2500)*(x[i]-400)**2+constY[i] - 20 
        
            stars[i] = screen.create_oval(x[i] - sizes[i], y[i] - sizes[i], x[i] + sizes[i], y[i] + sizes[i], fill=convertRGB(starRGB[0], starRGB[1], starRGB[2]), outline=convertRGB(starRGB[0], starRGB[1], starRGB[2]))  

        ground = screen.create_rectangle(0, 600, 810, 810, fill=groundColor, outline=groundColor)

        screen.update()    
        sleep(0.03)
        screen.delete(ground)
        for i in range(numStars):
            screen.delete(stars[i])

    #reset star color
    starRGB[0] = 255
    starRGB[1] = 255
    starRGB[2] = 255
 
    #night to day
    for f in range(255):
        #set sky and ground color
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

        #draw setting with sun
        if f > 255 - ((600+2*radius)/sunSpeed):
            y1 = y1 - sunSpeed
            sun = screen.create_oval(x1-radius, y1-radius, x1+radius, y1+radius, fill="yellow", outline="yellow")
            ground = screen.create_rectangle(0, 600, 800, 800, fill=groundColor, outline=groundColor)
            
            #draw clouds
            cloudRGB[0] = cloudRGB[0] + 1
            cloudRGB[1] = cloudRGB[1] + 1
            cloudRGB[2] = cloudRGB[2] + 1
            for i in range(numClouds):
                if cloudXStart[i] - 100 - 50 >= 800:
                    cloudXStart[i] = -150
                    for j in range(50):
                        cloudX[i][j] = cloudX[i][j] - 800 - 200 - 50 -50             

                cloudXStart[i] = cloudXStart[i] + 5
                for j in range(50):
                    cloudX[i][j] = cloudX[i][j] + 5
                    clouds[i][j] = screen.create_oval(cloudX[i][j] + cloudSize[i][j], cloudY[i][j] + cloudSize[i][j], cloudX[i][j] - cloudSize[i][j], cloudY[i][j] - cloudSize[i][j], fill=convertRGB(cloudRGB[0], cloudRGB[1], cloudRGB[2]), outline=convertRGB(cloudRGB[0], cloudRGB[1], cloudRGB[2]))
            
            screen.update()
            sleep(0.03)
            screen.delete(ground, sky, sun)


            for i in range(numClouds):
                for j in range(50):
                    screen.delete(clouds[i][j])

        #draw setting without sun
        else:
            ground = screen.create_rectangle(0, 600, 800, 800, fill=groundColor, outline=groundColor)
            
            #draw clouds
            cloudRGB[0] = cloudRGB[0] + 1
            cloudRGB[1] = cloudRGB[1] + 1
            cloudRGB[2] = cloudRGB[2] + 1
            for i in range(numClouds):
                if cloudXStart[i] - 100 - 50 >= 800:
                    cloudXStart[i] = -150
                    for j in range(50):
                        cloudX[i][j] = cloudX[i][j] - 800 - 200 - 50 -50             

                cloudXStart[i] = cloudXStart[i] + 5
                for j in range(50):
                    cloudX[i][j] = cloudX[i][j] + 5
                    clouds[i][j] = screen.create_oval(cloudX[i][j] + cloudSize[i][j], cloudY[i][j] + cloudSize[i][j], cloudX[i][j] - cloudSize[i][j], cloudY[i][j] - cloudSize[i][j], fill=convertRGB(cloudRGB[0], cloudRGB[1], cloudRGB[2]), outline=convertRGB(cloudRGB[0], cloudRGB[1], cloudRGB[2]))
            
            screen.update()
            sleep(0.03)
            screen.delete(ground, sky)

            for i in range(numClouds):
                for j in range(50):
                    screen.delete(clouds[i][j])


        
