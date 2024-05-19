import pygame
import sys
from init import WIDTH, HEIGHT

class GameOver:
    def __init__(self):
        pygame.font.init()
        self.font_large = pygame.font.SysFont('Pixel Sans Serif', 300)
        self.font_small = pygame.font.SysFont('Pixel Sans Serif', 100)
        
        self.game_over_text = self.font_large.render("Game Over", True, (255, 0, 0))
        self.game_over_rect = self.game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        
        self.restart_button_text = self.font_small.render("Restart", True, (255, 255, 255))
        self.restart_button_rect = self.restart_button_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.8))
        self.button_color = (0, 0, 0)

    def show(self, screen):
        while True:
            screen.fill((0, 0, 0))
            screen.blit(self.game_over_text, self.game_over_rect)
            pygame.draw.rect(screen, self.button_color, self.restart_button_rect.inflate(20, 20))
            screen.blit(self.restart_button_text, self.restart_button_rect)
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart_button_rect.collidepoint(event.pos):
                        return
