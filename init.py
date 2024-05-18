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

clock = pygame.time.Clock()

nb = 0

RUNNING = True
