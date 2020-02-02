# Chargement des modules
try:
    # Mes modules
    from player import Player
    from outils import *

    # Pygame
    import pygame

except ImportError as err:
    print("Echec importation: {0}").format(err)

# Menu

# Jeu
def jeu(fenetre: pygame.display):

    # Horloge du jeu
    clock = pygame.time.Clock()

    # Création du monde
    world = pygame.Surface((1000,1000))
    world.fill([255, 0, 0])

    # Création d'un joueur
    player = Player("test", world)

    # Création de la caméra
    camera = (100,100) # Create Camara Starting Position

    # Boucle du jeu
    running = True
    while running:

        # Fixation des fps
        dt = clock.tick(FPS) / 1000

        # Récupération des événements
        for event in pygame.event.get():

            # Quitter le jeu
            if event.type == pygame.QUIT:
                running = False

            #Bouger le player
            player.bouger(event)

        # Position de la caméra est du joueur
        camera = player.move(camera)

        # Rafraichir les fonds du jeu
        fenetre.fill([255, 255, 255])
        world.fill([255, 0, 0])

        # Afficher le joueur dans le monde
        player.update(dt)

        # Afficher le monde dans la fenetre
        fenetre.blit(world,camera)

        # Rafraichir pygame
        pygame.display.update()