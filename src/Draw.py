import pygame
from typing import List
from constants import *
import Levels
from Ball import Ball

class Draw():
    def __init__(self, window):
        self.window = window

    def show_available_levels(self, levels: Levels, home_screen: bool, events:List[pygame.event.Event], quit_homepage, show_locked) -> None:
        """
        shows how many levels are unlocked. Currently shown by either green (unlocked) or red (locked)
        
        Args: 
        Levels: object which contains how many have been unlocked
        home_screen: boolean of whether on home screen or not (allows flexibility later)

        Returns:
        None
        """
        if home_screen:
            mouse_pressed = False
            BOX_SIZE = 140
            mouse_coords = pygame.mouse.get_pos() 
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pressed = True
                else:
                    mouse_pressed = False
            arrow = False
            def make_squares(length_of_row, starting_x, y_val, offset, mouse_pressed, arrow):
                for i in range(length_of_row):  
                    # logic so that 
                    if mouse_pressed:
                        if is_mouse_in_box(mouse_coords, starting_x, y_val, BOX_SIZE, BOX_SIZE):
                            if levels.is_hole_unlocked(i+1+offset):
                                quit_homepage()
                            else:
                                show_locked(str(i+1+offset))
                    # decide on the colour (depending on whether unlocked)
                    if is_mouse_in_box(mouse_coords, starting_x, y_val, BOX_SIZE, BOX_SIZE):
                        arrow = True
                    
                    if levels.is_hole_unlocked(i+1+offset):
                        img_name = "level-yes.png"
                    else:
                        img_name = "level-no.png"
                    self.draw_img(get_and_scale_image(img_name, BOX_SIZE, BOX_SIZE), (starting_x, y_val))
                    make_and_place_text(starting_x+ BOX_SIZE/2, y_val+BOX_SIZE-10, "Ariel", 40, str(i+1+offset), WHITE, self.window)
                    starting_x += 150 # move along to next rectangle
                    if arrow:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    else:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                return arrow
            
            arrow = make_squares(5, 40, 250, 0, mouse_pressed, arrow) # first row
            make_squares(4, 100, 400, 5, mouse_pressed, arrow) # second row

        pygame.display.update()

    def draw_img(self, image, coords):
        self.window.blit(image, coords)

    def logo(self):
        make_and_place_text(SCREEN_WIDTH - 300, SCREEN_HEIGHT - 50, "Arial", 30, "Made by Bogey Boys Inc.", WHITE, self.window)

    def draw_colour(self):
        self.window.fill(BLACK)

    def draw_score(self, score):
        make_and_place_text(SCREEN_WIDTH - 40, 20, "Arial", 60, str(score.get_score()), WHITE, self.window)

    def draw_power(self, power_bar):
        pygame.draw.rect(self.window, WHITE, power_bar.bounding_rect)
        pygame.draw.rect(self.window, power_bar.colour, power_bar.rect)
