import pygame
import os
import sys

WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH = 1920
HEIGHT = 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tout feu tout flamme")

bg = [pygame.transform.scale(pygame.image.load(os.path.join('assets/volcano', f"volcano{i}.png")).convert(), (WIDTH, HEIGHT)) for i in range(1, 17)]
menu_bg = pygame.image.load(os.path.join('assets/menu', 'menu_bg.jpg')).convert()
start_button = pygame.image.load(os.path.join('assets/menu', 'start_button.png')).convert_alpha()

button_rect = start_button.get_rect(center=(WIDTH // 2, HEIGHT // 2))

clock = pygame.time.Clock()

nb = 0

RUNNING = True
