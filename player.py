import pygame
from sprite import Sprite
from plateforme import Platform
from stream import Stream

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

        self.stream = Stream(self.x,self.y,0)

        self.glissement = False

    # Définition du joueur
    def setLocation(self, x, y):
        self.x, self.y = x, y
        self.xVelocity  = 0
        self.jumpCounter = 0
        self.jumping = False
        self.falling = True
        self.blow = False

    def setStream(self,dir):
        if self.flip==True:
            self.stream= Stream(self.x,self.y,dir)
        else:
            self.stream= Stream(self.x, self.y,dir)

    # Actions du joueur
    def events(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            if self.y == self.stream.y and self.stream.dir==1 :
                self.xVelocity = -self.velocity -5
                self.blow = False
                self.flip = True
            elif self.y == self.stream.y and self.stream.dir==2 :
                self.xVelocity = -self.velocity +10
                self.blow = False
                self.flip = True
            else:
                self.xVelocity = -self.velocity
                self.blow = False
                self.flip = True
        elif keys[pygame.K_d]:
            if self.y == self.stream.y and self.stream.dir==2 :
                self.xVelocity = self.velocity +5
                self.blow = False
                self.flip = False
            elif self.y == self.stream.y and self.stream.dir==1 :
                self.xVelocity = self.velocity - 10
                self.blow = False
                self.flip = False
            else:
                self.xVelocity = self.velocity
                self.blow = False
                self.flip = False
        else: self.xVelocity = 0

        if keys[pygame.K_z] and not self.jumping and not self.falling:
            self.jumping = True
            self.jumpCounter = 0
            self.blow = False

        elif keys[pygame.K_DOWN] and self.xVelocity == 0 and not self.jumping and not self.falling:
            self.setStream(0)
            self.blow= True

        elif keys[pygame.K_UP] and self.xVelocity == 0 and not self.jumping and not self.falling:
            self.setStream(3)
            self.blow = True

        elif keys[pygame.K_RIGHT] and self.xVelocity == 0 and not self.jumping and not self.falling:
            self.setStream(2)
            self.blow = True
            self.flip = False


        elif keys[pygame.K_LEFT] and self.xVelocity == 0 and not self.jumping and not self.falling:
            self.setStream(1)
            self.blow = True
            self.flip = True

    # Déplacement du joueur
    def move(self):

        if self.xVelocity == 0 and self.stream.dir in [1, 2] and self.stream.y == self.y:
           self.x += -3 if self.stream.dir == 1 else 3
        else:
            self.x += self.xVelocity

        self.glissement = False

        if self.currentPlatorm:
            if not self.currentPlatorm.test(self) :
                self.falling = True
                self.currentPlatorm = None

        if self.jumping and self.stream.dir==3 and (self.stream.x-self.x<45 and self.stream.x-self.x>-45):
            self.y += self.jumpRange[self.jumpCounter] * 7
            self.jumpCounter += 1
            if self.jumpCounter >= len(self.jumpRange) / 2:
                self.jumping = False
                self.falling = True

        elif self.jumping:
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

        if self.blow:
            self.sprites['blow'].draw(fenetre, self.x, self.y, self.flip)
        elif self.xVelocity == 0:
            self.sprites['idle'].draw(fenetre, self.x, self.y, self.flip)
        elif self.jumping or self.flip:
            self.sprites['run'].draw(fenetre, self.x, self.y, self.flip)
        else:
            self.sprites['run'].draw(fenetre, self.x, self.y, self.flip)


