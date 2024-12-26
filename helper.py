import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def draw_start_menu(screen):
    font = pygame.font.SysFont('arial', 40)
    start_button = font.render('Start Asteroids', True, (255, 255, 255))
    press_key = font.render('(Press any key to start)', True, (255, 255, 255))
    screen.blit(start_button, (SCREEN_WIDTH/2 - start_button.get_width()/2, SCREEN_HEIGHT/2 + start_button.get_height()/2))
    screen.blit(press_key, (SCREEN_WIDTH/2 - press_key.get_width()/2, SCREEN_HEIGHT/2 + press_key.get_height() * 1.5))
    pygame.display.update()
    
def draw_game_over_screen(screen, score):
   font = pygame.font.SysFont('arial', 40)
   title = font.render('Game Over', True, (255, 255, 255))
   restart_button = font.render('R - Restart', True, (255, 255, 255))
   quit_button = font.render('Q - Quit', True, (255, 255, 255))
   your_score = font.render(f"Your Score: {score}", True, "white")
   screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/4))
   screen.blit(your_score, (SCREEN_WIDTH/2 - your_score.get_width()/2, SCREEN_HEIGHT/2 + your_score.get_height()/1.5))
   screen.blit(restart_button, (SCREEN_WIDTH/2 - restart_button.get_width()/2, SCREEN_HEIGHT/2 + restart_button.get_height() * 2))
   screen.blit(quit_button, (SCREEN_WIDTH/2 - quit_button.get_width()/2, SCREEN_HEIGHT/2 + quit_button.get_height() * 3))
   pygame.display.update()
