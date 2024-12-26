import pygame
import random
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_STANDARD_SHOOT_COOLDOWN, PLAYER_FAST_SHOOT_COOLDOWN, PLAYER_SUPER_FAST_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.weapon_cooldown = 0
        image = pygame.image.load("assets/spaceship.png")
        self.image = pygame.transform.scale(image, (PLAYER_RADIUS * 4, PLAYER_RADIUS * 4))
        self.weapon = "standard"
        self.weapon_timer = 0
        self.shot_cone_active = False
        self.shot_cone_timer = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, -self.rotation + 180)
        new_rect = rotated_image.get_rect(center = (self.position.x, self.position.y))
        screen.blit(rotated_image, new_rect)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt, _):
        self.weapon_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        
        # Shooting is always active
        if self.weapon_cooldown <= 0:
            self.shoot()
        
        if self.shot_cone_timer <= 0:
            self.shot_cone_active = False
        else:
            self.shot_cone_timer -= dt
        
        if self.weapon_timer <= 0:
            self.weapon = "standard"
        else:
            self.weapon_timer -= dt
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        # Determine weapon speed
        if self.weapon == "super_fast":
            self.weapon_cooldown = PLAYER_SUPER_FAST_SHOOT_COOLDOWN
        elif self.weapon == "fast":
            self.weapon_cooldown = PLAYER_FAST_SHOOT_COOLDOWN
        else: 
            self.weapon_cooldown = PLAYER_STANDARD_SHOOT_COOLDOWN
    
        # Determine weapon type
        if self.shot_cone_active:
            for i in range(-30, 30, 5):
                shot = Shot(self.position.x, self.position.y, self.rotation + i)
                shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation + i) * PLAYER_SHOOT_SPEED
        else: 
            shot = Shot(self.position.x, self.position.y, self.rotation)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
    def reset(self, screen, x, y):
        self.rotation = 0
        self.weapon_cooldown = 0
        self.weapon = "standard"
        self.shot_cone_active = False
        self.shot_cone_timer = 0
        self.position = pygame.Vector2(x, y)
        rotated_image = pygame.transform.rotate(self.image, -self.rotation + 180)
        new_rect = rotated_image.get_rect(center = (x, y))
        screen.blit(rotated_image, new_rect)
        
            