import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_vol1 = self.velocity.rotate(angle) * 1.2
        new_vol2 = self.velocity.rotate(-angle) * 1.2
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid1.velocity = new_vol1
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid2.velocity = new_vol2