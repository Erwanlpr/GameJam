import sys
import os
import pygame
from random import randint
from init import *
from player import Player

class Torch:
    
    def __init__(self):
        self.x = randint(0, WIDTH - 5)
        self.y = -200
        self.speed = 6
        self.img = pygame.image.load(os.path.join('assets', 'torch.png'))
        self.size = self.img.get_size()
        self.check = 0

    def movement(self):
        self.y += self.speed

    def resize(self, scale_factor):
        self.size = (int(self.size[0] * scale_factor), int(self.size[1] * scale_factor))
        self.img = pygame.transform.scale(self.img, self.size)
        
    def nb_torch(self, player : Player):
        pos_x = -15
        pos_y = 100
        for i in range(player.nb_torch):
            screen.blit(self.img, (pos_x, pos_y))
            pos_x += 95

    def position(self):
        if (self.check == 0):
            self.y = -200
            self.x = randint(5, WIDTH - 5)
        else:
            self.movement()
            screen.blit(self.img, (self.x, self.y))

    def win_touch(self, player : Player) -> bool:
        if ((self.y + self.size[1] - 40) < player.y):
            return False
        if ((self.x + self.size[0] - 40) < player.x):
            return False
        if ((self.x) > (player.x + player.size[0] - 30)):
            return False
        if (self.y > player.y):
            return False
        return True

    def win_collision(self, player : Player):
        if (self.win_touch(player) == True):
            player.nb_torch += 1
            self.check = 0
        if (self.y > HEIGHT):
            self.check = 0
