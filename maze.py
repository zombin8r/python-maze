from random import shuffle, randrange
from graphics import *

#All code  is written and tested by Nathan Carter, with the exception of generateMaze()
#which I modified for use in this program

#The graphics & roomtypes
def roomDraw(videoScreen,roomType,facingDirection):
	#All the graphics to draw on screen
	def ceiling(videoScreen):
		ceiling = Polygon(Point(150, 50), Point(500, 50), Point(400, 100), Point(250, 100))
		ceiling.setFill('#00BFFF')
		ceiling.draw(videoScreen)

	def floor(videoScreen):
		floor = Polygon(Point(250, 350), Point(400, 350), Point(500, 450), Point(150, 450))
		floor.setFill('#4DBD33')
		floor.draw(videoScreen)
		
	def mazeLeft(videoScreen):
		left = Polygon(Point(150, 50), Point(150, 450), Point(250, 350), Point(250, 100))
		left.setFill('#841F27')
		left.draw(videoScreen)

	def mazeRight(videoScreen):
		right = Polygon(Point(400, 100), Point(500, 50), Point(500, 450), Point(400, 350))
		right.setFill('#841F27')
		right.draw(videoScreen)

	def mazeFront(videoScreen):
		front = Polygon(Point(250, 100), Point(400, 100), Point(400, 350), Point(250, 350))
		front.setFill('#841F27')
		front.draw(videoScreen)
	
	#Draw doors for each roomtype if they exist
	def mazeFrontDoor(videoScreen):
		door = Polygon(Point(275, 125), Point(275, 350), Point(375, 350), Point(375, 125))
		door.setFill('white')
		door.draw(videoScreen)
		
	def mazeRightDoor(videoScreen):
		rightDoor = Polygon(Point(425, 125), Point(475, 100), Point(475, 425), Point(425, 375))
		rightDoor.setFill('white')
		rightDoor.draw(videoScreen)

	def mazeLeftDoor(videoScreen):
		leftDoor = Polygon(Point(175, 100), Point(225, 125), Point(225, 375), Point(175, 425))
		leftDoor.setFill('white')
		leftDoor.draw(videoScreen)
	
	#Draw the basic room graphics.
	ceiling(videoScreen)
	floor(videoScreen)
	mazeFront(videoScreen)
	mazeLeft(videoScreen)
	mazeRight(videoScreen)
	
	#Draw screen graphics based on direction and roomtype
	if roomType == 'southEnd':
		#if facingDirection == 0:
			#no door
		if facingDirection == 1:
			mazeLeftDoor(videoScreen)
		if facingDirection == 2:
			mazeFrontDoor(videoScreen)
		if facingDirection == 3:
			mazeRightDoor(videoScreen)
	
	if roomType == 'eastEnd': 
		if facingDirection == 0:
			mazeRightDoor(videoScreen)
		#if facingDirection == 1:
			#no door
		if facingDirection == 2:
			mazeLeftDoor(videoScreen)
		if facingDirection == 3:
			mazeFrontDoor(videoScreen)
	
	if roomType == 'northEnd': 
		if facingDirection == 0:
			mazeFrontDoor(videoScreen)
		if facingDirection == 1:
			mazeRightDoor(videoScreen)
		#if facingDirection == 2:
			#no door
		if facingDirection == 3:
			mazeLeftDoor(videoScreen)
	
	if roomType == 'westEnd':
		if facingDirection == 0:
			mazeLeftDoor(videoScreen)
		if facingDirection == 1:
			mazeFrontDoor(videoScreen)
		if facingDirection == 2:
			mazeRightDoor(videoScreen)
		#if facingDirection == 3:
			#no door
	if roomType == 'hallNorth':
		if facingDirection == 0:
			mazeFrontDoor(videoScreen)
		if facingDirection == 1:
			mazeRightDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 2:
			mazeFrontDoor(videoScreen)
		if facingDirection == 3:
			mazeRightDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		
	if roomType == 'hallEast':
		if facingDirection == 0:
			mazeRightDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 1:
			mazeFrontDoor(videoScreen)
		if facingDirection == 2:
			mazeRightDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 3:
			mazeFrontDoor(videoScreen)
		
	if roomType == 'southWest':
		if facingDirection == 0:
			mazeLeftDoor(videoScreen)
		if facingDirection == 1:
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 2:
			mazeFrontDoor(videoScreen)
			mazeRightDoor(videoScreen)
		if facingDirection == 3:
			mazeRightDoor(videoScreen)
	
	if roomType == 'southEast':
		if facingDirection == 0:
			mazeRightDoor(videoScreen)
		if facingDirection == 1:
			mazeLeftDoor(videoScreen)
		if facingDirection == 2:
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 3:
			mazeFrontDoor(videoScreen)
			mazeRightDoor(videoScreen)
		
	if roomType == 'northWest':
		if facingDirection == 0:
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 1:
			mazeFrontDoor(videoScreen)
			mazeRightDoor(videoScreen)
		if facingDirection == 2:
			mazeRightDoor(videoScreen)
		if facingDirection == 3:
			mazeLeftDoor(videoScreen)
			
	if roomType == 'northEast':
		if facingDirection == 0:
			mazeFrontDoor(videoScreen)
			mazeRightDoor(videoScreen)
		if facingDirection == 1:
			mazeRightDoor(videoScreen)
		if facingDirection == 2:
			mazeLeftDoor(videoScreen)
		if facingDirection == 3:
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
	
	if roomType == 'westWall':
		if facingDirection == 0:
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 1:
			mazeFrontDoor(videoScreen)
			mazeRightDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 2:
			mazeFrontDoor(videoScreen)
			mazeRightDoor(videoScreen)
		if facingDirection == 3:
			mazeRightDoor(videoScreen)
			mazeLeftDoor(videoScreen)
	
	if roomType == 'northWall':
		if facingDirection == 0:
			mazeFrontDoor(videoScreen)
			mazeRightDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 1:
			mazeFrontDoor(videoScreen)
			mazeRightDoor(videoScreen)
		if facingDirection == 2:
			mazeRightDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 3:
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
	
	if roomType == 'eastWall':
		if facingDirection == 0:
			mazeFrontDoor(videoScreen)
			mazeRightDoor(videoScreen)
		if facingDirection == 1:
			mazeRightDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 2:
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 3:
			mazeRightDoor(videoScreen)
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		
	if roomType == 'southWall':
		if facingDirection == 0:
			mazeRightDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 1:
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 2:
			mazeRightDoor(videoScreen)
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
		if facingDirection == 3:
			mazeFrontDoor(videoScreen)
			mazeRightDoor(videoScreen)
		
	if roomType == 'allDir': 
		if facingDirection == 0:
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
			mazeRightDoor(videoScreen)
		if facingDirection == 1:
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
			mazeRightDoor(videoScreen)
		if facingDirection == 2:
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
			mazeRightDoor(videoScreen)
		if facingDirection == 3:
			mazeFrontDoor(videoScreen)
			mazeLeftDoor(videoScreen)
			mazeRightDoor(videoScreen)

