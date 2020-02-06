import pygame
import sys
from sprite import Sprite


# Constantes
SIZE = WIDTH, HEIGHT= 1024, 768
WIDTH_CENTER, HEIGHT_CENTER = int(WIDTH / 2), int(HEIGHT / 2)
FPS = 12
RUNNING = True
NB_WIDTH_CELL = int(WIDTH / 72) + 1
NB_HEIGTH_CELL = int(HEIGHT / 70) + 1
WIDTH_CELL = WIDTH / NB_WIDTH_CELL
HEIGHT_CELL = HEIGHT / NB_HEIGTH_CELL
TOTALCELLS = NB_WIDTH_CELL * NB_HEIGTH_CELL

TUILES = {
    1: Sprite('Assets/Textures/mur.png', 1, 1, colorkey=False),
    2:  Sprite('Assets/Textures/sol_sable.png', 1, 1, colorkey=False),
    3:  Sprite('Assets/Textures/sol_sable_cote.png', 1, 1, colorkey=False),
    4:   Sprite('Assets/Textures/sol_sable_cote.png', 1, 1, colorkey=False),
    5:  Sprite('Assets/Textures/mur_cote.png', 1, 1, colorkey=False),
    6:  Sprite('Assets/Textures/mur_cote.png', 1, 1, colorkey=False),
    7: Sprite('Assets/Textures/plateforme_sable.png', 1, 1, colorkey=False),
    8: Sprite('Assets/Textures/entree.png', 1, 1, colorkey=False),
    9: Sprite('Assets/Textures/carrelage.png',1,1,colorkey=False),
    10: Sprite('Assets/Textures/carrelage_cote.png',1,1,colorkey=False),
    11: Sprite('Assets/Textures/carrelage_plateforme.png',1,1,colorkey=False),
    12: Sprite('Assets/Textures/carrelage_sol.png', 1, 1, colorkey=False),
    13: Sprite('Assets/Textures/carrelage_sol_cote.png', 1, 1, colorkey=False),
    14: Sprite('Assets/Textures/sortie.png', 1, 1, colorkey=False)

}

TUILES_FOND = {
    1: Sprite('Assets/Background/fond.png', 1, 1, colorkey=False),
    2: Sprite('Assets/Background/fond_trou01.png', 1, 1, colorkey=False),
    3: Sprite('Assets/Background/fond_trou02.png', 1, 1, colorkey=False),
    4: Sprite('Assets/Background/fond_trou03.png', 1, 1, colorkey=False),
    5: Sprite('Assets/Background/fond_trou04.png', 1, 1, colorkey=False),
    6: Sprite('Assets/Background/fond_light.png', 1, 1, colorkey=False),
    7: Sprite('Assets/Background/fonds_cassed.png',1,1, colorkey= False),
    8: Sprite('Assets/Background/fond_casseg.png',1,1,colorkey=False),
    10: Sprite('Assets/Background/fond_trou04.png', 1, 1, colorkey=False),
    11: Sprite('Assets/Background/fond_trou04.png', 1, 1, colorkey=False)
}

OBJETS = {
    1: Sprite('Assets/Background/fond_trou04.png', 1, 1, colorkey=False),
    2: Sprite('Assets/Background/fond_trou01.png', 1, 1, colorkey=False),
}


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