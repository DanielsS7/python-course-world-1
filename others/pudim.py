import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption( 'barulho')

while True:

    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()

    pygame.display.update()