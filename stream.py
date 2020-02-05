from utilitaries import *
from sprite import Sprite


class Stream:

    def __init__(self,x,y,dir):

        # Initialisation position et direction
        self.setStream(x, y,dir)

        # Sprite du vent
        self.windSprite = Sprite('Assets/Wind/vent.png', 10, 1)

    def setStream(self,x,y,dir):
        self.x, self.y, self.dir= x, y,dir

    def draw(self, screen, flip):
        if self.dir == 3:
            for y in range(int(NB_HEIGTH_CELL) + 1):
                self.windSprite.draw(screen, self.x, y * HEIGHT_CELL, flip=flip)
        else:
            for i in range(int(NB_WIDTH_CELL) + 1):
                self.windSprite.draw(screen, i * WIDTH_CELL, self.y, flip=flip)