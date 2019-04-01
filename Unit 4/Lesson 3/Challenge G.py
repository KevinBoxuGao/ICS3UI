from tkinter import *
from time import *
tk = Tk()
s = Canvas(tk, width=1000, height=1000, background="black")
s.pack()


ringColors = ["red", "yellow", "dark orange", "green", "blue", "purple"]
speed = 5
gap = 6                       #The gap between rings
xRightWall = 800      #How far to the right a ring is allowed to go before it stops
ringNumber = 0     #Which ring is currently being animated

while xRightWall > 500:

    # Resets the starting position of the next ring to the centre of the screen
    x1 = 500
    y1 = 500
    
    x2 = 500
    y2 = 500

    # Animates one ring from the center to the current right-most boundary
    while x2 < xRightWall:

        ring = s.create_rectangle(x1, y1, x2, y2, outline = ringColors[ringNumber%6], width=1  )
        
        #Makes the next ring smaller 
        x1 = x1 - speed
        y1 = y1 - speed         
        x2 = x2 + speed
        y2 = y2 + speed
       
        s.update()
        sleep(0.001)

        
        #Avoids deleting the very last frame in each ring, so that the picture keeps building on itself
        if x2 < xRightWall:  
            s.delete(ring)
    #Reduces xRightWall so that the next ring is smaller than the last one
    xRightWall = x2 - gap
    ringNumber= ringNumber+1


# Just for fun...wipe the slate clean with a black hole
sleep(2)

x1 = 500
y1 = 500

x2 = 500
y2 = 500

speed = 3

while x2 < 2000: 

        x1 = x1 - speed
        y1 = y1 - speed
        x2 = x2 + speed
        y2 = y2 + speed

        disk = s.create_oval(x1, y1, x2, y2, fill = "black", outline="red", width=4)
        s.update()
        sleep(0.001)
        s.delete(disk)
        
 
        

