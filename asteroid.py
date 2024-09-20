from constants import *
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)

        vector_1 = self.velocity.rotate(random_angle)
        vector_2 = self.velocity.rotate(-random_angle)

        old_radius = self.radius
        old_radius -= ASTEROID_MIN_RADIUS

        new_smaller_asteroid_1 = Asteroid(self.position.x, self.position.y, old_radius)
        new_smaller_asteroid_2 = Asteroid(self.position.x, self.position.y, old_radius)
        new_smaller_asteroid_1.velocity = vector_1*1.2
        new_smaller_asteroid_2.velocity = vector_2
        