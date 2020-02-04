import pygame
import sys

# Constantes
SIZE = WIDTH, HEIGHT= 1024, 768
WIDTH_CENTER, HEIGHT_CENTER = int(WIDTH / 2), int(HEIGHT / 2)
FPS = 10
RUNNING = True

# Fonctions
def events():
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            RUNNING = False
            sys.exit()

def init():
    pygame.init()
    CLOCK = pygame.time.Clock()
    return pygame.display.set_mode(SIZE)