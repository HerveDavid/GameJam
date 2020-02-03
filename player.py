import pygame
from sprite import Sprite

class Player():


    def __init__(self, x, y):

        self.sprite = Sprite('Assets/main_character_sprites.png', 8, 1, 5)
        self.x, self.y = x, y
        self.velocity = 10

    def draw(self, surface):
        if self.move() == pygame.K_RIGHT:
            self.sprite.draw(surface, self.x, self.y)
        elif self.move() == pygame.K_LEFT:
            self.sprite.draw(surface, self.x, self.y, True)
        else:
            self.sprite.draw(surface, self.x, self.y)


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
            return pygame.K_RIGHT

        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
            return pygame.K_LEFT

        return None
