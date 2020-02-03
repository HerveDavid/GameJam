import pygame
from sprite import Sprite

class Player():

    def __init__(self, sprite: Sprite, x, y):

        self.sprite = sprite
        self.x, self.y = x, y

    def draw(self, surface):
        if self.move():
            self.sprite.draw(surface, self.x, self.y)
        else:
            self.sprite.draw(surface, self.x, self.y)


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += 10
            return 1

        if keys[pygame.K_LEFT]:
            self.x -= 10
            return 1

        return 0
