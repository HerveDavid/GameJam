# Chargement des modules
try:
    # Mes modules
    from menu import menu
    from game import jeu
    from outils import *

    # Pygame
    import pygame
    from pygame.locals import *
    succes, echecs = pygame.init()
    print("{0} successes and {1} failures".format(succes, echecs))

except ImportError as err:
    print("Echec importation: {0}").format(err)



if __name__ == '__main__':

    # Initialisation
    fenetre = pygame.display.set_mode(SIZE)

    # Menu
    m = menu(fenetre)

    # Jeu
    if m == JOUER:
        jeu(fenetre)

