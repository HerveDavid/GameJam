from plateforme import *
from ennemy import *
import math
from datetime import datetime
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
        self.time = 0
        self.load()



    def load(self):

        # Background
        for y in range(len(self.fond)):

            for i in range(len(self.fond[y])):

                id = self.fond[y][i]

                if id:
                    self.background.append(Fond(i * WIDTH_CELL, y * HEIGHT_CELL, id))
                    if id == 10:
                        self.startx = int(i * WIDTH_CELL + WIDTH_CELL / 2)
                        self.starty = int(y * HEIGHT_CELL + 50)
                    elif id == 11:
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
                    elif -1:
                        self.platforms.append(Flag(i * WIDTH_CELL, y * HEIGHT_CELL))

        self.playerLose()

    def display(self, screen):


        self.background.draw(screen)

        self.platforms.draw(screen)

        self.player.falling = not self.platforms.collision(self.player)

        for e in self.enemies:
            e.draw(screen)

            if isinstance(e, Sirene):
                e.flip = self.player.x < e.x

                distance = math.hypot(abs(self.player.x - e.x), abs(self.player.y - e.y))

                if distance < e.attirance:
                    e.attire(self.player)

            if e.hitbox and self.player.hitbox:
                if e.hitbox.colliderect(self.player.hitbox):
                    self.playerLose()

        if self.player.stream.dir != 0:

            if self.time == 0:
                self.time = self.get_time()

            if abs(self.get_time() - self.time) <= 2:
                self.player.stream.draw(screen, self.player.flip)
                self.player.stream.fear(self.enemies)
            if abs(self.get_time() - self.time) > 2:
                self.player.setStream(0)
                self.player.blow = False
                self.time = 0


        if (self.player.y >= HEIGHT and self.player.falling)\
                or (self.player.x < 0 or self.player.x > WIDTH):
            self.playerLose()


        self.player.draw(screen)

        if self.player.hitbox and self.player.hitbox.colliderect(
                pygame.rect.Rect(self.endx, self.endy, WIDTH_CELL, HEIGHT_CELL)):
            return 1
        else:
            return 0

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
        channel.set_volume(0.6)
        if self.player.jumping:
            if not channel.get_busy():
                if not self.player.falling:
                    channel.play(sound_jump)
        if self.player.blow:
            if not channel.get_busy():
                    channel.set_volume(0.1)
                    channel.play(sound_flute)
        if self.player.xVelocity != 0 and self.player.falling == False and self.player.jumping == False:
            if not channel.get_busy():
                channel.set_volume(0.3)
                channel.play(sound_step)

    def playMixerAmbiant(self, channel, sound):
        channel.set_volume(0.4)
        if not channel.get_busy():
            channel.play(sound)

    def get_time(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        now = int(dt_string[len(dt_string) - 2] + dt_string[len(dt_string) - 1])
        if now == 0:
            return 1
        else:
            return now