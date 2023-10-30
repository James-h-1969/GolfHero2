import pygame
from typing import List
from constants import *
import Levels

class Draw():
    def __init__(self, window):
        self.window = window

    def showLevels(self, levels: Levels) -> None:
        """
        shows how many levels are unlocked. Currently shown by either green (unlocked) or red (locked)
        
        """
        def make_squares(length_of_row, starting_x, y_val, offset):
            for i in range(length_of_row):  
                level_rect = pygame.Rect(starting_x, y_val, 50, 50)  
                # decide on the colour (depending on whether unlocked)
                if levels.is_hole_unlocked(i+1+offset):
                    level_colour = GREEN
                else:
                    level_colour = RED
                pygame.draw.rect(self.window, level_colour, level_rect)
                starting_x += 100 # move along to next rectangle

        make_squares(5, 200, 300, 0) # first row
        make_squares(4, 250, 400, 5) # second row
        
        pygame.display.update()