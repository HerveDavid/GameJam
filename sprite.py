# Chargement des modules
try:
    import pygame
    from outils import *
except ImportError as err:
    print(err)

# Classe pour la création d'un sprite
class Sprite(pygame.sprite.Sprite):

    def __init__(self, nomFichier: str):

        # Héritage avec la classe mère
        super(Sprite, self).__init__()

        # Images du sprite pour l'animation
        self.images = chargeImages(nomFichier)
        self.index = 0



        # Hitbox rectangulaire
        self.rect = self.images[0].image.get_rect()
