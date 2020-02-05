from utilitaries import *

VIDE = ( 0 for i in range(NB_WIDTH_CELL))
PLEIN =  ( 1 for i in range(NB_WIDTH_CELL))
# Etage 1
etage1 = (
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 0, 8, 0, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 0, 0, 0, 0, 0, 3, 0, 2, 2, 0, 0, 0, 0, 3),
    (0, 0, 0, 0, 3, 0, 0, 8, 2, 2, 0, 0, 0, 3, 0),
    (0, 0, 0, 0, 0, 0, 4, 4, 1, 2, 0, 0, 3, 0, 0),
    (4, 4, 4, 4, 5, 0, 2, 1, 1, 2, 0, 4, 0, 0, 0),
    (1, 1, 1, 1, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0, 0)
)

fond1 = (
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

)

# Test
test = (
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8),
    (0, 0, 0, 0, 0, 0, 3, 0, 2, 2, 0, 0, 0, 0, 3),
    (0, 0, 0, 0, 3, 0, 0, 8, 2, 2, 0, 0, 0, 3, 0),
    (0, 0, 0, 0, 0, 0, 4, 4, 1, 2, 0, 0, 3, 0, 0),
    (4, 4, 4, 4, 5, 0, 2, 1, 1, 2, 0, 4, 0, 0, 0),
    (1, 1, 1, 1, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0, 0)

)
