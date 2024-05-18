import pygame
import os
from init import WIDTH, HEIGHT 

class Player:
    def __init__(self, screen_width, screen_height):
        self.images_left = [pygame.image.load(os.path.join('assets/jean-mich', f"jean-mich{i}.png")) for i in range(1, 5)]
        self.images_right = [pygame.image.load(os.path.join('assets/jean-mich', f"jean-mich{i}.png")) for i in range(5, 9)]
        self.image_neutral = pygame.image.load(os.path.join('assets/jean-mich', "jean-mich9.png"))
        self.image = self.image_neutral
        self.size = self.image.get_width()
        self.x = (screen_width - self.size) // 2
        self.y = screen_height - self.image.get_height() - 55
        self.speed = 10
        self.animation_index = 0
        self.animation_counter = 0
        self.direction = 'neutral'

    def move_player(self, keys):
        moved = False

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            moved = True
            self.direction = 'left'
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            moved = True
            self.direction = 'right'

        self.x = max(0, min(self.x, WIDTH - self.size))

        if moved:
            self.animation_counter += 1
            if self.animation_counter > 5:
                self.animation_counter = 0
                self.animation_index = (self.animation_index + 1) % 4
                if self.direction == 'right':
                    self.image = self.images_right[self.animation_index]
                else:
                    self.image = self.images_left[self.animation_index]
        else:
            self.image = self.image_neutral

player = Player(WIDTH, HEIGHT)
