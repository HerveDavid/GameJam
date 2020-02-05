from utilitaries import *
from sprite import Sprite

class Wind():

    def __init__(self):

        self.stream_horizontal = Sprite('Assets/Textures/vent_horizontal.png', 10, 1)
        self.stream_vertical = Sprite('Assets/Textures/vent.png', 10, 1)


class Stream:

    def __init__(self,x,y,dir):

        # Initialisation position et direction
        self.setStream(x, y,dir)

        # Sprite du vent
        self.windSprite = Wind()

    def setStream(self,x,y,dir):
        self.x, self.y, self.dir= x, y,dir

    def fear(self, enemies: ()):

        for e in enemies:

            if self.dir in [1, 2]:
                if self.y == e.y:
                    e.peur = True
            elif self.dir == 3:
                if self.x == e.x:
                    e.peur = True




    def draw(self, screen, flip):
        if self.dir == 3:
            for y in range(int(NB_HEIGTH_CELL) + 1):
                self.windSprite.stream_vertical.draw(screen, self.x, y * HEIGHT_CELL, flip=flip)
        else:
            for i in range(int(NB_WIDTH_CELL) + 1):
                self.windSprite.stream_horizontal.draw(screen, i * WIDTH_CELL, self.y, flip=flip)