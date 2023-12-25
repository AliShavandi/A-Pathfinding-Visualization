"""
Program: A* Pathfinding algorythm visualization in Python
Author: Ali Shavandi
Date: Dec 23, 2022
"""

#import modules and files
import pygame as pg
from Node import Node
import methods
from menu import main_menu

#window setup
WIDTH = 800
WINDOW = pg.display.set_mode((WIDTH, WIDTH))
pg.display.set_caption("A* Path Finding Algorithm")

#call main program function
main_menu(WINDOW, WIDTH)