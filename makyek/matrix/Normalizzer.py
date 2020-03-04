'''
Created on 26 feb 2019

@author: rodolfo
'''
from makyek.GlobalValues import HEIGHT, WIDTH, ROW_COUNT, COLUMN_COUNT


class Normalizer:
    '''Normalizzae class
    
    Class that transform convert Physic cordinates 
    to row/colum virtual cordinates
    '''

    @staticmethod
    def rowToPhysic(i : int):
        '''Row to physic Y cordinate
        
        Arguments:
            i {int} -- Row to convert
        
        Returns:
            int -- Physic y
        '''
        return HEIGHT/2 + i*HEIGHT


    @staticmethod
    def columToPhysic(j : int):
        """Colum to physic X cordinate
        
        Arguments:
            j {int} -- Colum to convert
        
        Returns:
            int -- Physic X
        """
        return WIDTH/2 + j*WIDTH

    @staticmethod
    def physicToRow(x : int):
        """Physic X cordinate to row

        Arguments:
            X {int} -- Cordinate to convert

        Returns:
            int -- X cordinate
        """
        for i in range(ROW_COUNT):
            if(x >= i*HEIGHT and x <= (i+1)*HEIGHT):
                return i

    @staticmethod
    def physicToColum(y : int):
        """Physic Y cordinate to colum

        Arguments:
            Y {int} -- Cordinate to convert

        Returns:
            int -- Y cordinate
        """
        for j in range(COLUMN_COUNT):
            if(y >= j*WIDTH and y <= (j+1)*WIDTH):
                return j
