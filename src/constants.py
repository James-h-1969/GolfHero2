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
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

def make_and_place_text(text_x:int, text_y:int, font_name:str, font_size:int,  text:str, colour:tuple, window):
    """
    creates text and puts it onto the screen

    Args:
    text_x -> x coordinate of the text
    text_y -> y_coordinate of the text
    font_name -> name of the font to use
    font_size -> size of the font
    text -> actual words to display
    colour -> colour of the font
    window -> window to display the text on

    Returns
    None
    
    """
    font = pygame.font.SysFont(font_name, font_size)
    text_placement = (text_x, text_y)  
    start = font.render(text, 1, colour)
    window.blit(start, text_placement)