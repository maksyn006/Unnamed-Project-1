from random import randint
from pygame import *

from bin.settings import *
init()

sc = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()


is_run = True
while is_run:
    for e in event.get():
        if e.type == QUIT:
            is_run = False
    sc.fill(WHITE)
    draw.rect(sc, RED, (randint(0, WIDTH), randint(0, HEIGHT), 50, 50))
    display.update()
    clock.tick(FPS)
quit()
