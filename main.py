# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from helper import draw_game_over_screen, draw_game_stats, draw_start_menu
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from upgradefield import UpgradeField
from upgrade import Upgrade, FastWeapon, SuperFastWeapon
from shot import Shot

def main():
    # Init game
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load("assets/night_sky.jpeg")
    font = pygame.font.SysFont('arial', 40)
    
    # Variables
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    level = 0
    level_timer = 10
    lvl_text = font.render(f'Level: 1', True, "lightgray")
    
    # Objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    upgrades = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Upgrade.containers = (upgrades, updatable, drawable)
    FastWeapon.containers = (upgrades, updatable, drawable)
    SuperFastWeapon.containers = (upgrades, updatable, drawable)
    UpgradeField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField()
    UpgradeField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  
    
    game_state = GAME_STATE["MENU"]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.blit(background, (0,0))
        
        if game_state == GAME_STATE["MENU"]:
            draw_start_menu(screen)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    game_state = GAME_STATE["GAME"]
        
        if game_state == GAME_STATE["OVER"]:
            draw_game_over_screen(screen, score)
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                for asteroid in asteroids:
                    asteroid.kill()
                for shot in shots:
                    shot.kill()
                for upgrade in upgrades:
                    upgrade.kill()
                player.reset(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                score = 0
                level = 0
                level_timer = 10
                lvl_text = font.render(f'Level: 1', True, "lightgray")
                game_state = GAME_STATE["GAME"]
            if keys[pygame.K_q]:
                pygame.quit()
                quit()
  
        if game_state == GAME_STATE["GAME"]:
        
            for object in updatable:
                object.update(dt, level)
            
            for asteroid in asteroids:
                if asteroid.explode == False:
                    for shot in shots:
                        if asteroid.check_collision(shot):
                            shot.kill()
                            score += asteroid.split()
                    if asteroid.check_collision(player):
                        game_state = GAME_STATE["OVER"]
            
            for upgrade in upgrades:
                for shot in shots:
                    if upgrade.check_collision(shot):
                        upgrade.upgrade(player)
                
            for object in drawable:
                object.draw(screen)
            
            score += SCORE_TIME_INCREMENT
            
            if level_timer < 8:
                lvl_text = font.render("", True, "white")
            
            level_timer -= dt
            if level_timer <= 0:
                level_timer = 10
                if level < len(ASTEROID_SPAWN_RATE):
                    level += 1
                    lvl_text = font.render(f'Level: {level + 1}', True, "lightgray")
            
            draw_game_stats(screen, score, level, lvl_text)
                
                
            pygame.display.flip()
            
            # Convert from ms to s; tick will pause the game until 1/60th of a second has passed
            dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
    