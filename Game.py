from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=900, background="white")

#object model for a piece of trash
class Trash:
	def __init__(self, x, y, width, height, type, trashGIF): #set object variables on initialization
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.type = type
		self.trashGIF = trashGIF

		self.clicked = False

	def reset(self): #Method, reset trash object variables, giving the illusion that a new trash item is created
		self.type = choice(trashType) #chooses random trash type
		typeIndex = trashType.index(self.type) 
		self.trashGIF = choice(allTrashItemGIFS[typeIndex])
		item = trashItemGIF(self.type) #creates temporary object to store values of gif
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
	def __init__(self, type):
		self.type = type
		typeIndex = trashType.index(type)
		self.gif = choice(allTrashItemGIFS[typeIndex])
		trashGIFIndex = allTrashItemGIFS[typeIndex].index(self.gif)
		self.dimensions = trashItemDimensions[typeIndex][trashGIFIndex]

#object for X drawing
class xDrawing:
	def __init__(self, x, y):
		width = 10
		cross1 = screen.create_line(x+width, y+width, x-width,y-width, width="3", fill="red")
		cross2 = screen.create_line(x+width, y-width, x-width, y+width, width="3", fill="red")

		self.drawing = [cross1, cross2]
		self.time = 20 #time for how many frames the image will appear for
# get distance between two points
def getDistance(x1, y1, x2, y2):
	return sqrt((x1-x2)**2 + (y1-y2)**2)

# SET UP OUR VALUES
# set our global variables
def setInitialValues():
	global score, lives, piecesOfTrash, ySpeed, trashType
	global xMouse, yMouse, mouseDown, escPressed, clickedItemNumber
	global glassItemGIF, organicItemGIF, paperItemGIF, plasticItemGIF, allTrashItemGIFS, trashBinsGIF
	global xDrawings
	global trashItemDimensions, trashBinRegions

	score = 0
	lives = 3
	piecesOfTrash = 10
	ySpeed = 2
	trashType = ['paper', 'organic', 'glass', 'plastic'] #list containing all possible types of trash

	mouseDown = False
	escPressed = False
	clickedItemNumber = 'None' #index used to identify which trash object is clicked(will be None when there aren't any)
	
	#arrays of trash item gifs in their respective type
	paperItemGIF = [PhotoImage(file="imgs/paper/paper1.gif"), PhotoImage(file="imgs/paper/paper2.gif"), PhotoImage(file="imgs/paper/paper3.gif")]
	organicItemGIF = [PhotoImage(file="imgs/organic/organic1.gif"), PhotoImage(file="imgs/organic/organic2.gif"), PhotoImage(file="imgs/organic/organic3.gif"), PhotoImage(file="imgs/organic/organic4.gif")]
	glassItemGIF = [PhotoImage(file="imgs/glass/glass1.gif"), PhotoImage(file="imgs/glass/glass2.gif"), PhotoImage(file="imgs/glass/glass3.gif"), PhotoImage(file="imgs/glass/glass4.gif")]
	plasticItemGIF = [PhotoImage(file="imgs/plastic/plastic1.gif"), PhotoImage(file="imgs/plastic/plastic2.gif"), PhotoImage(file="imgs/plastic/plastic3.gif"), PhotoImage(file="imgs/plastic/plastic4.gif")]
	#collection of all trash item images
	allTrashItemGIFS = [paperItemGIF, organicItemGIF, glassItemGIF, plasticItemGIF]

	trashBinsGIF = PhotoImage(file = "imgs/trash bins.gif")

	xDrawings = [] #array of all drawings of X's that indicate a lost life
	
	#multi-dimensional array that stores the fixed sizes of the gifs, has heirarchy of [type of item][item number][dimensions for each item]
	trashItemDimensions = [[[80,60],[111,71],[106,76]], [[57,74],[47,46],[46,58],[66,62]], [[29,82],[23,76],[23,81],[22,44]], [[28,80],[52,64],[60,79],[39,39]]]
	#array that stores range of valid x coordinates of each garbage bin 
	trashBinRegions = [[0,150],[150,300],[300,450],[450,600]]

