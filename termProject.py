from tkinter import *
import decimal
import math
import copy
from RubiksSolver import *


def roundHalfUp(d):
	rounding = decimal.ROUND_HALF_UP
	return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

####################################
# customize these functions
####################################

def init(data):
	# load data.xyz as appropriate
	data.mode = "startState"
	data.blockSize = data.height/9
	data.cubeLoc = data.blockSize*3
	data.startCube = ["white", "orange", "yellow", "green", "blue",\
					"yellow", "yellow", "red"]
	data.endCube = ['white','white','white','white','white','white','white',\
							'white',]
	data.colorBelow = ['orange','yellow','yellow','yellow','yellow','orange']
	data.colorAbove = ['red', 'white', 'white', 'white', 'white', 'red']
	data.timerDelay = 500
	data.startCounter, data.endCounter = 0,0
	data.faceOrder = ["white", "red", "green", "orange", "blue", "yellow"]
	data.colorOrder = ['w','r','g','o','b','y']
	data.blockWidth = 5 *((min(data.height,data.width)/500))
	data.diag = math.sqrt(2)*data.blockSize
	data.clickX = 0
	data.clickY = 0
	allStartFaces(data)
	data.currentFaceFill, data.currentColorFill = 0, 0
	data.currentMove = 0
	data.movePos = 0
	data.masterList = []

def allStartFaces(data):
	data.whiteFace = [0, 0, 0, 0, 0, 0, 0, 0]
	data.redFace = [0, 0, 0, 0, 0, 0, 0, 0]
	data.greenFace = [0, 0, 0, 0, 0, 0, 0, 0]
	data.orangeFace = [0, 0, 0, 0, 0, 0, 0, 0]
	data.blueFace = [0, 0, 0, 0, 0, 0, 0, 0]
	data.yellowFace = [0, 0, 0, 0, 0, 0, 0, 0]

def mousePressed(event, data):
	# use event.x and event.y
	if data.mode == "prepState":
		if (event.x-data.cubeLoc>= 0) and \
			(event.x-data.cubeLoc<= data.blockSize*3) and \
			(event.y-data.cubeLoc>= 0) and \
			(event.y-data.cubeLoc<= data.blockSize*3):
			#print(event.y, event.y)
			#print(data.cubeLoc, data.blockSize)
			row = (event.y-data.cubeLoc)//data.blockSize
			col = (event.x-data.cubeLoc)//data.blockSize
			#print(row, col)
			changeStartFaces(data, int(row), int(col))
	if data.mode == 'solveState':
		if event.y <= (data.height-10*(data.height/500)) \
				and event.y >= (data.height-31*(data.height/500)):
			if event.x >= (10*(data.width/500)) and \
					event.x <= (264*(data.width/500)):
				data.mode = 'helpState'
			elif event.x >= (data.width-207*(data.width/500)) and \
					event.x <= (data.width-10*(data.width/500)):
				data.mode = 'guideState'
	if data.mode == 'guideState':
		if event.y <= (data.height-10*(data.height/500)) and \
				event.y >= data.height-47*(data.height/500) and \
				event.x <= (85*(data.width/500)) and \
				event.x >= 10*(data.width/500):
			data.mode = 'solveState'
	if data.mode == 'endState':
		if event.y >= data.height-40 and event.y <= data.height-10 and \
			event.x >= 10 and event.x <= 220:
				data.currentColorFill = 0
				data.currentFaceFill = 0
				allStartFaces(data)
				data.mode = 'prepState'

def keyPressed(event, data):
	#use event.char and event.keysym
	if data.mode == 'startState':
		if event.keysym == "s":
			data.mode = "prepState"
			data.prepColor = data.faceOrder[data.currentFaceFill]
	elif data.mode == "prepState":
		data.currentMove = 0
		data.movePos = 0
		if event.keysym == 'n':
			data.whiteFace = ['b','y','g','r','o','b','b','o']
			data.redFace = ['w','b','r','w','y','y','o','o']
			data.greenFace = ['w','g','r','y','b','w','o','w']
			data.orangeFace = ['w','r','g','r','y','r','r','g']
			data.blueFace = ['y','b','o','w','b','g','g','o']
			data.yellowFace = ['y','g','r','o','w','y','g','b']
			cube = Cube(data.whiteFace,data.redFace,data.greenFace,\
							data.orangeFace,data.blueFace,data.yellowFace)
			data.masterList, data.movesLeft = cube.solveCube()
			if data.masterList == []:
				data.mode = 'illegalCube'
				data.currentFaceFill = 0
				data.currentColorFill = 0
			else:
				data.mode = 'solveState'
		if event.keysym == "space":
			if data.currentColorFill == 5:
				data.currentColorFill = 0
				if data.currentFaceFill == 5:
					cube = Cube(data.whiteFace,data.redFace,data.greenFace,\
								data.orangeFace,data.blueFace,data.yellowFace)
					data.masterList, data.movesLeft = cube.solveCube()
					if data.masterList == []:
						data.mode = 'illegalCube'
						data.currentFaceFill = 0
						data.currentColorFill = 0
					else:
						data.mode = 'solveState'
				else:
					data.currentFaceFill += 1
			else:
				data.currentColorFill += 1
		elif event.keysym == 'Left':
			if data.currentColorFill > 0:
				data.currentColorFill -= 1
			elif data.currentColorFill == 0:
				if data.currentFaceFill > 0:
					data.currentFaceFill -= 1
					data.currentColorFill = 5
		elif event.keysym == 'Right':
			if data.currentFaceFill == 5:
				cube = Cube(data.whiteFace,data.redFace,data.greenFace,\
								data.orangeFace,data.blueFace,data.yellowFace)
				data.masterList, data.movesLeft = cube.solveCube()
				if data.masterList == []:
					data.mode = 'illegalCube'
					data.currentFaceFill = 0
					data.currentColorFill = 0
				else:
					data.mode = 'solveState'
			elif data.currentFaceFill < 5:
				data.currentFaceFill += 1
				data.currentColorFill = 0
	elif data.mode == 'illegalCube':
		if event.keysym == 'space':
			data.currentColorFill = 0
			data.currentFaceFill = 0
			#allStartFaces(data)
			data.mode = 'prepState'
			#print(data.mode)
		elif event.keysym == 'n':
			data.currentColorFill = 0
			data.currentFaceFill = 0
			allStartFaces(data)
			data.mode = 'prepState'
			#print(data.mode)
	elif data.mode == 'solveState':
		if event.keysym == 'space':
			data.movesLeft -= 1
			moveLength = len(data.masterList[data.currentMove])
			length = len(data.masterList)
			if (data.currentMove+1 == length and moveLength == 2) or \
				(data.currentMove+1 == length and moveLength == 5 and \
					data.movePos == 1):
				data.mode = 'endState'
			elif moveLength == 5:
				if data.movePos == 0:
					data.movePos += 1
				elif data.movePos == 1:
					data.movePos = 0
					data.currentMove += 1
			elif moveLength == 2:
				data.currentMove += 1
		elif event.keysym == 'Left':
			if data.currentMove >= 0:
				data.movesLeft += 1
				if data.movePos == 1:
					data.movePos -= 1
				elif data.movePos == 0:
					if len(data.masterList[data.currentMove-1]) == 5:
						data.movePos = 1
						data.currentMove -=1
					elif len(data.masterList[data.currentMove-1]) == 2:
						data.movePos = 0
						data.currentMove -=1
	if data.mode == 'helpState':
		if event.keysym == 'space':
			data.currentColorFill = 0
			data.currentFaceFill = 0
			#allStartFaces(data)
			data.mode = 'prepState'
			#print(data.mode)
		elif event.keysym == 'n':
			data.currentColorFill = 0
			data.currentFaceFill = 0
			allStartFaces(data)
			data.mode = 'prepState'
			#print(data.mode)
