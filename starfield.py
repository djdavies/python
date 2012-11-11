#!/usr/bin/env python
import pygame # you need this
from random import randrange
MAX_STARS = 100
pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
stars = []
for i in range(MAX_STARS):
    star = [randrange(0, 639), randrange(0, 479), randrange(1, 16)]
    stars.append(star)
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    screen.fill((0,0,0))
    for star in stars:
        star[0] -= star[2]
        if star[0] < 0:
            star[0] = 640
        screen.set_at((star[0], star[1]), (255, 255, 255))

    pygame.display.flip()
