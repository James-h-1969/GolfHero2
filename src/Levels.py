from constants import *
import pygame
from Ball import Ball
from PowerBar import PowerBar

class Levels():
    def __init__(self, clock, draw):
        self.unlocked = [True, False, False, False, False, False, False, False, False]
        self.playing = 1
        self.clock = clock
        self.draw = draw

    def unlock_hole(self) -> int:
        """
        holds record of how many holes have been played so far

        Args:
        self -> changes own property

        Returns:
        i: how many holes have been unlocked
        """
        for i in range(HOLES):
            if not self.unlocked[i]:
                self.unlocked[i] == True
                return i
        return HOLES
    
    def is_hole_unlocked(self, i: int) -> bool:
        """
        checks whether a specific hole is unlocked

        Args:
        i: what hole to check

        Returns:
        is_unlocked: boolean of whether locked or not
        """
        return self.unlocked[i-1]

    def play_level(self) -> None:
        """
        plays the level till exit or finish
        
        """
        print("Starting Level " + str(self.playing) + " ! ")


        self.running = True
        ball = Ball(100, 300)
        power_bar = PowerBar()

        while self.running:
            self.clock.tick(FPS)
            events = pygame.event.get()
            check_exit(events)
            power_bar.current_power_bar()

            mouse_coords = pygame.mouse.get_pos() 
            self.draw.draw_colour()
            ball.draw_ball(self.draw.window)
            ball.show_arrow(self.draw.window, mouse_coords)
            if ball.y < BOTTOM_FLOOR_HEIGHT and ball.dy >= 0:
                ball.update_pos()
            else:
                ball.bounce(vert=True)
            self.draw.draw_power(power_bar)
            pygame.display.update()
            # Create a ball at the required place
            # check whether it gets to the hole


        if (self.playing == HOLES):
            print("Congratulations, You have finished the game")
            print("Ending your pygame session... Thanks for playing!")
            pygame.quit()
            sys.exit()
        
        # FINISHED THE HOLE #
        print("\nCongratulations, Level " + str(self.playing) + " Completed. Next hole unlocked!\n")
        self.unlocked[self.playing] = True
        self.playing += 1
        return "Level Select"

    def set_level(self, i: int) -> None:
        """
        updates the level that we are currently playing
        
        """
        self.playing = i


