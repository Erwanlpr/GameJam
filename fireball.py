import sys
import os
import pygame
from random import randint
from init import *

class Fireball:
    
    def __init__(self):
        self.x = randint(10, WIDTH - 10)
        self.y = -10
        self.speed = randint(3, 10)
        self.img = [pygame.image.load(os.path.join('assets/fireball', f"fireball{i}.png")) for i in range(1, 6)]
        self.index = 0

    def movement(self):
        if (self.y < HEIGHT - 55):
            self.y += self.speed
            if (self.index > 3):
                self.index = -1
            self.index += 1
        else:
            self.x = randint(10, WIDTH - 10)
            self.y = -10

list_fireball = []