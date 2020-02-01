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

        # Indice des images pour l'animation
        self.index = 0

        # Image actual du sprite
        self.image = self.images[self.index]

        # Hitbox rectangulaire
        self.rect = self.image.get_rect()

        # Nombre de frames
        self.frames = len(self.images)

        # Temps d'une frame
        self.temps = 1 / self.frames

        # Temps actuel de la frame
        self.frameActuel = 0

    # Anime le sprite par rapport au temps
    def animeSpriteTemps(self, temps: float):

        self.frameActuel += temps

        if self.frameActuel >= self.temps:
            self.frameActuel = 0
            self.index = int((self.index + 1) % self.frames)
            self.image = self.images[self.index]

    # Anime le sprite pour le groupe d'un sprite
    def update(self, dt):
        self.animeSpriteTemps(dt)