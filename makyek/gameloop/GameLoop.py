'''
Game loop main class
Created on 26 feb 2019

@author: rodolfo
'''

import arcade
from makyek.matrix.GameMatrix import GameMatrix
from makyek.matrix.Normalizzer import Normalizer


class GameLoop(arcade.Window):
    """Game loop class
    
    Arguments:
        arcade.Window {object} -- main class of arcade framework 
    """

    def __init__(self, width : int, height : int, title : str):
        """Constructor with parameters
        
        Arguments:
            width {int} -- width of window game
            height {int} -- height of window game
            title {str} -- title of window game
        """
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        # game matrix instance
        self.gameMatrix = GameMatrix()


    def on_draw(self):
        """Draw function
        
        main draw function
        """
        arcade.start_render()

        # draw game matrix
        self.gameMatrix.draw()

    def update(self, delta_time):
        """Main update function
        
        Arguments:
            delta_time {int} -- delta time between updates
        """
        self.gameMatrix.update()


    def on_mouse_press(self, x, y, button, modifiers):
        """Mouse press function
        
        Arguments:
            x {int} -- x of mouse
            y {int} -- y of mouse
            button {str} -- button pressed
        """
        # if we click and is our round
        if button == arcade.MOUSE_BUTTON_LEFT and self.gameMatrix.round == 0:

            # if is not clicked a player
            if(not self.gameMatrix.isClickedPlayer()):
                self.gameMatrix.clickedRow = Normalizer.physicToRow(y)
                self.gameMatrix.clickedColum = Normalizer.physicToColum(x)

            # if is already clicked a player
            else:
                self.gameMatrix.canMovePlayer(x, y)