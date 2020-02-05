import pygame
import sys

# Constantes
SIZE = WIDTH, HEIGHT= 1024, 768
WIDTH_CENTER, HEIGHT_CENTER = int(WIDTH / 2), int(HEIGHT / 2)
FPS = 10
RUNNING = True
NB_WIDTH_CELL = int(WIDTH / 72) + 1
NB_HEIGTH_CELL = int(HEIGHT / 70) + 1
WIDTH_CELL = WIDTH / NB_WIDTH_CELL
HEIGHT_CELL = HEIGHT / NB_HEIGTH_CELL
TOTALCELLS = NB_WIDTH_CELL * NB_HEIGTH_CELL

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
    return pygame.display.set_mode(SIZE)