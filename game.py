import pygame
from utilitaries import *
from plateforme import *

import random

class Game():

    def __init__(self, map: (), fond:  (), objets: (), player, enemies):

        self.map = map
        self.fond = fond
        self.objets = objets
        self.player = player
        self.enemies = enemies
        self.platforms = Platforms()
        self.background = Platforms()
        self.startx = 0
        self.starty = 0
        self.endx = 0
        self.endy = 0
        self.score = 0

        self.load()



    def load(self):

        # Background
        for y in range(len(self.fond)):

            for i in range(len(self.fond[y])):

                id = self.fond[y][i]

                if id:
                    self.background.append(Fond(i * WIDTH_CELL, y * HEIGHT_CELL, id))
                    if id == 6:
                        self.startx = int(i * WIDTH_CELL + WIDTH_CELL / 2)
                        self.starty = int(y * HEIGHT_CELL + 50)
                    elif id == 7:
                        self.endx = int(i * WIDTH_CELL)
                        self.endy = int(y * HEIGHT_CELL)

        # Objets
        for y in range(len(self.objets)):

            for i in range(len(self.objets[y])):

                id = self.objets[y][i]

                if id:
                    self.background.append(Objet(i * WIDTH_CELL, y * HEIGHT_CELL, id))



        # Map
        for y in range(len(self.map)):

            for i in range(len(self.map[y])):

                id = self.map[y][i]

                if id:
                    if id in range(0, len(TUILES)+1):
                        self.platforms.append(Platform(i * WIDTH_CELL, y * HEIGHT_CELL, id))
                    elif 8:
                        self.platforms.append(Flag(i * WIDTH_CELL, y * HEIGHT_CELL))

        self.playerLose()

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
            self.player.stream.fear(self.enemies)

        if (self.player.y >= HEIGHT and self.player.falling)\
                or (self.player.x < 0 or self.player.x > WIDTH):
            self.playerLose()

        if self.player.hitbox and self.player.hitbox.colliderect(pygame.rect.Rect(self.endx, self.endy, WIDTH_CELL, HEIGHT_CELL)):
            print("tu as gagné")

        self.player.draw(screen)


    def playerLose(self):
        self.player.x = self.startx
        self.player.y = self.starty
        self.score = 0

    def initMixer(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("Audio/1.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)


    def playMixerEnnemy(self, channel, sounds):
        channel.set_volume(0.5)
        random_sound = random.choice(sounds)
        if not channel.get_busy():
            if random.randint(0, 30) == 10:
                channel.play(random_sound)

    def playMixerPlayer(self, channel, sound_jump, sound_flute, sound_step):
        channel.set_volume(1.7)
        if self.player.jumping:
            if not channel.get_busy():
                if not self.player.falling:
                    channel.play(sound_jump)
        if self.player.blow:
            if not channel.get_busy():
                channel.set_volume(0.3)
                channel.play(sound_flute)
        if self.player.xVelocity != 0 and self.player.falling == False and self.player.jumping == False:
            if not channel.get_busy():
                channel.set_volume(0.5)
                channel.play(sound_step)

    def playMixerAmbiant(self, channel, sound):
        channel.set_volume(0.8)
        if not channel.get_busy():
            channel.play(sound)