def timerFired(data):
	if data.mode == "startState":
		data.startCounter += 1
	if data.mode == 'endState':
		data.endCounter += 1
	
def redrawAll(canvas, data):
	if data.mode == "startState":
		drawStartScreen(canvas, data)
	elif data.mode == "prepState":
		drawPrepScreens(canvas, data)
	elif data.mode == 'illegalCube':
		drawIllegalCubeScreen(canvas, data)
	elif data.mode == 'solveState':
		if data.currentMove == 0:
			firstSolveState(canvas, data)
		elif data.currentMove >= 1:
			showMoves(canvas,data)
			drawHelpBox(canvas,data)
			drawTurnGuideBox(canvas, data)
	elif data.mode == 'helpState':
		drawHelpScreen(canvas, data)
	elif data.mode == 'guideState':
		drawTurnGuide(canvas, data)
	elif data.mode == 'endState':
		endStateText(canvas, data)
		turningCubeEndScreen(canvas, data)
		drawRestartBox(canvas, data)

######################
# IMPORTANT CODE #
######################

def getAllFaces(data):
	allFaces = []
	allFaces.append(data.whiteFace)
	allFaces.append(data.redFace)
	allFaces.append(data.greenFace)
	allFaces.append(data.orangeFace)
	allFaces.append(data.blueFace)
	allFaces.append(data.yellowFace)
	return allFaces

def correctOrderCubeFace(face, faceList):
	newList = []
	newList.append(faceList[0])
	newList.append(faceList[1])
	newList.append(faceList[2])
	newList.append(faceList[7])
	newList.append(face)
	newList.append(faceList[3])
	newList.append(faceList[6])
	newList.append(faceList[5])
	newList.append(faceList[4])
	return newList

def incorrectOrderTransition(row,col):
	if row == 0:
		return col
	elif row == 1:
		if col == 0:
			return 7
		if col == 2:
			return 3
	elif row == 2:
		return 6-col



def drawCubeFace(canvas, data, colorList):
	#print(colorList)
	for piece in range(len(colorList)):
		colorLetter = colorList[piece]
		if colorLetter == 0:
			color = "gray"
		else:
			if colorLetter in data.faceOrder:
				color= colorLetter
			else:
				colorIndex = data.colorOrder.index(colorLetter)
				color = data.faceOrder[colorIndex]
		xIndex = piece % 3
		yIndex = piece // 3
		#print("color:", color, " order:", index, " x:" , xIndex, " y:", yIndex)
		startX = data.cubeLoc + xIndex*data.blockSize
		startY = data.cubeLoc + yIndex*data.blockSize
		canvas.create_rectangle(startX, startY, startX + data.blockSize,\
							startY + data.blockSize,\
							fill = color, width = data.blockWidth)

def findFace(color):
	if color == "white":
		return data.whiteFace
	elif color == "red":
		return data.redFace
	elif color == "green":
		return data.greenFace
	elif color == "orange":
		return data.orangeFace
	elif color == "blue":
		return data.blueFace
	elif color == "yellow":
		return data.yellowFace
	
def getFaceList(data, faceIndex):
	if faceIndex == 0:
		return data.whiteFace
	elif faceIndex == 1:
		return data.redFace
	elif faceIndex == 2:
		return data.greenFace
	elif faceIndex == 3:
		return data.orangeFace
	elif faceIndex == 4:
		return data.blueFace
	elif faceIndex == 5:
		return data.yellowFace

