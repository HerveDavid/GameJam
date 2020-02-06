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
    (2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
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
    (1, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2),
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
    (17, 0, 0, 0, 1, 0, 0, 0, 0, 0, 10, 0, 0, 0, 16),
    (1, 1, 17, 0, 1, 0, 0, 0, 0, 0, 10, 0, 16, 10, 10),
    (1, 1, 1, 1, 1, 17, 0, 0, 0, 16, 10, 10, 10, 10, 10),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (2, 2, 2, 2, 2, 2, 2, 15, 12, 12, 12, 12, 12, 12, 12),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 16, 10, 10, 10, 10),
    (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 10, 10),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16)
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
    (1, 1, 1, 1, 1, 7, 0, 0, 0, 8, 12, 12, 12, 12, 12),
    (10, 1, 5, 1, 1, 1, 7, 0, 8, 12, 12, 12, 12, 12, 11),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)

etage5 = (
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
    (0, 0, 12, 12, 12, 11, 0, 0, 0, 0, 0, 11,12, 12, 10),
    (12, 12, 12, 11, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12, 12),
    (12, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10)
)

enemies5= {
    Sirene(WIDTH_CELL*8+30, (NB_HEIGTH_CELL - 5) * HEIGHT_CELL+1),
    Sirene(WIDTH_CELL * 8 + 30, (NB_HEIGTH_CELL - 5) * HEIGHT_CELL + 1),
    Sirene(WIDTH_CELL * 8 + 30, (NB_HEIGTH_CELL - 5) * HEIGHT_CELL + 1),
    Sirene(WIDTH_CELL*8+30, (NB_HEIGTH_CELL - 5) * HEIGHT_CELL+1)
}

fond5 = (
    (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
    (12, 14, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
    (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
    (12, 12, 12, 12, 12, 12, 17, 12, 12, 12, 12, 12, 17, 12, 12),
    (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
    (12, 17, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11),
    (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
    (10, 12, 12, 12, 14, 14, 12, 12, 12, 12, 13, 12, 12, 12, 12),
    (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
    (12, 12, 12, 13, 12, 12, 12, 12, 14, 12, 12, 12, 12, 15, 12),
    (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
)

etage6 = (
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

enemies6= {
    Sirene(WIDTH_CELL*8+30, (NB_HEIGTH_CELL - 2) * HEIGHT_CELL+1),
    Sirene(WIDTH_CELL*14+32, 2 * HEIGHT_CELL+1)
}

fond6 = (
    (12, 12, 12, 12, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 15),
    (12, 12, 12, 12, 12, 12, 12, 12, 12, 17, 12, 12, 12, 12, 12),
    (12, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 16),
    (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
    (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
    (12, 12, 12, 12, 17, 12, 12, 12, 12, 12, 17, 12, 12, 12, 12),
    (12, 12, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
    (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
    (10, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
    (12, 12, 12, 12, 12, 12, 12, 12, 16, 12, 12, 12, 12, 13, 12),
    (12, 12, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12)
)

etage7 = (
    (0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
    (10, 0, 0, 0, 10, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1),
    (10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1),
    (10, 10, 10, 10, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (12, 12, 12, 12, 12, 12, 12, 15, 1, 1, 1, 1, 1, 1, 1),
    (10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1),
    (10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
)

enemies7= {
    Minotaur( -2*WIDTH_CELL , 7 * HEIGHT_CELL, -2*WIDTH_CELL -10, 2 * WIDTH_CELL + 4 * WIDTH_CELL),
    Sirene(WIDTH_CELL*3+32, 8 * HEIGHT_CELL),
    Sirene(WIDTH_CELL*3+32, 5 * HEIGHT_CELL),
    Sirene(WIDTH_CELL*3+32, 5 * HEIGHT_CELL),
}

fond7 = (
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (12, 12, 12, 16, 12, 7, 0, 0, 0, 8, 1, 1, 1, 1, 1),
    (10, 12, 12, 12, 12, 12, 7, 0, 8, 1, 1, 1, 1, 1, 11),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)

etage8 = (
    (14, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (2, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, -1, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 1),
    (8, 0, 0, -1, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 1),
    (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1)
)

enemies8= {

}

fond8 = (
    (11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)

etage9 = (
    (14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (2, 2, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, -2, 0, 7, 0, -3, 0, -3, 0, 7, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0),
    (0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 2),
    (0, -2, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 1),
    (8, -2, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 1),
    (2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
)

enemies9= {
     Sirene(WIDTH_CELL*3+32, 10 * HEIGHT_CELL),
    Minotaur(12 * WIDTH_CELL, 7 * HEIGHT_CELL, 11 * WIDTH_CELL-50, 12 * WIDTH_CELL + 4 * WIDTH_CELL),
    Minotaur(14 * WIDTH_CELL, 7 * HEIGHT_CELL, 11 * WIDTH_CELL-50, 12 * WIDTH_CELL + 4 * WIDTH_CELL),
    Minotaur(13 * WIDTH_CELL, 7 * HEIGHT_CELL, 11 * WIDTH_CELL-50, 12 * WIDTH_CELL + 4 * WIDTH_CELL)

}

fond9 = (
    (11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)