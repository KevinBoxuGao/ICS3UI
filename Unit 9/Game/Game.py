from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=1000, height=600, background="white")

# data model for pieces of trash
class Trash:
	def __init__(self, x, y, kind, trashGIF):
		self.x = x
		self.y = y
		self.kind = kind
		self.trashGIF = trashGIF
		self.ySpeed = ySpeed
		self.clicked = False

# get distance between two points
def getDistance(x1, y1, x2, y2):
	return sqrt((x1-x2)**2 + (y1-y2)**2)

# SET UP OUR VALUES
# set our global variables


def setInitialValues():
	global score, lives, piecesOfTrash, ySpeed, garbageKind
	global xMouse, yMouse, mouseDown, escPressed
	global glassGIF, organicGIF, paperGIF, plasticGIF
	global glassBinGIF, organicBinGIF, paperBinGIF, plasticBinGIF, allTrashGIFS

	glassGIF = [PhotoImage(file = "imgs/glass/glass1.gif"), PhotoImage(file = "imgs/glass/glass2.gif"), PhotoImage(file = "imgs/glass/glass3.gif")]
	organicGIF = [PhotoImage(file = "imgs/organic/organic1.gif"), PhotoImage(file = "imgs/organic/organic2.gif"), PhotoImage(file = "imgs/organic/organic3.gif")]
	paperGIF = [PhotoImage(file = "imgs/paper/paper1.gif"), PhotoImage(file = "imgs/paper/paper2.gif"), PhotoImage(file = "imgs/paper/paper3.gif")]
	plasticGIF = [PhotoImage(file = "imgs/plastic/plastic1.gif"), PhotoImage(file = "imgs/plastic/plastic2.gif"), PhotoImage(file = "imgs/plastic/plastic3.gif")]
	allTrashGIFS = [glassGIF, organicGIF, paperGIF, plasticGIF]

	glassBinGIF = PhotoImage(file = "imgs/glass/glassbin.gif")
	organicBinGIF = PhotoImage(file = "imgs/organic/organicbin.gif")
	paperBinGIF = PhotoImage(file = "imgs/paper/paperbin.gif")
	plasticBinGIF = PhotoImage(file = "imgs/plastic/plasticbin.gif")

	score = 0
	lives = 3
	piecesOfTrash = 10
	garbageKind = ['glass', 'organic', 'paper', 'plastic']

	ySpeed = 2
	mouseDown = False
	escPressed = False

# initializes values for pieces of garbage at the start of the game
def createTrash():
	global trash
	trash = []
	for i in range(piecesOfTrash):
		x = randint(20, 580)
		y = randint(-600, 0)
		kind = choice(garbageKind)

		kindIndex = garbageKind.index(kind)
		trashGIF = choice(allTrashGIFS[kindIndex])

		trash.append(Trash(x, y, kind, trashGIF))

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

# updates positions of each piece of trash
def updateTrash():
	for i in range(piecesOfTrash):
		trash[i].y = trash[i].y + trash[i].ySpeed  # increases position of trash
		# checks if piece of garbage has exceeded limit and is not clicked on
		if trash[i].y > 600 and trash[i].clicked == "False":
			lives = lives - 1
			# draw an x showcasing you missed garbage
			trash[i].y = randint(-600, 0)
			trash[i].x = randint(20, 580)
			trash[i].kind = choice(garbageKind)
			kindIndex = garbageKind.index(trash[i].kind)
			trash[i].trashGIF = choice(allTrashGIFS[kindIndex])

def drawTrashBins():
	screen.create_image(125, 600, anchor="center", image=glassBinGIF)
	screen.create_image(375, 600, anchor="center", image=organicBinGIF)
	screen.create_image(625, 600, anchor="center", image=paperBinGIF)
	screen.create_image(875, 600, anchor="center", image=plasticBinGIF)

# GETS CALLED CONSTANTLY FOR ANIMATION
# draw all of our graphics
def drawObjects():
	drawTrash()

# delete our drawings
def deleteObjects():
	deleteTrash()

# update positions of all of our objects
def updateObjects():
	updateTrash()


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
	drawTrashBins();

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
