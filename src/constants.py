import pygame
import sys
from typing import List

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650

FPS = 60


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
            pygame.quit()
            sys.exit()