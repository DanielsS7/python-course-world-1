import pygame
pygame.cdrom.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()