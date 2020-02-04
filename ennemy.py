from sprite import Sprite
from player import Player
from utilitaries import *

class Ennemy():

    def __init__(self,x,y, velocity=5):

        #liste des sprite d'animation des ennemis
        self.sprites ={}

        #position de l'ennemi
        self.x, self.y=x, y

        #vitesse de l'ennemi
        self.velocity = velocity

        # Changement de coté du sprite
        self.flip =  self.velocity < 0

        # Plateforme
        self.platform = (x, y)

    def events(self):
        None

    # l'ennemi se déplace
    def move(self):
        None

    # Procédure pour le dessin de l'ennemi
    def draw(self, surface):
        self.events()
        self.move()
        self.sprites['walks'].draw(surface, self.x, self.y, self.flip)

    # l'ennemi se déplace


class Minotaur(Ennemy):

    def __init__(self, x, y, parcours):

        super(Minotaur, self).__init__(x, y)

        # liste des sprite d'animation des ennemis
        self.sprites = {
            'idle': Sprite('Assets/Minotaur/min_idle_light.png', 10, 1, 2),
            'idleNo': Sprite('Assets/Minotaur/min_idle_NOlight.png', 10, 1, 2),
            'walks': Sprite('Assets/Minotaur/min_walking.png', 10, 1, 2),
        }

        self.parcours = parcours

    def events(self):
        if self.x < self.parcours[0] or self.x > self.parcours[1]:
            self.velocity = -self.velocity
            self.flip = self.velocity < 0

    def move(self):
        self.x += self.velocity

    def draw(self, fenetre):
        # self.events()
        self.move()

        if self.velocity == 0:
            self.sprites['idle'].draw(fenetre, self.x, self.y, self.flip)
        else:
            self.sprites['walks'].draw(fenetre, self.x, self.y, self.flip)
