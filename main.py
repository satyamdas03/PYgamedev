import random

import pygame

screen_size = [360,600]
screen = pygame.display.set_mode(screen_size)
score = 0
green = (0,255,0)
pygame.font.init()

def load(name):
    return pygame.image.load(name)

def display_score(score):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    score_text = 'Score:' + str(score)
    text = font.render(score_text, True, green)
    screen.blit(text, [20,10])

def get_rand_offset():
    return 100*random.randint(5,15)


def set_s_position(idx, pos):
    global  score
    if c_positions[idx] > 600:
        c_positions[idx] = 0 - get_rand_offset()
        score= score+50
    else:
        c_positions[idx] += 5


background = load(background.png)
chicken = load(chicken.png)
user = load(user.png)
c_positions = [0-get_rand_offset(), 0-get_rand_offset(), 0]
# ongoing..
# refer repl.it for help
