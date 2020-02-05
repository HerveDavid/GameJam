import pygame
from utilitaries import *
from plateforme import *

import random

class Game():

    def __init__(self, map: (), fond:  {}, player, enemies):

        self.map = map
        self.fond = fond
        self.player = player
        self.enemies = enemies
        self.platforms = Platforms()
        self.background = Platforms()
        self.load()
        self.score = 0

    def load(self):

        for y in range(len(self.fond)):

            for i in range(len(self.fond[y])):

                id = self.fond[y][i]

                if id:
                    self.background.append(Fond(i * WIDTH_CELL, y * HEIGHT_CELL, id))


        for y in range(len(self.map)):

            for i in range(len(self.map[y])):

                id = self.map[y][i]

                if id:
                    if id in range(0, len(TUILES)+1):
                        self.platforms.append(Platform(i * WIDTH_CELL, y * HEIGHT_CELL, id))
                    elif 8:
                        self.platforms.append(Flag(i * WIDTH_CELL, y * HEIGHT_CELL))

    def display(self, screen):

        self.background.draw(screen)

        self.platforms.draw(screen)

        self.player.falling = not self.platforms.collision(self.player)

        for e in self.enemies:
            e.draw(screen)
            if e.hitbox and self.player.hitbox:
                if e.hitbox.colliderect(self.player.hitbox):
                    self.playerLose()

        if self.player.stream.dir != 0:
            self.player.stream.draw(screen, self.player.flip)

        self.player.draw(screen)

        if self.player.y >= HEIGHT and self.player.falling:
            self.playerLose()

    def playerLose(self):
        self.player.y = 0
        self.player.x = WIDTH_CENTER
        self.score = 0

    def initMixer(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("Audio/1.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)


    def playMixerEnnemy(self, channel, sounds):
        channel.set_volume(0.8)
        random_sound = random.choice(sounds)
        if not channel.get_busy():
            if random.randint(0, 30) == 10:
                channel.play(random_sound)

    def playMixerPlayer(self, channel, sounds, sound_flute):
        channel.set_volume(1.7)
        random_sound = random.choice(sounds)
        if self.player.jumping:
            if not channel.get_busy():
                channel.play(random_sound)
        if self.player.blow:
            if not channel.get_busy():
                channel.set_volume(0.3)
                channel.play(sound_flute)

    def playMixerAmbiant(self, channel, sound):
        channel.set_volume(0.6)
        if not channel.get_busy():
            channel.play(sound)