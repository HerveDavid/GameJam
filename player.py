import pygame
from sprite import Sprite

class Player():

    def __init__(self, x, y):

        self.sprites = {
            'run': Sprite('Assets/Player/run.png', 8, 1, 5)
        }

        self.x, self.y = x, y
        self.velocity = 20
        self.flip = False

    def draw(self, surface):

        keys = pygame.key.get_pressed()

        # Joeur fait un jump à gauche ou droite
        if keys[pygame.K_SPACE] and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            self.jump(surface, keys[pygame.K_LEFT])

        # Joueur va à droite
        elif keys[pygame.K_RIGHT]:
            self.walk(surface, False)

        # Joueur va à gauche
        elif keys[pygame.K_LEFT]:
            self.walk(surface, True)

        else:
            self.sprites['run'].draw(surface, self.x, self.y, self.flip)

    def walk(self, surface, flip):

        self.flip = flip

        if flip:
            self.x -= self.velocity
        else:
            self.x += self.velocity

        self.sprites['run'].draw(surface, self.x, self.y, self.flip)

    def jump(self, surface, flip):

        self.flip = flip

        if flip:
            self.x -= self.velocity
            self.y -= 100
        else:
            self.x += self.velocity
            self.y -= 100

        self.sprites['run'].draw(surface, self.x, self.y, self.flip)