def titleDraw(titleScreen):

	#clear the keyboard
	getChar = ''
	mazeSizeX = ''
	mazeSizeY = ''
	#Draws the name of my game
	p = Line(Point(100,50), Point(100, 150))
	p.draw(titleScreen)
	p = Polygon(Point(100,50), Point(150,50), Point(150,100), Point(100,100))
	p.draw(titleScreen)
	r = Line(Point(200,50), Point(200,150))
	r.draw(titleScreen)
	r = Polygon(Point(200,100), Point(250,150))
	r.draw(titleScreen)
	r = Polygon(Point(200,50), Point(250,50), Point(250,100), Point(200,100))
	r.draw(titleScreen)
	o = Oval(Point(300,50), Point(350,150))
	o.draw(titleScreen)
	j = Line(Point(400,50), Point(450,50))
	j.draw(titleScreen)
	j = Line(Point(425,50),Point(425,150))
	j.draw(titleScreen)
	j = Line(Point(425,150), Point(400,150))
	j.draw(titleScreen)
	j = Line(Point(400,150), Point(400,100))
	j.draw(titleScreen)
	e = Line(Point(500,50), Point(550,50))
	e.draw(titleScreen)
	e = Line(Point(500,150), Point(550,150))
	e.draw(titleScreen)
	e = Line(Point(500,50), Point(500,150))
	e.draw(titleScreen)
	e = Line(Point(500,100), Point(525,100))
	e.draw(titleScreen)
	c = Line(Point(600,50), Point(600,150))
	c.draw(titleScreen)
	c = Line(Point(600,50), Point(650,50))
	c.draw(titleScreen)
	c = Line(Point(600,150), Point(650,150))
	c.draw(titleScreen)
	t = Line(Point(700,50), Point(750,50))
	t.draw(titleScreen)
	t = Line(Point(725,50), Point(725,150))
	t.draw(titleScreen)
	p = Line(Point(250,200), Point(250,300))
	p.draw(titleScreen)
	p = Polygon(Point(250,200), Point(300,200), Point(300,250), Point(250,250))
	p.draw(titleScreen)
	y = Line(Point(300,200), Point(325,250))
	y.draw(titleScreen)
	y = Line(Point(350,200), Point(325,250))
	y.draw(titleScreen)
	y = Line(Point(325,250), Point(325,300))
	y.draw(titleScreen)
	t = Line(Point(350,200), Point(400,200))
	t.draw(titleScreen)
	t = Line(Point(375,200), Point(375,300))
	t.draw(titleScreen)
	h = Line(Point(400,200), Point(400,300))
	h.draw(titleScreen)
	h = Line(Point(400,250), Point(450,250))
	h.draw(titleScreen)
	h = Line(Point(450,200), Point(450,300))
	h.draw(titleScreen)
	o = Oval(Point(450,200), Point(500,300))
	o.draw(titleScreen)
	n = Line(Point(500,200), Point(500,300))
	n.draw(titleScreen)
	n = Line(Point(500,200), Point(550,300))
	n.draw(titleScreen)
	n = Line(Point(550,200), Point(550,300))
	n.draw(titleScreen)
	line = Line(Point(225,300), Point(575,300))
	line.draw(titleScreen)
	message = Text(Point(150,400),'Enter the Width: ')
	message.draw(titleScreen)
	message.setSize(24)
	
	textPlaceX = 280
	textPlaceY = 400
	numCheck = ['1','2','3','4','5','6','7','8','9','0']
	while not getChar == 'Return':
		getChar = titleScreen.checkKey()
		if getChar in numCheck:
			if len(mazeSizeX) == 2: getChar = 'Return'
			else:
				mazeSizeX = mazeSizeX + getChar
				xDigit = Text(Point(textPlaceX,textPlaceY),getChar)
				xDigit.draw(titleScreen)
				xDigit.setSize(24)
				textPlaceX = textPlaceX + 17
	
	getChar = ''
	textPlaceX = 280
	textPlaceY = textPlaceY + 50
	message = Text(Point(150,450),'Enter the Height: ')
	message.draw(titleScreen)
	message.setSize(24)
	while not getChar == 'Return':
		getChar = titleScreen.checkKey()
		if getChar in numCheck:
			if len(mazeSizeY) == 2: getChar = 'Return'
			else:
				mazeSizeY = mazeSizeY + getChar
				yDigit = Text(Point(textPlaceX,textPlaceY),getChar)
				yDigit.draw(titleScreen)
				yDigit.setSize(24)
				textPlaceX = textPlaceX + 17
	
	#Check to see if maze is a reasonable size
	if mazeSizeX == '': mazeSizeX = "10"
	if mazeSizeY == '': mazeSizeY = "10"
	mazeWidth = int(mazeSizeX)
	mazeHeight = int(mazeSizeY)
	
	if mazeWidth * mazeHeight > 2026:
		message = Text(Point(300,500),'That is too big, using default size. ')
		message.draw(titleScreen)
		message.setSize(24)
		mazeWidth = 10
		mazeHeight = 10
	
	message = Text(Point(300,550),'Press any key to play!')
	message.draw(titleScreen)
	message.setSize(24)
	titleScreen.getKey()
		
	#print("mazeSizeX:", mazeWidth)
	#print("mazeSizeY:", mazeHeight)
	return mazeWidth, mazeHeight
	
	

