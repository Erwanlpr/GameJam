import pygame
import pygame.locals 
import sys
import os
from init import *
from player import *
from fireball import *

pygame.init()
player.zoom(2)

while RUNNING:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    if (len(list_fireball) < 10):
        list_fireball.append(Fireball())
    keys = pygame.key.get_pressed()
    player.move_player(keys)
    screen.blit(bg[int(nb / 9 % 15)], (0,0))
    screen.blit(player.image, (player.x, player.y))
    for i in range(len(list_fireball)):
        list_fireball[i].movement()
        screen.blit(list_fireball[i].img[list_fireball[i].index], (list_fireball[i].x, list_fireball[i].y))
    nb += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
