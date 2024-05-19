import pygame
import sys
import os
from init import WIDTH, HEIGHT

class GameWinner:
    def __init__(self):
        pygame.font.init()
        self.font_large = pygame.font.SysFont('Pixel Sans Serif', 250)
        self.font_small = pygame.font.SysFont('Pixel Sans Serif', 100)
        self.font_medium = pygame.font.SysFont('Pixel Sans Serif', 50)
        
        self.game_over_text = self.font_large.render("CONGRATULATION !", True, (0, 0, 255))
        self.game_over_rect = self.game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))

        self.edward_text = self.font_medium.render("Edward", True, (0, 0, 0))

        self.edward = [pygame.image.load(os.path.join('assets/edward', f"koala_{i}.png")) for i in range(1, 4)]
        self.edward_index = 0
        self.edward_x = 0
        self.edward_y = HEIGHT // 1.2
        self.edward_speed = 5

        self.restart_button_text = self.font_small.render("Restart", True, (255, 255, 255))
        self.restart_button_rect = self.restart_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.8))
        self.button_color = (255, 255, 255)

    def show(self, screen, minute, second):
        clock = pygame.time.Clock()
        while True:
            time_text = self.font_medium.render(f"You Survived: {minute}m:{second}s", True, (0, 0, 255))
            time_rect = time_text.get_rect(center=(WIDTH // 2, HEIGHT // 5))
            screen.fill((255, 255, 255))
            screen.blit(self.game_over_text, self.game_over_rect)

            self.edward_x += self.edward_speed
            if self.edward_x > WIDTH:
                self.edward_x = -self.edward[self.edward_index].get_width()

            self.edward_index = (self.edward_index + 1) % len(self.edward)
            screen.blit(self.edward[self.edward_index], (self.edward_x, self.edward_y))
            edward_text_rect = self.edward_text.get_rect(center=(self.edward_x + self.edward[self.edward_index].get_width() // 2, self.edward_y - 30))
            screen.blit(self.edward_text, edward_text_rect)

            pygame.draw.rect(screen, self.button_color, self.restart_button_rect.inflate(20, 20))
            screen.blit(self.restart_button_text, self.restart_button_rect)
            
            pygame.draw.rect(screen, self.button_color, time_rect.inflate(20, 20))
            screen.blit(time_text, time_rect)
            
            screen.blit(time_text, time_rect)
            
            pygame.display.flip()
            clock.tick(40)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart_button_rect.collidepoint(event.pos):
                        return
