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


enemiesTest = {
    Sirene(500, (NB_HEIGTH_CELL - 1) * HEIGHT_CELL)
}

etagetest = (
    (14, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 7, 0, -1, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 1),
    (0, 0, 0, 0, -2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 1),
    (0, 0, 0, 0, -2, 0, 0, 1, 7, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, -2, -2, -3, 0, -1, 0, 0, 0, 0, 0, 0, 1),
    (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1)
)

fondtest = (
    (11, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 2, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 6, 1),
    (1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 2, 1, 1, 3, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1),
    (10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
)

# Etage 1
etage1 = (
    (14, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, -1, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 1),
    (8, 0, 0, -1, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 1),
    (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1)
)

enemies1=(


)

fond1 = (
    (11, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 2, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 6, 1),
    (1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 2, 1, 1, 3, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1),
    (10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
)

#etage2
#spawn joueur (10, 10*HEIGHT_CELL)
etage2 = (
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 14),
    (1, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 1),
    (1, 0, 0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2),
    (1, 1, 1, 2, 2, 2, 4, 0, 0, 0, 0, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 0, 7, 0, 0, 0, 1, 1, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 1, 1, 1),
    (8, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1),
    (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1)
)

enemies2={
    Minotaur(12*WIDTH_CELL, 5*HEIGHT_CELL, 12*WIDTH_CELL, 12*WIDTH_CELL + 4 * WIDTH_CELL)
}

fond2 = (
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 11),
    (1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 3, 1),
    (1, 6, 1, 4, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1),
    (1, 1, 1, 1, 1, 6, 1, 1, 5, 1, 1, 1, 1, 2, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1),
    (1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1),
    (1, 1, 6, 1, 1, 6, 1, 1, 1, 1, 1, 1, 6, 1, 1),
    (10, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
)

#etage3
#Player(15 * WIDTH_CELL-20, 10*HEIGHT_CELL)

etage3 = (
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 14),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2),
    (1, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1),
    (1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 1, 1, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 0, 0),
    (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0),
    (1, 1, 1, 0, 0, 3, 2, 2, 4, 0, 0, 0, 0, -1, 8),
    (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2)
)

enemies3={
    Minotaur(7*WIDTH_CELL+20, 3*HEIGHT_CELL, 5*WIDTH_CELL+20, 5*WIDTH_CELL + 4 * WIDTH_CELL),
    Minotaur(5*WIDTH_CELL+20, 9*HEIGHT_CELL, 5*WIDTH_CELL+20, 5*WIDTH_CELL + 4 * WIDTH_CELL)
}

fond3 = (
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 11),
    (1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 3, 1),
    (1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1),
    (1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 5, 1, 1, 1, 6, 1, 1, 4, 1, 1),
    (1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5),
    (1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1),
    (1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
)

#etage 4

etage4 = (
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0),
    (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 10, 0, 0, 0, 10),
    (1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 10, 0, 10, 10, 10),
    (1, 1, 1, 1, 1, 1, 0, 0, 0, 10, 10, 10, 10, 10, 10),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (2, 2, 2, 2, 2, 2, 2, 2, 12, 12, 12, 12, 12, 12, 12),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10),
    (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10)
)

enemies4= {
    Minotaur(4*WIDTH_CELL+20, 7*HEIGHT_CELL, 2*WIDTH_CELL+20, 2*WIDTH_CELL + 4 * WIDTH_CELL),
    Minotaur(12*WIDTH_CELL+20, 7*HEIGHT_CELL, 9*WIDTH_CELL+20, 9*WIDTH_CELL + 4 * WIDTH_CELL)
}

fond4 = (
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 7, 0, 0, 0, 8, 1, 1, 4, 1, 1),
    (10, 1, 5, 1, 1, 1, 7, 0, 8, 1, 1, 1, 1, 1, 11),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)

etage5 = (
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 11, 11, 11, 0, 0, 11, 0, 0, 11, 0, 0, 11, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 11, 0, 0, 11, 0, 0,11, 0, 0),
    (0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (12, 12, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)

enemies5= {
    Sirene(WIDTH_CELL*8+30, (NB_HEIGTH_CELL - 2) * HEIGHT_CELL+1),
Sirene(WIDTH_CELL*14+30, 2 * HEIGHT_CELL+1)
}

fond5 = (
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
)