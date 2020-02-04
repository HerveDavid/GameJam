import pygame
from sprite import Sprite

class Player():

    def __init__(self, x, y):

        # Listes des sprites pour l'animation
        self.sprites = {
            'run': Sprite('Assets/Player/run.png', 8, 1),
            'jump': Sprite('Assets/Player/run.png', 8, 1),
            'idle': Sprite('Assets/Player/idle.png', 8, 1)
        }

        # Initialisation position
        self.setLocation(x, y)

        # Vitesse du joueur
        self.velocity = 20
        self.jumpRange = [-10, -6, -5, -4,  1, 4, 5, 6, 10]

        # Flip
        self.flip = False

    # Définir la position du joueur
    def setLocation(self, x, y):
        self.x, self.y = x, y
        self.xVelocity  = 20
        self.jumpCounter = 0
        self.jumping = False
        self.falling = False

    # Actions du joueur
    def events(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.xVelocity = -self.velocity
            self.flip = True
        elif keys[pygame.K_RIGHT]:
            self.xVelocity = self.velocity
            self.flip = False
        else: self.xVelocity = 0

        if keys[pygame.K_SPACE] and not self.jumping and not self.falling:
            self.jumping = True
            self.jumpCounter = 0

    # Déplacement du joueur
    def move(self):
        self.x += self.xVelocity

        if self.jumping:
            self.y += self.jumpRange[self.jumpCounter]
            self.jumpCounter += 1
            if self.jumpCounter >= len(self.jumpRange) - 1:
                self.jumping = False
                self.falling = True
        elif self.falling:
            if self.y < 300:
                self.y = 300
                self.falling = False
            else:
                self.y += self.velocity

    def draw(self, fenetre):
        self.events()
        self.move()

        if self.xVelocity == 0:
            self.sprites['idle'].draw(fenetre, self.x, self.y, self.flip)
        elif self.jumping or self.flip:
            self.sprites['jump'].draw(fenetre, self.x, self.y, self.flip)
        else:
            self.sprites['run'].draw(fenetre, self.x, self.y, self.flip)

