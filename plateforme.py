from sprite import Sprite
import pygame
import random as rd



class Platform():

    def __init__(self, x, y, type):

        if type == 1:
            self.sprite = Sprite('Assets/Textures/mur.png', 1, 1, colorkey=False)
        elif type == 2:
            self.sprite = Sprite('Assets/Textures/mur_cote.png', 1, 1, colorkey=False)
        elif type == 3:
            self.sprite = Sprite('Assets/Textures/plateforme_sable.png', 1, 1, colorkey=False)
        elif type == 4:
            self.sprite = Sprite('Assets/Textures/sol_sable.png', 1, 1, colorkey=False)
        elif type == 5:
            self.sprite = Sprite('Assets/Textures/sol_sable_cote.png', 1, 1, colorkey=False)


        self.x = x
        self.y = y
        self.width = self.x + self.sprite.cellWidth

        self.type = type

        self.hitbox = pygame.rect.Rect(self.x + self.sprite.handle[0][0],
                                       self.y + self.sprite.handle[0][1],
                                       self.sprite.cells[0][2] -10,
                                       self.sprite.cells[0][3]
                                       )


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

    def test(self, player):

        if player.x < self.x or player.x > self.width:
            return None
        elif player.y <= self.y and player.y + 20 >= self.y:
            return self
        else:
            return None

    def mur(self, player):
        # if player.xVelocity != 0:
        if self.type != 3 and player.hitbox and self.hitbox.colliderect(player.hitbox):
            # if not player.jumping:
           if not player.flip :
               player.x += -player.xVelocity
           else:
               player.x += -player.xVelocity



    def draw(self, screen):
        # if self.anime == (True, 3) and self.vectAle:
        #     self.index = (self.index+1) % len(self.vectAle)
        #     self.y += self.vectAle[self.index]

        self.sprite.draw(screen, self.x, self.y, handle=0)
        # pygame.draw.line(screen, [255, 0, 0], (self.x, self.y), (self.width, self.y), 1)
        # pygame.draw.rect(screen, [255, 0, 0], self.hitbox)

class Platforms():

    def __init__(self):

        self.containers = []

    def append(self, platform: Platform):

        self.containers.append(platform)

    def collision(self, player):

        for platform in self.containers:
            platform.mur(player)

            t = platform.test(player)


            if t:
                player.currentPlatform = t
                player.y = t.y
                return True

        return False


    def draw(self, screen):

        for platform in self.containers:
            platform.draw(screen)

