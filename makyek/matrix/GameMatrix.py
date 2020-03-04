'''
Game Matrix main file
Created on 26 feb 2019

@author: rodolfo
'''
from makyek.matrix.Normalizzer import Normalizer
from makyek.GlobalValues import ROW_COUNT, COLUMN_COUNT, LEVEL
from makyek.matrix.Cell import Cell

import subprocess
import os
from makyek.matrix.CellRangeGetter import CellRangeGetter

from random import randint


class GameMatrix:
    """Game matrix main class
    
    This class handle the principal parts of game
    """

    def __init__(self):
        """Constructor withou parameters
        """
        # matrix creation and initializzazion
        self.matrix = [[Cell('-') for i in range(ROW_COUNT)] for i in range(COLUMN_COUNT)]
        self.initGameMatrix()

        # set click cordinates (self.clickedRow, self.clickedColum, self.movedRow, self.movedColum, self.directionOfMove)
        self.resetClickCordinates()

        # operation todo by computer
        self.todo = ""

        # 0:player
        # 1:computer
        self.round = 0

        # init coreLogic file
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.initCoreLogicFile()

    def initCoreLogicFile(self):
        """Init core logic file for solver
        """
        # principal program
        self.program = []
#         print(se"../../coreLogic")
        # core file
        self.coreFile = open(self.dir_path + "/../../" + LEVEL, "r")
        for i in self.coreFile:
            self.program.append(i)
        self.coreFile.close()


    def initGameMatrix(self):
        '''
        Init the game matrix for the first time.
        Every 'C' is computer
        Every 'P' is player (the gamer)
        '''
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                # player first position
                if i==0 or i==2:
                    self.matrix[i][j].cellCharacter = 'P'
                # computer first position
                elif i==ROW_COUNT-3 or i==ROW_COUNT-1:
                    self.matrix[i][j].cellCharacter = 'C'
                # squares
                else:
                    self.matrix[i][j].cellCharacter = '-'

    def draw(self):
        """Main draw function
        """
        # for color alternation
        backgroundCount = 0

        for i in range(ROW_COUNT):
            backgroundCount=backgroundCount+1 # square color alternation
            for j in range(COLUMN_COUNT):
                backgroundCount=backgroundCount+1 # square color alternation
                #square
                Cell.drawSquare(i, j, backgroundCount)
                #player
                Cell.drawPlayer(i, j, self.matrix[i][j].cellCharacter)
                #cell info
                #Cell.drawTextInfo(i, j, self.matrix[i][j].cellCharacter, self.matrix[i][j].cellId)

        # if we click a player (FOR FIRST TIME)
        if(self.isClickedPlayer()):
            Cell.drawPlayerClicked(self.clickedRow, self.clickedColum)
            #Cell.drawHints(self.clickedRow, self.clickedColum)

