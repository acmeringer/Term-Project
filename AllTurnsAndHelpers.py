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