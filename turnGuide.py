from tkinter import *




def drawTurnGuideGrid(canvas):
    height = 500
    width = 500
    blockSize = height/9
    cubeLoc = blockSize*3
    blockWidth = 5 *((min(height,width))/500)
    y1 = 25*(height/500)
    y2 = height-25*(height/500)
    canvas.create_line(100*(width/500), y1, 100*(width/500), y2, \
                        fill='black', width=blockWidth)
    canvas.create_line(width/2, y1, width/2, y2, \
                        fill='black', width=blockWidth)
    canvas.create_line(width-100*(width/500), y1, width-100*(width/500), \
                        y2, fill='black', \
                        width=blockWidth)
    x1 = 100*(width/500)
    x2 = width-100*(width/500)
    for i in range(6):
        y = 25*(height/500) + 90*(height/500)*i
        canvas.create_line(x1, y, x2, y, fill='black',width=blockWidth)
    
def drawTurnGuideText(canvas):
    height = 500
    width = 500
    blockSize = height/9
    cubeLoc = blockSize*3
    blockWidth = 5 *((min(height,width))/500)
    textList = ['Turn face', 'Turn right side', 'Turn left side', 'Turn top',\
                'Turn bottom']
    x = (175)*(width/500)
    textFont = "Arial "+ str(int(19*(height/500)))+ " bold"
    textLine = textList[0]
    print(textLine)
    for i in range(5):
        textLine = textList[i]
        print(textLine)
        y = 70*(height/500) + 90*(height/500)*i
        canvas.create_text(x,y,text=textLine,fill='black',font=textFont)
    
def drawTurnFaceIcon(canvas):
    print('hi')
    height = 500
    width = 500
    size = 14*(width/500)
    blockWidth = 2*(width/500)
    cubeLocX = (325)*(width/500) - 21*(width/500)
    cubeLocY = 70*(height/500) - 21*(width/500)
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
    blockWidth = 1.5*(width/500)
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

def drawTurnRightSideIcon(canvas):
    height = 500
    width = 500
    cubeLocX = (325)*(width/500) - 24*(width/500)
    cubeLocY = 160*(height/500) - 24*(width/500)
    size = 16*(width/500)
    blockWidth = 2*(width/500)
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

def drawTurnLeftSideIcon(canvas):
    height = 500
    width = 500
    cubeLocX = (325)*(width/500) - 24*(width/500)
    cubeLocY = 250*(height/500) - 24*(width/500)
    size = 16*(width/500)
    blockWidth = 2*(width/500)
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

def drawTurnTopIcon(canvas):
    height = 500
    width = 500
    cubeLocX = (325)*(width/500) - 24*(width/500)
    cubeLocY = 340*(height/500) - 24*(width/500)
    size = 16*(width/500)
    blockWidth = 2*(width/500)
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

def drawTurnBottomIcon(canvas):
    height = 500
    width = 500
    cubeLocX = (325)*(width/500) - 24*(width/500)
    cubeLocY = 430*(height/500) - 24*(width/500)
    size = 16*(width/500)
    blockWidth = 2*(width/500)
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
    
def drawTurnIcons(canvas):
    drawTurnFaceIcon(canvas)
    drawTurnRightSideIcon(canvas)
    drawTurnLeftSideIcon(canvas)
    drawTurnTopIcon(canvas)
    drawTurnBottomIcon(canvas)
    
def drawGoBackBox(canvas):
    width = 500
    height = 500
    canvas.create_rectangle(10*(width/500), \
                            height-47*(height/500), \
                            85*(width/500), \
                            height-10*(height/500),\
                            fill = 'lightblue', width = 3*(width/500))
    textLine1 = 'Click here to'
    textLine2 = 'go back'
    textFont = "Arial "+str(int(12*(height/500)))
    canvas.create_text(47*(width/500),height-35*(height/500), \
                        text=textLine1, fill='black', font= textFont)
    canvas.create_text(47*(width/500),height-22*(height/500), \
                        text=textLine2, fill='black', font= textFont)

def draw(canvas, width, height):
    drawTurnGuideGrid(canvas)
    drawTurnGuideText(canvas)
    drawTurnIcons(canvas)
    drawGoBackBox(canvas)

def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")

runDrawing(500, 500)