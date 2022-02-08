import math
import string
import random
import copy

wf = ['o','r','o','o','y','o','r','r']   
rf = ['w','w','y','y','y','g','w','g']
gf = ['b','g','g','w','g','g','r','y']
of = ['w','w','o','r','g','y','w','b']
bf = ['g','b','b','w','b','b','r','o']
yf = ['r','y','b','o','o','b','y','r']

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
        self.facesAround =[[[1,0],[2,0],[3,0],[4,0]],\
                           [[0,0],[4,6],[5,0],[2,2]],\
                           [[0,2],[1,6],[5,6],[3,2]],\
                           [[0,4],[2,6],[5,4],[4,2]],\
                           [[0,6],[3,6],[5,2],[1,2]],\
                           [[1,4],[4,4],[3,4],[2,4]]]
        self.faceUp = ['red', 'white', 'white', 'white', 'white', 'red']
        self.masterList = [["Get ready to solve the Rubik's Cube", \
                        'Press the spacebar after you have completed a move']]
        self.moveCount = 0
        self.possiblePieces = [['w','r'],['w','g'],['w','o'],['w','b'],\
                            ['r','g'],['g','o'],['o','b'],['b','r'],\
                            ['y','r'],['y','g'],['y','o'],['y','b'],\
                            ['w','r','g'],['w','g','o'],['w','o','b'],\
                            ['w','b','r'],['y','r','g'],['y','g','o'],\
                            ['y','o','b'],['y','b','r']]

