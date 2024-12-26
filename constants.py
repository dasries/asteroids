SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = [1.0, 0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1]  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 10
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 250
PLAYER_SHOOT_SPEED = 500
PLAYER_STANDARD_SHOOT_COOLDOWN = 0.3
PLAYER_FAST_SHOOT_COOLDOWN = 0.2
PLAYER_SUPER_FAST_SHOOT_COOLDOWN = 0.1

SHOT_RADIUS = 5

SCORE_TIME_INCREMENT = 1

UPGRADE_RADIUS = 20
UPGRADE_SPAWN_RATE = 8.0
UPGRADE_DURATION = 8.0

GAME_STATE = {
    "MENU": "start_menu",
    "OVER": "game_over",
    "GAME": "game"
}