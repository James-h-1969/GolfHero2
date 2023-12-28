import pygame 
from constants import *
import numpy as np

class Ball():
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
        self.dx = 0
        self.dy = 0
        self.vec = 0
        self.dy_dot = GRAVITY
        self.airborne = True
        
    def update_pos(self):
        # called at each tik, will use equations of motion
        self.x += self.dx
        self.y += self.dy
        if self.airborne:
            self.dy += self.dy_dot
        if self.dy == 0:
            self.dx /= 1.1


    def give_velocity(self, vel:float):      
        self.dx = self.vector[0] * vel / 7000
        self.dy = -1 * self.vector[1] * vel / 7000

    def bounce(self, vert:bool, lim:int):
        if vert:
            self.dy = self.dy * -1 * ELASTICITY_COEFFICENT
            self.y = lim + self.dy
            self.dx /= 1.2
            if abs(self.dy) < 1:
                self.airborne = False
                self.dy = 0
        else:
            self.dx = self.dx * -1 * ELASTICITY_COEFFICENT
            self.x = lim + self.dx
      
    def draw_ball(self, window) -> None:
        pygame.draw.circle(window, WHITE, (self.x, self.y), BALL_SIZE)

    def show_arrow(self, window, mouse_coords, power_strength):
        if self.airborne:
            return
        self.vector = np.array([mouse_coords[0]-self.x,mouse_coords[1]-self.y])
        unit_vector = (power_strength+100)/200 * ARROW_SIZE * self.vector/np.linalg.norm(self.vector)
        pygame.draw.line(window, RED, (self.x, self.y), (self.x + unit_vector[0], self.y + unit_vector[1]), ARROW_THICKNESS)

    def set_airborne(self):
        self.airborne = True

