import pygame
from init import *

class Player:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load('assets/jean-mich/jean-mich9.png')
        self.size = self.image.get_width()
        self.x = (screen_width - self.size) // 2
        self.y = screen_height - self.image.get_height() - 80
        self.speed = 10

    def move_player(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        self.x = max(0, min(self.x, WIDTH - self.size))

player = Player(WIDTH, HEIGHT)