import math
import string
import random
import copy

wf = ['g','o','b','g','y','r','b','w']   
rf = ['r','y','y','y','w','o','g','b']
gf = ['b','w','w','y','w','b','w','b']
of = ['y','y','o','w','g','o','g','b']
bf = ['r','r','r','o','o','g','o','g']
yf = ['o','w','b','b','b','g','r','r']

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
        self.facesAround = [[rf,gf,of,bf],[wf,bf,yf,gf],[wf,rf,yf,of],\
                        [wf,gf,yf,bf],[wf,of,yf,rf],[rf,bf,of,gf]]
        self.allFaces = [self.wf, self.rf, self.gf, self.of, self.bf, self.yf]

    def solveFirstTierCross(self):
        for faceIndex in range(len(self.allFaces)):
            face = self.allFaces[faceIndex]
            print(face)
            if faceIndex == 0:
                self.solveFirstTierCrossTop(face, faceIndex)
            '''
            elif faceIndex in {1,2,3,4}:
                for pieceIndex in range(len(face)):
                    if pieceIndex%2 == 1:
                        piece = face[pieceIndex]
                        if piece == 'w':
                            diff = 5 - pieceIndex
                            if diff == 0:
                                pass
                            elif diff == 2:
                                pass
                            elif diff == 4:
                                self.turnTopRight(faceIndex)
                                self.turnRightDown(faceIndex)
                                self.turnFaceRight(faceIndex)'''
            print("all faces", self.allFaces)

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
    
    def findOtherFace(self, faceIndex, pieceIndex):
        if faceIndex == 0:
            return (self.allFaces[pieceIndex//2+1], faceIndex+(pieceIndex//2)+1)
    
    def firstTierCrossMoveTop(self, diff, faceIndex):
        if diff==1:
            self.turnFaceLeft(faceIndex)
        elif diff==2:
            self.turnFaceRight(faceIndex)
            self.turnFaceRight(faceIndex)
        elif diff==3:
            self.turnFaceRight(faceIndex)

    def turnFaceRight(self, faceIndex):
        print('beginning', self.wf)
        currentFace = self.faceNameOrder[faceIndex]
        printStatement = 'Turn the ' + currentFace + ' face to the right'
        print(printStatement)
        faceList = self.allFaces[faceIndex]
        newFace = copy.copy(faceList)
        for piece in range(len(faceList)):
            newPos = (piece+2)%8
            newFace[newPos] = faceList[piece]
        print('newface', newFace)
        self.allFaces[faceIndex] = newFace
        print('ending', self.wf)
        tier = []
        for side in self.facesAround[faceIndex]:
            tier.append(side[0])
            tier.append(side[1])
            tier.append(side[2])
        for i in range(len(self.facesAround[faceIndex])):
            face = self.facesAround[faceIndex][i]
            if i==0:
                face[0] = tier[9]
                face[1] = tier[10]
                face[2] = tier[11]
            else:
                face[0] = tier[(i-1)*3]
                face[1] = tier[(i-1)*3+1]
                face[2] = tier[(i-1)*3+2]
            self.face = face
            print(faceIndex, face)
  
    def turnFaceLeft(self, faceIndex):
        currentFace = faceNameOrder[faceIndex]
        printStatement = 'Turn the ' + currentFace + ' face to the left'
        print(printStatement)
        faceList = allFaces[faceIndex]
        newFace = copy.copy(faceList)
        for piece in rangeren(len(faceList)):
            newPos = (piece-2)%8
            newFace[newPos] = faceList[piece]
        tier = []
        for side in facesAround[faceIndex]:
            tier.append(side[0])
            tier.append(side[1])
            tier.append(side[2])
        for i in facesAround[faceIndex]:
            face = facesAround[faceIndex][i]
            if i==3:
                face[0] = tier[0]
                face[1] = tier[1]
                face[2] = tier[2]
            else:
                face[0] = tier[(i+1)*3]
                face[1] = tier[(i+1)*3+1]
                face[2] = tier[(i+1)*3+2]

    def turnTopRight(self, oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        printStatement = 'Turn the top of the ' + currentFace + ' face to the right'
        print(printStatement)
        if oldFaceIndex == 0 or oldFaceIndex == 5:
            faceIndex = 1
        else:
            faceIndex = 0
        faceList = self.allFaces[faceIndex]
        newFace = copy.copy(faceList)
        for piece in range(len(faceList)):
            newPos = (piece-2)%8
            newFace[newPos] = faceList[piece]
        tier = []
        for side in self.facesAround[faceIndex]:
            tier.append(side[0])
            tier.append(side[1])
            tier.append(side[2])
        for i in range(len(self.facesAround[faceIndex])):
            face = self.facesAround[faceIndex][i]
            if i==3:
                face[0] = tier[0]
                face[1] = tier[1]
                face[2] = tier[2]
            else:
                face[0] = tier[(i+1)*3]
                face[1] = tier[(i+1)*3+1]
                face[2] = tier[(i+1)*3+2]
  
    def turnTopLeft(self,oldFaceIndex):
        currentFace = faceNameOrder[oldFaceIndex]
        printStatement = 'Turn the top of the ' + currentFace + ' face to the left'
        print(printStatement)
        if oldFaceIndex == 0 or oldFaceIndex == 5:
            faceIndex = 1
        else:
            faceIndex = 0
        faceList = allFaces[faceIndex]
        newFace = copy.copy(faceList)
        for piece in rangeren(len(faceList)):
            newPos = (piece-2)%8
            newFace[newPos] = faceList[piece]
        tier = []
        for side in facesAround[faceIndex]:
            tier.append(side[0])
            tier.append(side[1])
            tier.append(side[2])
        for i in facesAround[faceIndex]:
            face = facesAround[faceIndex][i]
            if i==3:
                face[0] = tier[0]
                face[1] = tier[1]
                face[2] = tier[2]
            else:
                face[0] = tier[(i+1)*3]
                face[1] = tier[(i+1)*3+1]
                face[2] = tier[(i+1)*3+2]
  
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
        faceList = allFaces[faceIndex]
        newFace = copy.copy(faceList)
        for piece in range(len(faceList)):
            newPos = (piece+2)%8
            newFace[newPos] = faceList[piece]
        faceList = newFace
        tier = []
        for side in facesAround[faceIndex]:
            tier.append(side[0])
            tier.append(side[1])
            tier.append(side[2])
        for i in range(len(facesAround[faceIndex])):
            face = facesAround[faceIndex][i]
            if i==0:
                face[0] = tier[9]
                face[1] = tier[10]
                face[2] = tier[11]
            else:
                face[0] = tier[(i-1)*3]
                face[1] = tier[(i-1)*3+1]
                face[2] = tier[(i-1)*3+2]
            print(faceIndex, face)
  
    def turnRightDown(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        printStatement = 'Turn the right side of the ' + currentFace + ' face down'
        print(printStatement)
        if oldFaceIndex == 0:
            faceIndex = 2
        elif oldFaceIndex == 5 or oldFaceIndex == 1:
            faceIndex = 4
        else:
            faceIndex = oldFaceIndex-1
        faceList = self.allFaces[faceIndex]
        newFace = copy.copy(faceList)
        for piece in range(len(faceList)):
            newPos = (piece-2)%8
            newFace[newPos] = faceList[piece]
        tier = []
        for side in self.facesAround[faceIndex]:
            tier.append(side[0])
            tier.append(side[1])
            tier.append(side[2])
        for i in range(len(self.facesAround[faceIndex])):
            face = self.facesAround[faceIndex][i]
            if i==3:
                face[0] = tier[0]
                face[1] = tier[1]
                face[2] = tier[2]
            else:
                face[0] = tier[(i+1)*3]
                face[1] = tier[(i+1)*3+1]
                face[2] = tier[(i+1)*3+2]

cube = Cube(wf,rf,gf,of,bf,yf)

cube.solveFirstTierCross()