import pygame
import random
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED, UPGRADE_RADIUS, UPGRADE_DURATION
from shot import Shot

class Upgrade(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, UPGRADE_RADIUS * 2)
        self.image = None
        
    def draw(self, screen):
        screen.blit(self.image, self.position)
        
    def update(self, dt, _):
        self.position += self.velocity * dt
        
    def player_collision():
        pass
    
class FastWeapon(Upgrade):
    def __init__(self, position):
        super().__init__(position)
        image = pygame.image.load("assets/fast.png")
        self.image = pygame.transform.scale(image, (UPGRADE_RADIUS * 2, UPGRADE_RADIUS * 2))
    
    def upgrade(self, player):
        player.weapon = "fast"
        player.weapon_timer = UPGRADE_DURATION
        self.kill()
        
class SuperFastWeapon(Upgrade):
    def __init__(self, position):
        super().__init__(position)
        image = pygame.image.load("assets/super_fast.png")
        self.image = pygame.transform.scale(image, (UPGRADE_RADIUS * 2, UPGRADE_RADIUS * 2))
    
    def upgrade(self, player):
        player.weapon = "super_fast"
        player.weapon_timer = UPGRADE_DURATION
        self.kill()
    
class ShotCone(Upgrade):
    def __init__(self, position):
        super().__init__(position)
        image = pygame.image.load("assets/fire.png")
        self.image = pygame.transform.scale(image, (UPGRADE_RADIUS * 2, UPGRADE_RADIUS * 2))
        
    def upgrade(self, player):
        self.kill()
        player.shot_cone_timer = UPGRADE_DURATION
        player.shot_cone_active = True
        
class Fireball(Upgrade):
    def __init__(self, position):
        super().__init__(position)
        image = pygame.image.load("assets/fireball.png")
        self.image = pygame.transform.scale(image, (UPGRADE_RADIUS * 2, UPGRADE_RADIUS * 2))
        
    def upgrade(self, player):
        self.kill()
        for i in range(0, 360, 10):
            shot = Shot(player.position.x, player.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(i) * PLAYER_SHOOT_SPEED
        
    
    