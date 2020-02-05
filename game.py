import pygame
from utilitaries import *
from plateforme import *

class Game():

    def __init__(self, map: (), player, enemies):

        self.map = map
        self.player = player
        self.enemies = enemies
        self.platforms = Platforms()
        self.load()
        self.score = 0

    def load(self):

        for y in range(len(self.map)):

            for i in range(len(self.map[y])):

                id = self.map[y][i]

                if id:

                    self.platforms.append(Platform(i * WIDTH_CELL, y * HEIGHT_CELL, id))

    def display(self, screen):

        self.platforms.draw(screen)

        self.player.falling = not self.platforms.collision(self.player)

        for e in self.enemies:

            e.draw(screen)


        self.player.draw(screen)

        if self.player.y >= HEIGHT and self.player.falling:
            self.player.y = 0
            self.player.x = WIDTH_CENTER
            self.score = 0
