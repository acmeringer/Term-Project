import math
import string
import random
import copy

wf = ['w','w','g','w','y','o','y','o']   
rf = ['b','y','w','g','y','o','b','y']
gf = ['g','w','r','r','y','r','b','w']
of = ['w','w','y','r','o','o','y','b']
bf = ['g','r','g','w','b','b','g','y']
yf = ['o','b','r','y','r','g','w','g']

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

    def solveFirstTierCross(self):
        for faceIndex in range(6):
            face = self.getFace(faceIndex)
            #print('index', faceIndex, 'face', face)
            if faceIndex == 0:
                self.solveFirstTierCrossTop(faceIndex)
            elif faceIndex in [1,2,3,4]:
                self.solveFirstTierCrossMiddle(faceIndex)
            elif faceIndex == 5:
                #print('yes')
                self.solveFirstTierCrossBottom(faceIndex)
            currentWhite = copy.copy(self.getFace(0))
        for check in range(1,8,2):
            if currentWhite[check] != 'w':
                self.solveFirstTierCross()
        print("all faces", self.getAllFaces())
    
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
        face = copy.copy(self.getFace(faceIndex))
        #print('face update',face)
        for pieceIndex in range(8):
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
                #print('othersidepiece', piece)
                pieceIndex = self.faceOrder.index(piece)
                #print(pieceIndex, faceIndex)
                diff = pieceIndex - faceIndex
                if diff == -1 or diff == 3:
                    self.turnFaceLeft(faceIndex)
                    self.turnRightUp(faceIndex)
                    self.turnFaceRight(faceIndex)
                elif diff == 1 or diff == -3:
                    self.turnFaceRight(faceIndex)
                    self.turnLeftUp(faceIndex)
                    self.turnFaceLeft(faceIndex)
                if diff == 2 or diff == -2:
                    self.turnBottomRight(faceIndex)
                    self.turnFaceLeft(faceIndex+1)
                    self.turnRightUp(faceIndex+1)
                    self.turnFaceRight(faceIndex+1)
                if diff == 0:
                    #print('woooo')
                    self.turnBottomRight(faceIndex)
                    self.turnRightUp(faceIndex)
                    self.turnFaceLeft(faceIndex)
                    self.turnRightDown(faceIndex)
                newFace = self.solveFirstTierCrossMiddleHelp(faceIndex)
                self.turnFaceRight(newFace)
                self.turnFaceRight(newFace)
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

    def checkIsRightPiece(self, faceIndex, pieceIndex):
        face = copy.copy(self.getFace(faceIndex))
        colorIndex = self.faceOrder.index(face[pieceIndex])
        if colorIndex == faceIndex:
            return True
        return True

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
                otherSideFaceIndex = \
                    self.facesAround[faceIndex][pieceIndex//2][0]
                diff = otherSideFaceIndex - otherSidePieceIndex
                if diff == 2 or diff == -2:
                    self.turnFaceRight(faceIndex)
                    self.turnFaceRight(faceIndex)
                elif diff == 1 or diff == -3:
                    self.turnFaceLeft(faceIndex)
                elif diff == 3 or diff == -1:
                    self.turnFaceRight(faceIndex)
                self.turnFaceRight(otherSideFaceIndex)
                self.turnFaceRight(otherSideFaceIndex)
                self.solveFirstTierCrossBottom(faceIndex)
    
    def solveFirstTierCorners(self):
        self.fixFirstTierCornersTop()
    
    def fixFirstTierCornersTop(self):
        numFaces = 6
        for pieceIndex in range(0,7,2):
            face = copy.copy(self.getFace(0))
            if face[piece] == 'w':
                if not self.checkCorner(0, pieceIndex):
                    newFaceIndex = pieceIndex//2 + 1
                    self.turnRightDown(newFaceIndex)
                    seld.turnBottomLeft(newFaceIndex)
                    self.turnRightUp(newFaceIndex)
                    frontCorner, leftCorner = \
                            getOtherCornerPieces(self, faceIndex, pieceIndex)
                    leftCornerIndex = self.faceOrder.index[leftCorner]
                    diff = leftCornerIndex - newFaceIndex
                    if diff == 2 or diff == -2:
                        self.turnBottomRight(newFaceIndex)
                        self.turnBottomRight(newFaceIndex)
                    elif diff == 3 or diff == -1:
                        self.turnBottomRight(newFaceIndex)
                    elif diff == 1 or diff == -3:
                        self.turnBottomLeftt(newFaceIndex)
                    lastFaceIndex = (leftCornerIndex%4)+1
                    self.turnRightDown(lastFaceIndex)
                    seld.turnBottomLeft(lastFaceIndex)
                    self.turnRightUp(lastFaceIndex)
                    newPieceIndex = (lastFaceIndex-1)*2
                    self.shiftCorner(0, newPieceIndex)
                if frontCorner == 'w':
                    pass
                elif leftCorner == 'w':
                    pass
    
    def checkCorner(self, faceIndex, pieceIndex):
        if faceIndex == 0:
            checkFaceIndex = pieceIndex//2
            checkFace = copy.copy(self.getFace(checkFaceIndex))
            if self.faceOrder[checkFaceIndex] == checkFace[3]:
                return True
        return False

    def getOtherCornerPieces(self, faceIndex, pieceIndex):
        if faceIndex == 0:
            if pieceIndex == 0:
                face1 = copy.copy(self.getFace(1))
                face2 = copy.copy(self.getFace(4))
            elif pieceIndex%2==0:
                face1 = copy.copy(self.getFace(pieceIndex//2+1))
                face2 = copy.copy(self.getFace(pieceIndex//2))
            return face1[0], face2[3]
    
    def shiftCorner(self,faceIndex,pieceIndex):
        if faceIndex == 0:
            fixFaceIndex = pieceIndex//2 + 1
            self.turnRightDown(fixFaceIndex)
            seld.turnBottomLeft(fixFaceIndex)
            self.turnRightUp(fixFaceIndex)
            self.turnBottomRight(fixFaceIndex)
            self.turnRightDown(fixFaceIndex)
            seld.turnBottomRight(fixFaceIndex)
            self.turnRightUp(fixFaceIndex)
            self.turnBottomLeft(fixFaceIndex)
        
    
    def solveSecondTier(self):
        pass
    
    def solveThirdTierCross(self):
        pass
    
    def solveThirdTierSides(self):
        pass
    
    def solveThirdTierCorners(self):
        pass
    
    def fixThirdTierCorners(self):
        pass
    
    def solveCube(self):
        self.solveFirstTierCross()
        self.solveFirstTierCorners()
        self.solveSecondTier()
        self.solveThirdTierCross()
        self.solveThirdTierSides()
        self.solveThirdTierCorners()
        self.fixThirdTierCorners()

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
        currentFace = self.faceNameOrder[oldFaceIndex]
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
    
    def turnLeftUp(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        printStatement = 'Turn the left side of the ' + currentFace + ' face up'
        print(printStatement)
        if oldFaceIndex == 0:
            faceIndex = 4
        elif oldFaceIndex == 4:
            faceIndex = 2
        elif oldFaceIndex == 5:
            faceIndex = 3
        else:
            faceIndex = oldFaceIndex+1
        self.turnLeft(faceIndex)
  
    def turnLeftDown(self,oldFaceIndex):
        currentFace = self.faceNameOrder[oldFaceIndex]
        printStatement = 'Turn the left side of the ' + currentFace +\
                        ' face down'
        print(printStatement)
        if oldFaceIndex == 0:
            faceIndex = 4
        elif oldFaceIndex == 4:
            faceIndex = 2
        elif oldFaceIndex == 5:
            faceIndex = 3
        else:
            faceIndex = oldFaceIndex+1
        self.turnRight(faceIndex)
    
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

#cube.solveFirstTierCross()


'''def findOtherFace(self, faceIndex, pieceIndex):
        if faceIndex == 0:
        return (self.getFace(pieceIndex//2+1), faceIndex+(pieceIndex//2)+1)'''