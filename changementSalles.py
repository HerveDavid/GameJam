from maps import *
from game import Game
from utilitaries import *

# toutesSalles = {
#     Game(map=etage2, fond=fond2, objets=(), player=player, enemies=enemies2)
# }

def initSalles(player):
    salles = {
        1: Game(map=etage1, fond=fond1, objets=(), player=Player(0, 0), enemies=enemies1),
        2: Game(map=etage2, fond=fond2, objets=(), player=Player(0, 0), enemies=enemies2),
    }
    return salles
