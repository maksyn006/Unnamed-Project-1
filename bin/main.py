from random import randint

import pygame
from settings import *
pygame.init()

sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

is_run = True
while is_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_run = False
    sc.fill(WHITE)
    pygame.draw.rect(sc, RED, (randint(0, WIDTH), randint(0, HEIGHT), 50, 50))
    pygame.display.update()
pygame.quit()
