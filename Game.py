from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=900, background="white")

#object model for a piece of trash
class Trash:
	def __init__(self, x, y, width, height, category, trashGIF): #set object variables on initialization
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.category = category
		self.trashGIF = trashGIF

		self.clicked = False

	def reset(self): #Method, reset trash object variables, giving the illusion that a new trash item is created
		self.category = choice(trashCategory) #chooses random trash category
		categoryIndex = trashCategory.index(self.category) 
		self.trashGIF = choice(allTrashItemGIFS[categoryIndex])
		item = trashItemGIF(self.category) #creates temporary object to store values of gif
		self.trashGIF = item.gif 
		self.width = item.dimensions[0]
		self.height = item.dimensions[1]
		self.x = randint(0+(self.width//2), 600-(self.width//2))
		self.y = randint(-900+(self.height//2), 0-(self.height//2))

	def lostLife(self): #Method, 
		xDrawings.append(xDrawing(self.x, self.y)) #add xDrawing in place of trash that wasn't placed in the correct bin in time
	
	def update(self): #Method, set object location
		global lives, score
		if self.clicked == False:
			self.y = self.y + ySpeed  # increases position of trash
			#checks if piece of trash has exceeded limit and is not clicked on
			if self.y+(self.height//2) > 900:
				lives = lives - 1
				self.lostLife()
				self.reset()
		
#object containing trash item gif information
class trashItemGIF:
	def __init__(self, category):
		self.category = category
		categoryIndex = trashCategory.index(category) #gets the index of the category so that we can access the correct array of gifs
		self.gif = choice(allTrashItemGIFS[categoryIndex])
		trashGIFIndex = allTrashItemGIFS[categoryIndex].index(self.gif) #gets the index for the specific trash item in the category array so that we can access it's dimensions
		self.dimensions = trashItemDimensions[categoryIndex][trashGIFIndex]

#object for X drawing
class xDrawing:
	def __init__(self, x, y):
		width = 10
		cross1 = screen.create_line(x+width, y+width, x-width,y-width, width="3", fill="red")
		cross2 = screen.create_line(x+width, y-width, x-width, y+width, width="3", fill="red")

		self.drawing = [cross1, cross2] 
		self.time = 20 #time for how many frames the image will appear for

# SET UP OUR VALUES
# set our global variables
def setInitialValues():
	global score, lives, piecesOfTrash, ySpeed, trashCategory
	global xMouse, yMouse, mouseDown, escPressed, clickedItemNumber, hoveredBin
	global paperItemGIF, organicItemGIF, glassItemGIF, plasticItemGIF, allTrashItemGIFS, recycleLogoGIF
	global paperBinDrawing, organicBinDrawing, glassBinDrawing, plasticBinDrawing, trashBinDrawings, xDrawings
	global introScreenGIF, instructionsScreenGIF, difficultyScreenGIF, loadingScreenGIF, gameOverScreenGIF
	global trashItemDimensions, trashBinRegions

	score = 0
	lives = 3
	piecesOfTrash = 10
	ySpeed = 2
	trashCategory = ['paper', 'organic', 'glass', 'plastic'] #list containing all possible categorys of trash

	mouseDown = False
	escPressed = False
	clickedItemNumber = 'None' #index used to identify which trash object is clicked(will be None when there aren't any)
	hoveredBin = 'None' #identify which garbage bin is hovered on by the mouse when holding an item

	#arrays of trash item gifs in their respective category
	paperItemGIF = [PhotoImage(file="imgs/paper/paper1.gif"), PhotoImage(file="imgs/paper/paper2.gif"), PhotoImage(file="imgs/paper/paper3.gif")]
	organicItemGIF = [PhotoImage(file="imgs/organic/organic1.gif"), PhotoImage(file="imgs/organic/organic2.gif"), PhotoImage(file="imgs/organic/organic3.gif"), PhotoImage(file="imgs/organic/organic4.gif")]
	glassItemGIF = [PhotoImage(file="imgs/glass/glass1.gif"), PhotoImage(file="imgs/glass/glass2.gif"), PhotoImage(file="imgs/glass/glass3.gif"), PhotoImage(file="imgs/glass/glass4.gif")]
	plasticItemGIF = [PhotoImage(file="imgs/plastic/plastic1.gif"), PhotoImage(file="imgs/plastic/plastic2.gif"), PhotoImage(file="imgs/plastic/plastic3.gif"), PhotoImage(file="imgs/plastic/plastic4.gif")]
	#collection of all trash item images
	allTrashItemGIFS = [paperItemGIF, organicItemGIF, glassItemGIF, plasticItemGIF]

	recycleLogoGIF = PhotoImage(file="imgs/recycling logo.gif")

	#have arrays that stores all of the drawings of the recycling bin
	paperBinDrawing = []
	organicBinDrawing = []
	glassBinDrawing = []
	plasticBinDrawing = []
	trashBinDrawings = []

	xDrawings = [] #array of all drawings of X's that indicate a lost life
	
	trashBinGIF = PhotoImage(file="imgs/trash bins.gif")
	#images for game screens
	#introScreenGIF = PhotoImage(file="")
	#instructionsScreenGIF = PhotoImage(file="")
	#difficultyScreenGIF = PhotoImage(file="")
	#loadingScreenGIF = PhotoImage(file="")
	#gameOverScreenGIF = PhotoImage(file="")

	#multi-dimensional array that stores the fixed sizes of the gifs, has heirarchy of [category of item][item number][dimensions for each item]
	trashItemDimensions = [[[80,60],[111,71],[106,76]], [[57,74],[47,46],[46,58],[66,62]], [[29,82],[23,76],[23,81],[22,44]], [[28,80],[52,64],[60,79],[39,39]]]
	#array that stores range of valid x coordinates of each garbage bin 
	trashBinRegions = [[0,150],[150,300],[300,450],[450,600]]

#Functions for interacting with trash items
#initializes trash objects and their values at the start of the game
def createTrash():
	global trash 
	trash = [] #array containing all trash objects
	for i in range(piecesOfTrash):
		category = choice(trashCategory) #chooses random trash category
		itemDrawing = trashItemGIF(category) #creates temporary drawing object so that we can access it's details

		trashGIF = itemDrawing.gif 
		width = itemDrawing.dimensions[0]
		height = itemDrawing.dimensions[1]

		x = randint(0+(width//2), 600-(width//2)) #we make sure that the object generated is always on screen by taking into account the width of the object
		y = randint(-900+(height//2), 0-(height//2)) #we make sure that the object generated is always on screen by taking into account the height of the object

		trash.append(Trash(x, y, width, height, category, trashGIF)) #adds a trash object with our calculated values to our trash item list

# draws each piece of trash to the screen
def drawTrash():
	global trashImage
	trashImage = [0] * piecesOfTrash #sets up each trash image to be assigned
	for i in range(piecesOfTrash): #assign each trashImage according to trash object values
		trashImage[i] = screen.create_image(trash[i].x, trash[i].y, anchor="center", image=trash[i].trashGIF)

# deletes each piece of trash on the screen
def deleteTrash():
	for i in range(piecesOfTrash):
		screen.delete(trashImage[i])

#calls update method of each trash object to update values
def updateTrash():
	for i in range(piecesOfTrash):
		trash[i].update()

#draw in the background
def drawTrashBins():
	global paperBinDrawing, organicBinDrawing, glassBinDrawing, plasticBinDrawing
	global trashBinDrawings

	#paper bin
	startX = 80
	wheel1 = screen.create_rectangle(17, 885, 33, 905, fill="black")
	wheel2 = screen.create_rectangle(127, 885, 143, 905, fill="black")
	body = screen.create_polygon(10, 740, 150, 740, 135, 900, 25, 900, fill="yellow", outline="black")
	lid = screen.create_polygon(10, 740, 150, 740, 140, 730, 20, 730, fill="yellow", outline="black")
	label = screen.create_text(80, 850, text="PAPER", font = "Roboto 16", anchor=CENTER, fill="white")
	logo = screen.create_image(80, 800, anchor="center", image=recycleLogoGIF)
	#lidOpen = screen.create_polygon(10, 740, 10, 600, 0, 610, 0, 720, fill="yellow", outline="black")
	paperBinDrawing = [wheel1, wheel2, body, lid, label, logo, paperBinDrawing]

	#organic bin
	startX = 230
	wheel1 = screen.create_rectangle(167, 885, 183, 905, fill="black")
	wheel2 = screen.create_rectangle(277, 885, 293, 905, fill="black")
	body = screen.create_polygon(160, 740, 300, 740, 285, 900, 175, 900, fill="green", outline="black")
	lid = screen.create_polygon(160, 740, 300, 740, 290, 730, 170, 730, fill="green", outline="black")
	label = screen.create_text(230, 850, text="ORGANIC", font = "Roboto 16", anchor=CENTER, fill="white")
	logo = screen.create_image(230, 800, anchor="center", image=recycleLogoGIF)
	#lidOpen = screen.create_polygon(160, 740, 160, 600, 150, 610, 150, 720, fill="green", outline="black")
	organicBinDrawing = [wheel1, wheel2, body, lid, label, logo, paperBinDrawing]	

	#glass bin
	startX = 380
	wheel1 = screen.create_rectangle(317, 885, 333, 905, fill="black")
	wheel2 = screen.create_rectangle(427, 885, 443, 905, fill="black")
	body = screen.create_polygon(310, 740, 450, 740, 435, 900, 325, 900, fill="blue", outline="black")
	lid = screen.create_polygon(310, 740, 450, 740, 440, 730, 320, 730, fill="blue", outline="black")
	label = screen.create_text(380, 850, text="GLASS", font = "Roboto 16", anchor=CENTER, fill="white")
	logo = screen.create_image(380, 800, anchor="center", image=recycleLogoGIF)
	#lidOpen = screen.create_polygon(310, 740, 310, 600, 300, 610, 300, 720, fill="blue", outline="black")
	glassBinDrawing = [wheel1, wheel2, body, lid, label, logo, paperBinDrawing]

	#plastic bin
	startX = 530
	wheel1 = screen.create_rectangle(467, 885, 483, 905, fill="black")
	wheel2 = screen.create_rectangle(577, 885, 593, 905, fill="black")
	body = screen.create_polygon(460, 740, 600, 740, 585, 900, 475, 900, fill="red", outline="black")
	lid = screen.create_polygon(460, 740, 600, 740, 590, 730, 470, 730, fill="red", outline="black")
	label = screen.create_text(startX, 850, text="PLASTIC", font = "Roboto 16", anchor=CENTER, fill="white")
	logo = screen.create_image(startX, 800, anchor="center", image=recycleLogoGIF)
	#lidOpen = screen.create_polygon(460, 740, 460, 600, 450, 610, 450, 720, fill="red", outline="black")
	plasticBinDrawing = [wheel1, wheel2, body, lid, label, logo, paperBinDrawing]

	trashBinDrawings = [paperBinDrawing, organicBinDrawing, glassBinDrawing, plasticBinDrawing]

# GETS CALLED CONSTANTLY FOR ANIMATION
# draw all of our graphics
def updateStatistics():
	global scoreDisplay, livesDisplay

	scoreMessage = "Score: " + str(score)
	livesMessage = "Lives: " + str(lives)

	scoreDisplay = screen.create_text(100, 36, text = scoreMessage, font = "Times 36", anchor=CENTER, fill="black")
	livesDisplay = screen.create_text(500, 36, text = livesMessage, font = "Times 36", anchor=CENTER, fill="black")

def drawObjects():
	drawTrash()
	updateStatistics()

# delete our drawings so they can be redrawn
def deleteObjects():
	deleteTrash()
	screen.delete(scoreDisplay)
	screen.delete(livesDisplay)
	for i in xDrawings: #check if timers of x drawings is up
		if i.time == 0: #if the timer is up
			screen.delete(i.drawing[0]) #remove cross1 of the x from the screen
			screen.delete(i.drawing[1]) #remove cross2 of the x from the screen
			xDrawings.remove(i) #delete the xDrawing object

def mouseInsideImage(xImage, yImage, width, height):
	#detects if the x and y of the mouse is inside the image by also taking into account the height and width
	if xImage - width <= xMouse <= xImage + width and yImage - height <= yMouse <= yImage + height: 
		return True
	else:
		return False

#update positions of all of our objects
def updateObjects():
	updateTrash() 
	for i in xDrawings: #updates the timer for each xDrawing
		i.time -= 1

#Functions for drawing different screens
#def drawLoading():
#	loadingScreenGIF = screen.create_image()

def drawGameOver():
	scoreDisplay = screen.create_text()
	

# KEYBIND HANDLERS
# gets called when user clicks mouse
def mouseClickHandler(event):
	global xMouse, yMouse, mouseDown, clickedItemNumber

	xMouse=event.x
	yMouse=event.y

	mouseDown=True
	#checks if you clicked on a trash item
	for i in range(piecesOfTrash-1, -1, -1): #loop backwards through images so that image drawn on top is clicked if there is overlap
		item = trash[i]
		if mouseInsideImage(item.x, item.y, item.width, item.height) == True:
			item.clicked = True
			clickedItemNumber = i #records the index of our object so that we can set it's clicked value as false later once it is dropped
			break #make sure once we find one object that is valid to be clicked, we don't move another object as well

# gets called when mouse is moving and checks if mouse is clicked
def mouseMotionHandler(event):
	global xMouse, yMouse, mouseDown, clickedItemNumber, hoveredBin

	xMouse=event.x
	yMouse=event.y

	if mouseDown == True and clickedItemNumber != 'None': #let the trash follow the mouse if there is a valid clicked item as well as if the mouse is clicked
		trash[clickedItemNumber].x = xMouse
		trash[clickedItemNumber].y = yMouse

		#if yMouse+(trash[clickedItemNumber].height//2) > 700:#animate opened lid when hovering over trash bin
		#	for i in range(len(trashBinRegions)-1):
		#		if trashBinRegions[i][0] <= yMouse and trashBinRegions[i][1] >= yMouse:
		#			hoveredBin = i

# gets called when mouse is released
def mouseReleaseHandler(event):
	global xMouse, yMouse, mouseDown, clickedItemNumber, lives, score, trash

	mouseDown=False

	xMouse=event.x
	yMouse=event.y

	#checks if trash is placed in the right bin
	if trash[clickedItemNumber].y+(trash[clickedItemNumber].height//2) > 700: #makes sure the bottom of the image is on the garbage bins
		categoryIndex = trashCategory.index(trash[clickedItemNumber].category) #gives us the index of the category of the trash in the trashCategory array so we can access the correct information
		if trashBinRegions[categoryIndex][0] <= trash[clickedItemNumber].x and trash[clickedItemNumber].x <= trashBinRegions[categoryIndex][1]: #detects if the x of the image is in the correct area when dropped, thus giving you a point
			score = score + 1
			trash[clickedItemNumber].reset()
		else: #if you didn't drop the trash in the right bin
			lives = lives - 1

			trash[clickedItemNumber].lostLife()
			trash[clickedItemNumber].reset()

	trash[clickedItemNumber].clicked = False
	clickedItemNumber = 'None'

# gets called when key is pressed
def keyDownHandler(event):
	global escPressed
	if event.keysym == "Escape":  #end game if esc is pressed
		escPressed = True

def stopGame():
	root.destroy()

def runGame():
	#drawLoading()
	setInitialValues()
	createTrash()
	drawTrashBins()
	#screen.delete(loadingScreenGIF)
	sleep(1)
	
	while escPressed == False:
		drawObjects()
		screen.update()
		sleep(0.03)

		deleteObjects()
		updateObjects()
	stopGame()
	sleep(1)


# At the bottom
root.after(0, runGame)

# keybindings
screen.bind("<Button-1>", mouseClickHandler)
screen.bind("<ButtonRelease-1>", mouseReleaseHandler)
screen.bind("<Motion>", mouseMotionHandler)

screen.bind("<Key>", keyDownHandler)

screen.pack()
screen.focus_set()
root.mainloop()
