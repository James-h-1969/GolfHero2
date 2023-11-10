import pygame
from constants import *
import os

class StartScreen():
    def __init__(self, clock, draw, levels, window):
        self.clock = clock
        self.draw = draw 
        self.levels = levels
        self.running = True # start while running
        self.window = window
        # showing if they click a lvl that is locked
        self.showing_locked = False
        self.locked_level = ""


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
            events = pygame.event.get()
            check_exit(events)
            # add music
            self.draw.draw_img(get_and_scale_image('background.jpg', SCREEN_WIDTH, SCREEN_HEIGHT), (0,0)) # draws background
            make_and_place_text(SCREEN_WIDTH/2 - 220, 110, "Ariel", 140, "Pick Hole", WHITE, self.window) # writes title
            self.draw.logo() # shows made by bogey boys
            if self.showing_locked:
                make_and_place_text(SCREEN_WIDTH/2 - 90, 560, "Ariel", 40, "Hole " + self.locked_level + " is locked.", RED, self.window) # writes title
            self.draw.show_available_levels(self.levels, True, events, self.quit_homepage, self.show_locked) # show how many levels there are currently selected

    def quit_homepage(self):
        self.running = False

    def show_locked(self, hole: str):
        self.showing_locked = True
        self.locked_level = hole

