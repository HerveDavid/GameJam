import pygame
from sprite import Sprite

class Stream:

    def __init__(self,x,y,dir):

        # Initialisation position et direction
        self.setStream(x, y,dir)

    def setStream(self,x,y,dir):
        self.x, self.y, self.dir= x, y,dir

