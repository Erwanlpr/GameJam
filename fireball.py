import sys
import os
import pygame
from random import randint
from init import *

class Fireball:
    
    def __init__(self):
        self.x = randint(0, WIDTH - 5)
        self.y = -200
        self.speed = randint(3, 10)
        self.img = [pygame.image.load(os.path.join('assets/fireball', f"fireball{i}.png")) for i in range(1, 6)]
        self.size = self.img[0].get_size()
        self.index = 0

    def movement(self):
        if (self.y < (HEIGHT - 50)):
            self.y += self.speed
            if (self.index > 3):
                self.index = -1
            self.index += 1
        else:
            self.x = randint(0, WIDTH - 5)
            self.y = -200

list_fireball = []