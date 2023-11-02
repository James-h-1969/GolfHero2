import pygame
from typing import List
from constants import *
import Levels

class Draw():
    def __init__(self, window):
        self.window = window

    def show_available_levels(self, levels: Levels, home_screen: bool) -> None:
        """
        shows how many levels are unlocked. Currently shown by either green (unlocked) or red (locked)
        
        Args: 
        Levels: object which contains how many have been unlocked
        home_screen: boolean of whether on home screen or not (allows flexibility later)

        Returns:
        None
        """
        if home_screen:
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

    def draw_background(self, image):
        self.window.blit(image, (0, 0))