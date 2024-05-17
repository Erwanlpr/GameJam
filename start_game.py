import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Déplacement du joueur")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

player_size = 50
player_rect = pygame.Rect((screen_width - player_size) // 2, (screen_height - player_size) // 2, player_size, player_size)
player_speed = 5

clock = pygame.time.Clock()

def move_player(keys):
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    elif keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    elif keys[pygame.K_UP]:
        player_rect.y -= player_speed
    elif keys[pygame.K_DOWN]:
        player_rect.y += player_speed

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    move_player(keys)

    player_rect.x = max(0, min(player_rect.x, screen_width - player_size))
    player_rect.y = max(0, min(player_rect.y, screen_height - player_size))

    pygame.draw.rect(screen, RED, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()