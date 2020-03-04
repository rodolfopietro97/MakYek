'''
Main file of project
Created on 26 feb 2019

@author: rodolfo
'''
import arcade
from makyek.gameloop.GameLoop import GameLoop
from makyek.GlobalValues import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH

if __name__ == '__main__':
    GameLoop(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()