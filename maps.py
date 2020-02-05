from utilitaries import *
from ennemy import *

VIDE = ( 0 for i in range(NB_WIDTH_CELL))

init()

# TUILES = {
#     1: Sprite('Assets/Textures/mur.png', 1, 1, colorkey=False),
#     2:  Sprite('Assets/Textures/sol_sable.png', 1, 1, colorkey=False),
#     3:  Sprite('Assets/Textures/sol_sable_cote.png', 1, 1, colorkey=False),
#     4:   Sprite('Assets/Textures/sol_sable_cote.png', 1, 1, colorkey=False),
#     5:  Sprite('Assets/Textures/mur_cote.png', 1, 1, colorkey=False),
#     6: Sprite('Assets/Textures/mur_cote.png', 1, 1, colorkey=False),
#     7: Sprite('Assets/Textures/plateforme_sable.png', 1, 1, colorkey=False)
# }


# Etage 1
# etage1 = (
#     (1, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
#     (1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
#     (0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
#     (0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 1),
#     (0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 1),
#     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 8, 0, 1),
#     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 1),
#     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 1),
#     (0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 1),
#     (8, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 1),
#     (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1)
#
# )
#
# enemies1={
#
# }

#etage2
#minotaur = Minotaur(12*WIDTH_CELL, 5*HEIGHT_CELL, 12*WIDTH_CELL, 12*WIDTH_CELL + 4 * WIDTH_CELL)
#spawn joueur (10, 10*HEIGHT_CELL)
etage2 = (
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 1),
    (1, 0, 0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2),
    (1, 1, 1, 2, 2, 2, 4, 0, 0, 0, 0, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 0, 7, 0, 0, 0, 1, 1, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 1, 1, 1),
    (8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1),
    (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1)
)

enemies2={
    Minotaur(12*WIDTH_CELL, 5*HEIGHT_CELL, 12*WIDTH_CELL, 12*WIDTH_CELL + 4 * WIDTH_CELL)
}

#etage3
#Player(15 * WIDTH_CELL-20, 10*HEIGHT_CELL)

etage3 = (
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2),
    (1, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1),
    (1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 1, 1, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 0, 0),
    (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0),
    (1, 1, 1, 0, 0, 3, 2, 2, 4, 0, 0, 0, 0, 0, 8),
    (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2)
)

enemies3={
    Minotaur(7*WIDTH_CELL+20, 3*HEIGHT_CELL, 5*WIDTH_CELL+20, 5*WIDTH_CELL + 4 * WIDTH_CELL),
    Minotaur(5*WIDTH_CELL+20, 9*HEIGHT_CELL, 5*WIDTH_CELL+20, 5*WIDTH_CELL + 4 * WIDTH_CELL)
}

#etage 4

etage4 = (
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
    (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1),
    (1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
)

enemies4= {
    Minotaur(4*WIDTH_CELL+20, 7*HEIGHT_CELL, 2*WIDTH_CELL+20, 2*WIDTH_CELL + 4 * WIDTH_CELL),
    Minotaur(12*WIDTH_CELL+20, 7*HEIGHT_CELL, 9*WIDTH_CELL+20, 9*WIDTH_CELL + 4 * WIDTH_CELL)
}