# ---------- MOVEMENT CHECK ----------

    def moveDestinationIsFree(self):
        """Move destination is free

        Check that wen we want to move a player, the destination is free
        
        Returns:
            bool -- If the destination is free
        """
        return self.matrix[self.movedRow][self.movedColum].cellCharacter == '-'



    def canMoveInDirection1(self):
        """Can move in direction 1

        function that told us if we can move a player in direction 1.
        Directions:
            
                    1
                    ^
                    | 
        4 < - < -     - > 2
                    |
                    3

        
        Returns:
            bool -- if we can move in direction 1
        """
        canDo2Step = self.movedRow == self.clickedRow +2 and self.movedColum == self.clickedColum
        canDo1Step = self.movedRow == self.clickedRow +1 and self.movedColum == self.clickedColum
        return (canDo1Step or canDo2Step) and self.moveDestinationIsFree()

    def canMoveInDirection2(self):
        """Can move in direction 2

        function that told us if we can move a player in direction 3.
        Directions:
            
                    1
                    ^
                    | 
        4 < - < -     - > 2
                    |
                    3

        
        Returns:
            bool -- if we can move in direction 2
        """
        canDo2Step = self.movedRow == self.clickedRow and self.movedColum == self.clickedColum + 2
        canDo1Step = self.movedRow == self.clickedRow and self.movedColum == self.clickedColum + 1
        destinationIsFree = self.matrix[self.movedRow][self.movedColum].cellCharacter == '-'
        return (canDo1Step or canDo2Step) and self.moveDestinationIsFree()


    def canMoveInDirection3(self):
        """Can move in direction 2

        function that told us if we can move a player in direction 3.
        Directions:
            
                    1
                    ^
                    | 
        4 < - < -     - > 2
                    |
                    3

        
        Returns:
            bool -- if we can move in direction 3
        """
        canDo2Step = self.movedRow == self.clickedRow -2 and self.movedColum == self.clickedColum
        canDo1Step = self.movedRow == self.clickedRow -1 and self.movedColum == self.clickedColum
        return (canDo1Step or canDo2Step) and self.moveDestinationIsFree()


    def canMoveInDirection4(self):
        """Can move in direction 4

        function that told us if we can move a player in direction 4.
        Directions:
            
                    1
                    ^
                    | 
        4 < - < -     - > 2
                    |
                    3

        
        Returns:
            bool -- if we can move in direction 4
        """
        canDo3Step = self.movedRow == self.clickedRow and self.movedColum == self.clickedColum - 3
        canDo2Step = self.movedRow == self.clickedRow and self.movedColum == self.clickedColum - 2
        canDo1Step = self.movedRow == self.clickedRow and self.movedColum == self.clickedColum - 1
        return (canDo1Step or canDo2Step or canDo3Step) and self.moveDestinationIsFree()

    def canMovePlayer(self, x : int, y : int):
        """if we can move a player

        This function control if we can move a plyer.
        We can move a pleyer if:
            We can move it in a 1 or four direction
            The destination cell is free
        
        Arguments:
            x {int} -- Destination x of cell
            y {int} -- Destination y of cell
        """
        # get the logic matrix cordinates
        self.movedRow = Normalizer.physicToRow(y)
        self.movedColum = Normalizer.physicToColum(x)

        # direction 1
        if self.canMoveInDirection1():
            self.directionOfMove = 1

        # direction 2
        elif self.canMoveInDirection2():
            self.directionOfMove = 2

        # direction 3
        elif self.canMoveInDirection3():
            self.directionOfMove = 3

        # direction 4
        elif self.canMoveInDirection4():
            self.directionOfMove = 4

        # we cant move in one of directions
        else:
            self.resetClickCordinates()

        # move the player and eat cells
        self.movePlayer()

        # round of computer (if the move of player is done, computer can move)
        if self.directionOfMove!=-1:
            self.solve()
            self.round = 1

        # finish or invalid direction
        self.resetClickCordinates()


