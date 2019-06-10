from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=900, background="white")

#data model for pieces of trash
class Trash:
	def __init__(self, x, y, width, height, kind, trashGIF): #set object variables
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.kind = kind
		self.trashGIF = trashGIF

		self.clicked = False

	def update(self): #set object location
		self.y = self.y + ySpeed  # increases position of trash
		# checks if piece of garbage has exceeded limit and is not clicked on
		if self.y+(self.height//2) > 700 and self.clicked == False:
			#lives = lives - 1
			xDrawings.append(xDrawing(self.x, self.y))

			#reassigns all of the values of the trash object
			self.kind = choice(garbageKind) #chooses random garbage kind
			kindIndex = garbageKind.index(self.kind)
			self.trashGIF = choice(allTrashItemsGIFS[kindIndex])

			item = trashItemGIF(self.kind) #creates temporary object to store values of gif
			self.trashGIF = item.gif 
			self.width = item.dimensions[0]
			self.height = item.dimensions[1]

			self.x = randint(0+(self.width//2), 600-(self.width//2))
			self.y = randint(-900+(self.height//2), 0-(self.height//2))

#object containing trash item gif information
class trashItemGIF:
	def __init__(self, kind):
		self.kind = kind
		kindIndex = garbageKind.index(kind)
		self.gif = choice(allTrashItemsGIFS[kindIndex])
		trashGIFIndex = allTrashItemsGIFS[kindIndex].index(self.gif)
		self.dimensions = trashItemDimensions[kindIndex][trashGIFIndex]

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
	global score, lives, piecesOfTrash, ySpeed, garbageKind
	global xMouse, yMouse, mouseDown, escPressed
	global glassGIF, organicGIF, paperGIF, plasticGIF, allTrashItemsGIFS
	global trashItemDimensions
	global garbageBinsGIF
	
	global xDrawings #array of all drawings of X's that indicate a lost life
	xDrawings = []

	#trash item images
	glassGIF = [PhotoImage(file="imgs/glass/glass1.gif"), PhotoImage(file="imgs/glass/glass2.gif"), PhotoImage(file="imgs/glass/glass3.gif"), PhotoImage(file="imgs/glass/glass4.gif")]
	organicGIF = [PhotoImage(file="imgs/organic/organic1.gif"), PhotoImage(file="imgs/organic/organic2.gif"), PhotoImage(file="imgs/organic/organic3.gif"), PhotoImage(file="imgs/organic/organic4.gif")]
	paperGIF = [PhotoImage(file="imgs/paper/paper1.gif"), PhotoImage(file="imgs/paper/paper2.gif"), PhotoImage(file="imgs/paper/paper3.gif")]
	plasticGIF = [PhotoImage(file="imgs/plastic/plastic1.gif"), PhotoImage(file="imgs/plastic/plastic2.gif"), PhotoImage(file="imgs/plastic/plastic3.gif"), PhotoImage(file="imgs/plastic/plastic4.gif")]
	#collection of all trash item images
	allTrashItemsGIFS = [glassGIF, organicGIF, paperGIF, plasticGIF]
	#multi-dimensional array that has heirarchy of an array of each kind of item, then dimensions for each item
	trashItemDimensions = [[[29,82],[23,76],[23,81],[22,44]], [[57,74],[47,46],[46,58],[66,62]], [[80,60],[111,71],[106,76]], [[28,80],[52,64],[60,79],[39,39]]]

	garbageBinsGIF = PhotoImage(file = "imgs/garbage bins.gif")
	garbageKind = ['glass', 'organic', 'paper', 'plastic']

	score = 0
	lives = 3
	piecesOfTrash = 10
	ySpeed = 2
	mouseDown = False
	escPressed = False

#background drawings
def drawTrashBins():
	screen.create_image(300, 800, anchor="center", image=garbageBinsGIF)

#Functions for interacting with trash items
# initializes values for pieces of garbage at the start of the game
def createTrash():
	global trash
	trash = []
	for i in range(piecesOfTrash):
		kind = choice(garbageKind) #chooses random garbage kind
		item = trashItemGIF(kind)

		trashGIF = item.gif 
		width = item.dimensions[0]
		height = item.dimensions[1]

		x = randint(0+(width//2), 600-(width//2))
		y = randint(-900+(height//2), 0-(height//2))

		trash.append(Trash(x, y, width, height, kind, trashGIF))

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
def drawObjects():
	drawTrash()

# delete our drawings
def deleteObjects():
	deleteTrash()
	#check if timers of x drawings is up
	for i in xDrawings:
		if i.time == 0:
			screen.delete(i.drawing[0])
			screen.delete(i.drawing[1])
			xDrawings.remove(i)

'''def mouseInsideImage(xImage, yImage):
	if getDistance(xImage, xMouse, yImage, yMouse) < 
		return True
	else:
		return False'''

# update positions of all of our objects
def updateObjects():
	updateTrash()
	for i in xDrawings:
		i.time -= 1


# KEYBIND HANDLERS
# gets called when mouse is clicked
def mouseClickHandler(event):
	global xMouse, yMouse, mouseDown

	xMouse=event.x
	yMouse=event.y

	mouseDown=True
	

# gets called when mouse is moving and checks if mouse is clicked
def mouseMotionHandler(event):
	global xMouse, yMouse

	xMouse=event.x
	yMouse=event.y

	# if mouseDown == True:

# gets called when mouse is released
def mouseReleaseHandler(event):
	global xMouse, yMouse, mouseDown

	mouseDown=False

	xMouse=event.x
	yMouse=event.y

# gets called when key is pressed
def keyDownHandler(event):
	global escPressed
	if event.keysym == "Escape":  # end game if esc is pressed
		escPressed=True




def endGame():
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
	endGame()

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
