import math
import string
import random
import copy

wf = ['o','b','w','r','b','r','w','w']   
rf = ['b','o','w','o','r','g','w','w']
gf = ['o','w','r','b','g','y','o','o']
of = ['g','y','y','g','y','b','b','g']
bf = ['b','o','o','r','r','r','y','y']
yf = ['r','w','g','b','y','y','g','g']

class Cube(object):
    def __init__(self,wf,rf,gf,of,bf,yf):
        self.wf = wf
        self.rf = rf
        self.gf = gf
        self.of = of
        self.bf = bf
        self.yf = yf
        self.faceOrder = ["w", "r", "g", "o", "b", "y"]
        self.faceNameOrder = ['white','red','green','orange','blue','yellow']
        #self.facesAround = [[rf,gf,of,bf],[wf,bf,yf,gf],[wf,rf,yf,of],\
                        #[wf,gf,yf,bf],[wf,of,yf,rf],[rf,bf,of,gf]]
        self.facesAround =[[[1,0],[2,0],[3,0],[4,0]],\
                           [[0,0],[4,6],[5,0],[2,2]],\
                           [[0,2],[1,6],[5,6],[3,2]],\
                           [[0,4],[2,6],[5,4],[4,2]],\
                           [[0,6],[3,6],[5,2],[1,2]],\
                           [[1,4],[4,4],[3,4],[2,4]]]
        self.allFaces = [self.wf, self.rf, self.gf, self.of, self.bf, self.yf]

    def getAllFaces(self):
        allFaces = []
        allFaces.append(self.wf)
        allFaces.append(self.rf)
        allFaces.append(self.gf)
        allFaces.append(self.of)
        allFaces.append(self.bf)
        allFaces.append(self.yf)
        return allFaces

    def getFace(self, faceIndex):
        if faceIndex == 0:
            return self.wf
        elif faceIndex == 1:
            return self.rf
        elif faceIndex == 2:
            return self.gf
        elif faceIndex == 3:
            return self.of
        elif faceIndex == 4:
            return self.bf
        elif faceIndex == 5:
            return self.yf
    
    def getFaceIndex(self, face):
        if face == self.wf:
            return 0
        elif face == self.rf:
            return 1
        elif face == self.gf:
            return 2
        elif face == self.of:
            return 3
        elif face == self.bf:
            return 4
        elif face == self.yf:
            return 5
    
    def assignNew(self, faceIndex, newList):
        if faceIndex == 0:
            self.wf = newList
        elif faceIndex == 1:
            self.rf = newList
        elif faceIndex == 2:
            self.gf = newList
        elif faceIndex == 3:
            self.of = newList
        elif faceIndex == 4:
            self.bf = newList
        elif faceIndex == 5:
            self.yf = newList

    def solveFirstTierCross(self):
        for faceIndex in range(len(self.allFaces)):
            face = self.getFace(faceIndex)
            print(face)
            if faceIndex == 0:
                self.solveFirstTierCrossTop(face, faceIndex)
            elif faceIndex in {1,2,3,4}:
                self.solveFirstTierCrossMiddle(faceIndex)
            print("all faces", self.getAllFaces())

    def solveFirstTierCrossTop(self, face, faceIndex):
        pieceIndex = 0
        for pieceIndex in range(len(face)):
            piece = face[pieceIndex]
            if pieceIndex%2 == 1:
                if piece == "w":
                    otherFace, otherFaceIndex = \
                                        self.findOtherFace(faceIndex, pieceIndex)
                    if otherFace[1] != self.faceOrder[otherFaceIndex]:
                        otherColor = otherFace[1]
                        otherColorIndex = self.faceOrder.index(otherColor)
                        diff = otherFaceIndex - otherColorIndex
                        self.firstTierCrossMoveTop(diff, faceIndex)
    
    def solveFirstTierCrossMiddle(self, faceIndex):
        face = copy.copy(self.getFace(faceIndex))
        for pieceIndex in range(len(face)):
            if pieceIndex%2 == 1:
                piece = face[pieceIndex]
                if piece == 'w':
                    diff = 5 - pieceIndex
                    if diff == -2:
                        self.turnFaceRight(faceIndex)
                        self.turnTopRight(faceIndex)
                        self.turnRightDown(faceIndex)
                        self.turnFaceRight(faceIndex)
                    elif diff == 2:
                        self.turnFaceLeft(faceIndex)
                        self.turnTopRight(faceIndex)
                        self.turnRightDown(faceIndex)
                        self.turnFaceRight(faceIndex)
                    elif diff == 4:
                        self.turnTopRight(faceIndex)
                        self.turnRightDown(faceIndex)
                        current = copy.copy(self.getFace(faceIndex))
                        print('current', current[3])
                        print('middle', self.faceOrder[faceIndex])
                        if self.faceOrder[faceIndex] == current[3]:
                            self.turnFaceLeft(faceIndex)
                            break
                        self.turnFaceRight(faceIndex)
        newFace = copy.copy(self.getFace(faceIndex))
        color = newFace[5]
        colorIndex = self.faceOrder.index(color)
        newDiff = colorIndex - faceIndex
        if newDiff == 0:
            self.turnFaceRight(faceIndex)
            self.turnFaceRight(faceIndex)
        elif newDiff == 1 or newDiff == -3:
            self.turnBottomLeft(faceIndex)
            self.turnFaceRight(faceIndex)
            self.turnFaceRight(faceIndex)
        elif newDiff == 3 or newDiff == -1:
            self.turnBottomRight(faceIndex)
            self.turnFaceRight(faceIndex)
            self.turnFaceRight(faceIndex)
        elif newDiff == 2 or newDiff == -2:
            self.turnBottomRight(faceIndex)
            self.turnBottomRight(faceIndex)
            self.turnFaceRight(faceIndex)
            self.turnFaceRight(faceIndex)
    
    def findOtherFace(self, faceIndex, pieceIndex):
        if faceIndex == 0:
            return (self.getFace(pieceIndex//2+1), faceIndex+(pieceIndex//2)+1)
    
    def firstTierCrossMoveTop(self, diff, faceIndex):
        if diff==1:
            self.turnFaceLeft(faceIndex)
        elif diff==2:
            self.turnFaceRight(faceIndex)
            self.turnFaceRight(faceIndex)
        elif diff==3:
            self.turnFaceRight(faceIndex)

    def turnRight(self, faceIndex):
        faceList = copy.copy(self.getFace(faceIndex))
        newFace = copy.copy(faceList)
        for piece in range(len(faceList)):
            newPos = (piece+2)%8
            newFace[newPos] = faceList[piece]
        self.assignNew(faceIndex, newFace)
        tier = []
        for j in range(len(self.facesAround[faceIndex])):
            side = copy.copy(self.getFace(self.facesAround[faceIndex][j][0]))
            start1 = self.facesAround[faceIndex][j][1]
            tier.append(side[0])
            tier.append(side[1])
            tier.append(side[2])
        #print('TIER', tier)
        for i in range(len(self.facesAround[faceIndex])):
            face = copy.copy(self.getFace(self.facesAround[faceIndex][i][0]))
            start2 = self.facesAround[faceIndex][i][1]
            #print(face, start2)
            if i==0:
                face[(start2)%8] = tier[9]
                face[(start2+1)%8] = tier[10]
                face[(start2+2)%8] = tier[11]
                #print('redface', face)
            else:
                face[(start2)%8] = tier[(i-1)*3]
                face[(start2+1)%8] = tier[(i-1)*3+1]
                face[(start2+2)%8] = tier[(i-1)*3+2]
            self.assignNew(self.facesAround[faceIndex][i][0], face)
        #print("all faces", self.getAllFaces())

    def turnLeft(self, faceIndex):
        faceList = copy.copy(self.getFace(faceIndex))
        newFace = copy.copy(faceList)
        for piece in range(len(faceList)):
            newPos = (piece-2)%8
            newFace[newPos] = faceList[piece]
        self.assignNew(faceIndex, newFace)
        tier = []
        for j in range(len(self.facesAround[faceIndex])):
            #print('AHHHH', self.facesAround[faceIndex][j][0])
            side = copy.copy(self.getFace(self.facesAround[faceIndex][j][0]))
            start1 = self.facesAround[faceIndex][j][1]
            #print('side', side)
            tier.append(side[(start1)%8])
            tier.append(side[(start1+1)%8])
            tier.append(side[(start1+2)%8])
        #print('FINDEX', faceIndex)
        #print('TIER', tier)
        for i in range(len(self.facesAround[faceIndex])):
            face = copy.copy(self.getFace(self.facesAround[faceIndex][i][0]))
            start2 = self.facesAround[faceIndex][i][1]
            if i==3:
                face[(start2)%8] = tier[0]
                face[(start2+1)%8] = tier[1]
                face[(start2+2)%8] = tier[2]
            else:
                face[(start2)%8] = tier[(i+1)*3]
                face[(start2+1)%8] = tier[(i+1)*3+1]
                face[(start2+2)%8] = tier[(i+1)*3+2]
            self.assignNew(self.facesAround[faceIndex][i][0], face)
        #print("all faces", self.getAllFaces())

    def turnFaceRight(self, faceIndex):
        currentFace = self.faceNameOrder[faceIndex]
        printStatement = 'Turn the ' + currentFace + ' face to the right'
        print(printStatement)
        self.turnRight(faceIndex)
  
    def turnFaceLeft(self, faceIndex):
        currentFace = self.faceNameOrder[faceIndex]
        printStatement = 'Turn the ' + currentFace + ' face to the left'
        print(printStatement)
        self.turnLeft(faceIndex)

    def turnTopRight(self, oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        printStatement = 'Turn the top of the ' + currentFace + ' face to the right'
        print(printStatement)
        if oldFaceIndex == 0 or oldFaceIndex == 5:
            faceIndex = 1
        else:
            faceIndex = 0
        self.turnLeft(faceIndex)
  
    def turnTopLeft(self,oldFaceIndex):
        currentFace = faceNameOrder[oldFaceIndex]
        printStatement = 'Turn the top of the ' + currentFace + ' face to the left'
        print(printStatement)
        if oldFaceIndex == 0 or oldFaceIndex == 5:
            faceIndex = 1
        else:
            faceIndex = 0
        self.turnRight(faceIndex)
  
    def turnRightUp(self,oldFaceIndex):
        currentFace = faceNameOrder[oldFaceIndex]
        printStatement = 'Turn the right side of the ' + currentFace + ' face up'
        print(printStatement)
        if oldFaceIndex == 0:
            faceIndex = 2
        elif oldFaceIndex == 5 or oldFaceIndex == 1:
            faceIndex = 4
        else:
            faceIndex = oldFaceIndex-1
        self.turnRight(faceIndex)
  
    def turnRightDown(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        printStatement = 'Turn the right side of the ' + currentFace +\
                            ' face down'
        print(printStatement)
        if oldFaceIndex == 0:
            faceIndex = 2
        elif oldFaceIndex == 5 or oldFaceIndex == 1:
            faceIndex = 4
        else:
            faceIndex = oldFaceIndex-1
        self.turnLeft(faceIndex)
    
    def turnBottomRight(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        printStatement = 'Turn the botton of the ' + currentFace + ' face right'
        print(printStatement)
        if oldFaceIndex == 0:
            faceIndex = 3
        elif oldFaceIndex == 5:
            faceIndex = 3
        else:
            faceIndex = 5
        self.turnRight(faceIndex)
    
    def turnBottomLeft(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        printStatement = 'Turn the botton of the ' + currentFace + ' face left'
        print(printStatement)
        if oldFaceIndex == 0:
            faceIndex = 3
        elif oldFaceIndex == 5:
            faceIndex = 3
        else:
            faceIndex = 5
        self.turnLeft(faceIndex)
        

cube = Cube(wf,rf,gf,of,bf,yf)

cube.solveFirstTierCross()