def drawRightCubeFace(canvas,data,colorList):
	newCubeX = data.cubeLoc + 3*data.blockSize
	newCubeY = data.cubeLoc + data.blockSize
	for piece in range(9):
		colorLetter = colorList[piece]
		if colorLetter in data.faceOrder:
			color = colorLetter
		else:
			colorIndex = data.colorOrder.index(colorLetter)
			color = data.faceOrder[colorIndex]
		xIndex = piece % 3
		yIndex = piece // 3
		x1 = newCubeX + 20*(xIndex)*(data.width/500)
		y1 = newCubeY + yIndex*(data.blockSize) - xIndex*(10)*(data.width/500)
		x2 = x1
		y2 = y1 - data.blockSize
		x3 = x2 + 20*(data.width/500)
		y3 = y2 - 10*(data.width/500)
		x4 = x3
		y4 = y3 + data.blockSize
		canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,\
								fill = color, width = data.blockWidth)
		canvas.create_line(x1,y1,x2,y2,fill='black',width=data.blockWidth/2)
		canvas.create_line(x2,y2,x3,y3,fill='black',width=data.blockWidth/2)
		canvas.create_line(x3,y3,x4,y4,fill='black',width=data.blockWidth/2)
		canvas.create_line(x4,y4,x1,y1,fill='black',width=data.blockWidth/2)

def drawTopCubeFace(canvas,data,colorList):
	newCubeX = data.cubeLoc + 40*(data.width/500)
	newCubeY = data.cubeLoc - 20*(data.width/500)
	for piece in range(9):
		colorLetter = colorList[piece]
		if colorLetter in data.faceOrder:
			color = colorLetter
		else:
			colorIndex = data.colorOrder.index(colorLetter)
			color = data.faceOrder[colorIndex]
		xIndex = piece % 3
		yIndex = piece // 3
		x1 = newCubeX + xIndex*(data.blockSize) - 20*(yIndex)*(data.width/500)
		y1 = newCubeY + yIndex*(10)*(data.width/500)
		x2 = x1 + 20*(data.width/500)
		y2 = y1 - 10*(data.width/500)
		x3 = x2 + data.blockSize
		y3 = y2
		x4 = x1 + data.blockSize
		y4 = y1
		canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,\
								fill = color, width = data.blockWidth)
		canvas.create_line(x1,y1,x2,y2,fill='black',width=data.blockWidth/2)
		canvas.create_line(x2,y2,x3,y3,fill='black',width=data.blockWidth/2)
		canvas.create_line(x3,y3,x4,y4,fill='black',width=data.blockWidth/2)
		canvas.create_line(x4,y4,x1,y1,fill='black',width=data.blockWidth/2)

######################
# START CODE #
######################

def drawStartScreen(canvas, data):
	startScreenText(canvas, data)
	turningCubeStartScreen(canvas, data)

def startScreenText(canvas, data):
	firstLineY = 60*(data.height/500)
	secondLineY = 105*(data.height/500)
	thirdLineY = data.height - 105*(data.height/500)
	fourthLineY = data.height - 75*(data.height/500)
	titleFont = "Arial " + str(roundHalfUp(40*(data.height/500))) + " bold"
	introFont = "Arial " + str(roundHalfUp(30*(data.height/500))) + " bold"
	hintFont = "Arial " + str(roundHalfUp(18*(data.height/500)))
	hintText = 'Hint: the "red face" is the one with the red piece in the middle'
	canvas.create_text(data.width/2,firstLineY,text="Welcome to the Rubik's",
						fill="red",font= titleFont)
	canvas.create_text(data.width/2,secondLineY, text="Cube Solver",
						fill="red", font= titleFont)
	canvas.create_text(data.width/2, thirdLineY, text="Press 's' to start",
						fill="red", font= introFont)
	canvas.create_text(data.width/2, fourthLineY, text=hintText,
						fill="red", font= hintFont)

def turningCubeStartScreen(canvas, data):
	if data.startCounter % 2 == 0:
		drawCubeBackStart(canvas, data)
		startColors = correctOrderCubeFace("white", data.startCube)
		drawCubeTwistStart(canvas, data, startColors)
		data.startCube = twistFrontRightStart(data, data.startCube)
	else:
		colorList = correctOrderCubeFace("white", data.startCube)
		drawCubeFace(canvas, data, colorList)

def drawCubeBackStart(canvas, data):
	start = data.cubeLoc
	end = data.cubeLoc + 3*data.blockSize
	center = data.cubeLoc+((3/2)*data.blockSize)
	canvas.create_polygon(start, start, center, start, center, center,\
						fill = "green", width = data.blockWidth)
	canvas.create_polygon(center, start, end, start, center, center,\
						fill = "green", width = data.blockWidth)
	canvas.create_polygon(end, start, end, center, center, center,\
						fill = "white", width = data.blockWidth)
	canvas.create_polygon(end, center, end, end, center, center,
						fill = "white", width = data.blockWidth)
	canvas.create_polygon(end, end, center, end, center, center,\
						fill = "red", width = data.blockWidth)
	canvas.create_polygon(center, end, start, end, center, center,\
						fill = "orange", width = data.blockWidth)
	canvas.create_polygon(start, end, start, center, center, center,\
						fill = "blue", width = data.blockWidth)
	canvas.create_polygon(start, center, start, start, center, center,\
						fill = "yellow", width = data.blockWidth)
	canvas.create_line(start, start, end, start, fill="black",\
						width = data.blockWidth)
	canvas.create_line(end, start, end, end, fill="black",\
						width=data.blockWidth)
	canvas.create_line(end, end, start, end, fill="black",\
						width=data.blockWidth)
	canvas.create_line(start, end, start, start, fill="black",\
						width=data.blockWidth)
	canvas.create_line(start, start, end, end, fill="black",\
						width=data.blockWidth)
	canvas.create_line(end, start, start, end, fill="black",\
						width=data.blockWidth)

