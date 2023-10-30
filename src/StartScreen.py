import pygame
from constants import *

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
            checkExit(pygame.event.get())
            self.draw.showLevels(self.levels) # show how many levels there are currently selected


