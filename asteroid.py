import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        new_velocity_l = self.velocity.rotate(-angle)
        new_velocity_r = self.velocity.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_l = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_r = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid_l.velocity = new_velocity_l * 1.2
        new_asteroid_r.velocity = new_velocity_r * 1.2

    def update(self, dt):
        self.position += self.velocity * dt