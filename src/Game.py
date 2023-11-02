import pygame
from constants import *
import sys
from StartScreen import *
from Draw import *
from Levels import *


def main():
    print("Beginning Golf Hero 2 ... Good luck!")
    
    ##  INITIATE THE PYGAME FUNCTIONS  ##
    pygame.init()
    WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # set the screen dimensions
    CLOCK = pygame.time.Clock() # create the clock    
    pygame.display.set_caption("GOLF HERO 2") # set the caption of the window

    ## CREATE INSTANCES OF EACH OBJECT ##
    draw = Draw(WINDOW)
    levels = Levels()
    start_screen = StartScreen(CLOCK, draw, levels, WINDOW)

    ## BEGIN GAME LOGIC ##
    start_screen.begin()

if __name__ == "__main__":
    main()