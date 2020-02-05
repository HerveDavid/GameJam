import pygame
from sprite import Sprite
from plateforme import Platform

class Player():

    def __init__(self, x, y):

        # Listes des sprites pour l'animation
        self.sprites = {
            'run': Sprite('Assets/Player/run.png', 8, 1),
            'blow': Sprite('Assets/Player/joueur_souffle.png', 20, 1),
            'idle': Sprite('Assets/Player/idle.png', 4, 1)
        }

        # Initialisation position
        self.setLocation(x, y)

        # Vitesse du joueur
        self.velocity = 20
        self.jumpRange = [-10, -6, -5, -4,  1, 4, 5, 6, 10]

        # Flip
        self.flip = False

        # Current plateforme
        self.currentPlatorm = None

        self.hitbox = None

    # Définir la position du joueur
    def setLocation(self, x, y):
        self.x, self.y = x, y
        self.xVelocity  = 0
        self.jumpCounter = 0
        self.jumping = False
        self.falling = True
        self.blow = False

    # Actions du joueur
    def events(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.xVelocity = -self.velocity
            self.blow = False
            self.flip = True
        elif keys[pygame.K_RIGHT]:
            self.xVelocity = self.velocity
            self.blow = False
            self.flip = False
        else: self.xVelocity = 0

        if keys[pygame.K_SPACE] and not self.jumping and not self.falling:
            self.jumping = True
            self.jumpCounter = 0
        elif keys[pygame.K_UP] and self.xVelocity == 0 and not self.jumping and not self.falling:
            self.blow = True

    # Déplacement du joueur
    def move(self):

        self.x += self.xVelocity

        if self.currentPlatorm:
            if not self.currentPlatorm.test(self) :
                self.falling = True
                self.currentPlatorm = None

        if self.jumping:
            self.y += self.jumpRange[self.jumpCounter] * 5
            self.jumpCounter += 1
            if self.jumpCounter >= len(self.jumpRange) /2:
                self.jumping = False
                self.falling = True
        elif self.falling and not self.currentPlatorm:
            self.y += 20

    def draw(self, fenetre):
        self.events()
        self.move()

        self.hitbox = pygame.rect.Rect(self.x + self.sprites['run'].handle[1][0],
                                       self.y + self.sprites['run'].handle[8][1] -5,
                                       self.sprites['run'].cells[0][2],
                                       self.sprites['run'].cells[0][3] + 5
                                       )
        pygame.draw.rect(fenetre, [0, 255, 0], self.hitbox)

        if self.blow:
            self.sprites['blow'].draw(fenetre, self.x, self.y, self.flip)
        elif self.xVelocity == 0:
            self.sprites['idle'].draw(fenetre, self.x, self.y, self.flip)
        elif self.jumping or self.flip:
            self.sprites['run'].draw(fenetre, self.x, self.y, self.flip)
        else:
            self.sprites['run'].draw(fenetre, self.x, self.y, self.flip)

