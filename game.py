import pygame
import pygame.locals 
import sys
import os
from init import *
from player import *

pygame.init()

while RUNNING:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    keys = pygame.key.get_pressed()
    player.move_player(keys)
    screen.blit(bg[int(nb / 9 % 15)], (0,0))
    nb += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