### HELPER FUNCTIONS ###

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
    
    def isOtherSide(self, faceIndex, pieceIndex, color):
        newSideIndex = self.facesAround[faceIndex][pieceIndex//2][0]
        sideFace = copy.copy(self.getFace(newSideIndex))
        newIndex = self.facesAround[faceIndex][pieceIndex//2][1] + 1
        checkPiece = sideFace[newIndex]
        if checkPiece == color:
            return True
        return False
    
    def getOtherSide(self, faceIndex, pieceIndex):
        newSideIndex = self.facesAround[faceIndex][pieceIndex//2][0]
        sideFace = copy.copy(self.getFace(newSideIndex))
        newIndex = self.facesAround[faceIndex][pieceIndex//2][1] + 1
        checkPiece = sideFace[newIndex]
        return checkPiece

    def checkIsRightPiece(self, faceIndex, pieceIndex):
        face = copy.copy(self.getFace(faceIndex))
        colorIndex = self.faceOrder.index(face[pieceIndex])
        if colorIndex == faceIndex:
            return True
        return True

    def getOtherCornerPieces(self, faceIndex, pieceIndex):
        if faceIndex == 0:
            #print('hi')
            if pieceIndex == 0:
                #print('yes')
                face1 = copy.copy(self.getFace(1))
                face2 = copy.copy(self.getFace(4))
            elif pieceIndex%2==0:
                face1 = copy.copy(self.getFace(pieceIndex//2+1))
                face2 = copy.copy(self.getFace(pieceIndex//2))
            return face1[2], face2[0]
        if faceIndex == 5:
            if pieceIndex == 0:
                face1 = copy.copy(self.getFace(1))
                face2 = copy.copy(self.getFace(2))
            elif pieceIndex == 2:
                face1 = copy.copy(self.getFace(4))
                face2 = copy.copy(self.getFace(1))
            elif pieceIndex == 4:
                face1 = copy.copy(self.getFace(3))
                face2 = copy.copy(self.getFace(4))
            elif pieceIndex == 6:
                face1 = copy.copy(self.getFace(2))
                face2 = copy.copy(self.getFace(3))
            return face1[6], face2[4]
    
    def masterListCube(self, faceIndex):
        faceList = copy.copy(self.getFace(faceIndex))
        face = self.faceOrder[faceIndex]
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
    
    def correctOrderCubeFace(self, face, faceList):
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
    
    def masterListFaces(self, faceIndex):
        faces = []
        frontFace = self.masterListCube(faceIndex)
        faces.append(frontFace)
        topFaceIndex = self.facesAround[faceIndex][0][0]
        topFaceName = self.faceNameOrder[topFaceIndex]
        topFaceStart = self.facesAround[faceIndex][0][1]
        oldTopFace = copy.copy(self.getFace(topFaceIndex))
        editTopFace = []
        for i in range(8):
            editTopFace.append(oldTopFace[(topFaceStart+4+i)%8])
        topFace = self.correctOrderCubeFace(topFaceName, editTopFace)
        faces.append(topFace)
        rightFaceIndex = self.facesAround[faceIndex][1][0]
        rightFaceName = self.faceNameOrder[rightFaceIndex]
        rightFaceStart = self.facesAround[faceIndex][1][1]
        oldRightFace = copy.copy(self.getFace(rightFaceIndex))
        editRightFace = []
        for i in range(8):
            editRightFace.append(oldRightFace[(rightFaceStart+2+i)%8])
        rightFace = self.correctOrderCubeFace(rightFaceName, editRightFace)
        faces.append(rightFace)
        return faces
    
    def isLegalCube(self):
        #print("all faces", self.getAllFaces())
        possiblePieces = copy.deepcopy(self.possiblePieces)
        for faceIndex in range(0,6):
            face = copy.copy(self.getFace(faceIndex))
            if 0 in face:
                return False
        for color in self.faceOrder:
            colorCount = 0
            for faceIndex in range(0,6):
                face = copy.copy(self.getFace(faceIndex))
                colorCount += face.count(color)
            #print(color, colorCount) 
            if colorCount != 8:
                return False
        for whiteCross in range(1,8,2):
            piece1 = self.wf[whiteCross]
            piece2 = self.getOtherSide(0,whiteCross)
            try1 = [piece1, piece2]
            try2 = [piece2, piece1]
            #print(try1, try2, possiblePieces)
            if try1 in possiblePieces:
                index = possiblePieces.index(try1)
                possiblePieces.pop(index)
            elif try2 in possiblePieces:
                index = possiblePieces.index(try2)
                possiblePieces.pop(index)
            elif (try1 not in possiblePieces) and (try2 not in possiblePieces):
                return False
        for yellowCross in range(1,8,2):
            piece1 = self.yf[yellowCross]
            piece2 = self.getOtherSide(5,yellowCross)
            try1 = [piece1, piece2]
            try2 = [piece2, piece1]
            #print(try1, try2, possiblePieces)
            if try1 in possiblePieces:
                index = possiblePieces.index(try1)
                possiblePieces.pop(index)
            elif try2 in possiblePieces:
                index = possiblePieces.index(try2)
                possiblePieces.pop(index)
            elif (try1 not in possiblePieces) and (try2 not in possiblePieces):
                return False
        for middleIndex in range(1,5):
            face = copy.copy(self.getFace(middleIndex))
            piece1 = face[3]
            piece2 = self.getOtherSide(middleIndex,3)
            try1 = [piece1, piece2]
            try2 = [piece2, piece1]
            #print(try1, try2, possiblePieces)
            if try1 in possiblePieces:
                index = possiblePieces.index(try1)
                possiblePieces.pop(index)
            elif try2 in possiblePieces:
                index = possiblePieces.index(try2)
                possiblePieces.pop(index)
            elif (try1 not in possiblePieces) and (try2 not in possiblePieces):
                return False
        for whiteCorner in range(0,8,2):
            piece1 = self.wf[whiteCorner]
            piece2, piece3 = self.getOtherCornerPieces(0, whiteCorner)
            try1 = [piece1, piece2, piece3]
            try2 = [piece1, piece3, piece2]
            try3 = [piece2, piece1, piece3]
            try4 = [piece2, piece3, piece1]
            try5 = [piece3, piece1, piece2]
            try6 = [piece3, piece2, piece1]
            #print(try1, try2, try3,try4, try5, try6,possiblePieces)
            if try1 in possiblePieces:
                index = possiblePieces.index(try1)
                possiblePieces.pop(index)
            elif try2 in possiblePieces:
                index = possiblePieces.index(try2)
                possiblePieces.pop(index)
            elif try3 in possiblePieces:
                index = possiblePieces.index(try3)
                possiblePieces.pop(index)
            elif try4 in possiblePieces:
                index = possiblePieces.index(try4)
                possiblePieces.pop(index)
            elif try5 in possiblePieces:
                index = possiblePieces.index(try5)
                possiblePieces.pop(index)
            elif try6 in possiblePieces:
                index = possiblePieces.index(try6)
                possiblePieces.pop(index)
            elif (try1 not in possiblePieces) and (try2 not in possiblePieces)\
             and (try3 not in possiblePieces) and (try4 not in possiblePieces)\
             and (try5 not in possiblePieces) and (try6 not in possiblePieces):
                return False
        return True
        for yellowCorner in range(0,8,2):
            piece1 = self.yf[yellowCorner]
            piece2, piece3 = self.getOtherCornerPieces(5, yellowCorner)
            try1 = [piece1, piece2, piece3]
            try2 = [piece1, piece3, piece2]
            try3 = [piece2, piece1, piece3]
            try4 = [piece2, piece3, piece1]
            try5 = [piece3, piece1, piece2]
            try6 = [piece3, piece2, piece1]
            #print(try1, try2, try3,try4, try5, try6,possiblePieces)
            if try1 in possiblePieces:
                index = possiblePieces.index(try1)
                possiblePieces.pop(index)
            elif try2 in possiblePieces:
                index = possiblePieces.index(try2)
                possiblePieces.pop(index)
            elif try3 in possiblePieces:
                index = possiblePieces.index(try3)
                possiblePieces.pop(index)
            elif try4 in possiblePieces:
                index = possiblePieces.index(try4)
                possiblePieces.pop(index)
            elif try5 in possiblePieces:
                index = possiblePieces.index(try5)
                possiblePieces.pop(index)
            elif try6 in possiblePieces:
                index = possiblePieces.index(try6)
                possiblePieces.pop(index)
            elif (try1 not in possiblePieces) and (try2 not in possiblePieces)\
             and (try3 not in possiblePieces) and (try4 not in possiblePieces)\
             and (try5 not in possiblePieces) and (try6 not in possiblePieces):
                return False
        return True

### SOLVE FIRST TIER CROSS ###

    def solveFirstTierCross(self):
        #print('SOLVE FIRST TIER CROSS START')
        #print("all faces", self.getAllFaces())
        if not self.firstTierCrossDone():
            for faceIndex in range(6):
                face = self.getFace(faceIndex)
                #print('index', faceIndex, 'face', face)
                if faceIndex == 0:
                    #print('white')
                    self.solveFirstTierCrossTop(faceIndex)
                    #self.solveFirstTierCross()
                    #print("all faces", self.getAllFaces())
                elif faceIndex in [1,2,3,4]:
                    #print('middle', faceIndex)
                    self.solveFirstTierCrossMiddle(faceIndex)
                    #self.solveFirstTierCross()
                    #print("all faces", self.getAllFaces())
                elif faceIndex == 5:
                    #print('yellow')
                    #print('yes')
                    self.solveFirstTierCrossBottom(faceIndex)
                    #self.solveFirstTierCross()
                    #print("all faces", self.getAllFaces())
            self.solveFirstTierCross()
    
    def firstTierCrossDone(self):
        whiteFace = copy.copy(self.getFace(0))
        #print('WHITEFACE', whiteFace)
        if whiteFace[1] == 'w' and whiteFace[3] == 'w' and \
            whiteFace[5] == 'w' and whiteFace[7] == 'w' and \
            self.getOtherSide(0, 1)=='r' and self.getOtherSide(0, 3)=='g' \
            and self.getOtherSide(0, 5)=='o' and self.getOtherSide(0, 7)=='b':
            return True
        else:
            return False
    
    def solveFirstTierCrossTop(self, faceIndex):
        pieceIndex = 0
        for pieceIndex in range(8):
            face = self.getFace(faceIndex)
            piece = face[pieceIndex]
            if pieceIndex%2 == 1:
                if piece == "w":
                    otherPiece = self.getOtherSide(faceIndex, pieceIndex)
                    otherPieceIndex = self.faceOrder.index(otherPiece)
                    otherFaceIndex=self.facesAround[faceIndex][pieceIndex//2][0]
                    if otherFaceIndex != otherPieceIndex:
                        diff = otherFaceIndex - otherPieceIndex
                        self.firstTierCrossMoveTop(diff, faceIndex)
        self.checkFirstTierCrossTop(faceIndex)
    
    def checkFirstTierCrossTop(self, faceIndex):
        pieceIndex = 0
        for pieceIndex in range(8):
            face = self.getFace(faceIndex)
            piece = face[pieceIndex]
            if pieceIndex%2 == 1:
                if piece == "w":
                    otherPiece = self.getOtherSide(faceIndex, pieceIndex)
                    otherPieceIndex = self.faceOrder.index(otherPiece)
                    otherFaceIndex=self.facesAround[faceIndex][pieceIndex//2][0]
                    if otherFaceIndex != otherPieceIndex:
                        self.turnFaceRight(otherFaceIndex)
                        self.turnFaceRight(otherFaceIndex)
                        newFaceIndex = 5
                        self.solveFirstTierCrossBottom(newFaceIndex)
    
    def firstTierCrossMoveTop(self, diff, faceIndex):
        if diff == 1 or diff == -3:
            self.turnFaceLeft(faceIndex)
        elif diff == 2 or diff == -2:
            self.turnFaceRight(faceIndex)
            self.turnFaceRight(faceIndex)
        elif diff == 3 or diff == -1:
            self.turnFaceRight(faceIndex)
    
    def solveFirstTierCrossMiddle(self, faceIndex):
        #print('face update',face)
        for pieceIndex in range(8):
            face = copy.copy(self.getFace(faceIndex))
            if pieceIndex == 1 and face[pieceIndex] == 'w':
                #print('1')
                self.turnFaceRight(faceIndex)
                self.turnRightDown(faceIndex)
                self.turnBottomLeft(faceIndex)
                self.turnRightUp(faceIndex)
                newFace = self.solveFirstTierCrossMiddleHelp(faceIndex)
                #print(newFace)
                self.turnFaceRight(newFace)
                self.turnFaceRight(newFace)
                self.solveFirstTierCrossMiddle(faceIndex)
            elif pieceIndex == 3 and face[pieceIndex] == 'w':
                #print('2')
                otherSide = self.getOtherSide(faceIndex, pieceIndex)
                otherIndex = self.faceOrder.index(otherSide)
                if otherIndex == (faceIndex+2)%4 + 1:
                    self.turnRightUp(faceIndex)
                else:
                    self.turnRightDown(faceIndex)
                    self.turnBottomLeft(faceIndex)
                    self.turnRightUp(faceIndex)
                    newFace = self.solveFirstTierCrossMiddleHelp(faceIndex)
                    self.turnFaceRight(newFace)
                    self.turnFaceRight(newFace)
                    self.solveFirstTierCrossMiddle(faceIndex)
            elif pieceIndex == 5 and face[pieceIndex] == 'w':
                #print('3')
                piece = self.getOtherSide(faceIndex, pieceIndex)
                #print('piece', piece)
                #print('othersidepiece', piece)
                pieceIndex = self.faceOrder.index(piece)
                #print(pieceIndex, faceIndex)
                diff = pieceIndex - faceIndex
                #print('diff', diff)
                if diff == -1 or diff == 3:
                    self.turnFaceLeft(faceIndex)
                    self.turnRightUp(faceIndex)
                    self.turnFaceRight(faceIndex)
                elif diff == 1 or diff == -3:
                    self.turnFaceRight(faceIndex)
                    self.turnLeftUp(faceIndex)
                    self.turnFaceLeft(faceIndex)
                if diff == 2 or diff == -2:
                    #print('woo')
                    self.turnBottomRight(faceIndex)
                    self.turnFaceLeft((faceIndex+2)%4+1)
                    self.turnRightUp((faceIndex+2)%4+1)
                    self.turnFaceRight((faceIndex+2)%4+1)
                if diff == 0:
                    #print('woooo')
                    self.turnBottomRight(faceIndex)
                    self.turnRightUp(faceIndex)
                    self.turnFaceLeft(faceIndex)
                    self.turnRightDown(faceIndex)
                #print(self.getAllFaces())
                self.solveFirstTierCrossMiddle(faceIndex)
            elif pieceIndex == 7 and face[pieceIndex] == 'w':
                #print('4')
                self.turnLeftDown(faceIndex)
                self.turnBottomRight(faceIndex)
                self.turnLeftUp(faceIndex)
                newFace = self.solveFirstTierCrossMiddleHelp(faceIndex)
                self.turnFaceRight(newFace)
                self.turnFaceRight(newFace)
                self.solveFirstTierCrossMiddle(faceIndex)
        #print("all faces", self.getAllFaces())

    def solveFirstTierCrossMiddleHelp(self, faceIndex):
        face = copy.copy(self.getFace(faceIndex))
        #print("HERE", face)
        colorIndex = self.faceOrder.index(face[5])
        #print("HERE2", colorIndex)
        diff = colorIndex - faceIndex
        if diff == 1 or diff == -3:
            self.turnBottomLeft(faceIndex)
        elif diff == -1 or diff == 3:
            self.turnBottomRight(faceIndex)
        elif diff == 2 or diff == -2:
            self.turnBottomRight(faceIndex)
            self.turnBottomRight(faceIndex)
        return colorIndex
    
    def solveFirstTierCrossBottom(self, faceIndex):
        for pieceIndex in range(8):
            face = copy.copy(self.getFace(faceIndex))
            if pieceIndex%2==1 and face[pieceIndex] == 'w':
                otherSide = self.getOtherSide(faceIndex, pieceIndex)
                otherSidePieceIndex = self.faceOrder.index(otherSide)
                #print(otherSide, otherSidePieceIndex)
                otherSideFaceIndex = \
                    self.facesAround[faceIndex][pieceIndex//2][0]
                #print(otherSideFaceIndex)
                diff = otherSideFaceIndex - otherSidePieceIndex
                if diff == 2 or diff == -2:
                    self.turnFaceRight(faceIndex)
                    self.turnFaceRight(faceIndex)
                elif diff == 1 or diff == -3:
                    self.turnFaceRight(faceIndex)
                elif diff == 3 or diff == -1:
                    self.turnFaceLeft(faceIndex)
                self.turnFaceRight(otherSidePieceIndex)
                self.turnFaceRight(otherSidePieceIndex)
                self.solveFirstTierCrossBottom(faceIndex)
    

### SOLVE FIRST TIER CORNERS ###

    def solveFirstTierCorners(self):
        #print('SOLVE FIRST TIER CORNERS START')
        if not self.firstTierCornersDone():
            #print('FIRST TIER CORNERS START')
            #print("all faces", self.getAllFaces())
            #print('lit')
            self.fixFirstTierCornersTop()
            #print("all faces", self.getAllFaces())
            #self.solveFirstTierCorners()
            #print("all faces", self.getAllFaces())
            #print('WOOOOOOO')
        if not self.firstTierCornersDone():
            self.fixFirstTierCornersBottom()
            #print("all faces", self.getAllFaces())
            self.solveFirstTierCorners()
            #print("all faces", self.getAllFaces())
            #print('FIRST CORNERS CROSS END')
    
    def firstTierCornersDone(self):
        whiteFace = copy.copy(self.getFace(0))
        redFace = copy.copy(self.getFace(1))
        greenFace = copy.copy(self.getFace(2))
        orangeFace = copy.copy(self.getFace(3))
        blueFace = copy.copy(self.getFace(4))
        if whiteFace[0] == 'w' and whiteFace[2] == 'w' and whiteFace[4] == 'w' \
            and whiteFace[6] == 'w' and redFace[0] == 'r' and \
            greenFace[0] == 'g' and orangeFace[0] == 'o' and blueFace[0] == 'b':
            return True
        else:
            return False
    
    def firstTierCornersTopDone(self):
        whiteFace = copy.copy(self.getFace(0))
        redFace = copy.copy(self.getFace(1))
        greenFace = copy.copy(self.getFace(2))
        orangeFace = copy.copy(self.getFace(3))
        blueFace = copy.copy(self.getFace(4))
        if whiteFace[0] == 'w' and blueFace[0] != 'b':
            return False
        if whiteFace[2] == 'w' and redFace[0] != 'r':
            return False
        if whiteFace[4] == 'w' and greenFace[0] != 'g':
            return False
        if whiteFace[6] == 'w' and orangeFace[0] != 'o':
            return False
        if (redFace[0] == 'w' or redFace[2] == 'w' or greenFace[0] == 'w' or \
            greenFace[2] == 'w' or orangeFace[0] == 'w' or orangeFace[2] == 'w'\
            or blueFace[0] == 'w' or blueFace[2] == 'w'):
            return False
        return True
    
    def fixFirstTierCornersTop(self):
        #print('IS DONE', self.firstTierCornersTopDone())
        #print("all faces", self.getAllFaces())
        if not self.firstTierCornersTopDone():
            #print("all faces", self.getAllFaces())
            #print('litty')
            faceIndex = 0
            numFaces = 6
            for pieceIndex in range(0,7,2):
                face = copy.copy(self.getFace(faceIndex))
                #print('piece', face[pieceIndex])
                if face[pieceIndex] == 'w':
                    #print(self.getOtherCornerPieces(faceIndex, pieceIndex))
                    if not self.checkCorner(faceIndex, pieceIndex):
                        #print('wooo')
                        frontCorner, leftCorner = \
                            self.getOtherCornerPieces(faceIndex, pieceIndex)
                        #print(frontCorner, leftCorner)
                        leftCornerIndex = self.faceOrder.index(leftCorner)
                        newFaceIndex = pieceIndex//2 + 1
                        self.turnRightDown(newFaceIndex)
                        self.turnBottomLeft(newFaceIndex)
                        self.turnRightUp(newFaceIndex)
                        diff = leftCornerIndex - newFaceIndex
                        #print(diff)
                        if diff == 2 or diff == -2:
                            self.turnBottomRight(newFaceIndex)
                            self.turnBottomRight(newFaceIndex)
                        elif diff == 3 or diff == -1:
                            self.turnBottomRight(newFaceIndex)
                        elif diff == 1 or diff == -3:
                            self.turnBottomLeft(newFaceIndex)
                        lastFaceIndex = (leftCornerIndex%4)+1
                        self.turnRightDown(lastFaceIndex)
                        self.turnBottomLeft(lastFaceIndex)
                        self.turnRightUp(lastFaceIndex)
                        newPieceIndex = ((lastFaceIndex+2)%4+1)*2-1
                        self.shiftCornerTop(0, newPieceIndex)
                        self.shiftCornerTop(0, newPieceIndex)
                        if not self.firstTierCornersTopDone():
                            self.fixFirstTierCornersTop()
                else:
                    frontCorner, leftCorner = \
                        self.getOtherCornerPieces(faceIndex, pieceIndex)
                    #print(faceIndex, pieceIndex)
                    #print('front', frontCorner, 'left', leftCorner)
                    topPieceIndex = self.faceOrder.index(face[pieceIndex])
                    frontFaceIndex = pieceIndex//2 + 1
                    diff = topPieceIndex - frontFaceIndex
                    if frontCorner == 'w':
                        #print('diff', diff)
                        if diff == 0:
                            tempFaceIndex = pieceIndex//2 + 1
                            self.turnRightDown(tempFaceIndex)
                            self.turnBottomLeft(tempFaceIndex)
                            self.turnRightUp(tempFaceIndex)
                            newFaceIndex = (tempFaceIndex%4+1)
                            self.turnRightDown(newFaceIndex)
                            self.turnBottomLeft(newFaceIndex)
                            self.turnRightUp(newFaceIndex)
                            self.shiftCornerTop(newFaceIndex)
                        elif diff == 1 or diff == -3:
                            self.turnRightDown(frontFaceIndex)
                            self.turnBottomLeft(frontFaceIndex)
                            self.turnRightUp(frontFaceIndex)
                            self.turnBottomLeft(frontFaceIndex)
                            newFaceIndex = (frontFaceIndex+1)%4+1
                            self.turnRightDown(newFaceIndex)
                            self.turnBottomLeft(newFaceIndex)
                            self.turnRightUp(newFaceIndex)
                            self.shiftCornerTop(newFaceIndex)
                        elif diff == 3 or diff == -1:
                            self.shiftCornerTop(frontFaceIndex)
                            self.shiftCornerTop(frontFaceIndex)
                        elif diff == 2 or diff == -2:
                            self.turnRightDown(frontFaceIndex)
                            self.turnBottomRight(frontFaceIndex)
                            self.turnRightUp(frontFaceIndex)
                            self.turnBottomRight(frontFaceIndex)
                            newFaceIndex = (frontFaceIndex+2)%4+1
                            self.turnRightDown(newFaceIndex)
                            self.turnBottomLeft(newFaceIndex)
                            self.turnRightUp(newFaceIndex)
                            self.shiftCornerTop(newFaceIndex)
                            self.shiftCornerTop(newFaceIndex)
                        self.fixFirstTierCornersTop()
                    elif leftCorner == 'w':
                        #print(diff)
                        if diff == 0:
                            self.shiftCornerTop(frontFaceIndex)
                        elif diff == 1 or diff == -3:
                            self.turnRightDown(frontFaceIndex)
                            self.turnBottomLeft(frontFaceIndex)
                            self.turnRightUp(frontFaceIndex)
                            newFaceIndex = (frontFaceIndex)%4+1
                            self.turnRightDown(newFaceIndex)
                            self.turnBottomLeft(newFaceIndex)
                            self.turnRightUp(newFaceIndex)
                        elif diff == 3 or diff == -1:
                            self.turnRightDown(frontFaceIndex)
                            self.turnBottomRight(frontFaceIndex)
                            self.turnRightUp(frontFaceIndex)
                            self.turnBottomRight(frontFaceIndex)
                            newFaceIndex = frontFaceIndex%4 + 1
                            self.turnRightDown(newFaceIndex)
                            self.turnBottomLeft(newFaceIndex)
                            self.turnRightUp(newFaceIndex)
                            self.shiftCornerTop(newFaceIndex)
                        elif diff == 2 or diff == -2:
                            self.turnRightDown(frontFaceIndex)
                            self.turnBottomLeft(frontFaceIndex)
                            self.turnRightUp(frontFaceIndex)
                            self.turnBottomLeft(frontFaceIndex)
                            newFaceIndex = (frontFaceIndex+1)%4 + 1
                            #print(newFaceIndex)
                            self.turnRightDown(newFaceIndex)
                            self.turnBottomLeft(newFaceIndex)
                            self.turnRightUp(newFaceIndex)
                        if not self.firstTierCornersTopDone():
                            self.fixFirstTierCornersTop()
    
    def fixFirstTierCornersBottom(self):
        #print("all faces", self.getAllFaces())
        if not self.firstTierCornersDone():
            #print('start again')
            faceIndex = 5
            numFaces = 6
            for pieceIndex in range(0,7,2):
                face = copy.copy(self.getFace(faceIndex))
                #print('piece', face[pieceIndex])
                if face[pieceIndex] == 'w':
                    #print('one')
                    frontCorner, leftCorner = \
                            self.getOtherCornerPieces(faceIndex, pieceIndex)
                    if pieceIndex == 0:
                        currentFaceIndex = 1
                    else:
                        currentFaceIndex = 5 - pieceIndex//2
                    diff = currentFaceIndex - self.faceOrder.index(frontCorner)
                    #print(diff)
                    if diff == 2 or diff == -2:
                        self.turnFaceLeft(faceIndex)
                        newFaceIndex = (currentFaceIndex+1)%4+1
                    elif diff == 0:
                        self.turnFaceRight(faceIndex)
                        newFaceIndex = currentFaceIndex
                    elif diff == 1 or diff == -3:
                        self.turnFaceRight(faceIndex)
                        self.turnFaceRight(faceIndex)
                        if currentFaceIndex == 1:
                            newFaceIndex = 4
                        else:
                            newFaceIndex = currentFaceIndex - 1
                    elif diff == 3 or diff == -1:
                        if currentFaceIndex == 4:
                            newFaceIndex = 1
                        else:
                            newFaceIndex = currentFaceIndex+1
                    self.turnRightDown(newFaceIndex)
                    self.turnBottomLeft(newFaceIndex)
                    self.turnRightUp(newFaceIndex)
                    self.turnBottomRight(newFaceIndex)
                    self.shiftCornerTop(newFaceIndex)
                    self.fixFirstTierCornersBottom()
                else:
                    #print('hi1')
                    frontCorner, leftCorner = \
                        self.getOtherCornerPieces(faceIndex, pieceIndex)
                    #print('front', frontCorner, 'left', leftCorner)
                    topPieceIndex = self.faceOrder.index(face[pieceIndex])
                    #print(topPieceIndex)
                    if frontCorner == 'w':
                        #print('hi2')
                        if pieceIndex == 0:
                            currentFaceIndex = 1
                        else:
                            currentFaceIndex = 5 - pieceIndex//2
                        piece = face[pieceIndex]
                        diff = currentFaceIndex - self.faceOrder.index(piece)
                        #print(currentFaceIndex, self.faceOrder.index(piece))
                        #print(diff, 'diff')
                        if diff == -1 or diff == 3:
                            self.turnFaceLeft(faceIndex)
                            newFaceIndex = (currentFaceIndex+1)%4 + 1
                        elif diff == 1 or diff == -3:
                            self.turnFaceRight(faceIndex)
                            newFaceIndex = currentFaceIndex
                        elif diff == 2 or diff == -2:
                            self.turnFaceRight(faceIndex)
                            self.turnFaceRight(faceIndex)
                            if currentFaceIndex == 1:
                                newFaceIndex = 4
                            else:
                                newFaceIndex = currentFaceIndex - 1
                            #print("WOOB", newFaceIndex)
                        elif diff == 0:
                            if currentFaceIndex == 4:
                                newFaceIndex = 1
                            else:
                                newFaceIndex = currentFaceIndex+1
                        #print(newFaceIndex, 'YAY')
                        self.turnRightDown(newFaceIndex)
                        self.turnBottomLeft(newFaceIndex)
                        self.turnRightUp(newFaceIndex)
                        self.fixFirstTierCornersBottom() 
                    elif leftCorner == 'w':
                        if pieceIndex == 0:
                            currentFaceIndex = 1
                        else:
                            currentFaceIndex = 5 - pieceIndex//2
                        #print("HEREFIRST", currentFaceIndex)
                        diff =currentFaceIndex-self.faceOrder.index(frontCorner)
                        #print(diff)
                        if diff == -1 or diff == 3:
                            self.turnFaceLeft(faceIndex)
                            newFaceIndex = (currentFaceIndex+1)%4+1
                            #print('maybe1', newFaceIndex)
                        elif diff == 1 or diff == -3:
                            self.turnFaceRight(faceIndex)
                            newFaceIndex = currentFaceIndex
                            #print('maybe2', newFaceIndex)
                        elif diff == 2 or diff == -2:
                            self.turnFaceRight(faceIndex)
                            self.turnFaceRight(faceIndex)
                            if currentFaceIndex == 1:
                                newFaceIndex = 4
                            else:
                                newFaceIndex = currentFaceIndex - 1
                            #print('maybe3', newFaceIndex)
                            #print("WOOB", newFaceIndex)
                        elif diff == 0:
                            if currentFaceIndex == 4:
                                newFaceIndex = 1
                            else:
                                newFaceIndex = currentFaceIndex+1
                            #print('maybe4', newFaceIndex)
                        #print("HERE", newFaceIndex)
                        self.turnRightDown(newFaceIndex)
                        self.turnBottomLeft(newFaceIndex)
                        self.turnRightUp(newFaceIndex)
                        self.turnBottomRight(newFaceIndex)
                        self.shiftCornerTop(newFaceIndex)
                        self.shiftCornerTop(newFaceIndex)
                        self.fixFirstTierCornersBottom()
    
    def checkCorner(self, faceIndex, pieceIndex):
        if faceIndex == 0:
            checkFaceIndex = pieceIndex//2
            #print(checkFaceIndex)
            checkFace = copy.copy(self.getFace(checkFaceIndex))
            if self.faceOrder[checkFaceIndex] == checkFace[0]:
                return True
        return False
    
    def shiftCornerTop(self,faceIndex,pieceIndex=2):
        if faceIndex == 0:
            fixFaceIndex = pieceIndex//2 + 1
            self.turnRightDown(fixFaceIndex)
            self.turnBottomLeft(fixFaceIndex)
            self.turnRightUp(fixFaceIndex)
            self.turnBottomRight(fixFaceIndex)
            self.turnRightDown(fixFaceIndex)
            self.turnBottomLeft(fixFaceIndex)
            self.turnRightUp(fixFaceIndex)
            self.turnBottomRight(fixFaceIndex)
        elif faceIndex in [1,2,3,4]:
            self.turnRightDown(faceIndex)
            self.turnBottomLeft(faceIndex)
            self.turnRightUp(faceIndex)
            self.turnBottomRight(faceIndex)
            self.turnRightDown(faceIndex)
            self.turnBottomLeft(faceIndex)
            self.turnRightUp(faceIndex)
            self.turnBottomRight(faceIndex)


### SOLVE SECOND TIER ###
    
    def solveSecondTier(self):
        #print('SECOND TIER START')
        #print("all faces", self.getAllFaces())
        #print('yay')
        faceIndex = 5
        for pieceIndex in range(1,8,2):
            #print("all faces", self.getAllFaces())
            yellowFace = copy.copy(self.getFace(faceIndex))
            piece = yellowFace[pieceIndex]
            otherPiece = self.getOtherSide(faceIndex, pieceIndex)
            #print('piece', piece, 'otherPiece', otherPiece)
            if piece != 'y' and otherPiece != 'y':
                #print('found')
                otherPieceIndex = self.faceOrder.index(otherPiece)
                pieceColorIndex = self.faceOrder.index(piece)
                currentFaceIndex = self.facesAround[faceIndex][pieceIndex//2][0]
                faceDiff = otherPieceIndex - currentFaceIndex
                if faceDiff == 1 or faceDiff == -3:
                    self.turnFaceLeft(faceIndex)
                elif faceDiff == 2 or faceDiff == -2:
                    self.turnFaceRight(faceIndex)
                    self.turnFaceRight(faceIndex)
                elif faceDiff == 3 or faceDiff == -1:
                    self.turnFaceRight(faceIndex)
                #print('here')
                newFaceIndex = otherPieceIndex
                pieceDiff = pieceColorIndex - otherPieceIndex
                #print(pieceDiff)
                if pieceDiff == 1 or pieceDiff == -3:
                    self.moveMiddlePieceLeft(newFaceIndex)
                if pieceDiff == 3 or pieceDiff == -1:
                    self.moveMiddlePieceRight(newFaceIndex)
                self.solveSecondTier()
            #print("all faces", self.getAllFaces())
        #print('IS DONE', self.secondTierDone())
        while not self.secondTierDone():
            self.fixSecondTier()
        #print("all faces", self.getAllFaces())
        #print('SECOND TIER END')
    
    def secondTierDone(self):
        redFace = copy.copy(self.getFace(1))
        if redFace[3] != 'r' or redFace[7] != 'r':
            return False
        greenFace = copy.copy(self.getFace(2))
        if greenFace[3] != 'g' or greenFace[7] != 'g':
            return False
        orangeFace = copy.copy(self.getFace(3))
        if orangeFace[3] != 'o' or orangeFace[7] != 'o':
            return False
        blueFace = copy.copy(self.getFace(4))
        if blueFace[3] != 'b' or blueFace[7] != 'b':
            return False
        return True
    
    def moveMiddlePieceLeft(self, faceIndex):
        self.turnBottomRight(faceIndex)
        self.turnLeftDown(faceIndex)
        self.turnBottomLeft(faceIndex)
        self.turnLeftUp(faceIndex)
        self.turnBottomLeft(faceIndex)
        self.turnFaceLeft(faceIndex)
        #print("all faces", self.getAllFaces())
        self.turnBottomRight(faceIndex)
        #print("all faces", self.getAllFaces())
        self.turnFaceRight(faceIndex)
        #print("all faces", self.getAllFaces())
    
    def moveMiddlePieceRight(self, faceIndex):
        self.turnBottomLeft(faceIndex)
        #print("all faces", self.getAllFaces())
        self.turnRightDown(faceIndex)
        #print("all faces", self.getAllFaces())
        self.turnBottomRight(faceIndex)
        #print("all faces", self.getAllFaces())
        self.turnRightUp(faceIndex)
        #print("all faces", self.getAllFaces())
        self.turnBottomRight(faceIndex)
        #print("all faces", self.getAllFaces())
        self.turnFaceRight(faceIndex)
        #print("all faces", self.getAllFaces())
        self.turnBottomLeft(faceIndex)
        #print("all faces", self.getAllFaces())
        self.turnFaceLeft(faceIndex)
        #print("all faces", self.getAllFaces())
    
    def fixSecondTier(self):
        #print('FIXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        for faceIndex in range(1,5):
            #print('yep')
            face1 = copy.copy(self.getFace(faceIndex))
            #print('okay')
            piece1 = face1[3]
            #print('faceIndex', faceIndex, 'piece1', piece1)
            if self.faceOrder.index(piece1) != faceIndex:
                #print('otherSide', self.getOtherSide(faceIndex, 5))
                if face1[5] == 'y' or self.getOtherSide(faceIndex, 5) == 'y':
                    self.moveMiddlePieceRight(faceIndex)
                    self.solveSecondTier()
            face2 = copy.copy(self.getFace(faceIndex))
            piece2 = face2[7]
            #print('faceIndex', faceIndex, 'piece2', piece2)
            if self.faceOrder.index(piece2) != faceIndex:
                if face2[5] == 'y' or self.getOtherSide(faceIndex, 5) == 'y':
                    self.moveMiddlePieceLeft(faceIndex)
                    self.solveSecondTier
        if not self.secondTierDone():
            self.turnFaceRight(5)
    
### SOLVE THIRD TIER CROSS ###
    
    def solveThirdTierCross(self):
        #print('START THIRD')
        #print("all faces", self.getAllFaces())
        yellowFace = copy.copy(self.getFace(5))
        #print(yellowFace)
        #print(self.thirdTierCrossDone())
        if not self.thirdTierCrossDone():
            #print('here')
            yellowFace = copy.copy(self.getFace(5))
            yellowPieces = []
            for pieceIndex in range(1,8,2):
                if yellowFace[pieceIndex] == 'y':
                    yellowPieces.append(pieceIndex)
            #print('YELLOW PIECES', yellowPieces)
            #print(len(yellowPieces))
            if len(yellowPieces) <= 1:
                self.adjustThirdTierCross(1)
                self.solveThirdTierCross()
            else:
                #print('YELLOW PIECES', yellowPieces)
                diff = yellowPieces[1] - yellowPieces[0]
                #print(diff)
                if diff == 2:
                    if yellowPieces[0] == 1:
                        faceIndex = 2
                    elif yellowPieces[0] == 3:
                        faceIndex = 1
                    elif yellowPieces[0] == 5:
                        faceIndex = 4
                    elif yellowPieces[0] == 7:
                        faceIndex = 3
                    #print('face', faceIndex)
                    self.adjustThirdTierCross(faceIndex)
                    self.solveThirdTierCross()
                elif diff == 6:
                    self.adjustThirdTierCross(3)
                    self.solveThirdTierCross()
                elif diff == 4:
                    if yellowPieces[0] == 1 or yellowPieces[0] == 5:
                        faceIndex = 2
                    if yellowPieces[0] == 3 or yellowPieces[0] == 7:
                        faceIndex = 1
                    #print('face', faceIndex)
                    self.adjustThirdTierCross(faceIndex)
                    self.solveThirdTierCross()

    def thirdTierCrossDone(self):
        yellowFace = copy.copy(self.getFace(5))
        return (yellowFace[1] == 'y') and (yellowFace[3] == 'y') and \
                (yellowFace[5] == 'y') and (yellowFace[7] == 'y')

    def adjustThirdTierCross(self, faceIndex):
        self.turnFaceRight(faceIndex)
        self.turnBottomRight(faceIndex)
        self.turnLeftDown(faceIndex)
        self.turnBottomLeft(faceIndex)
        self.turnLeftUp(faceIndex)
        self.turnFaceLeft(faceIndex)


### SOLVE THIRD TIER SIDES ###
    
    def solveThirdTierSides(self):
        #print("START WOOOOO")
        #print("all faces", self.getAllFaces())
        #print('done?', self.thirdTierSidesDone())
        if not self.thirdTierSidesDone():
            otherSideList = []
            for pieceIndex in range(1, 8, 2):
                otherSideList.append(self.getOtherSide(5, pieceIndex))
            #print(otherSideList)
            faceIndex = self.checkThirdTierSidesList(otherSideList)
            if faceIndex == 'nope':
                self.adjustThirdTierSides(1)
                self.solveThirdTierSides()
            else:
                if not self.thirdTierSidesDone():
                    self.adjustThirdTierSides(faceIndex)
                    self.solveThirdTierSides()
        #print("all faces", self.getAllFaces())

    def thirdTierSidesDone(self):
        if self.getOtherSide(5, 1) != 'r':
            return False
        if self.getOtherSide(5, 3) != 'b':
            return False
        if self.getOtherSide(5, 5) != 'o':
            return False
        if self.getOtherSide(5, 7) != 'g':
            return False
        return True
    
    def checkThirdTierSidesList(self, otherSideList):
        if otherSideList[0] == 'b' and otherSideList[1] == 'o':
            self.turnFaceRight(5)
            return 2
        if otherSideList[1] == 'b' and otherSideList[2] == 'o':
            return 2
        if otherSideList[2] == 'b' and otherSideList[3] == 'o':
            self.turnFaceLeft(5)
            return 2
        if otherSideList[3] == 'b' and otherSideList[0] == 'o':
            self.turnFaceRight(5)
            self.turnFaceRight(5)
            return 2
        if otherSideList[0] == 'o' and otherSideList[1] == 'g':
            self.turnFaceRight(5)
            self.turnFaceRight(5)
            return 1            
        if otherSideList[1] == 'o' and otherSideList[2] == 'g':
            self.turnFaceRight(5)
            return 1
        if otherSideList[2] == 'o' and otherSideList[3] == 'g':
            return 1
        if otherSideList[3] == 'o' and otherSideList[0] == 'g':
            self.turnFaceLeft(5)
            return 1
        if otherSideList[0] == 'g' and otherSideList[1] == 'r':
            self.turnFaceLeft(5)
            return 4
        if otherSideList[1] == 'g' and otherSideList[2] == 'r':
            self.turnFaceRight(5)
            self.turnFaceRight(5)
            return 4
        if otherSideList[2] == 'g' and otherSideList[3] == 'r':
            self.turnFaceRight(5)
            return 4
        if otherSideList[3] == 'g' and otherSideList[0] == 'r':
            return 4
        if otherSideList[0] == 'r' and otherSideList[1] == 'b':
            return 3
        if otherSideList[1] == 'r' and otherSideList[2] == 'b':
            self.turnFaceLeft(5)
            return 3
        if otherSideList[2] == 'r' and otherSideList[3] == 'b':
            self.turnFaceRight(5)
            self.turnFaceRight(5)
            return 3
        if otherSideList[3] == 'r' and otherSideList[0] == 'b':
            self.turnFaceRight(5)
            return 3
        if (otherSideList[0] == 'r' and otherSideList[2] == 'o') or \
            (otherSideList[2] == 'r' and otherSideList[0] == 'o') or \
            (otherSideList[0] == 'g' and otherSideList[2] == 'b') or \
            (otherSideList[2] == 'g' and otherSideList[0] == 'b'):
            return 2
        if (otherSideList[1] == 'r' and otherSideList[3] == 'o') or \
            (otherSideList[3] == 'r' and otherSideList[1] == 'o') or \
            (otherSideList[1] == 'g' and otherSideList[3] == 'b') or \
            (otherSideList[3] == 'g' and otherSideList[1] == 'b'):
            return 1
        return 'nope'
        
    
    def adjustThirdTierSides(self, faceIndex):
        self.turnLeftDown(faceIndex)
        self.turnBottomRight(faceIndex)
        self.turnLeftUp(faceIndex)
        self.turnBottomRight(faceIndex)
        self.turnLeftDown(faceIndex)
        self.turnBottomRight(faceIndex)
        self.turnBottomRight(faceIndex)
        self.turnLeftUp(faceIndex)
        self.turnBottomRight(faceIndex)
    

### SOLVE THIRD TIER CORNERS ###


    def solveThirdTierCorners(self):
        if not self.thirdTierCornersDone():
            yellowFace = copy.copy(self.getFace(5))
            piece0 = yellowFace[0]
            piece2 = yellowFace[2]
            piece4 = yellowFace[4]
            piece6 = yellowFace[6]
            frontCorner0, leftCorner0 = self.getOtherCornerPieces(5, 0)
            frontCorner2, leftCorner2 = self.getOtherCornerPieces(5, 2)
            frontCorner4, leftCorner4 = self.getOtherCornerPieces(5, 4)
            frontCorner6, leftCorner6 = self.getOtherCornerPieces(5, 6)
            if ((piece0 == 'r' or frontCorner0 == 'r' or leftCorner0 == 'r') \
            and (piece0 == 'g' or frontCorner0 == 'g' or leftCorner0 == 'g')):
                self.adjustThirdTierCorners(4)
                self.solveThirdTierCorners()
            elif ((piece2 == 'r' or frontCorner2 == 'r' or leftCorner2 == 'r') \
            and (piece2 == 'b' or frontCorner2 == 'b' or leftCorner2 == 'b')):
                self.adjustThirdTierCorners(1)
                self.solveThirdTierCorners()
            elif ((piece4 == 'o' or frontCorner4 == 'o' or leftCorner4 == 'o') \
            and (piece4 == 'b' or frontCorner4 == 'b' or leftCorner4 == 'b')):
                self.adjustThirdTierCorners(3)
                self.solveThirdTierCorners()
            elif ((piece6 == 'o' or frontCorner6 == 'o' or leftCorner6 == 'o') \
            and (piece6 == 'g' or frontCorner6 == 'g' or leftCorner6 == 'g')):
                self.adjustThirdTierCorners(2)
                self.solveThirdTierCorners()
            else:
                self.adjustThirdTierCorners(1)
                self.solveThirdTierCorners()
        #print("all faces", self.getAllFaces())
    
    def thirdTierCornersDone(self):
        yellowFace = copy.copy(self.getFace(5))
        piece0 = yellowFace[0]
        piece2 = yellowFace[2]
        piece4 = yellowFace[4]
        piece6 = yellowFace[6]
        frontCorner0, leftCorner0 = self.getOtherCornerPieces(5, 0)
        frontCorner2, leftCorner2 = self.getOtherCornerPieces(5, 2)
        frontCorner4, leftCorner4 = self.getOtherCornerPieces(5, 4)
        frontCorner6, leftCorner6 = self.getOtherCornerPieces(5, 6)
        if not ((piece0 == 'r' or frontCorner0 == 'r' or leftCorner0 == 'r') \
            and (piece0 == 'g' or frontCorner0 == 'g' or leftCorner0 == 'g')):
            return False
        if not ((piece2 == 'r' or frontCorner2 == 'r' or leftCorner2 == 'r') \
            and (piece2 == 'b' or frontCorner2 == 'b' or leftCorner2 == 'b')):
            return False
        if not ((piece4 == 'o' or frontCorner4 == 'o' or leftCorner4 == 'o') \
            and (piece4 == 'b' or frontCorner4 == 'b' or leftCorner4 == 'b')):
            return False
        if not ((piece6 == 'o' or frontCorner6 == 'o' or leftCorner6 == 'o') \
            and (piece6 == 'g' or frontCorner6 == 'g' or leftCorner6 == 'g')):
            return False
        return True
    
    def adjustThirdTierCorners(self, faceIndex):
        self.turnBottomRight(faceIndex)
        self.turnLeftDown(faceIndex)
        self.turnBottomLeft(faceIndex)
        self.turnRightDown(faceIndex)
        self.turnBottomRight(faceIndex)
        self.turnLeftUp(faceIndex)
        self.turnBottomLeft(faceIndex)
        self.turnRightUp(faceIndex)
    
### FIX THIRD TIER CORNERS ###
    
    def fixThirdTierCorners(self):
        if not self.thirdTierCornersAlignmentDone():
            yellowFace = copy.copy(self.getFace(5))
            if yellowFace[0] == 'g':
                self.adjustCornerTop()
                self.adjustCornerTop()
            if yellowFace[0] == 'r':
                self.adjustCornerTop()
            self.turnBottomRight(1)
            if yellowFace[6] == 'o':
                self.adjustCornerTop()
                self.adjustCornerTop()
            if yellowFace[6] == 'g':
                self.adjustCornerTop()
            self.turnBottomRight(1)
            if yellowFace[4] == 'b':
                self.adjustCornerTop()
                self.adjustCornerTop()
            if yellowFace[4] == 'o':
                self.adjustCornerTop()
            self.turnBottomRight(1)
            if yellowFace[2] == 'r':
                self.adjustCornerTop()
                self.adjustCornerTop()
            if yellowFace[2] == 'b':
                self.adjustCornerTop()
            self.turnBottomRight(1)
    
    def thirdTierCornersAlignmentDone(self):
        yellowFace = copy.copy(self.getFace(5))
        if yellowFace[0] == 'y' and yellowFace[2] == 'y' and \
                yellowFace[4] == 'y' and yellowFace[6] == 'y':
            return True
        else:
            return False
    
    def adjustCornerTop(self):
        self.turnLeftUp(1)
        self.turnTopRight(1)
        self.turnLeftDown(1)
        self.turnTopLeft(1)
        self.turnLeftUp(1)
        self.turnTopRight(1)
        self.turnLeftDown(1)
        self.turnTopLeft(1)
    
### SOLVE CUBE ###
    
    def solveCube(self):
        if self.isLegalCube():
            self.solveFirstTierCross()
            self.solveFirstTierCorners()
            self.solveSecondTier()
            self.solveThirdTierCross()
            self.solveThirdTierSides()
            self.solveThirdTierCorners()
            self.fixThirdTierCorners()
            return self.masterList, self.moveCount
            #print("all faces", self.getAllFaces())
        else:
            return [], 0

### TURNS ###

    def turnRight(self, faceIndex):
        faceNow = self.getFace(faceIndex)
        faceList = copy.copy(self.getFace(faceIndex))
        newFace = copy.copy(faceList)
        for piece in range(len(faceList)):
            newPos = (piece+2)%8
            newFace[newPos] = faceList[piece]
        self.assignNew(faceIndex, newFace)
        tier = []
        #faceNow = self.getFace(faceIndex)
        #print(faceNow, 'turned face')
        for j in range(len(self.facesAround[faceIndex])):
            side = copy.copy(self.getFace(self.facesAround[faceIndex][j][0]))
            start1 = self.facesAround[faceIndex][j][1]
            tier.append(side[start1])
            tier.append(side[(start1+1)%8])
            tier.append(side[(start1+2)%8])
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
            #print(self.facesAround[faceIndex][i][0], face)
            self.assignNew(self.facesAround[faceIndex][i][0], face)
        #faceNow = self.getFace(faceIndex)
        #print('faceNOW', faceNow)
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

    def turnFaceRight(self, faceIndex):
        currentFace = self.faceNameOrder[faceIndex]
        faceAbove = self.faceUp[faceIndex]
        text1 = 'Hold the cube with the ' + currentFace + ' face towards you '
        text2 = 'The ' + faceAbove + ' face must be on top'
        length = len(self.masterList)
        facesBefore = copy.deepcopy(self.masterListFaces(faceIndex))
        printStatement = 'Turn the ' + currentFace + ' face to the right'
        #print(printStatement)
        self.turnRight(faceIndex)
        facesAfter =copy.deepcopy(self.masterListFaces(faceIndex))
        self.adjustList(text1, text2, facesBefore, printStatement, facesAfter,\
                                                                currentFace)   
        #print(self.masterList) 
  
    def turnFaceLeft(self, faceIndex):
        currentFace = self.faceNameOrder[faceIndex]
        faceAbove = self.faceUp[faceIndex]
        text1 = 'Hold the cube with the ' + currentFace + ' face towards you '
        text2 = 'The ' + faceAbove + ' face must be on top'
        length = len(self.masterList)
        facesBefore = copy.deepcopy(self.masterListFaces(faceIndex))
        printStatement = 'Turn the ' + currentFace + ' face to the left'
        #print(printStatement)
        self.turnLeft(faceIndex)
        facesAfter = copy.deepcopy(self.masterListFaces(faceIndex))
        self.adjustList(text1, text2, facesBefore, printStatement, facesAfter,\
                                                                currentFace) 

    def turnTopRight(self, oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        faceAbove = self.faceUp[oldFaceIndex]
        text1 = 'Hold the cube with the ' + currentFace + ' face towards you '
        text2 = 'The ' + faceAbove + ' face must be on top'
        length = len(self.masterList)
        facesBefore = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        printStatement = 'Turn the top of the ' + currentFace + \
                                                        ' face to the right'
        #print(printStatement)
        if oldFaceIndex == 0 or oldFaceIndex == 5:
            faceIndex = 1
        else:
            faceIndex = 0
        self.turnLeft(faceIndex)
        facesAfter = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        self.adjustList(text1, text2, facesBefore, printStatement, facesAfter,\
                                                                currentFace)
  
    def turnTopLeft(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        faceAbove = self.faceUp[oldFaceIndex]
        text1 = 'Hold the cube with the ' + currentFace + ' face towards you '
        text2 = 'The ' + faceAbove + ' face must be on top'
        length = len(self.masterList)
        facesBefore = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        printStatement = 'Turn the top of the ' + currentFace + \
                                                    ' face to the left'
        #print(printStatement)
        if oldFaceIndex == 0 or oldFaceIndex == 5:
            faceIndex = 1
        else:
            faceIndex = 0
        self.turnRight(faceIndex)
        facesAfter = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        self.adjustList(text1, text2, facesBefore, printStatement, facesAfter,\
                                                                currentFace)
  
    def turnRightUp(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        faceAbove = self.faceUp[oldFaceIndex]
        text1 = 'Hold the cube with the ' + currentFace + ' face towards you '
        text2 = 'The ' + faceAbove + ' face must be on top'
        length = len(self.masterList)
        facesBefore = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        printStatement = 'Turn the right side of the ' + currentFace +' face up'
        #print(printStatement)
        if oldFaceIndex == 0:
            faceIndex = 2
        elif oldFaceIndex == 5 or oldFaceIndex == 1:
            faceIndex = 4
        else:
            faceIndex = oldFaceIndex-1
        self.turnRight(faceIndex)
        facesAfter = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        self.adjustList(text1, text2, facesBefore, printStatement, facesAfter,\
                                                                currentFace)
  
    def turnRightDown(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        faceAbove = self.faceUp[oldFaceIndex]
        text1 = 'Hold the cube with the ' + currentFace + ' face towards you '
        text2 = 'The ' + faceAbove + ' face must be on top'
        length = len(self.masterList)
        facesBefore = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        printStatement = 'Turn the right side of the ' + currentFace +\
                            ' face down'
        #print(printStatement)
        if oldFaceIndex == 0:
            faceIndex = 2
        elif oldFaceIndex == 5 or oldFaceIndex == 1:
            faceIndex = 4
        else:
            faceIndex = oldFaceIndex-1
        self.turnLeft(faceIndex)
        facesAfter = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        self.adjustList(text1, text2, facesBefore, printStatement, facesAfter,\
                                                                currentFace) 
    
    def turnLeftUp(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        faceAbove = self.faceUp[oldFaceIndex]
        text1 = 'Hold the cube with the ' + currentFace + ' face towards you '
        text2 = 'The ' + faceAbove + ' face must be on top'
        length = len(self.masterList)
        facesBefore = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        printStatement = 'Turn the left side of the ' + currentFace + ' face up'
        #print(printStatement)
        if oldFaceIndex == 0:
            faceIndex = 4
        elif oldFaceIndex == 4:
            faceIndex = 1
        elif oldFaceIndex == 5:
            faceIndex = 2
        else:
            faceIndex = oldFaceIndex+1
        self.turnLeft(faceIndex)
        facesAfter = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        self.adjustList(text1, text2, facesBefore, printStatement, facesAfter,\
                                                                currentFace)
  
    def turnLeftDown(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        faceAbove = self.faceUp[oldFaceIndex]
        text1 = 'Hold the cube with the ' + currentFace + ' face towards you '
        text2 = 'The ' + faceAbove + ' face must be on top'
        length = len(self.masterList)
        facesBefore = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        printStatement = 'Turn the left side of the ' + currentFace +\
                        ' face down'
        #print(printStatement)
        if oldFaceIndex == 0:
            faceIndex = 4
        elif oldFaceIndex == 4:
            faceIndex = 1
        elif oldFaceIndex == 5:
            faceIndex = 2
        else:
            faceIndex = oldFaceIndex+1
        self.turnRight(faceIndex)
        facesAfter = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        self.adjustList(text1, text2, facesBefore, printStatement, facesAfter,\
                                                                currentFace) 
    
    def turnBottomRight(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        faceAbove = self.faceUp[oldFaceIndex]
        text1 = 'Hold the cube with the ' + currentFace + ' face towards you '
        text2 = 'The ' + faceAbove + ' face must be on top'
        length = len(self.masterList)
        facesBefore = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        printStatement = 'Turn the bottom of the ' + currentFace + ' face right'
        #print(printStatement)
        if oldFaceIndex == 0 or oldFaceIndex == 5:
            faceIndex = 3
        else:
            faceIndex = 5
        self.turnRight(faceIndex)
        facesAfter = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        self.adjustList(text1, text2, facesBefore, printStatement, facesAfter,\
                                                                currentFace) 
    
    def turnBottomLeft(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        faceAbove = self.faceUp[oldFaceIndex]
        text1 = 'Hold the cube with the ' + currentFace + ' face towards you '
        text2 = 'The ' + faceAbove + ' face must be on top'
        length = len(self.masterList)
        facesBefore = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        printStatement = 'Turn the bottom of the ' + currentFace + ' face left'
        #print(printStatement)
        if oldFaceIndex == 0 or oldFaceIndex == 5:
            faceIndex = 3
        else:
            faceIndex = 5
        self.turnLeft(faceIndex)
        facesAfter = copy.deepcopy(self.masterListFaces(oldFaceIndex))
        self.adjustList(text1, text2, facesBefore, printStatement, facesAfter,\
                                                                currentFace) 

    def adjustList(self, text1, text2, facesBefore, printStatement, facesAfter,\
                                                                currentFace):
        length = len(self.masterList)
        if length >= 2:
            lastMove = copy.copy(self.masterList[length-1])
            if len(lastMove) == 2:
                checkString = lastMove[0]
                oldPlace = checkString[:len(checkString)-2]
                oldDir = checkString[len(checkString)-1]
                newPlace = printStatement[:len(printStatement)-2]
                newDir = printStatement[len(printStatement)-1]
                if printStatement == checkString:
                    newAddition = []
                    newPrintStatement = printStatement + ' twice'
                    newAfter = facesAfter
                    newAddition.append(newPrintStatement)
                    newAddition.append(facesAfter)
                    self.masterList[length-1] = newAddition
                elif oldPlace == newPlace:
                    if oldDir == 'Up' and newDir == 'Down' or\
                        oldDir == 'Down' and newDir == 'Up' or\
                        oldDir == 'Left' and newDir == 'Right' or\
                        oldDir == 'Right' and newDir == 'Left':
                        self.masterList.pop()
                        self.moveCount -= 1
                elif currentFace in checkString:
                    newAddition = []
                    newAddition.append(printStatement)
                    newAddition.append(facesAfter)
                    self.masterList.append(newAddition)
                    self.moveCount += 1
                else:
                    newAddition = []
                    newAddition.append(text1)
                    newAddition.append(text2)
                    newAddition.append(facesBefore)
                    newAddition.append(printStatement)
                    newAddition.append(facesAfter)
                    self.masterList.append(newAddition)
                    self.moveCount += 2
            elif len(lastMove) == 5:
                checkString1 = lastMove[0]
                checkString2 = lastMove[3]
                if printStatement == checkString2:
                    #newAddition = []
                    newPrintStatement = printStatement + ' twice'
                    newAfter = facesAfter
                    lastMove[3] = newPrintStatement
                    lastMove[4] = newAfter
                    self.masterList[length-1] = lastMove
                elif text1 == checkString1:
                    newAddition = []
                    newAddition.append(printStatement)
                    newAddition.append(facesAfter)
                    self.masterList.append(newAddition)
                    self.moveCount += 1
                else:
                    newAddition = []
                    newAddition.append(text1)
                    newAddition.append(text2)
                    newAddition.append(facesBefore)
                    newAddition.append(printStatement)
                    newAddition.append(facesAfter)
                    self.masterList.append(newAddition)
                    self.moveCount += 2
        else:
            newAddition = []
            newAddition.append(text1)
            newAddition.append(text2)
            newAddition.append(facesBefore)
            newAddition.append(printStatement)
            newAddition.append(facesAfter)
            self.masterList.append(newAddition)
            self.moveCount += 2

cube = Cube(wf,rf,gf,of,bf,yf)
    
#cube.solveCube()


'''def findOtherFace(self, faceIndex, pieceIndex):
        if faceIndex == 0:
        return (self.getFace(pieceIndex//2+1), faceIndex+(pieceIndex//2)+1)'''