import pygame
from sprite import Sprite

class Platform():

    def __init__(self, x, y, width):

        self.x = x
        self.y = y
        self.width = self.x + width

    def test(self, player):

        if player.x < self.x or player.x > self.width: return None
        if player.y <= self.y and player.y + player.velocity >= self.y: return self
        return None

    def draw(self, screen):

        pygame.draw.line(screen, [255, 0, 0], (self.x, self.y), (self.width, self.y), 2)

class Platforms():

    def __init__(self):

        self.containers = []

    def append(self, platform: Platform):

        self.containers.append(platform)

    def collision(self, player):

        if not player.falling: return False

        for platform in self.containers:

            t = platform.test(player)

            if t:
                player.currentPlatform = t
                player.y = t.y
                player.falling = False
                return True

        return False

    def draw(self, screen, player):
        # self.collision(player)
        for platform in self.containers:
            platform.draw(screen)

        print(self.collision(player))


        player.draw(screen)