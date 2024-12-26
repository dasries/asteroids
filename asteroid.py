import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        image = pygame.image.load("assets/asteroid.png")
        self.image = pygame.transform.scale(image, (radius, radius))
        self.rotation = 0
        
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        new_rect = rotated_image.get_rect(center = (self.position.x, self.position.y))
        screen.blit(rotated_image, new_rect)
    
    def update(self, dt, _):
        self.position += self.velocity * dt
        self.rotation += random.randint(20, 150) * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 1000
        angle = random.uniform(20, 50)
        vec_one = pygame.Vector2(self.velocity.rotate(angle))
        vec_two = pygame.Vector2(self.velocity.rotate(-angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vec_one * 1.2
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vec_two * 1.2
        return 100    
        
        