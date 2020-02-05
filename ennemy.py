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

        # Hitbox
        self.hitbox = None

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

    def __init__(self, x, y, start, end):

        super(Minotaur, self).__init__(x, y)

        # liste des sprite d'animation des ennemis
        self.sprites = {
            'idle': Sprite('Assets/Minotaur/min_idle_light.png', 10, 1, 2),
            'idleNo': Sprite('Assets/Minotaur/min_idle_NOlight.png', 10, 1, 2),
            'walks': Sprite('Assets/Minotaur/min_walking.png', 10, 1, 2),
        }

        self.start = start
        self.end = end


    def events(self):
        if self.x < self.start or self.x > self.end:
            self.velocity = -self.velocity
            self.flip = self.velocity < 0

    def move(self):
        self.x += self.velocity

    def draw(self, fenetre):
        self.events()
        self.move()

        self.hitbox = pygame.rect.Rect(self.x + self.sprites['idle'].handle[7][0],
                                       self.y + self.sprites['idle'].handle[7][1],
                                       self.sprites['idle'].cells[0][2] - 20,
                                       self.sprites['idle'].cells[0][3]
                                       )
        pygame.draw.rect(fenetre, [255, 0, 255], self.hitbox)

        if self.velocity == 0:
            self.sprites['idle'].draw(fenetre, self.x, self.y, self.flip)
        else:
            self.sprites['walks'].draw(fenetre, self.x, self.y, self.flip)


