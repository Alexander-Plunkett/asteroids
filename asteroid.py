import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity = 0):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def move(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_velocity_one = self.velocity.rotate(random_angle) * 1.2
        new_velocity_two = self.velocity.rotate(-random_angle) * 1.2
        
        Asteroid(self.position.x, self.position.y, new_radius, new_velocity_one)
        Asteroid(self.position.x, self.position.y, new_radius, new_velocity_two)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def isColliding(self, CircleShape):
        distance_between = pygame.math.Vector2.distance_to(CircleShape.position, self.position)
        if distance_between < (self.radius + CircleShape.radius):
            return True
        return False

    def update(self, dt):
        self.move(dt)