def drawCubeTwistStart(canvas, data, colorList):
	#print(colorList)
	start = data.cubeLoc - data.diag/2
	end = data.cubeLoc + 3*data.blockSize + data.diag/2
	center = data.height/2
	diff = data.diag/2
	canvas.create_polygon(center, start, center-diff, start+diff,\
						center, center-diff, center+diff, start+diff,\
						fill = colorList[0], width = data.blockWidth)
	canvas.create_polygon(center+diff, start+diff, center, center-diff,\
						center+diff, center, end-diff, center-diff,\
						fill = colorList[1], width = data.blockWidth)
	canvas.create_polygon(end-diff, center-diff, end-data.diag, center,\
						end-diff, center+diff, end, center,\
						fill = colorList[2], width = data.blockWidth)
	canvas.create_polygon(center-diff, start+diff, start+diff, center-diff,\
						center-diff, center, center, center-diff,\
						fill = colorList[3], width = data.blockWidth)
	canvas.create_polygon(center, center-diff, center-diff, center,\
						center, center+diff, center+diff, center,\
						fill = colorList[4], width = data.blockWidth)
	canvas.create_polygon(center+diff, center, center, center+diff,\
						center+diff, end-diff, end-diff, center+diff,\
						fill = colorList[5], width = data.blockWidth)
	canvas.create_polygon(start+diff, center-diff, start, center,\
						start+diff, center+diff, center-diff, center,\
						fill = colorList[6], width = data.blockWidth)
	canvas.create_polygon(center-diff, center, start+diff, center+diff,\
						center-diff, end-diff, center, center+diff,\
						fill = colorList[7], width = data.blockWidth)
	canvas.create_polygon(center, center+diff, center-diff, end-diff,\
						center, end, center+diff, end-diff,\
						fill = colorList[8], width = data.blockWidth)
	drawTwistGrid(canvas, data)

def drawTwistGrid(canvas, data):
	start = data.cubeLoc - data.diag/2
	end = data.cubeLoc + 3*data.blockSize + data.diag/2
	center = data.cubeLoc+((3/2)*data.blockSize)
	diff = data.diag/2
	#lines from the left down
	canvas.create_line(center, start, end, center, fill="black",\
						width=data.blockWidth)
	canvas.create_line(center-diff, start+diff, end-diff, center+diff,\
						fill="black", width = data.blockWidth)
	canvas.create_line(start+diff, center-diff, center+diff, end-diff,\
						fill="black", width = data.blockWidth)
	canvas.create_line(start, center, center, end, fill="black",\
						width=data.blockWidth)
	#lines from the right down
	canvas.create_line(center, start, start, center, fill="black",\
						width=data.blockWidth)
	canvas.create_line(center+diff, start+diff, start+diff, center+diff,
						fill="black", width = data.blockWidth)
	canvas.create_line(end-diff, center-diff, center-diff, end-diff,\
						fill="black", width = data.blockWidth)
	canvas.create_line(end, center, center, end, fill="black",\
						width=data.blockWidth)

def twistFrontRightStart(data, colorList):
	newList = []
	for i in range(len(colorList)):
		newList.append(None)
	for oldSpot in range(len(colorList)):
		color = colorList[oldSpot]
		newSpot = (oldSpot + 2) % 8
		newList[newSpot] = color
		#print("old:", oldSpot, " new:", newSpot)
	#print(newList)
	return newList


######################
# PREP CODE #
######################

#["white", "red", "green", "orange", "blue", "yellow"]

def drawPrepText(canvas, data):
	firstLineY = 80*(data.height/500)
	secondLineY = 115*(data.height/500)
	thirdLineY = 135*(data.height/500)
	adjustY = data.height - 120*(data.height/500)
	goBackY = data.height - 100*(data.height/500)
	fixY = data.height - 80*(data.height/500)
	firstLineFont = "Arial "+str(roundHalfUp(20*(data.height/500)))+" bold"
	secondLineFont= "Arial "+str(roundHalfUp(15*(data.height/500)))+" bold"
	adjustFont = "Arial "+str(roundHalfUp(15*(data.height/500)))
	fixFont = "Arial "+str(roundHalfUp(12.47*(data.height/500)))
	colorFill = data.faceOrder[data.currentColorFill]
	colorBelow = data.colorBelow[data.currentFaceFill]
	colorAbove = data.colorAbove[data.currentFaceFill]
	currentFace = data.faceOrder[data.currentFaceFill]
	if colorFill == 'white':
		textColor1 = 'black'
	else:
		textColor1 = colorFill
	if currentFace == 'white':
		textColor2 = 'black'
	else:
		textColor2 = currentFace
	firstLineText1 = "Click on the "
	firstLineText2 = colorFill
	firstLineText3 = " squares on the "
	firstLineText4 = currentFace
	firstLineText5 = ' face'
	secondLineText = 'Press the spacebar when you are done filling in the color'
	thirdLineText = \
				'or press the right arrow when you are done filling in a face'
	adjustLineText = 'Hold the cube with the ' + colorAbove + \
						' face up and the ' + colorBelow + ' face down'
	goBackLineText = 'Press the left arrow to ' +\
						'go back to a color you passed'
	fixLineText = "If you accidentally click with the wrong color, " + \
					"click the square again with the right color"
					
	canvas.create_text(85*(data.width/500),firstLineY,text=firstLineText1,\
						fill='black',font= firstLineFont)
	canvas.create_text(177*(data.width/500),firstLineY,text=firstLineText2,\
						fill=textColor1,font= firstLineFont)
	canvas.create_text(287*(data.width/500),firstLineY,text=firstLineText3,\
						fill='black',font= firstLineFont)
	canvas.create_text(396*(data.width/500),firstLineY,text=firstLineText4,\
						fill=textColor2,font= firstLineFont)
	canvas.create_text(455*(data.width/500),firstLineY,text=firstLineText5,\
						fill='black',font= firstLineFont)
						
	canvas.create_text(data.width/2,secondLineY,text=adjustLineText,\
						fill="black",font= secondLineFont)
	canvas.create_text(data.width/2,thirdLineY,text=secondLineText,\
						fill="black",font= secondLineFont)
	canvas.create_text(data.width/2,adjustY,text=goBackLineText,\
						fill='black',font= adjustFont)
	canvas.create_text(data.width/2,goBackY,text=thirdLineText,\
						fill='black',font= adjustFont)
	canvas.create_text(data.width/2,fixY,text=fixLineText,\
						fill='black',font= fixFont)