#draw in background
def drawTrashBins():
	screen.create_image(300, 800, anchor="center", image=trashBinsGIF)

#Functions for interacting with trash items
#initializes trash objects and their values at the start of the game
def createTrash():
	global trash 
	trash = [] #array containing all trash objects
	for i in range(piecesOfTrash):
		type = choice(trashType) #chooses random trash type
		item = trashItemGIF(type)

		trashGIF = item.gif 
		width = item.dimensions[0]
		height = item.dimensions[1]

		x = randint(0+(width//2), 600-(width//2))
		y = randint(-900+(height//2), 0-(height//2))

		trash.append(Trash(x, y, width, height, type, trashGIF))

# draws each piece of trash to the screen
def drawTrash():
	global trashImage
	trashImage = [0] * piecesOfTrash
	for i in range(piecesOfTrash):
		trashImage[i] = screen.create_image(trash[i].x, trash[i].y, anchor="center", image=trash[i].trashGIF)

# deletes each piece of trash on the screen
def deleteTrash():
	for i in range(piecesOfTrash):
		screen.delete(trashImage[i])

def updateTrash():
	for i in range(piecesOfTrash):
		trash[i].update()

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
# delete our drawings
def deleteObjects():
	deleteTrash()
	#check if timers of x drawings is up
	screen.delete(scoreDisplay)
	screen.delete(livesDisplay)
	for i in xDrawings:
		if i.time == 0:
			screen.delete(i.drawing[0])
			screen.delete(i.drawing[1])
			xDrawings.remove(i)

def mouseInsideImage(xImage, yImage, width, height):
	if xImage - width <= xMouse <= xImage + width and yImage - height <= yMouse <= yImage + height:
		return True
	else:
		return False

# update positions of all of our objects
def updateObjects():
	updateTrash()
	for i in xDrawings:
		i.time -= 1

# KEYBIND HANDLERS
# gets called when mouse is clicked
def mouseClickHandler(event):
	global xMouse, yMouse, mouseDown, clickedItemNumber

	xMouse=event.x
	yMouse=event.y

	mouseDown=True
	for i in range(piecesOfTrash-1, -1, -1): #loop backwards through images so that image on top is clicked
		item = trash[i]
		if mouseInsideImage(item.x, item.y, item.width, item.height) == True:
			item.clicked = True
			clickedItemNumber = i #records the index of our object so that we can set it's clicked value as false
			break

# gets called when mouse is moving and checks if mouse is clicked
def mouseMotionHandler(event):
	global xMouse, yMouse, clickedItemNumber

	xMouse=event.x
	yMouse=event.y

	if mouseDown == True and clickedItemNumber != 'None':
		trash[clickedItemNumber].x = xMouse
		trash[clickedItemNumber].y = yMouse
		
# gets called when mouse is released
def mouseReleaseHandler(event):
	global xMouse, yMouse, mouseDown, clickedItemNumber, lives, score, trash

	mouseDown=False

	xMouse=event.x
	yMouse=event.y

	#checks if trash is placed in the right bin
	if trash[clickedItemNumber].y+(trash[clickedItemNumber].height//2) > 700:
		typeIndex = trashType.index(trash[clickedItemNumber].type)
		if trashBinRegions[typeIndex][0] <= trash[clickedItemNumber].x and trash[clickedItemNumber].x <= trashBinRegions[typeIndex][1]:
			score = score + 1
			trash[clickedItemNumber].reset()
		else: 
			lives = lives - 1

			trash[clickedItemNumber].lostLife()
			trash[clickedItemNumber].reset()

	trash[clickedItemNumber].clicked = False
	clickedItemNumber = 'None'
# gets called when key is pressed
def keyDownHandler(event):
	global escPressed
	if event.keysym == "Escape":  # end game if esc is pressed
		escPressed=True




def stopGame():
	root.destroy()

def runGame():
	setInitialValues()
	createTrash()
	drawTrashBins()

	while escPressed == False:
		drawObjects()
		screen.update()
		sleep(0.03)

		deleteObjects()
		updateObjects()
	stopGame()
	print(score)

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
