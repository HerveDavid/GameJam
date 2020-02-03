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

        if keys[pygame.K_RIGHT]:
            self.walk(surface, False)
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