def drawPrepScreens(canvas, data):
	drawPrepText(canvas, data)
	list = copy.copy(getFaceList(data, data.currentFaceFill))
	face = data.colorOrder[data.currentFaceFill]
	faceList = copy.copy(correctOrderCubeFace(face, list))
	drawCubeFace(canvas, data, faceList)

def changeStartFaces(data, row, col):
	pos = incorrectOrderTransition(row,col)
	if isinstance(pos, int):
		color = data.colorOrder[data.currentColorFill]
		#print(pos)
		if data.currentFaceFill == 0:
			data.whiteFace[pos] = color
		elif data.currentFaceFill == 1:
			data.redFace[pos] = color
		elif data.currentFaceFill == 2:
			data.greenFace[pos] = color
		elif data.currentFaceFill == 3:
			data.orangeFace[pos] = color
		elif data.currentFaceFill == 4:
			data.blueFace[pos] = color
		elif data.currentFaceFill == 5:
			data.yellowFace[pos] = color


#correctOrderCubeFace(face, faceList)
#incorrectOrderTransition(row,col)
#drawCubeFace(canvas, data, colorList)

######################
# ILLEGAL CODE #
######################

def drawIllegalCubeScreen(canvas, data):
	firstLineText = 'This is an illegal Cube'
	secondLineText = 'Press the spacebar to edit the cube you have entered'
	thirdLineText = "Press 'n' to try again with a blank cube"
	firstLineFont = "Arial "+str(roundHalfUp(40*(data.height/500)))+" bold"
	secondLineFont= "Arial "+str(roundHalfUp(15*(data.height/500)))+" bold"
	firstLineY = 200*(data.height/500)
	secondLineY = 270*(data.height/500)
	thirdLineY = 290*(data.height/500)
	canvas.create_text(data.width/2,firstLineY,text=firstLineText,\
						fill="black",font= firstLineFont)
	canvas.create_text(data.width/2,secondLineY,text=secondLineText,\
						fill="black",font= secondLineFont)
	canvas.create_text(data.width/2,thirdLineY,text=thirdLineText,\
						fill="black",font= secondLineFont)



######################
# SOLVE CODE #
######################



#firstSolveState(canvas, data)
#showMoves(canvas,data)

def firstSolveState(canvas, data):
	list = copy.copy(data.masterList[0])
	firstLineText = list[0]
	secondLineText = list[1]
	thirdLineText = 'The face displayed under each move is what the face '
	fourthLineText = 'should look like after completeing the move'
	fifthLineText = 'Press the spacebar to begin'
	firstLineFont = "Arial "+str(roundHalfUp(27*(data.height/500)))+" bold"
	secondLineFont= "Arial "+str(roundHalfUp(18*(data.height/500)))+" bold"
	thirdLineFont= "Arial "+str(roundHalfUp(15*(data.height/500)))+" bold"
	fifthLineFont= "Arial "+str(roundHalfUp(30*(data.height/500)))+" bold"
	firstLineY = 80*(data.height/500)
	secondLineY = 150*(data.height/500)
	thirdLineY = 200*(data.height/500)
	fourthLineY = 230*(data.height/500)
	fifthLineY = 375*(data.height/500)
	canvas.create_text(data.width/2,firstLineY,text=firstLineText,\
						fill="red",font= firstLineFont)
	canvas.create_text(data.width/2,secondLineY,text=secondLineText,\
						fill="black",font= secondLineFont)
	canvas.create_text(data.width/2,thirdLineY,text=thirdLineText,\
						fill="black",font= thirdLineFont)
	canvas.create_text(data.width/2,fourthLineY,text=fourthLineText,\
						fill="black",font= thirdLineFont)
	canvas.create_text(data.width/2,fifthLineY,text=fifthLineText,\
						fill="black",font= fifthLineFont)

def showMoves(canvas, data):
	drawMovesLeft(canvas, data)
	move = copy.copy(data.masterList[data.currentMove])
	if len(move) == 5:
		if data.movePos == 0:
			firstLineText = move[0]
			secondLineText = move[1]
			face1 = move[2][0]
			face2 = move[2][1]
			face3 = move[2][2]
			firstLineFont = "Arial "+str(roundHalfUp(20*(data.height/500)))+" bold"
			secondLineFont= "Arial "+str(roundHalfUp(18*(data.height/500)))+" bold"
			firstLineY = 80*(data.height/500)
			secondLineY = 110*(data.height/500)
			canvas.create_text(data.width/2,firstLineY,text=firstLineText,\
							fill="black",font= firstLineFont)
			canvas.create_text(data.width/2,secondLineY,text=secondLineText,\
							fill="black",font= secondLineFont)
		elif data.movePos == 1:
			textLine = move[3]
			face1 = move[4][0]
			face2 = move[4][1]
			face3 = move[4][2]
			textFont = "Arial "+str(roundHalfUp(20*(data.height/500)))+" bold"
			textY = 80*(data.height/500)
			canvas.create_text(data.width/2,textY,text=textLine,\
							fill="black",font= textFont)
	if len(move) == 2:
		textLine = move[0]
		face1 = move[1][0]
		face2 = move[1][1]
		face3 = move[1][2]
		textFont = "Arial "+str(roundHalfUp(20*(data.height/500)))+" bold"
		textY = 80*(data.height/500)
		canvas.create_text(data.width/2,textY,text=textLine,\
						fill="black",font= textFont)
	drawCubeFace(canvas, data, face1)
	drawTopCubeFace(canvas,data, face2)
	drawRightCubeFace(canvas,data, face3)

