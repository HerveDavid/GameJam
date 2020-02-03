import pygame
from sprite import Sprite

class Player():

    def __init__(self, x, y):

        self.sprite = Sprite('Assets/RobocopWalk.png', 8, 1, 5)
        self.x, self.y = x, y

    def draw(self, surface):
        if self.move() == 1:
            self.sprite.draw(surface, self.x, self.y)
        elif self.move() == 2:
            self.sprite.draw(surface, self.x, self.y, True)
        else:
            self.sprite.draw(surface, self.x, self.y)


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += 10
            return 1

        if keys[pygame.K_LEFT]:
            self.x -= 10
            return 2

        return 0
