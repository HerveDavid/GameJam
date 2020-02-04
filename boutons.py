import pygame
from sprite import Sprite

class Bouton():

    def __init__(self, x, y):

        # Listes des sprites pour les boutons
        self.sprites = {
            'start': Sprite('Assets/Boutons/start.png', 1, 1),
            'credits': Sprite('Assets/Boutons/credits.png', 1, 1)
        }

        # Position du player
        self.x, self.y = x, y

    def draw(self, surface):
        self.sprites['credits'].draw(surface, self.x, self.y)