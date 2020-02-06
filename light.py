from sprite import Sprite

class Light():

    def __init__(self, x, y):

        self.sprite = Sprite('Assets/Minotaur/cercle.png', 1, 1, colorkey=False, scale=2)

        self.x = x
        self.y = y
        self.flip = False

    def draw(self, fenetre):

      self.sprite.draw(fenetre, self.x, self.y, flip=self.flip)