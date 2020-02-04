import pygame
from sprite import Sprite

class Ennemy():

    def __init__(self,x,y):

        #liste des sprite d'animation des ennemis
        self.sprites ={
            'idle': Sprite('Assets/Minotaur/min_idle_light.png', 10, 1),
            'idleNo': Sprite('Assets/Minotaur/min_idle_NOlight.png', 10, 1),
            'walks': Sprite('Assets/Minotaur/min_walking.png', 10, 1),
        }

        #position de l'ennemi
        self.x, self.y=x, y

        #vitesse de l'ennemi
        self.velocity = 10

        # Changement de coté du sprite
        self.flip = False

        # Plateforme
        self.platform = (x, y)

    # Procédure pour le dessin de l'ennemi
    def draw(self, surface):
        self.sprites['walks'].draw(surface, self.x, self.y, self.flip)

    # l'ennemi se déplace
    def walk(self, surface, flip):

            self.flip = flip

            if flip:
                self.x -= self.velocity
            else:
                self.x += self.velocity

            self.sprites['idle'].draw(surface, self.x, self.y, self.flip)