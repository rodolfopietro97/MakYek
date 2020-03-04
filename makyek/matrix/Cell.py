'''
Cell class
Created on 26 feb 2019

@author: rodolfo
'''
import arcade
import itertools
from makyek.matrix.Normalizzer import Normalizer
from makyek.GlobalValues import WIDTH, HEIGHT
from makyek.matrix.CellRangeGetter import CellRangeGetter


class Cell:
    """Cell class
    This class rapresent a logical cell of matrix
    """
    counter = itertools.count()
    
    def __init__(self, cellCharacter : str):
        """Constructor with parameters

        Arguments:
            cellCharacter {str} -- Character contained in a cell

        """
        self.cellCharacter = cellCharacter
        # autoincrement cell id
        self.cellId = next(self.counter)



    @staticmethod
    def drawSquare(i : int, j : int, backgroundCount : int):
        """Draw a square in game matric
        
        Arguments:
            i {int} -- Row in which we draw square
            j {int} -- Colum in which we draw square
            backgroundCount {int} -- background of square (odd or even)
        """
        if(backgroundCount%2 == 0):
            arcade.draw_rectangle_filled(
                            Normalizer.columToPhysic(j), 
                            Normalizer.rowToPhysic(i), 
                            WIDTH, 
                            HEIGHT, 
                            (255,206,158))
        else:
            arcade.draw_rectangle_filled(
                            Normalizer.columToPhysic(j), 
                            Normalizer.rowToPhysic(i), 
                            WIDTH, 
                            HEIGHT, 
                            (209,139,71))


    @staticmethod
    def drawPlayer(i : int, j : int, type : str):
        """Draw a circle (Player or Computer)
        
        Arguments:
            i {int} -- Row in which we draw player
            j {int} -- Colum in which we draw player
            type {str} -- C (computer) or P (player)
        """
        # computer
        if(type == 'C'):
            arcade.draw_ellipse_filled(
                Normalizer.columToPhysic(j)+2,
                Normalizer.rowToPhysic(i)+2,
                WIDTH/2-5,
                HEIGHT/2-5,
                arcade.color.BLACK)
        # player
        elif(type == 'P'):
            arcade.draw_ellipse_filled(
                Normalizer.columToPhysic(j)+2,
                Normalizer.rowToPhysic(i)+2,
                WIDTH/2-5,
                HEIGHT/2-5,
                arcade.color.WHITE)

    @staticmethod
    def drawPlayerClicked(i : int, j : int):
        """Draw a clicked player
        
        Arguments:
            i {int} -- Row in which we draw player
            j {int} -- Colum in which we draw playe
        """
        arcade.draw_ellipse_filled(
            Normalizer.columToPhysic(j)+2,
            Normalizer.rowToPhysic(i)+2,
            WIDTH/2-5,
            HEIGHT/2-5,
            arcade.color.BLUE)

    @staticmethod
    def drawHints(i : int, j : int):
        """Draw game hints
        
        Arguments:
            i {int} -- Row in which we draw player
            j {int} -- Colum in which we draw playe
        """
        eatableCells = CellRangeGetter.getEatableCellsDirection(4, i, j)
        
        for c in eatableCells:
            arcade.draw_ellipse_filled(
                    Normalizer.columToPhysic(c[1])+2,
                    Normalizer.rowToPhysic(c[0])+2,
                    WIDTH/2-5,
                    HEIGHT/2-5,
                    arcade.color.BLUE)



    @staticmethod
    def drawTextInfo(i : int, j : int, cellCharacter : str, cellId : int):
        """Draw text info of a cell

        Useful in debug
        
        Arguments:
            i {int} -- Row in which we draw text
            j {int} -- Colum in which we draw text
            cellCharacter {str} -- Character contained in the cell
            cellCharacter {int} -- Id contained in the cell
        """
        arcade.draw_text("(R:" + str(i) + " , C:" + str(j) + ")\n" + cellCharacter + " , " + str(cellId) + ")", 
            Normalizer.columToPhysic(j), 
            Normalizer.rowToPhysic(i), 
            arcade.color.RED, 
            5)
