import pygame
import pygame.locals 
import sys
import os
from init import *

BLACK = (0, 0, 0)

pygame.init()
font = pygame.font.SysFont(None, 40)


def draw_text(text,font, color, surface, x, y):
    text_object = font.render(text, True, color)
    text_rect = text_object.get_rect()
    text_rect.center = (y, x)   
    surface.blit(text_object, text_rect)

#in boucle while running :
    # mouse_pos = pygame.mouse.get_pos()
    # button_start = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
    # pygame.draw.rect(screen, BLACK, button_start)
    # draw_text("Start", font, WHITE, screen, WIDTH // 2, HEIGHT // 2)

    # if event.type == pygame.K_ESCAPE:
    #         print("STARTING GAME !")
    # pygame.display.update()

    # keys = pygame.key.get_pressed()
    # player.move_player(keys)