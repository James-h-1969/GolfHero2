import pygame 
from constants import *
import numpy as np

class Ball():
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
        self.dx = 0
        self.dy = 0
        self.dy_dot = GRAVITY
        
    def update_pos(self):
        # called at each tik, will use equations of motion
        self.x += self.dx
        self.y += self.dy
        self.dy += self.dy_dot

    def give_velocity(self, dx:float, dy:float):
        self.dx = dx
        self.dy = dy

    def bounce(self, vert:bool):
        if vert:
            self.dy = self.dy * -1 * ELASTICITY_COEFFICENT
            self.y += self.dy
        else:
            self.dx = self.dx * -1 * ELASTICITY_COEFFICENT
            self.x += self.dx
      
    def draw_ball(self, window) -> None:
        pygame.draw.circle(window, WHITE, (self.x, self.y), BALL_SIZE)

    def show_arrow(self, window, mouse_coords):
        vector = np.array([mouse_coords[0]-self.x,mouse_coords[1]-self.y])
        unit_vector = ARROW_SIZE * vector/np.linalg.norm(vector)
        pygame.draw.line(window, RED, (self.x, self.y), (self.x + unit_vector[0], self.y + unit_vector[1]), ARROW_THICKNESS)

