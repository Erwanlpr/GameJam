import sys
import os
import pygame
from random import randint
from init import *

class Torch:
    
    def __init__(self):
        self.x = randint(0, WIDTH - 5)
        self.y = -200
        self.speed = 15
        self.img = pygame.image.load(os.path.join('assets', 'torch.png'))
        self.size = self.img.get_size()

    def movement(self):
        if (self.y < (HEIGHT - 50 - self.size[1])):
            self.y += self.speed
        else:
            self.y = -200

    def resize(self, scale_factor):
        self.size = (int(self.size[0] * scale_factor), int(self.size[1] * scale_factor))
        self.img = pygame.transform.scale(self.img, self.size)