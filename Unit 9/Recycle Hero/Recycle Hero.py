from tkinter import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=900, background="#e6e6e6")


#====== Data Models For Objects ======#
# object for a piece of trash item
class Trash:
    # set trash object variables on initialization
    def __init__(self, x, y, width, height, category, trashGIF):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.category = category
        self.trashGIF = trashGIF

        self.clicked = False


    def reset(self):  # Method, reset trash object variables, giving the illusion that a new trash item is created
        self.category = choice(trashCategory)  #chooses random trash category
        categoryIndex = trashCategory.index(self.category)
        self.trashGIF = choice(allTrashItemGIFS[categoryIndex])
        # creates temporary object to store values of gif
        item = trashItemGIF(self.category)
        self.trashGIF = item.gif
        self.width = item.dimensions[0]
        self.height = item.dimensions[1]
        self.x = randint(0+(self.width//2), 600-(self.width//2))
        self.y = randint(-900+(self.height//2), 0-(self.height//2))


    def lostLife(self):  # Method, add an xDrawing at the location of the trash item, indicating a lost life
        global lives
        lives = lives - 1
        # add xDrawing in place of trash that wasn't placed in the correct bin in time
        xDrawings.append(xDrawing(self.x, self.y))


    def update(self):  # Method, set object location
        if self.clicked == False:
            self.y = self.y + ySpeed  # increases position of trash
            # checks if piece of trash has exceeded limit and is not clicked on
            if self.y+(self.height//2) > 900:
                self.lostLife()
                self.reset()

# object containing trash item gif information
class trashItemGIF:
    def __init__(self, category):
        self.category = category
        # gets the index of the category so that we can access the correct array of gifs
        categoryIndex = trashCategory.index(category)
        self.gif = choice(allTrashItemGIFS[categoryIndex])
        # gets the index for the specific trash item in the category array so that we can access it's dimensions
        trashGIFIndex = allTrashItemGIFS[categoryIndex].index(self.gif)
        self.dimensions = trashItemDimensions[categoryIndex][trashGIFIndex]

# object for X drawing
class xDrawing:
    def __init__(self, x, y):
        width = 10
        cross1 = screen.create_line(x+width, y+width, x-width, y-width, width="3", fill="red")
        cross2 = screen.create_line(x+width, y-width, x-width, y+width, width="3", fill="red")

        self.drawing = [cross1, cross2]
        self.time = 20  # time for how many frames the image will appear for


#====== Setting Up Values ======#
def importImages():
    global paperItemGIF, organicItemGIF, glassItemGIF, plasticItemGIF, allTrashItemGIFS, recycleLogoGIF
    global introScreenGIF, instructionsScreenGIF, difficultyScreenGIF, loadingScreenGIF, gameOverScreenGIF
    #constants that aren't images but are details about them 
    global trashCategory, trashItemDimensions, trashBinRegions

    # arrays of trash item gifs in their respective category
    paperItemGIF = [PhotoImage(file="imgs/paper/paper1.gif"), PhotoImage(file="imgs/paper/paper2.gif"), PhotoImage(file="imgs/paper/paper3.gif")]
    organicItemGIF = [PhotoImage(file="imgs/organic/organic1.gif"), PhotoImage(file="imgs/organic/organic2.gif"), PhotoImage(file="imgs/organic/organic3.gif")]
    glassItemGIF = [PhotoImage(file="imgs/glass/glass1.gif"), PhotoImage(file="imgs/glass/glass2.gif"), PhotoImage(file="imgs/glass/glass3.gif")]
    plasticItemGIF = [PhotoImage(file="imgs/plastic/plastic1.gif"), PhotoImage(file="imgs/plastic/plastic2.gif"), PhotoImage(file="imgs/plastic/plastic3.gif")]
    # collection of all trash item images
    allTrashItemGIFS = [paperItemGIF, organicItemGIF, glassItemGIF, plasticItemGIF]

    recycleLogoGIF = PhotoImage(file="imgs/recycling logo.gif")

    # images for game screens
    introScreenGIF = PhotoImage(file="imgs/gameScreens/intro.gif")
    instructionsScreenGIF = PhotoImage(file="imgs/gameScreens/instructions.gif")
    difficultyScreenGIF = PhotoImage(file="imgs/gameScreens/difficulty.gif")
    loadingScreenGIF = PhotoImage(file="imgs/gameScreens/loading.gif")
    gameOverScreenGIF = PhotoImage(file="imgs/gameScreens/gameOver.gif")

    # list containing all possible categorys of trash
    trashCategory = ['paper', 'organic', 'glass', 'plastic']
    # multi-dimensional array that stores the fixed sizes of the gifs, has heirarchy of [category of item][item number][dimensions for each item]
    trashItemDimensions = [[[75, 76], [87, 64], [42, 60]], [[35, 42], [35, 42], [50, 92]], [[23, 46], [30, 45], [50, 72]], [[35, 105], [60, 80], [60, 55]]]
    # array that stores range of valid x coordinates of each garbage bin
    trashBinRegions = [[0, 150], [150, 300], [300, 450], [450, 600]]


def setInitialValues():
    global score, lives, piecesOfTrash, ySpeed, difficulty
    global clickedItemNumber, hoveredBin, escPressed
    global xDrawings, lidOpen
    global trashItems, trashImage 

    score = 0
    lives = 3

    #set our variables dependent on gamemode
    if difficulty == "easy":
        piecesOfTrash = 6
        ySpeed = 2
    elif difficulty == "medium":
        piecesOfTrash = 8
        ySpeed = 3
    else: #hard mode
        piecesOfTrash = 10
        ySpeed = 4

    # index used to identify which trash object is clicked(will be None when there aren't any)
    clickedItemNumber = 'None'
    # identify which garbage bin is hovered on by the mouse when holding an item
    hoveredBin = 'None'
    escPressed = False

    xDrawings = []  #array of all drawings of X's that indicate a lost life
    lidOpen = 0 #our drawing for the open lid of a hovered recycling bin

    trashItems = []  #stores out trash item objects with information
    trashImage = [0]*piecesOfTrash #stores the image objects for each trash item

#====== Functions For Trash Items ======#
# initializes trash objects and their values at the start of the game
def createTrash():
    for i in range(piecesOfTrash):
        category = choice(trashCategory)  # chooses random trash category
        # creates temporary drawing object so that we can access it's details
        itemDrawing = trashItemGIF(category)

        trashGIF = itemDrawing.gif
        width = itemDrawing.dimensions[0]
        height = itemDrawing.dimensions[1]

        # we make sure that the object generated is always on screen by taking into account the width of the object
        x = randint(0+(width//2), 600-(width//2))
        # we make sure that the object generated is always on screen by taking into account the height of the object
        y = randint(-900+(height//2), 0-(height//2))

        # adds a trash object with our calculated values to our trash item list
        trashItems.append(Trash(x, y, width, height, category, trashGIF))


#draws each piece of trash to the screen
def drawTrash():
    for i in range(piecesOfTrash):  #assign each trashImage according to trash object values
        trashImage[i] = screen.create_image(trashItems[i].x, trashItems[i].y, anchor="center", image=trashItems[i].trashGIF)


#deletes each piece of trash on the screen
def deleteTrash():
    for i in range(piecesOfTrash):
        screen.delete(trashImage[i])


#calls update method of each trash object to update values
def updateTrash():
    for i in range(piecesOfTrash):
        trashItems[i].update()


#====== Background ======#
def drawBackground():
    #draw bricks for the background
    for y in range(0, 820, 20): #goes row by row
        if (y/20) % 2 == 0: #check if row is even so that we can offset the bricks
            start = -30 
        else: #even row
            start = 0
        for x in range(start, 600, 60): #draw every brick in the row
            screen.create_rectangle(x, y, x+60, y+20, outline="#BFBFBF")

    #draw the ground
    screen.create_rectangle(0,820, 600, 900, fill="grey", outline="grey")


def drawTrashBins():
    global trashBinLids

    #paper bin
    wheel1 = screen.create_rectangle(17, 885, 33, 905, fill="black")
    wheel2 = screen.create_rectangle(127, 885, 143, 905, fill="black")
    body = screen.create_polygon(10, 740, 150, 740, 135, 900, 25, 900, fill="#DDDD00", outline="black")
    paperBinLid = screen.create_polygon(10, 740, 150, 740, 140, 730, 20, 730, fill="#DDDD00", outline="black")
    label = screen.create_text(80, 850, text="PAPER", font="Roboto 16", anchor=CENTER, fill="white")
    logo = screen.create_image(80, 800, anchor="center", image=recycleLogoGIF)
    
    #organic bin
    wheel1 = screen.create_rectangle(167, 885, 183, 905, fill="black")
    wheel2 = screen.create_rectangle(277, 885, 293, 905, fill="black")
    body = screen.create_polygon(160, 740, 300, 740, 285, 900, 175, 900, fill="#00CC00", outline="black")
    organicBinLid = screen.create_polygon(160, 740, 300, 740, 290, 730, 170, 730, fill="#00CC00", outline="black")
    label = screen.create_text(230, 850, text="ORGANIC", font="Roboto 16", anchor=CENTER, fill="white")
    logo = screen.create_image(230, 800, anchor="center", image=recycleLogoGIF)
    
    #glass bin
    wheel1 = screen.create_rectangle(317, 885, 333, 905, fill="black")
    wheel2 = screen.create_rectangle(427, 885, 443, 905, fill="black")
    body = screen.create_polygon(310, 740, 450, 740, 435, 900, 325, 900, fill="#0066CC", outline="black")
    glassBinLid = screen.create_polygon(310, 740, 450, 740, 440, 730, 320, 730, fill="#0066CC", outline="black")
    label = screen.create_text(380, 850, text="GLASS", font="Roboto 16", anchor=CENTER, fill="white")
    logo = screen.create_image(380, 800, anchor="center", image=recycleLogoGIF)

    #plastic bin
    wheel1 = screen.create_rectangle(467, 885, 483, 905, fill="black")
    wheel2 = screen.create_rectangle(577, 885, 593, 905, fill="black")
    body = screen.create_polygon(460, 740, 600, 740, 585, 900, 475, 900, fill="#CC0000", outline="black")
    plasticBinLid = screen.create_polygon(460, 740, 600, 740, 590, 730, 470, 730, fill="#CC0000", outline="black")
    label = screen.create_text(530, 850, text="PLASTIC", font="Roboto 16", anchor=CENTER, fill="white")
    logo = screen.create_image(530, 800, anchor="center", image=recycleLogoGIF)

    trashBinLids = [paperBinLid, organicBinLid, glassBinLid, plasticBinLid]


def updateStatistics():
    global scoreDisplay, livesDisplay
    scoreMessage = "Score: " + str(score)
    livesMessage = "Lives: " + str(lives)

    scoreDisplay = screen.create_text(100, 36, text=scoreMessage, font="Times 36", anchor=CENTER, fill="black")
    livesDisplay = screen.create_text(500, 36, text=livesMessage, font="Times 36", anchor=CENTER, fill="black")

#====== Functions Called For Our Animation Loop ======#
#draw all of our graphics
def drawObjects():
    drawTrash()
    updateStatistics()


#delete our drawings so they can be redrawn
def deleteObjects():
    deleteTrash()
    screen.delete(scoreDisplay)
    screen.delete(livesDisplay)
    for i in xDrawings:  # check if timers of x drawings is up
        if i.time == 0:  # if the timer is up
            # remove cross1 of the x from the screen
            screen.delete(i.drawing[0])
            # remove cross2 of the x from the screen
            screen.delete(i.drawing[1])
            xDrawings.remove(i)  # delete the xDrawing object


#update positions of all of our objects
def updateObjects():
    updateTrash()
    for i in xDrawings:  #updates the timer for each xDrawing
        i.time -= 1

#====== KeyBind Handlers======#
# gets called when user clicks mouse
def mouseClickHandler(event):
    global xMouse, yMouse, mouseDown, gameMode, clickedItemNumber

    xMouse = event.x
    yMouse = event.y

    if gameMode == "intro":
        #detects if mouse clicked a button
        if 125 <= xMouse <= 475: #checks if mouse click is in correct x since both buttons have the same x region
            if 450 <= yMouse < 525: #clicked play button
                gameMode = "difficulty"
                drawDifficultyScreen()
                screen.delete(introScreen)
            elif 575 <= yMouse <= 650: #clicked instructions button
                gameMode = "instructions" #instructions
                drawInstructionsScreen()
                screen.delete(introScreen)

    elif gameMode == "instructions":
        if 20 <= yMouse <= 80 and 20 <= xMouse <= 220: #checks if you clicked the back button
            gameMode = "intro"
            drawIntroScreen()
            screen.delete(instructionsScreen)

    elif gameMode == "difficulty":
        global difficulty
        if 20 <= yMouse <= 80 and 20 <= xMouse <= 220: #checks if you clicked the back button
            gameMode = "intro"
            drawIntroScreen()
            screen.delete(difficultyScreen)

        #checks if your mouse clicked one of the difficulties 
        elif 150 <= xMouse <= 450: 
            #checks x values of difficulty buttons to see which one you clicked
            if 200 <= yMouse <= 275: #clicked on easy mode
                difficulty = "easy"
                screen.delete(difficultyScreen)
                runGame()
            elif 400 <= yMouse <= 475: #clicked on medium mode
                difficulty = "medium"
                screen.delete(difficultyScreen)
                runGame()
            elif 600 <= yMouse <= 675: #clicked on hard mode
                difficulty = "hard"
                screen.delete(difficultyScreen)
                runGame()

    elif gameMode == "play":
        mouseDown = True
        # checks if you clicked on a trash item
        for i in range(piecesOfTrash-1, -1, -1): #loop backwards through images so that image drawn on top is clicked if there is overlap
            item = trashItems[i]
            if mouseInsideImage(item.x, item.y, item.width, item.height) == True:
                item.clicked = True #records the index of our object so that we can set it's clicked value as false later once it is dropped
                clickedItemNumber = i
                break #make sure once we find one object that is valid to be clicked, we don't move another object as well

    elif gameMode == "game over":
        #checked if you clicked any of the buttons
        if 150 <= xMouse <= 450 and 550 <= yMouse <= 750: #clicked the play again button
            gameMode = "play"
            screen.delete(gameOverScreen[0])
            screen.delete(gameOverScreen[0])
            runGame()
        if 175 <= xMouse <= 425 and 800 <= yMouse <= 900: #clicked the home button that returns you to the intro
            gameMode = "intro"
            drawIntroScreen()
            screen.delete(gameOverScreen[0])
            screen.delete(gameOverScreen[0])


# gets called when mouse is moving and checks if mouse is clicked
def mouseMotionHandler(event):
    global xMouse, yMouse, mouseDown, hoveredBin

    global lidOpen

    xMouse = event.x
    yMouse = event.y

    if gameMode == "play":
        # let the trash follow the mouse if there is a valid clicked item as well as if the mouse is clicked
        if mouseDown == True and clickedItemNumber != 'None': 
            #makes it so clicked item is following mouse
            trashItems[clickedItemNumber].x = xMouse
            trashItems[clickedItemNumber].y = yMouse

            #animate opened lid when hovering over trash bin with item ready to be dropped
            if yMouse+(trashItems[clickedItemNumber].height//2) > 700: #check if y position of mouse is over a trash bin
                for i in range(4): #loop through our trashBinRegions to see which one we are hovering over
                    if trashBinRegions[i][0] <= xMouse and trashBinRegions[i][1] >= xMouse: #if the x position of the mouse is in the trash bin's region
                        
                        if i == hoveredBin: #don't do anything if we are still hovering over the same trash bin
                            break
                        else:
                            if hoveredBin != 'None': #we must delete the previous open lid and draw the closed lid if there was a previous hoveredBin
                                screen.delete(lidOpen)
                                #we assign the lid drawing of bin that is not hovered over anymore so that we can redraw it back to the screen
                                if hoveredBin == 0: #if we are hovering the paper bin
                                    trashBinLids[hoveredBin] = screen.create_polygon(10, 740, 150, 740, 140, 730, 20, 730, fill="#DDDD00", outline="black")
                                elif hoveredBin == 1: #if we are hovering the organic bin
                                    trashBinLids[hoveredBin] = screen.create_polygon(160, 740, 300, 740, 290, 730, 170, 730, fill="#00CC00", outline="black")
                                elif hoveredBin == 2: #if we are hovering the glass bin
                                    trashBinLids[hoveredBin] = screen.create_polygon(310, 740, 450, 740, 440, 730, 320, 730, fill="#0066CC", outline="black")
                                else: #if we are hovering the plastic bin
                                    trashBinLids[hoveredBin] = screen.create_polygon(460, 740, 600, 740, 590, 730, 470, 730, fill="#CC0000", outline="black")

                            hoveredBin = i
                            screen.delete(trashBinLids[hoveredBin])
                            if hoveredBin == 0:
                                lidOpen = screen.create_polygon(10, 740, 10, 600, 0, 610, 0, 720, fill="yellow", outline="black")    
                            elif hoveredBin == 1:
                                lidOpen = screen.create_polygon(160, 740, 160, 600, 150, 610, 150, 720, fill="green", outline="black")
                            elif hoveredBin == 2:
                                lidOpen = screen.create_polygon(310, 740, 310, 600, 300, 610, 300, 720, fill="blue", outline="black")
                            else:
                                lidOpen = screen.create_polygon(460, 740, 460, 600, 450, 610, 450, 720, fill="red", outline="black")

            else:
                #we only need to delete the open lid and redraw the closed lid
                if hoveredBin != 'None': #if we are not hovering over a trash bin anymore
                    screen.delete(lidOpen)
                    #we assign the lid drawing of bin that is not hovered over anymore so that we can redraw it back to the screen
                    if hoveredBin == 0: #if we are hovering the paper bin
                        trashBinLids[hoveredBin] = screen.create_polygon(10, 740, 150, 740, 140, 730, 20, 730, fill="#DDDD00", outline="black")
                    elif hoveredBin == 1: #if we are hovering the organic bin
                        trashBinLids[hoveredBin] = screen.create_polygon(160, 740, 300, 740, 290, 730, 170, 730, fill="#00CC00", outline="black")
                    elif hoveredBin == 2: #if we are hovering the glass bin
                        trashBinLids[hoveredBin] = screen.create_polygon(310, 740, 450, 740, 440, 730, 320, 730, fill="#0066CC", outline="black")
                    else: #if we are hovering the plastic bin
                        trashBinLids[hoveredBin] = screen.create_polygon(460, 740, 600, 740, 590, 730, 470, 730, fill="#CC0000", outline="black")
                    hoveredBin = 'None'

        else: #make sure to delete the trash lid and redraw it once we drop an item as well
            if hoveredBin != 'None': #if there was a trash bin we were hovering over previously
                screen.delete(lidOpen)
                #we assign the lid drawing of bin that is not hovered over anymore so that we can redraw it back to the screen
                if hoveredBin == 0: #if we are hovering the paper bin
                    trashBinLids[hoveredBin] = screen.create_polygon(10, 740, 150, 740, 140, 730, 20, 730, fill="#DDDD00", outline="black")
                elif hoveredBin == 1: #if we are hovering the organic bin
                    trashBinLids[hoveredBin] = screen.create_polygon(160, 740, 300, 740, 290, 730, 170, 730, fill="#00CC00", outline="black")
                elif hoveredBin == 2: #if we are hovering the glass bin
                    trashBinLids[hoveredBin] = screen.create_polygon(310, 740, 450, 740, 440, 730, 320, 730, fill="#0066CC", outline="black")
                else: #if we are hovering the plastic bin
                    trashBinLids[hoveredBin] = screen.create_polygon(460, 740, 600, 740, 590, 730, 470, 730, fill="#CC0000", outline="black")
                hoveredBin = 'None'     
    
# gets called when mouse is released
def mouseReleaseHandler(event):
    global xMouse, yMouse, clickedItemNumber, score

    mouseDown = False

    xMouse = event.x
    yMouse = event.y

    if gameMode == "play":
        # checks if trash is placed in the right bin
        if trashItems[clickedItemNumber].y+(trashItems[clickedItemNumber].height//2) > 700: # makes sure the bottom of the image is on the garbage bins
            # gives us the index of the category of the trash in the trashCategory array so we can access the correct information
            categoryIndex = trashCategory.index(trashItems[clickedItemNumber].category)
            # detects if the x of the image is in the correct area when dropped, thus giving you a point
            if trashBinRegions[categoryIndex][0] <= trashItems[clickedItemNumber].x and trashItems[clickedItemNumber].x <= trashBinRegions[categoryIndex][1]:
                score = score + 1
                trashItems[clickedItemNumber].reset()
            else: #if you didn't drop the trash in the right bin
                trashItems[clickedItemNumber].lostLife() #decrease life counter as well as draw x indicating lose life
                trashItems[clickedItemNumber].reset()
        trashItems[clickedItemNumber].clicked = False
        clickedItemNumber = 'None'


#gets called when key is pressed
def keyDownHandler(event):
    global escPressed, gameMode
    if event.keysym == "Escape": #if esc is pressed
        if gameMode == "intro": #if at intro, close the window
            root.destroy()

        elif gameMode == "instructions": #if at instructions, go back to intro
            gameMode = "intro"
            drawIntroScreen()
            screen.delete(instructionsScreen)

        elif gameMode == "difficulty": #if at difficulty screen, go back to intro
            gameMode = "intro"
            drawIntroScreen()
            screen.delete(difficultyScreen)

        elif gameMode == "play": #if playing, end game
            escPressed = True


# helper function to help mouseClickHandler if it is clicking on an image 
def mouseInsideImage(xImage, yImage, width, height):
    # detects if the x and y of the mouse is inside the image by also taking into account the height and width
    if xImage - width <= xMouse <= xImage + width and yImage - height <= yMouse <= yImage + height:
        return True
    else:
        return False


#====== Draw Diffrent Screen States ======#
def drawIntroScreen():
    global introScreen
    introScreen = screen.create_image(300, 450, anchor="center", image=introScreenGIF)


def drawInstructionsScreen():
    global instructionsScreen
    instructionsScreen = screen.create_image(300, 450, anchor="center", image=instructionsScreenGIF)


def drawDifficultyScreen():
    global difficultyScreen
    difficultyScreen = screen.create_image(300, 450, anchor="center", image=difficultyScreenGIF)


def drawLoadingScreen():
    global loadingScreen
    loadingScreen = screen.create_image(300, 450, anchor='center', image=loadingScreenGIF)


def drawGameOver():
    global gameOverScreen
    gameOverBackground = screen.create_image(300, 450, anchor=CENTER, image=gameOverScreenGIF)
    scoreDisplay = screen.create_text(300, 220, text=score, font="Roboto 72", anchor=CENTER, fill="#e6e6e6")
    gameOverScreen = [gameOverBackground, scoreDisplay]



#clean up leftover drawings that have a aren't normally deleted in the animation loop
#this includes leftover xDrawings as well as trash bins that aren't constantly deleted in the animation loop
def cleanUp(): 
    screen.delete('all') #instead of looping through the array of trash bins and xDrawings, we just delete everything on screen  
    drawBackground() #redraw our background

def runGame():
    global gameMode, ySpeed
    drawLoadingScreen()
    screen.update()
    setInitialValues()
    gameMode = "play"
    createTrash()
    drawTrashBins()
    sleep(1)
    screen.delete(loadingScreen)

    while lives > 0 and escPressed == False:
        updateObjects()
        drawObjects()
        screen.update()
        sleep(0.03)
        deleteObjects()
    cleanUp()
    gameMode = "game over"
    drawGameOver()

#boot up the start menu
def start():
    global gameMode, mouseDown
    importImages()
    gameMode = "intro"
    drawBackground()
    drawIntroScreen()
    
    mouseDown = False

# At the bottom
root.after(0, start)

# keybindings
root.bind("<Button-1>", mouseClickHandler)
root.bind("<ButtonRelease-1>", mouseReleaseHandler)
root.bind("<Motion>", mouseMotionHandler)

root.bind("<Key>", keyDownHandler)

screen.pack()
screen.focus_set()
root.mainloop()