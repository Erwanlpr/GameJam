import pygame
import pygame.locals 
import sys
import os

WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH = 1920
HEIGHT = 1080

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Déplacement du joueur")

bg = [pygame.transform.scale(pygame.image.load(os.path.join('assets', f"volcano{str(i)}.png")).convert(), (WIDTH, HEIGHT - 69)) for i in range(1, 17)]

class Player:
    def __init__(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.speed = 5
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

clock = pygame.time.Clock()

player = Player(WIDTH, HEIGHT)
player_rect = pygame.Rect((WIDTH - player.size) // 2, (HEIGHT - player.size) // 2, player.size, player.size)

print("%d\n", len(bg))
nb = 0
running = True
while running:
    screen.fill(WHITE)

    screen.blit(bg[int(nb / 9 % 15)], (0,0))
    nb += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    player.move_player(keys)

    player.x = max(0, min(player.x, WIDTH - player.size))
    player.y = max(0, min(player.y, HEIGHT - player.size))

    pygame.draw.rect(screen, RED, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
