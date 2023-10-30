import pygame
from constants import *
import sys



def main():
    ##  INITIATE THE PYGAME FUNCTIONS  ##
    pygame.init()
    WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # set the screen dimensions
    CLOCK = pygame.time.Clock() # create the clock    
    pygame.display.set_caption("GOLF HERO") # set the caption of the window


    running = True
    while running:
        CLOCK.tick(FPS)
        checkExit(pygame.event.get())


if __name__ == "__main__":
    main()