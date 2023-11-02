import pygame
from constants import *
import os

class StartScreen():
    def __init__(self, clock, draw, levels):
        self.clock = clock
        self.draw = draw 
        self.levels = levels
        self.running = True # start while running

    def begin(self):
        print("Initiating start screen ... ")
        # can add more here to add to the story
        self.homepage()       

    def homepage(self):
        """
        homepage that can come back to and choose specific level 
        
        """
        print("Entering the home page ... ")
        while self.running:
            self.clock.tick(FPS)
            check_exit(pygame.event.get())
            # add music
            self.draw.draw_background(get_and_scale_image('background.jpg', SCREEN_WIDTH, SCREEN_HEIGHT)) # draws background
            # add title
            # clicking on box should result in either starting level or displaying (you dont have access to this level)
            self.draw.show_available_levels(self.levels, True) # show how many levels there are currently selected


