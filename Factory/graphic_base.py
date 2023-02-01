import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((800,600))

player_quits = False

while not player_quits:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_quits = True

    pygame.display.flip()
