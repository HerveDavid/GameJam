from utilitaries import *

VIDE = ( 0 for i in range(NB_WIDTH_CELL))

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
etage1 = (
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0),
    (0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 3, 2, 4, 0, 0),
    (2, 2, 2, 2, 4, 0, 0, 0, 0, 3, 1, 1, 6, 0, 0),
    (1, 1, 1, 1, 1, 0, 3, 4, 4, 1, 1, 1, 6, 0, 0)

)
