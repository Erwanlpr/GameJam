import pygame
import sys
import os
from init import WIDTH, HEIGHT

class Menu:

    def __init__(self):
        pygame.font.init()
        self.menu_bg = pygame.image.load(os.path.join('assets/menu', 'menu_bg.jpg')).convert()
        self.start_button = pygame.image.load(os.path.join('assets/menu', 'start_button.png')).convert_alpha()
        self.button_rect = self.start_button.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.size = (WIDTH, HEIGHT)
        self.size_bttn = (WIDTH, HEIGHT)
        self.x = 0
        self.y = 0

        self.title_image = pygame.image.load(os.path.join('assets/menu', 'title.png')).convert_alpha()
        self.title_rect = self.title_image.get_rect(center=(WIDTH // 2, HEIGHT // 4))

    def main_menu(self, screen, scale_factor, button_scale):
        self.size_bttn = (int(self.size_bttn[0] * button_scale), int(self.size_bttn[1] * button_scale))
        self.size = (int(self.size[0] * scale_factor), int(self.size[1] * scale_factor))
        self.menu_bg = pygame.transform.scale(self.menu_bg, self.size)
        self.start_button = pygame.transform.scale(self.start_button, self.size_bttn)
        self.button_rect = self.start_button.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.x = (WIDTH - self.size[0]) // 2
        self.y = HEIGHT - self.size[1] - 55
        
        while True:
            screen.blit(self.menu_bg, (0, 0))
            screen.blit(self.start_button, self.button_rect.topleft)
            screen.blit(self.title_image, self.title_rect)

            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        return
