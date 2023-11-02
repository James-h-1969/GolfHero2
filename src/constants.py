import pygame
import sys
import os
from typing import List

# constants for the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650

#timing constants
FPS = 60

# golf constants
HOLES = 9

# colour constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# HELPER FUNCTIONS
def check_exit(events: List[pygame.event.Event]):
    """
    Sees whether the program should exit

    Args:
    events -> List of events at the given moment

    Returns:
    None -> will exit if needed
    """
    for event in events:
        if event.type == pygame.QUIT:
            print("Ending your pygame session... Thanks for playing!")
            pygame.quit()
            sys.exit()

def get_and_scale_image(image_name: str, width: int, height: int):
    """
    finds the image and scales it to the required width and height

    Args:
    image_name -> name of the string in the images directory
    width -> new width of the image
    height -> new height of the image

    Returns:
    img -> the new image
    """
    img = pygame.transform.scale(pygame.image.load(os.path.join('src', 'imgs', image_name)).convert_alpha(), (width, height))
    return img