import pygame
import random
from upgrade import FastWeapon, SuperFastWeapon, Fireball, ShotCone
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, UPGRADE_RADIUS, UPGRADE_SPAWN_RATE

class UpgradeField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-UPGRADE_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + UPGRADE_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -UPGRADE_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + UPGRADE_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, position, velocity):
        random_weapon_num = random.randint(0,3)
        upgrade = None
        if random_weapon_num == 0:
            upgrade = FastWeapon(position)
        elif random_weapon_num == 1:
            upgrade = SuperFastWeapon(position)
        elif random_weapon_num == 3:
            upgrade = Fireball(position)
        else:
            upgrade = ShotCone(position)
        upgrade.velocity = velocity

    def update(self, dt, level):
        self.spawn_timer += dt
        if self.spawn_timer > UPGRADE_SPAWN_RATE - level/100 * random.uniform(0,1):
            self.spawn_timer = 0

            # spawn a new upgrade at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            self.spawn(position, velocity)