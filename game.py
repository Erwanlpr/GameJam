import pygame
import pygame.locals 
import sys
import os
from init import *
from player import *
from fireball import *
from collision import collision
from menu import *
from win import *
from game_over import GameOver

pygame.init()

olympic_torch = Torch()
check = 1
game_over_screen = GameOver()
game_over = False
menu = Menu()
menu.main_menu(1, 0.15)
player.zoom(2)
total_secs = 0
total_mins = 0
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Pixel Sans Serif', 70)
olympic_torch.resize(0.5)

while RUNNING:
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.USEREVENT:
            if (total_secs >= 59):
                total_mins += 1
                total_secs = -1 
            total_secs += 1

    if (len(list_fireball) < 10):
        list_fireball.append(Fireball())
    keys = pygame.key.get_pressed()
    collision(player, list_fireball)
    player.move_player(keys)
    screen.blit(bg[int(nb / 9 % 15)], (0,0))
    screen.blit(player.image, (player.x, player.y))
    for i in range(len(list_fireball)):
        list_fireball[i].movement()
        screen.blit(list_fireball[i].img[list_fireball[i].index], (list_fireball[i].x, list_fireball[i].y))
    nb += 1
    player.drawing_life()

    if (total_mins % 1 == 0 and total_mins > 0 and total_secs == 0):
        olympic_torch.check = 1
    olympic_torch.position()
    olympic_torch.win_collision(player)
    if (total_secs > 9):
        screen.blit(font.render((str(total_mins)+":"+str(total_secs)), True, WHITE), (WIDTH - 150, 15))
    else:
        screen.blit(font.render((str(total_mins)+":0"+str(total_secs)), True, WHITE), (WIDTH - 150, 15))

    if player.life <= 0:
        game_over = True
        game_over_screen.show(screen, total_mins, total_secs)
        player = Player(WIDTH, HEIGHT)
        player.zoom(2)
        list_fireball = []
        total_secs = 0
        total_mins = 0
        nb = 0
        game_over = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
