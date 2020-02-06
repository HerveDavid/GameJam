import copy
from utilitaries import *

class Platform():

    def __init__(self, x, y, type=1):


        self.sprite = TUILES[type]

        self.x = x
        self.y = y
        self.width = self.x + self.sprite.cellWidth

        self.type = type

        self.hitbox = pygame.rect.Rect(self.x,
                                       self.y,
                                       self.sprite.cells[0][2] -10,
                                       self.sprite.cells[0][3]
                                       )


        self.handle = 0

    def test(self, player):

        if player.x < self.x or player.x > self.width:
            return None
        elif player.y <= self.y and player.y + 20 >= self.y:
            return self
        else:
            return None

    def mur(self, player):
        # if player.xVelocity != 0:
        if self.type != 7 and player.hitbox and self.hitbox and self.hitbox.colliderect(player.hitbox):

            if player.y < self.hitbox.y:
                player = self.hitbox.y - 10

            if  player.y > self.hitbox.y + self.hitbox.height:
                player.y += 20

            if player.hitbox.x < self.hitbox.x:
                player.x += -player.hitbox.width
                player.y += -10
            elif player.x > self.hitbox.x:
                player.x = self.hitbox.x + WIDTH_CELL + 20
            #
            # if player.x < self.hitbox.x:
            #     player.x = self.hitbox.x - self.hitbox.width / 2
            # elif player.x > self.hitbox.x:
            #     player.x = self.hitbox.x + WIDTH_CELL + 20

            # if not player.flip :
            #     player.x += -player.xVelocity
            # else:
            #     player.x += -player.xVelocity

            None



    def draw(self, screen):
        # if self.anime == (True, 3) and self.vectAle:
        #     self.index = (self.index+1) % len(self.vectAle)
        #     self.y += self.vectAle[self.index]
        if self.type in (3, 8):
            self.sprite.draw(screen, self.x, self.y,flip=True, handle=0)
        else:
            self.sprite.draw(screen, self.x, self.y, handle=0)

        # pygame.draw.line(screen, [255, 0, 0], (self.x, self.y), (self.width, self.y), 1)

class Flag(Platform):

    def __init__(self, x, y):

        super(Flag, self).__init__(x, y)

        self.spriteNoWind =  copy.copy(Sprite('Assets/Textures/drapeau.png', 10, 1))
        self.sprite = copy.copy(Sprite('Assets/Textures/drapeau_vent.png', 10, 1))

        # self.hitbox = pygame.rect.Rect(self.x + self.sprite.handle[0][0],
        #                                self.y + self.sprite.handle[0][1],
        #                                self.sprite.cellWidth,
        #                                self.sprite.cellHeight
        #                                )

        self.flip = True
        self.hitbox = None
        self.wind = False

    def test(self, player):
        self.wind = player.stream.dir in [1, 2]
        self.flip = player.stream.dir == 1
        return None

    def draw(self, screen):

        if self.wind:
            self.sprite.draw(screen, self.x + 12, self.y + 8, flip=self.flip, handle=0)
        else:
            self.spriteNoWind.draw(screen, self.x + 12, self.y +8,flip=self.flip, handle=0)

class Fond(Platform):

    def __init__(self, x, y, index):

        super(Fond, self).__init__(x, y, 1)

        self.sprite = TUILES_FOND[index]

    def test(self, player):
        None

    def draw(self, screen):
        self.sprite.draw(screen, self.x, self.y, handle=0)

class Objet(Platform):

    def __init__(self, x ,y, id):

        super(Objet, self).__init__(x,y, 1)

        self.sprite = OBJETS[id]

    def test(self, player):
        None

    def mur(self, player):
        None



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

