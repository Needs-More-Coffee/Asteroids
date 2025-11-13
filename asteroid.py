import random

import pygame
from circleshape import CircleShape
from constants import *
from logger import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        new_radius = self.radius = ASTEROID_MIN_RADIUS

        angle1 = random.uniform(20, 50)
        angle2 = random.uniform(20, 50)

        vector1 = self.velocity.rotate(angle1)
        vector2 = self.velocity.rotate(-angle2)
        
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vector1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vector2 