def drawMovesLeft(canvas, data):
	goBackY = data.height - 120*(data.height/500)
	countY = data.height - 100*(data.height/500)
	currentFont = "Arial "+str(roundHalfUp(15*(data.height/500)))
	goBackLineText = 'Press the left arrow to go to the previous move'
	if data.movesLeft == 1:
		countLineText = 'There is ' + str(data.movesLeft) + ' move left'
	else:
		countLineText = 'There are ' + str(data.movesLeft) + ' moves left'
	canvas.create_text(data.width/2,goBackY,text=goBackLineText,\
						fill='black',font= currentFont)
	canvas.create_text(data.width/2,countY,text=countLineText,\
						fill='black',font= currentFont)
	
def drawHelpBox(canvas, data):
	canvas.create_rectangle(10*(data.width/500), \
							data.height-31*(data.height/500), \
							264*(data.width/500), \
							data.height-10*(data.height/500),\
							fill = 'coral1', width = 3*(data.width/500))
	textLine = 'Lost? Click here to re-enter your cube'
	textFont = "Arial "+str(roundHalfUp(14*(data.height/500)))
	canvas.create_text(138*(data.width/500),data.height-20*(data.height/500), \
						text=textLine, fill='black', font= textFont)

def drawTurnGuideBox(canvas, data):
	canvas.create_rectangle(data.width-207*(data.width/500), \
							data.height-31*(data.height/500), \
							data.width-10*(data.width/500), 
							data.height-10*(data.height/500),\
							fill = 'coral1', width = 3*(data.width/500))
	textLine = 'Click here for the turn guide'
	textFont = "Arial "+str(roundHalfUp(15*(data.height/500)))
	canvas.create_text(data.width-109*(data.width/500), \
						data.height-20*(data.height/500),text=textLine,\
						fill='black',font= textFont)



######################
# HELP CODE #
######################

def drawHelpScreen(canvas, data):
	firstLineText = 'Oops!'
	secondLineText = 'Press the spacebar to edit the cube you originally entered'
	thirdLineText = "Press 'n' to try again with a blank cube"
	firstLineFont = "Arial "+str(roundHalfUp(50*(data.height/500)))+" bold"
	secondLineFont= "Arial "+str(roundHalfUp(15*(data.height/500)))+" bold"
	firstLineY = 200*(data.height/500)
	secondLineY = 270*(data.height/500)
	thirdLineY = 290*(data.height/500)
	canvas.create_text(data.width/2,firstLineY,text=firstLineText,\
						fill="black",font= firstLineFont)
	canvas.create_text(data.width/2,secondLineY,text=secondLineText,\
						fill="black",font= secondLineFont)
	canvas.create_text(data.width/2,thirdLineY,text=thirdLineText,\
						fill="black",font= secondLineFont)


######################
# TURN GUIDE CODE #
######################

def drawTurnGuide(canvas, data):
	drawTurnGuideGrid(canvas, data)
	drawTurnGuideText(canvas, data)
	drawTurnIcons(canvas, data)
	drawGoBackBox(canvas, data)

def drawTurnGuideGrid(canvas, data):
	y1 = 25*(data.height/500)
	y2 = data.height-25*(data.height/500)
	canvas.create_line(100*(data.width/500), y1, 100*(data.width/500), y2, \
						fill='black', width=data.blockWidth)
	canvas.create_line(data.width/2, y1, data.width/2, y2, \
						fill='black', width=data.blockWidth)
	canvas.create_line(data.width-100*(data.width/500), y1,\
						data.width-100*(data.width/500), y2, fill='black', \
						width=data.blockWidth)
	x1 = 100*(data.width/500)
	x2 = data.width-100*(data.width/500)
	for i in range(6):
		y = 25*(data.height/500) + 90*(data.height/500)*i
		canvas.create_line(x1, y, x2, y, fill='black',width=data.blockWidth)

def drawTurnGuideText(canvas, data):
	textList = ['Turn face', 'Turn right side', 'Turn left side', 'Turn top',\
				'Turn bottom']
	x = (175)*(data.width/500)
	textFont = "Arial "+ str(int(19*(data.height/500)))+ " bold"
	textLine = textList[0]
	for i in range(5):
		textLine = textList[i]
		y = 70*(data.height/500) + 90*(data.height/500)*i
		canvas.create_text(x,y,text=textLine,fill='black',font=textFont)

def drawTurnFaceIcon(canvas, data):
	size = 14*(data.width/500)
	blockWidth = 2*(data.width/500)
	cubeLocX = (325)*(data.width/500) - 21*(data.width/500)
	cubeLocY = 70*(data.height/500) - 21*(data.width/500)
	diag = 2**(0.5) * size
	diff = diag/2
	startX = cubeLocX - diag/2
	startY = cubeLocY - diag/2
	endX = cubeLocX + 3*size + diag/2
	endY = cubeLocY + 3*size + diag/2
	centerX = cubeLocX+((3/2)*size)
	centerY = cubeLocY+((3/2)*size)
	for index in range(9):
		xIndex = index % 3
		yIndex = index // 3
		color = 'white'
		x1 = cubeLocX + xIndex*size
		y1 = cubeLocY + yIndex*size
		canvas.create_rectangle(x1, y1, x1 + size,\
							y1 + size,\
							fill = color, width = blockWidth)
	blockWidth = 1.5*(data.width/500)
	canvas.create_polygon(startX, centerY, centerX, startY, endX, centerY,\
							centerX, endY, fill = 'yellow')
	canvas.create_line(centerX, startY, endX, centerY, fill="black",\
							width=blockWidth)
	canvas.create_line(centerX-diff, startY+diff, endX-diff, centerY+diff,\
							fill="black", width = blockWidth)
	canvas.create_line(startX+diff, centerY-diff, centerX+diff, endY-diff,\
							fill="black", width = blockWidth)
	canvas.create_line(startX, centerY, centerX, endY, fill="black",\
							width=blockWidth)
	canvas.create_line(centerX, startY, startX, centerY, fill="black",\
							width=blockWidth)
	canvas.create_line(centerX+diff, startY+diff, startX+diff, centerY+diff,
							fill="black", width = blockWidth)
	canvas.create_line(endX-diff, centerY-diff, centerX-diff, endY-diff,\
							fill="black", width = blockWidth)
	canvas.create_line(endX, centerY, centerX, endY, fill="black",\
							width=blockWidth)

