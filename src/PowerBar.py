import pygame
from constants import *

class PowerBar():
    def __init__(self):
        self.strength = 0

    def current_power_bar(self):
        self.rect = pygame.Rect(PADDING, SCREEN_HEIGHT - 2 * PADDING, self.strength, PADDING)
        self.bounding_rect = pygame.Rect(PADDING - 5, SCREEN_HEIGHT - 2 * PADDING - 5, MAX_POWER + 10, PADDING + 10)
        if self.strength < 150:
            self.colour = GREEN
        elif self.strength < 250:
            self.colour = YELLOW
        elif self.strength < 350:
            self.colour = ORANGE
        else:
            self.colour = RED

    def add_power(self):
        if self.strength < MAX_POWER:
            self.strength += POWER_INCREMENT

    def reset(self):
        self.strength = 0

