import pygame.draw
from constants import *
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface = screen, color = "white", center = self.position, radius = self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        if self.radius <=ASTEROID_MIN_RADIUS:
            self.kill()

        rand_ang = random.uniform(20, 50)
        new_vector_plus = self.velocity.rotate(rand_ang)
        new_vector_minus = self.velocity.rotate(-rand_ang)

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        split_ast1 = Asteroid(self.position.x, self.position.y, new_rad)
        split_ast1.velocity = new_vector_plus * 1.2
        split_ast2 = Asteroid(self.position.x, self.position.y, new_rad)
        split_ast2.velocity = new_vector_minus * 1.2

        self.kill()
