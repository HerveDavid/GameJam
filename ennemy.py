from sprite import Sprite
from player import Player
from utilitaries import *
from light import Light

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
        self.sprites['idle'].draw(surface, self.x, self.y, self.flip)


class   Minotaur(Ennemy):

    def __init__(self, x, y, start, end):

        super(Minotaur, self).__init__(x, y)

        # liste des sprite d'animation des ennemis
        self.sprites = {
            'idle': Sprite('Assets/Minotaur/min_idle_light.png', 10, 1, 2),
            'idleNo': Sprite('Assets/Minotaur/min_idle_NOlight.png', 10, 1, 2),
            'walks': Sprite('Assets/Minotaur/min_walking.png', 10, 1, 2),
        }

        self.light = Light(self.x, self.y)

        self.start = start
        self.end = end
        self.peur = False


    def events(self):
        if self.x < self.start or self.x > self.end:
            self.velocity = -self.velocity
            self.flip = self.velocity < 0

    def move(self):
        self.x += self.velocity
        self.light.x += self.velocity

    def attack(self):

        self.peur = True


    def draw(self, fenetre):
        s = ''
        if not self.peur:

            self.events()
            self.move()

            self.hitbox = pygame.rect.Rect(self.x + self.sprites[s].handle[7][0] - 20,
                                           self.y + self.sprites[s].handle[7][1],
                                           self.sprites[s].cells[0][2] + 30,
                                           self.sprites[s].cells[0][3]
                                           )

            self.light.draw(fenetre)

            if self.velocity == 0:
                self.sprites['idle'].draw(fenetre, self.x, self.y, self.flip)
                s = 'idle'
            else:
                self.sprites['walks'].draw(fenetre, self.x, self.y, self.flip)
                s = 'walks'



        else:
            self.hitbox = None
            self.sprites['idleNo'].draw(fenetre, self.x, self.y, self.flip)
            s = 'idleNo'
            self.peur = False



        # pygame.draw.rect(fenetre,[255, 0, 0], self.hitbox)


class Sirene(Ennemy):

    def __init__(self, x, y):

        super(Sirene, self).__init__(x, y, 0)

        self.sprites = {
            'idle': Sprite('Assets/Siren/sirene.png', 4, 1)
        }

        self.attirance = 250

    def attire(self, player):

        if player.x < self.x:
            player.x += 5
        else:
            player.x += -5