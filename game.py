import pygame
from utilitaries import *
from plateforme import *

class Game():

    def __init__(self, map: (), player):

        self.map = map
        self.player = player
        self.platforms = Platforms()
        self.load()

    def load(self):

        for y in range(len(self.map)):

            for i in range(len(self.map[y])):

                id = self.map[y][i]

                if id:

                    self.platforms.append(Platform(i * WIDTH_CELL, y * HEIGHT_CELL, id))


    def display(self, screen):

        self.platforms.draw(screen)
        self.player.falling = not self.platforms.collision(self.player)

        self.player.draw(screen)

        if self.player.y >= HEIGHT and self.player.falling:
            self.player.y = 300