#Generate a random solvable maze
def generateMaze(mazeWidth, mazeHeight):

	#This function returns a solvable maze, used under the GNU Free Documentation Licence
	#which provides effective freedom to copy and redistribute code, with or without modifying it,
	#either commercially or noncommercially. The full license is available at http://www.gnu.org/licenses/fdl-1.2.html
	#Source code at http://rosettacode.org/wiki/Maze_generation#Python
	#Modified for my purposes

	def make_maze(mazeWidth, mazeHeight):
		vis = [[0] * mazeWidth + [1] for _ in range(mazeHeight)] + [[1] * (mazeWidth + 1)]
		ver = [["|  "] * mazeWidth + ['|'] for _ in range(mazeHeight)] + [[]]
		hor = [["+--"] * mazeWidth + ['+'] for _ in range(mazeHeight + 1)]

		def walk(x, y):
			q = 0
			vis[y][x] = 1

			d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
			shuffle(d)
			for (xx, yy) in d:
				q = q + 1
				if vis[yy][xx]: continue
				if xx == x: hor[max(y, yy)][x] = "+  "
				if yy == y: ver[y][max(x, xx)] = "   "
				walk(xx, yy)

		walk(randrange(mazeWidth), randrange(mazeHeight))

		s = ""
		for (a, b) in zip(hor, ver):
			s += ''.join(a + b)
		return s


	#initial array setup and draw out the maze string
	maze = [[0 for x in range(mazeHeight)] for y in range(mazeWidth)]
	
	#Makes the maze
	randomMaze = make_maze(mazeWidth,mazeHeight)
	room = ""
	#calculate the row size length (in characters) of the subrows
	subrowLength = mazeWidth * 3 + 1
	#calculate the row size (in characters) of the second subrow
	#row2 = row1 * 2
	#count every column in the maze
	for x in range(0,mazeWidth):
		#for every column, get every row
		for y in range(0,mazeHeight):
			#for every column and row, get a subrow
			for subrow in range(0,3):
			
				#This is a super complicated math formula, that takes room sections
				#from the randomMaze string and indentifies what room type they are.
				#Warning... the math hurts the head, and it took me a long time to figure it out.
				#basically, roomSubrowPosition is the starting position of the subrow depending on
				#the x and y coordinates of the maze.  Each room in the string is made of a box
				#at x,y containing 3 subrows.  I assign room to a string containing all 3 subrows,
				#and compare that to room types.
				roomSubrowPosition = subrow*subrowLength+y*subrowLength*2+x*3
				
				#grab the section of randomMaze that contains the current subrow and append it to room.
				#Each column is 4 characters wide, so grab 4 characters.
				room = room + randomMaze[roomSubrowPosition:roomSubrowPosition+4]

			#Assings roomtypes to our maze array for each x and y coordinate.
			if room == '+--+|  |+  +': maze[x][y] = 'northEnd'
			if room == '+--+   |+--+': maze[x][y] = 'eastEnd'
			if room == '+  +|  |+--+': maze[x][y] = 'southEnd'
			if room == '+--+|   +--+': maze[x][y] = 'westEnd'
			if room == '+  +|  |+  +': maze[x][y] = 'hallNorth'
			if room == '+--+    +--+': maze[x][y] = 'hallEast'
			if room == '+  +|   +--+': maze[x][y] = 'southWest'
			if room == '+  +   |+--+': maze[x][y] = 'southEast'
			if room == '+--+|   +  +': maze[x][y] = 'northWest'
			if room == '+--+   |+  +': maze[x][y] = 'northEast'
			if room == '+  +|   +  +': maze[x][y] = 'westWall'
			if room == '+--+    +  +': maze[x][y] = 'northWall'
			if room == '+  +   |+  +': maze[x][y] = 'eastWall'
			if room == '+  +    +--+': maze[x][y] = 'southWall'
			if room == '+  +    +  +': maze[x][y] = 'allDir'
			#Reassigns room to an empty string to execute this code again until the ranges are met.
			room = ""
	#Returns the maze so that when the code is executed into main() so it can draw out the maze.
	return maze
	

