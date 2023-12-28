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

    def play_level(self, score) -> None:
        """
        plays the level till exit or finish
        
        """
        print("Starting Level " + str(self.playing) + " ! ")


        self.running = True
        ball = Ball(100, 300)
        power_bar = PowerBar()
        pressed = False

        while self.running:
            self.clock.tick(FPS)
            events = pygame.event.get()
            check_exit(events)

            # Handle adding the power
            if check_button_down(events, "SPACE"):
                pressed = True
            if check_button_up(events, "SPACE"):
                pressed = False
                if not ball.airborne:
                    ball.give_velocity(power_bar.strength) # need to give a dx, dy. should get this from the direction of the arrow (in the ball, and the power)
                    ball.set_airborne()
                    score.add_to_score(1)
                power_bar.reset()
            if pressed:
                power_bar.add_power()

            power_bar.current_power_bar()

            mouse_coords = pygame.mouse.get_pos() 
            self.draw.draw_colour()
            ball.draw_ball(self.draw.window)
            ball.show_arrow(self.draw.window, mouse_coords, power_bar.strength)

            if ball.y < BOTTOM_FLOOR_HEIGHT and ball.x >= 0 and ball.x < SCREEN_WIDTH:
                ball.update_pos()
            else:
                if ball.y >= BOTTOM_FLOOR_HEIGHT:
                    ball.bounce(vert=True, lim=BOTTOM_FLOOR_HEIGHT)
                else:
                    if ball.x < 0:
                        ball.bounce(vert=False, lim=0)
                    else:
                        ball.bounce(vert=False, lim=SCREEN_WIDTH)

            

            self.draw.draw_power(power_bar)
            self.draw.draw_score(score)
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


