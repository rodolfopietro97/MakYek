'''
Created on 2 mar 2019

@author: rodolfo
'''
from makyek.GlobalValues import ROW_COUNT, COLUMN_COUNT

class CellRange:
    
    def __init__(self):
        self.cells = []
        
    def append(self, cell):
        if (cell[0] in range(0, ROW_COUNT)) and (cell[1] in range(0, COLUMN_COUNT)):
            self.cells.append((cell[0], cell[1]))
        

class CellRangeGetter:
    '''
    Cell range getter class
    '''


    @staticmethod
    def getEatableCellsDirection(direction : int, i : int, j : int, i1 : int, j1 : int):
        nearCells = CellRange()
        
        if direction == 1:
            if(i1 == i+2): # if i make a double movement
                nearCells.append((i+1, j))
            
            for ti in range(i, i1+1):
                nearCells.append((ti, j-1))
                nearCells.append((ti, j+1))

        
        elif direction == 2:
            if(j1 == j+2):
                nearCells.append((i, j+1))

            for tj in range(j, j1+1):
                nearCells.append((i-1, tj))
                nearCells.append((i+1, tj))

        
        elif direction == 3:
            if(i1 == i-2): # if i make a double movement
                nearCells.append((i-1, j))
                
            for ti in range(i1, i+1):
                nearCells.append((ti, j-1))
                nearCells.append((ti, j+1))

        
        elif direction == 4:
            if(j1 == j-2):
                nearCells.append((i, j-1))
            if(j1 > j-2):
                nearCells.append((i, j-1))
                nearCells.append((i, j-2))

            for tj in range(j1, j+1):
                nearCells.append((i-1, tj))
                nearCells.append((i+1, tj))

        
        return nearCells.cells
    
        