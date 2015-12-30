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

def find_game_region():
    """
    Uses image top_right_corner.png to find the coordinates of the game.
    Inputs: none
    Outputs: *****the output the locateOnScreen******
    """
    logging.debug('About to take a screenshot and look for top_right_corner.png')
    coors = pyautogui.locateOnScreen("images/top_right_corner.png")
    if region is None:
        raise Exception('The game was not found on this screen. Is it invisible?')
    return (coors[0],coors[1])

def main():
    """
    Just now runs main()
    inputs: none
    outputs: none
    """
    print find_game_region()

if __name__ == "__main__":
    main()
