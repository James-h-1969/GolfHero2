import pygame
import sys
from typing import List

# constants for the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650

#timing constants
FPS = 60

# golf constants
HOLES = 9

# HELPER FUNCTIONS
def checkExit(events: List[pygame.event.Event]):
    """
    Sees whether the program should exit

    Args:
    events -> List of events at the given moment

    Returns:
    None -> will exit if needed
    """
    for event in events:
        if event.type == pygame.QUIT:
            print(" Ending your pygame session... Thanks for playing!")
            pygame.quit()
            sys.exit()
