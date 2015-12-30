#!/usr/bin/env python
"""
This is the main file for a script that reads info off a game on kongregate.com and acts upon it.

"""
# import line/s for builtin modules
import pyautogui, logging, time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

# logging.disable(logging.DEBUG) # uncomment to block debug log messages

__author__ = "Alex Flores Escarcega"
__copyright__ = "Copyright 2007, Alex Flores Escarcega"
__credits__ = ["Alex Flores Escarcega"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Alex Flores Escarcega"
__email__ = "alex.floresescar@gmail.com"
__status__ = "Development"

# game located at http://www.kongregate.com/games/Volch/endless-expansion?haref=HP_TGTM_endless-expansion

GAME_REGION = (0, 0, 1000, 600)  # The x and y coordinates of the game window. 1000 is the width and 600 the height.


def find_game_region():
    """
    Uses image top_right_corner.png to find the coordinates of the game.
    Inputs: none
    Outputs: *****the output the locateOnScreen******
    """
    logging.debug('About to take a screenshot and look for top_right_corner.png')
    coors = pyautogui.locateOnScreen("images/top_right_corner.png")
    if coors is None:
        raise Exception('The game was not found on this screen. Is it invisible?')
    return (coors[0], coors[1])


def set_game_region():
    """x
    Sets the constant GAME_REGION to whatever find_game_region finds it at.
    Input: None
    Output: None
    """
    game_dimenstions = find_game_region()
    global GAME_REGION
    GAME_REGION = (game_dimenstions[0]-600, game_dimenstions[1]-30, 1000, 600)  # The top left corner of game is 600 px away from where top left of image and 30 px above.
    logging.debug("Set GAME_REGION to: " + str(GAME_REGION) + "")

def block_to_coors(block):
    """
    Determines what the coors are of a block given.
    Input: Block indices
    Output: (x,y) Otherwise known as the coordinates on the screen of the blocks
    """
class Block():
    """Provides the template for what a block should be and what values it holds.



def main():
    """
    Just now runs main()
    inputs: none
    outputs: none
    """
    set_game_region()
    print GAME_REGION

if __name__ == "__main__":
    main()
