import pygame
from sprite import Sprite

class Platform():

    def __init__(self, x, y, width):

        self.sprite = Sprite('Assets/Textures/plateforme_sable.png', 1, 1,colorkey=False)

        self.x = x
        self.y = y
        self.width = self.x + width

    def test(self, player):

        if player.x < self.x or player.x > self.width:
            return None
        elif player.y <= self.y and player.y + player.velocity >= self.y:
            return self
        else:
            return None

    def draw(self, screen):
        self.sprite.draw(screen, self.x, self.y, handle=1)
        pygame.draw.line(screen, [255, 0, 0], (self.x, self.y), (self.width, self.y), 2)

class Platforms():

    def __init__(self):

        self.containers = []

    def append(self, platform: Platform):

        self.containers.append(platform)

    def collision(self, player):

        # if player.falling:

        for platform in self.containers:

            t = platform.test(player)

            if t:
                player.currentPlatform = t
                player.y = t.y
                # player.falling = False
                return True

        return False

    def draw(self, screen, player):

        for platform in self.containers:
            platform.draw(screen)

        player.falling = not self.collision(player)


        player.draw(screen)