# Chargement des modules
try:
    import pygame
    from outils import *
    from button import Button
except ImportError as err:
    print("Echec importation: {0}").format(err)

# Menu
def menu(fenetre: pygame.display):

    fenetre.fill([255, 255, 255])
    btnJouer = Button(WIDTH/2 - WIDTH/4, HEIGHT/2 - HEIGHT/4, 500, 100, "Jouer")

    running = True

    while running:

        # Récupération des événements
        for event in pygame.event.get():

            # Quitter le jeu
            if event.type == pygame.QUIT:
                running = False

        # Bouton
        if btnJouer.draw(fenetre):
            running = False
            return JOUER

        # Rafraichir pygame
        pygame.display.update()


    return 0