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
                    if id in range(0, len(TUILES)+1):
                        self.platforms.append(Platform(i * WIDTH_CELL, y * HEIGHT_CELL, id))
                    elif 8:
                        self.platforms.append(Flag(i * WIDTH_CELL, y * HEIGHT_CELL))

    def display(self, screen):

        self.platforms.draw(screen)

        self.player.falling = not self.platforms.collision(self.player)

        for e in self.enemies:
            e.draw(screen)
            if e.hitbox and self.player.hitbox:
                if e.hitbox.colliderect(self.player.hitbox):
                    self.playerLose()


        self.player.draw(screen)

        if self.player.y >= HEIGHT and self.player.falling:
            self.playerLose()

    def playerLose(self):
        self.player.y = 9*HEIGHT_CELL
        self.player.x = 10
        self.score = 0
