import pygame,sys
from setting import *
from level import Level
from game_data import level_0

# Pygame setup
pygame.init()
# screen_width = 1280
# screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_0, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)