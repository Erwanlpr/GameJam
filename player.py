import pygame
import os
from init import WIDTH, HEIGHT

class Player:

    def __init__(self, screen_width, screen_height):
        self.images_left = [pygame.image.load(os.path.join('assets/jean-mich', f"jean-mich{i}.png")) for i in range(1, 5)]
        self.images_right = [pygame.image.load(os.path.join('assets/jean-mich', f"jean-mich{i}.png")) for i in range(5, 9)]
        self.image_neutral = pygame.image.load(os.path.join('assets/jean-mich', "jean-mich9.png"))
        self.image = self.image_neutral
        self.original_size = self.image.get_size()
        self.size = self.original_size
        self.x = (screen_width - self.size[0]) // 2
        self.y = screen_height - self.size[1] - 55
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

        self.x = max(0, min(self.x, WIDTH - self.size[0]))

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

    def zoom(self, scale_factor):
        self.size = (int(self.original_size[0] * scale_factor), int(self.original_size[1] * scale_factor))
        self.images_left = [pygame.transform.scale(img, self.size) for img in self.images_left]
        self.images_right = [pygame.transform.scale(img, self.size) for img in self.images_right]
        self.image_neutral = pygame.transform.scale(self.image_neutral, self.size)
        self.image = self.image_neutral if self.direction == 'neutral' else self.images_right[0] if self.direction == 'right' else self.images_left[0]
        self.x = (WIDTH - self.size[0]) // 2
        self.y = HEIGHT - self.size[1] - 55

player = Player(WIDTH, HEIGHT)