def drawTurnRightSideIcon(canvas, data):
	cubeLocX = (325)*(data.width/500) - 24*(data.width/500)
	cubeLocY = 160*(data.height/500) - 24*(data.width/500)
	size = 16*(data.width/500)
	blockWidth = 2*(data.width/500)
	for index in range(9):
		xIndex = index % 3
		yIndex = index // 3
		if xIndex == 2:
			color = 'yellow'
		else:
			color = 'white'
		startX = cubeLocX + xIndex*size
		startY = cubeLocY + yIndex*size
		canvas.create_rectangle(startX, startY, startX + size,\
							startY + size,\
							fill = color, width = blockWidth)

def drawTurnLeftSideIcon(canvas, data):
	cubeLocX = (325)*(data.width/500) - 24*(data.width/500)
	cubeLocY = 250*(data.height/500) - 24*(data.width/500)
	size = 16*(data.width/500)
	blockWidth = 2*(data.width/500)
	for index in range(9):
		xIndex = index % 3
		yIndex = index // 3
		if xIndex == 0:
			color = 'yellow'
		else:
			color = 'white'
		startX = cubeLocX + xIndex*size
		startY = cubeLocY + yIndex*size
		canvas.create_rectangle(startX, startY, startX + size,\
							startY + size,\
							fill = color, width = blockWidth)

def drawTurnTopIcon(canvas, data):
	cubeLocX = (325)*(data.width/500) - 24*(data.width/500)
	cubeLocY = 340*(data.height/500) - 24*(data.width/500)
	size = 16*(data.width/500)
	blockWidth = 2*(data.width/500)
	for index in range(9):
		xIndex = index % 3
		yIndex = index // 3
		if yIndex == 0:
			color = 'yellow'
		else:
			color = 'white'
		startX = cubeLocX + xIndex*size
		startY = cubeLocY + yIndex*size
		canvas.create_rectangle(startX, startY, startX + size,\
							startY + size,\
							fill = color, width = blockWidth)

def drawTurnBottomIcon(canvas, data):
	cubeLocX = (325)*(data.width/500) - 24*(data.width/500)
	cubeLocY = 430*(data.height/500) - 24*(data.width/500)
	size = 16*(data.width/500)
	blockWidth = 2*(data.width/500)
	for index in range(9):
		xIndex = index % 3
		yIndex = index // 3
		if yIndex == 2:
			color = 'yellow'
		else:
			color = 'white'
		startX = cubeLocX + xIndex*size
		startY = cubeLocY + yIndex*size
		canvas.create_rectangle(startX, startY, startX + size,\
							startY + size,\
							fill = color, width = blockWidth)

def drawTurnIcons(canvas, data):
	drawTurnFaceIcon(canvas, data)
	drawTurnRightSideIcon(canvas, data)
	drawTurnLeftSideIcon(canvas, data)
	drawTurnTopIcon(canvas, data)
	drawTurnBottomIcon(canvas, data)

def drawGoBackBox(canvas, data):
	canvas.create_rectangle(10*(data.width/500), \
							data.height-47*(data.height/500), \
							85*(data.width/500), \
							data.height-10*(data.height/500),\
							fill = 'coral1', width = 3*(data.width/500))
	textLine1 = 'Click here to'
	textLine2 = 'go back'
	textFont = "Arial "+str(int(12*(data.height/500)))
	canvas.create_text(47*(data.width/500),data.height-35*(data.height/500), \
						text=textLine1, fill='black', font= textFont)
	canvas.create_text(47*(data.width/500),data.height-22*(data.height/500), \
						text=textLine2, fill='black', font= textFont)


######################
# END CODE #
######################

def endStateText(canvas, data):
	textLine = "YOU HAVE SOLVED A RUBIK'S CUBE!!!"
	#face = ['w','w','w','w','w','w','w','w','w']
	textFont = "Arial "+str(roundHalfUp(20*(data.height/500)))+" bold"
	textY = 80*(data.height/500)
	canvas.create_text(data.width/2,textY,text=textLine,\
						fill="black",font= textFont)
	#drawCubeFacePrep(canvas, data, face)
	
def turningCubeEndScreen(canvas, data):
	if data.endCounter % 2 == 0:
		drawCubeBackEnd(canvas, data)
		endColors = correctOrderCubeFace("white", data.endCube)
		drawCubeTwistEnd(canvas, data, endColors)
		data.endCube = twistFrontRightStart(data, data.endCube)
	else:
		colorList = correctOrderCubeFace("white", data.endCube)
		drawCubeFace(canvas, data, colorList)

def drawCubeBackEnd(canvas, data):
	start = data.cubeLoc
	end = data.cubeLoc + 3*data.blockSize
	center = data.cubeLoc+((3/2)*data.blockSize)
	canvas.create_polygon(start, start, center, start, center, center,\
						fill = "red", width = data.blockWidth)
	canvas.create_polygon(center, start, end, start, center, center,\
						fill = "red", width = data.blockWidth)
	canvas.create_polygon(end, start, end, center, center, center,\
						fill = "green", width = data.blockWidth)
	canvas.create_polygon(end, center, end, end, center, center,
						fill = "green", width = data.blockWidth)
	canvas.create_polygon(end, end, center, end, center, center,\
						fill = "orange", width = data.blockWidth)
	canvas.create_polygon(center, end, start, end, center, center,\
						fill = "orange", width = data.blockWidth)
	canvas.create_polygon(start, end, start, center, center, center,\
						fill = "blue", width = data.blockWidth)
	canvas.create_polygon(start, center, start, start, center, center,\
						fill = "blue", width = data.blockWidth)
	canvas.create_line(start, start, end, start, fill="black",\
						width = data.blockWidth)
	canvas.create_line(end, start, end, end, fill="black",\
						width=data.blockWidth)
	canvas.create_line(end, end, start, end, fill="black",\
						width=data.blockWidth)
	canvas.create_line(start, end, start, start, fill="black",\
						width=data.blockWidth)
	canvas.create_line(start, start, end, end, fill="black",\
						width=data.blockWidth)
	canvas.create_line(end, start, start, end, fill="black",\
						width=data.blockWidth)

