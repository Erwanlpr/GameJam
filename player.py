import pygame
from init import *

class Player:
    def __init__(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.speed = 50
        self.size = 50

    def move_player(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
        elif keys[pygame.K_UP]:
            self.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
        player.x = max(0, min(self.x, WIDTH - self.size))
        player.y = max(0, min(self.y, HEIGHT - self.size))

player = Player(WIDTH, HEIGHT)
player_rect = pygame.Rect((WIDTH - player.size) // 2, (HEIGHT - player.size) // 2, player.size, player.size)
