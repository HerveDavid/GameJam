from sprite import Sprite
import pygame
import random as rd



class Platform():

    def __init__(self, x, y, type):

        self.sprite = Sprite('Assets/Textures/plateforme_sable.png', 1, 1, colorkey=False)
        self.mask = pygame.mask.from_surface(self.sprite.sheet)
        # self.sprite_mask = pygame.mask.from_surface(self.sprite)
        # if type == 1:
        #     # self.sprite = Sprite('Assets/Textures/mur.png', 1, 1, colorkey=False)
        # elif type == 2:
        #     # self.sprite = Sprite('Assets/Textures/mur_cote.png', 1, 1, colorkey=False)
        # elif type == 3:
        #     # self.sprite = Sprite('Assets/Textures/plateforme_sable.png', 1, 1, colorkey=False)
        # elif type == 4:
        #     # self.sprite = Sprite('Assets/Textures/sol_sable.png', 1, 1, colorkey=False)
        # elif type == 5:
        #     # self.sprite = Sprite('Assets/Textures/sol_sable_cote.png', 1, 1, colorkey=False)



        self.x = x
        self.y = y

        self.anime = type in [3], type
        if self.anime == (True, 3):
            self.vectAle = []

            r_nb = rd.randrange(0, 5, 1)

            if r_nb:
                for i in range(r_nb):
                    if i > r_nb / 2:
                        self.vectAle.append(i)
                    else:
                        self.vectAle.append(-i)

            self.index = 0
        self.width = self.x + self.sprite.cellWidth

    def test(self, player):

        if player.x < self.x or player.x > self.width:
            return None
        elif player.y <= self.y and player.y + player.velocity >= self.y:
            return self
        else:
            return None

    def draw(self, screen):
        # if self.anime == (True, 3) and self.vectAle:
        #     self.index = (self.index+1) % len(self.vectAle)
        #     self.y += self.vectAle[self.index]

        self.sprite.draw(screen, self.x, self.y, handle=0)
        pygame.draw.line(screen, [255, 0, 0], (self.x, self.y), (self.width, self.y), 1)

class Platforms():

    def __init__(self):

        self.containers = []

    def append(self, platform: Platform):

        self.containers.append(platform)

    def collision(self, player):

        for platform in self.containers:

            t = platform.test(player)

            if t:
                player.currentPlatform = t
                player.y = t.y
                # player.falling = False
                return True

        return False

    def draw(self, screen):

        for platform in self.containers:
            platform.draw(screen)

