#! /usr/env/bin python3

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
screen.fill((180, 180, 180))


circle(screen, (255, 255, 0), (400, 400), 200)
circle(screen, (255, 255, 255), (400, 400), 200, 5)

line(screen, (0, 0, 0), (150, 200), (350, 300), 20)
line(screen, (0, 0, 0), (450, 300), (650, 250), 20)
circle(screen, (255, 0, 0), (300, 350), 50)
circle(screen, (0, 0, 0), (300, 350), 20)
circle(screen, (255, 0, 0), (500, 340), 40)
circle(screen, (0, 0, 0), (500, 340), 20)



rect(screen, (0, 0, 0), (300, 500, 200, 50))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
