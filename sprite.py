# Chargement des modules
try:
    import pygame
    from outils import *
except ImportError as err:
    print("Echec importation: {0}").format(err)

# Classe pour la création d'un sprite
class Sprite(pygame.sprite.Sprite):

    def __init__(self, images, scale=0.8):

        # Héritage avec la classe mère
        super(Sprite, self).__init__()

        # Images du sprite pour l'animation
        if isinstance(images, str):
            self.images = chargeImages(images, scale)
        elif isinstance(images, list):
            self.images = images
        else:
            self.images = None

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

        # Déplacement du sprite
        self.deplacement = pygame.math.Vector2(0, 0)


    # Anime le sprite par rapport au temps
    def animeSpriteTemps(self, temps: float):

        self.frameActuel += temps

        if self.frameActuel >= self.temps:
            self.frameActuel = 0
            self.index = int((self.index + 1) % self.frames)
            self.image = self.images[self.index]

        self.rect.move_ip(self.deplacement)

    # Anime le sprite pour le groupe d'un sprite
    def update(self, dt):
        self.animeSpriteTemps(dt)