def drawCubeTwistEnd(canvas, data, colorList):
	#print(colorList)
	start = data.cubeLoc - data.diag/2
	end = data.cubeLoc + 3*data.blockSize + data.diag/2
	center = data.height/2
	diff = data.diag/2
	canvas.create_polygon(center, start, center-diff, start+diff,\
						center, center-diff, center+diff, start+diff,\
						fill = colorList[0], width = data.blockWidth)
	canvas.create_polygon(center+diff, start+diff, center, center-diff,\
						center+diff, center, end-diff, center-diff,\
						fill = colorList[1], width = data.blockWidth)
	canvas.create_polygon(end-diff, center-diff, end-data.diag, center,\
						end-diff, center+diff, end, center,\
						fill = colorList[2], width = data.blockWidth)
	canvas.create_polygon(center-diff, start+diff, start+diff, center-diff,\
						center-diff, center, center, center-diff,\
						fill = colorList[3], width = data.blockWidth)
	canvas.create_polygon(center, center-diff, center-diff, center,\
						center, center+diff, center+diff, center,\
						fill = colorList[4], width = data.blockWidth)
	canvas.create_polygon(center+diff, center, center, center+diff,\
						center+diff, end-diff, end-diff, center+diff,\
						fill = colorList[5], width = data.blockWidth)
	canvas.create_polygon(start+diff, center-diff, start, center,\
						start+diff, center+diff, center-diff, center,\
						fill = colorList[6], width = data.blockWidth)
	canvas.create_polygon(center-diff, center, start+diff, center+diff,\
						center-diff, end-diff, center, center+diff,\
						fill = colorList[7], width = data.blockWidth)
	canvas.create_polygon(center, center+diff, center-diff, end-diff,\
						center, end, center+diff, end-diff,\
						fill = colorList[8], width = data.blockWidth)
	drawTwistGrid(canvas, data)

def drawTwistGrid(canvas, data):
	start = data.cubeLoc - data.diag/2
	end = data.cubeLoc + 3*data.blockSize + data.diag/2
	center = data.cubeLoc+((3/2)*data.blockSize)
	diff = data.diag/2
	#lines from the left down
	canvas.create_line(center, start, end, center, fill="black",\
						width=data.blockWidth)
	canvas.create_line(center-diff, start+diff, end-diff, center+diff,\
						fill="black", width = data.blockWidth)
	canvas.create_line(start+diff, center-diff, center+diff, end-diff,\
						fill="black", width = data.blockWidth)
	canvas.create_line(start, center, center, end, fill="black",\
						width=data.blockWidth)
	#lines from the right down
	canvas.create_line(center, start, start, center, fill="black",\
						width=data.blockWidth)
	canvas.create_line(center+diff, start+diff, start+diff, center+diff,
						fill="black", width = data.blockWidth)
	canvas.create_line(end-diff, center-diff, center-diff, end-diff,\
						fill="black", width = data.blockWidth)
	canvas.create_line(end, center, center, end, fill="black",\
						width=data.blockWidth)

def twistFrontRightStart(data, colorList):
	newList = []
	for i in range(len(colorList)):
		newList.append(None)
	for oldSpot in range(len(colorList)):
		color = colorList[oldSpot]
		newSpot = (oldSpot + 2) % 8
		newList[newSpot] = color
		#print("old:", oldSpot, " new:", newSpot)
	#print(newList)
	return newList

def drawRestartBox(canvas, data):
	canvas.create_rectangle(10, data.height-40, 220, data.height-10,\
							fill = 'coral1', width = data.blockWidth)
	textLine = 'Click here to try another cube'
	textFont = "Arial "+str(roundHalfUp(15*(data.height/500)))
	canvas.create_text(115,data.height-25,text=textLine,\
						fill='black',font= textFont)


####################################
# use the run function as-is
####################################

def run(width=500, height=500):
	#print('1')
	def redrawAllWrapper(canvas, data):
		canvas.delete(ALL)
		canvas.create_rectangle(0, 0, data.width,\
								data.height,fill='LightSkyBlue1',
								width=0)
		redrawAll(canvas, data)
		canvas.update()    
		
	def mousePressedWrapper(event, canvas, data):
		mousePressed(event, data)
		redrawAllWrapper(canvas, data)
	
	def keyPressedWrapper(event, canvas, data):
		keyPressed(event, data)
		redrawAllWrapper(canvas, data)
	
	def timerFiredWrapper(canvas, data):
		timerFired(data)
		redrawAllWrapper(canvas, data)
		#pause, then call timerFired again
		canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
		#Set up data and call init
	class Struct(object): pass
	data = Struct()
	#print('2')
	data.width = width
	data.height = height
	data.timerDelay = 100 # milliseconds
	root = Tk()
	#print('3')
	init(data)
	#print('ugh')
	#print('why')
	#create the root and the canvas
	canvas = Canvas(root, width=data.width, height=data.height)
	canvas.pack()
	#set up events
	root.bind("<Button-1>", lambda event:
							mousePressedWrapper(event, canvas, data))
	root.bind("<Key>", lambda event:
							keyPressedWrapper(event, canvas, data))
	timerFiredWrapper(canvas, data)
	#and launch the app
	root.mainloop()  # blocks until window is closed
	print("bye!")

run(500,500)

