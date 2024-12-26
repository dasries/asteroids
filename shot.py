import pygame
import random
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        image = pygame.image.load("assets/shot.png")
        self.image = pygame.transform.scale(image, (SHOT_RADIUS * 4, SHOT_RADIUS * 4))
        self.rotation = rotation
        
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        new_rect = rotated_image.get_rect(center = (self.position.x, self.position.y))
        screen.blit(rotated_image, new_rect)
    
    def update(self, dt, _):
        self.position += self.velocity * dt