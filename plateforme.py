import pygame
from sprite import Sprite
from player import Player

class Platform():

    def __init__(self, x, y, width):

        self.x = x
        self.y = y
        self.width = self.x + width

    def test(self, player: Player):

        if player.x < self.x or player.x > self.width: None
        if player.y <= self.y and player.y + max(player.arcJump) >= self.y: return self
        return None

class Platforms():

    def __init__(self):

        self.containers = []

    def append(self, platform: Platform):

        self.containers.append(platform)

    def collision(self, player: Player):

        if not player.falling: return False
        for platform in self.containers:

            t = platform.test(player)

            if t:
                player.currentPlatform = t
                player.y = t.y
                player.falling = False
                return True

        return False