# ---------- MOVEMENT DO ----------

    def resetClickCordinates(self):
        """Reset to -1 all click temporary cordinates
        """
        self.clickedRow = self.clickedColum = self.movedRow = self.movedColum = self.directionOfMove = -1

        
    def eatPlayerCells(self, direction, i, j, i1, j1):
        eatableCells = CellRangeGetter.getEatableCellsDirection(direction, i, j, i1, j1)
        for c in eatableCells:
            eatableI = c[0]
            eatableJ = c[1]
            if self.matrix[eatableI][eatableJ].cellCharacter == 'P':
                self.matrix[eatableI][eatableJ].cellCharacter = 'C'


    def eatComputerCells(self, direction, i, j, i1, j1):
        eatableCells = CellRangeGetter.getEatableCellsDirection(direction, i, j, i1, j1)
        for c in eatableCells:
            eatableI = c[0]
            eatableJ = c[1]
            if self.matrix[eatableI][eatableJ].cellCharacter == 'C':
                self.matrix[eatableI][eatableJ].cellCharacter = 'P'

        
    def getMovement(self):
        movements = self.todo[1:-2]
        movement = movements.split(', ')
        return movement[0][5:-1]
        
    def moveComputer(self):
        # if there are movements
        if 'move' in self.todo:
            self.todo = self.getMovement()

            # print("Faccio la mossa: " + self.todo)
            #print(self.todo)
            
            # get the cell of moving
            cellOfMoving = self.todo.split(',')
            #print(self.todo)
            #print(cellOfMoving[0])
            toI = int(cellOfMoving[1])
            toJ=int(cellOfMoving[2])
    
            # get the row and colum of cel of moving (dependently CellId)
            for i in range(ROW_COUNT):
                for j in range(COLUMN_COUNT):
                    if(self.matrix[i][j].cellId == int(cellOfMoving[0])):
                        fromI = i
                        fromJ = j
                        break
                    
            # old cell
            self.matrix[fromI][fromJ].cellCharacter = '-'
            self.matrix[fromI][fromJ].cellId = self.matrix[toI][toJ].cellId
    
            # new cell
            self.matrix[toI][toJ].cellCharacter = 'C'
            self.matrix[toI][toJ].cellId = int(cellOfMoving[0])
            
            # eat cells
            
            # if computer move in direction 1
            if toI > fromI and toJ == fromJ:
                self.eatPlayerCells(1, fromI, fromJ, toI, toJ)
                
            # if computer move in direction 2
            if toI == fromI and toJ > fromJ:
                self.eatPlayerCells(2, fromI, fromJ, toI, toJ)
                
            # if computer move in direction 3
            if toI < fromI and toJ == fromJ:
                self.eatPlayerCells(3, fromI, fromJ, toI, toJ)
                
            # if computer move in direction 4
            if toI == fromI and toJ < fromJ:
                self.eatPlayerCells(4, fromI, fromJ, toI, toJ)
            
            
        # if there aren't movements
        else:
            self.initGameMatrix()
        
        
        self.round = 0


    def movePlayer(self):
        if(self.directionOfMove != -1):
            self.matrix[self.movedRow][self.movedColum].cellCharacter = 'P'
            self.matrix[self.clickedRow][self.clickedColum].cellCharacter = '-'
            self.eatComputerCells(self.directionOfMove, self.clickedRow, self.clickedColum, self.movedRow, self.movedColum)

    def update(self):
        onePlayer = False
        oneEnemy = False
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                if(self.matrix[i][j].cellCharacter=='P'):
                    onePlayer = True
                if(self.matrix[i][j].cellCharacter=='C'):
                    oneEnemy = True
                if(oneEnemy and onePlayer):
                    break

        if(not oneEnemy or not onePlayer):
            print("Partita terminata")
            self.initGameMatrix()

        if(self.round==1):
            self.moveComputer()


    def isClickedPlayer(self):
        """Is clicked a player
        Told us if a Player is clicked
        Returns:
            bool -- If a player is clicked
        """
        return self.clickedRow!=-1 and self.clickedColum!=-1 and self.matrix[self.clickedRow][self.clickedColum].cellCharacter=='P'



# ---------- SOLVER PART ----------

    def makeFacts(self, facts : list):
        """Make facts by current matrix
        
        Arguments:
            facts {object} -- Facts list
        """
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                if(self.matrix[i][j].cellCharacter == '-'):
                    facts.append("free(" + str(i) + "," + str(j) + ").")
                elif(self.matrix[i][j].cellCharacter == 'P'):
                    facts.append("enemy(" + str(i) + "," + str(j) + ").")
                elif(self.matrix[i][j].cellCharacter == 'C'):
                    facts.append("computer(" + str(self.matrix[i][j].cellId) + "," + str(i) + "," + str(j) + ").")

    def createSolverFile(self, facts : object):
        """Create solver file (../coreFile)
        
        Arguments:
            facts {object} -- Facts list
        """
        solverFile = open(self.dir_path + "/../../coreFile", "w")
        for i in facts:
            solverFile.write(i)
        solverFile.write("\n")
        for i in self.program:
            solverFile.write(i)

        solverFile.close()



    def solve(self):
        """Solve the program (computer move)
        """
        # calculate facts
        facts = []
        self.makeFacts(facts)

        # if there are more than one cell the game continue
        computers = [i for i in facts if 'computer' in i]
        if len(computers) > 1:
            # create solver file
            self.createSolverFile(facts)
    
            try:
                finalCommand = subprocess.check_output("idlv " + self.dir_path + "/../../coreFile" + " --filter=move/3 | wasp | grep move\(.*\)", shell=True)
                self.todo = str(finalCommand, "utf-8")

            except subprocess.CalledProcessError as e:
                # solver error
                print("Il solver non ha più mosse, hai vinto!")
#                 raise RuntimeError("Solver error")
                self.initGameMatrix()
                self.todo=""            
        
        else:
            self.initGameMatrix()
            
            