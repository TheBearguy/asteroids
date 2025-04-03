import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape): 
    def __init__(self, x, y, radius): 
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt): 
        self.position += self.velocity * dt 
    
    def split(self): 
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS: 
            self.kill()
        angle = random.uniform(20,50) 
        positive_direction = self.velocity.rotate(angle) 
        negative_direction = self.velocity.rotate(-angle)
        smol_radius = self.radius - ASTEROID_MIN_RADIUS
        smol_asteroid_one = Asteroid(self.position.x, self.position.y, smol_radius)
        smol_asteroid_two = Asteroid(self.position.x, self.position.y, smol_radius)
        smol_asteroid_one.velocity = positive_direction * 1.2
        smol_asteroid_two.velocity = negative_direction