#Draw your position on the map.  If cheat is True, draw the entire map
def refMap(videoMap,mazeWidth,mazeHeight,maze,posX,posY,cheat=False):
	def drawNorthEnd(videoMap, roomX, roomY):
		line = Line(Point(roomX,roomY), Point(roomX,roomY+10))
		line.draw(videoMap)
		line = Line(Point(roomX,roomY), Point(roomX+10,roomY))
		line.draw(videoMap)
		line = Line(Point(roomX+10,roomY), Point(roomX+10,roomY+10))
		line.draw(videoMap)
	def drawSouthEnd(videoMap, roomX, roomY):
		line = Line(Point(roomX,roomY), Point(roomX,roomY+10))
		line.draw(videoMap)
		line = Line(Point(roomX,roomY+10), Point(roomX+10,roomY+10))
		line.draw(videoMap)
		line = Line(Point(roomX+10,roomY+10), Point(roomX+10,roomY))
		line.draw(videoMap)
	def drawEastEnd(videoMap, roomX, roomY):
		line = Line(Point(roomX,roomY), Point(roomX+10,roomY))
		line.draw(videoMap)
		line = Line(Point(roomX+10,roomY), Point(roomX+10,roomY+10))
		line.draw(videoMap)
		line = Line(Point(roomX+10,roomY+10), Point(roomX,roomY+10))
		line.draw(videoMap)
	def drawWestEnd(videoMap, roomX, roomY):
		line = Line(Point(roomX+10,roomY), Point(roomX,roomY))
		line.draw(videoMap)
		line = Line(Point(roomX,roomY), Point(roomX,roomY+10))
		line.draw(videoMap)
		line = Line(Point(roomX,roomY+10), Point(roomX+10,roomY+10))
		line.draw(videoMap)
	def drawHallNorth(videoMap, roomX, roomY):
		line = Line(Point(roomX,roomY), Point(roomX,roomY+10))
		line.draw(videoMap)
		line = Line(Point(roomX+10,roomY), Point(roomX+10,roomY+10))
		line.draw(videoMap)
	def drawHallEast(videoMap,roomX,roomY):
		line = Line(Point(roomX,roomY), Point(roomX+10,roomY))
		line.draw(videoMap)
		line = Line(Point(roomX,roomY+10), Point(roomX+10,roomY+10))
		line.draw(videoMap)
	def drawSouthWest(videoMap,roomX,roomY):
		line = Line(Point(roomX,roomY), Point(roomX,roomY+10))
		line.draw(videoMap)
		line = Line(Point(roomX,roomY+10), Point(roomX+10,roomY+10))
		line.draw(videoMap)
	def drawSouthEast(videoMap,roomX,roomY):
		line = Line(Point(roomX+10,roomY), Point(roomX+10,roomY+10))
		line.draw(videoMap)
		line = Line(Point(roomX+10,roomY+10), Point(roomX,roomY+10))
		line.draw(videoMap)
	def drawNorthWest(videoMap,roomX,roomY):
		line = Line(Point(roomX+10,roomY), Point(roomX,roomY))
		line.draw(videoMap)
		line = Line(Point(roomX,roomY), Point(roomX,roomY+10))
		line.draw(videoMap)
	def drawNorthEast(videoMap,roomX,roomY):
		line = Line(Point(roomX,roomY), Point(roomX+10,roomY))
		line.draw(videoMap)
		line = Line(Point(roomX+10,roomY), Point(roomX+10,roomY+10))
		line.draw(videoMap)
	def drawWestWall(videoMap,roomX,roomY):
		line = Line(Point(roomX,roomY), Point(roomX,roomY+10))
		line.draw(videoMap)
	def drawNorthWall(videoMap,roomX,roomY):
		line = Line(Point(roomX,roomY), Point(roomX+10,roomY))
		line.draw(videoMap)
	def drawEastWall(videoMap,roomX,roomY):
		line = Line(Point(roomX+10,roomY), Point(roomX+10,roomY+10))
		line.draw(videoMap)
	def drawSouthWall(videoMap,roomX,roomY):
		line = Line(Point(roomX,roomY+10), Point(roomX+10,roomY+10))
		line.draw(videoMap)
	def drawAllDir(videoMap,roomX,roomY):
		pt = Point(roomX,roomY)
		pt.draw(videoMap)
		pt = Point(roomX+10,roomY)
		pt.draw(videoMap)
		pt = Point(roomX,roomY+10)
		pt.draw(videoMap)
		pt = Point(roomX+10,roomY+10)
		pt.draw(videoMap)
	#This is the function that draws out the maze on the reference map based on your x and y position.
	def drawIt(videoMap,mazeX,mazeY,roomX,roomY):
		if maze[mazeX][mazeY] == 'northEnd': drawNorthEnd(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'southEnd': drawSouthEnd(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'eastEnd': drawEastEnd(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'westEnd': drawWestEnd(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'hallNorth': drawHallNorth(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'hallEast': drawHallEast(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'southWest': drawSouthWest(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'southEast': drawSouthEast(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'northWest': drawNorthWest(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'northEast': drawNorthEast(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'westWall': drawWestWall(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'northWall': drawNorthWall(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'eastWall': drawEastWall(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'southWall': drawSouthWall(videoMap,roomX,roomY)
		if maze[mazeX][mazeY] == 'allDir': drawAllDir(videoMap,roomX,roomY)
	#This will draw the entire map on the reference map, effectively making it a cheat command.
	if cheat:
		for mazeY in range(0,mazeHeight):
			for mazeX in range(0,mazeWidth):
				roomX = mazeX * 10
				roomY = mazeY * 10
				#Each maze type to be drawn on screen
				drawIt(videoMap,mazeX,mazeY,roomX,roomY)
	#This will map the walls of the current position on the reference map.
	else:
		roomX = posX * 10
		roomY = posY * 10
		drawIt(videoMap,posX,posY,roomX,roomY)
		
				
#THE MAIN PROGRAM
def main():
	
	#Display the title screen, and get the size of the maze from the player.
	titleScreen = GraphWin('Title Screen', 800, 600)
	titleScreen.setBackground('#ffff66')
	mazeWidth, mazeHeight = titleDraw(titleScreen)
	titleScreen.close()

	

	#Define our important variables	
	#facingDirection meaning:
	#0 = south		1 = east
	#2 = north		3 = west
	facingDirection = 0
	
	#Our location in the maze, start out at x,y = 0,0
	posX = 0
	posY = 0
	
	#Stores keyboard input when a key is pressed
	getChar = ''
	
	#if exit is ever true, then we quit the game
	exit = False

	#setup the maze
	maze = generateMaze(mazeWidth, mazeHeight)
	print('finished generating maze')
	videoScreen = GraphWin('Maze Mania', 800, 600)
	videoMap = GraphWin('Reference Map', mazeWidth*10+2, mazeHeight*10+5)
	print('opened up video screen & map screen')
	roomDraw(videoScreen,maze[posX][posY],facingDirection)
	print('finished drawing current room')
	
	#draw initial position on the map
	refMap(videoMap,mazeWidth,mazeHeight,maze,posX,posY)
	line = Line(Point(posX * 10 + 5, posY * 10 + 6), Point(posX * 10 + 5, posY * 10 + 10))
	line.setArrow("last")
	line.draw(videoMap)
	
	#repeat the game until exit key is pressed
	while ( exit == False ):
		#wait until the player presses a valid button
		while (not (getChar in ['a', 'd', 'w', 'C', 'Q'])):
			getChar = videoScreen.checkKey()
			if (not getChar): getChar = videoMap.checkKey()
		
		#if the cheat key is pressed, show the entire map
		if getChar == 'C':
			refMap(videoMap,mazeWidth,mazeHeight,maze,posX,posY,True)

		if getChar == 'a':
			#turn left
			facingDirection = facingDirection + 1
			if facingDirection == 4: facingDirection = 0
			roomDraw(videoScreen,maze[posX][posY],facingDirection)
				
		if getChar == 'd':
			#turn right)
			facingDirection = facingDirection - 1
			if facingDirection == -1: facingDirection = 3
			roomDraw(videoScreen,maze[posX][posY],facingDirection)
				
		if getChar == 'w':
			#move forward on specific room types and only if there is a door in front of the player or not.
			if facingDirection == 0:
				if maze[posX][posY] in ['northEnd', 'hallNorth', 'northWest', 'northEast', 'westWall', 'northWall', 'eastWall', 'allDir']:
					posY = posY + 1

			if facingDirection == 1:
				if maze[posX][posY] in ['westEnd', 'hallEast', 'southWest', 'northWest', 'westWall', 'northWall', 'southWall', 'allDir']:
					posX = posX + 1

			if facingDirection == 2:
				if maze[posX][posY] in ['southEnd', 'hallNorth', 'southWest', 'southEast', 'westWall', 'eastWall', 'southWall', 'allDir']:
					posY = posY - 1
		
			if facingDirection == 3:
				if maze[posX][posY] in ['eastEnd', 'hallEast', 'northEast', 'southEast', 'eastWall', 'northWall', 'southWall', 'allDir']:
					posX = posX - 1
						
			roomDraw(videoScreen,maze[posX][posY],facingDirection)
			refMap(videoMap,mazeWidth,mazeHeight,maze,posX,posY)
			#print('Current Position',posX,',',posY)

		#erase the current positional arrow
		line.undraw()
		
		#and draw it in the new position and/or direction.
		if facingDirection == 0:
			line = Line(Point(posX * 10 + 5, posY * 10 + 6), Point(posX * 10 + 5, posY * 10 + 10))
			line.setArrow("last")
		if facingDirection == 1:
			line = Line(Point(posX * 10 + 6, posY * 10 + 6), Point(posX * 10 + 10, posY * 10 + 6))
			line.setArrow("last")
		if facingDirection == 2:
			line = Line(Point(posX * 10 + 5, posY * 10), Point(posX * 10 + 5, posY * 10 + 4))
			line.setArrow("first")
		if facingDirection == 3:
			line = Line(Point(posX * 10 + 1, posY * 10 + 5), Point(posX * 10 + 5, posY * 10 + 5))
			line.setArrow("first")
		line.draw(videoMap)
		
		#Give a winning screen on end of the maze
		if posX == mazeWidth-1 and posY == mazeHeight-1:
			print('You are zee Weiner, here have some cake.')
			#do winner stuff here
	
		#Give us a quit button to exit the program		
		if getChar == 'Q': 
			print ('you are the weakest link, goodbye!')
			exit = True
		
		#reset the keyboard for new input
		getChar=''
		
#Calls on our important and main function to initiate the game.
main()