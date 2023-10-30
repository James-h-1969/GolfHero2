import pygame
from constants import *

class StartScreen():
    def __init__(self, clock, draw, levels):
        self.clock = clock
        self.running = True # start while running
        self.draw = draw 
        self.levels = levels

    def begin(self):
        while self.running:
            self.clock.tick(FPS)
            checkExit(pygame.event.get())


