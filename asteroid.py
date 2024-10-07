import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def move(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def isColliding(self, CircleShape):
        distance_between = pygame.math.Vector2.distance_to(CircleShape.position, self.position)
        if distance_between < (self.radius + CircleShape.radius):
            return True
        return False

    def update(self, dt):
        self.move(dt)