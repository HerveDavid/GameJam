import pygame
from sprite import Sprite

class Bouton:
    def __init__(self, x, y):

        # Listes des sprites pour l'animation
        self.sprites = {
            'start': Sprite('Assets/Buttons/start.png', 1, 1),
            'credits': Sprite('Assets/Buttons/credits.png', 1, 1)
        }


        # Position du bouton
        self.x, self.y = x, y

    # Procédure pour le dessin du joueur
    def draw(self, surface):
        self.sprites['credits'].draw(surface, self.x, self.y)