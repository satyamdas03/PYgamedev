import pygame

screen_size = [360,600]
screen = pygame.display.set_mode(screen_size)
score = 0
green = (0,255,0)
pygame.font.init()

def load(name):
    return pygame.image.load(name)