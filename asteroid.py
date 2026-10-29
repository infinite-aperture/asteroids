import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self, dt: float) -> None:
        self.position = self.position + (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            log_event("asteroid_shot")
            return
        else:
            log_event("asteroid_split")
            first_angle = random.uniform(20,50)
            first_velocity = self.velocity.rotate(first_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity= first_velocity * 1.2
            asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid2.velocity= -first_velocity *1.2
            log_event("asteroid_split")
