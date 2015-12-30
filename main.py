#!/usr/bin/env python
"""
This is the main file for a script that reads info off a game on kongregate.com and acts upon it.

"""
# import line/s for builtin modules
# import pyautogui

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
    Finds the top left coordinates of the game by substracting (700 + 300) from the location of the game. 
    The 300 comes from the width of the top_right_corner.png file that is used to locate the top right corner.
    Input: None.
    Output: the top left coordinates. Two elements in a tuple.

    coors = pyautogui.locateOnScreen("images/top_right_corner.png")
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
