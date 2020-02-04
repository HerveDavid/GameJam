import pygame
from sprite import Sprite

class Player():

    def __init__(self, x, y):

        # Listes des sprites pour l'animation
        self.sprites = {
            'run': Sprite('Assets/Player/run.png', 8, 1)
        }

        # Position du player
        self.x, self.y = x, y

        # Vistesse du joueur
        self.velocity = 20

        # Changement de coté du sprite
        self.flip = False

        # Saut
        self.jumping = False

        # courbe du saut
        self.arcJump = [-10, -6, -5, -4,  1, 4, 5, 6, 10]
        # self.arcJump = [i for i in self.arcJump]
        self.arcJumpIndex = 0

        # Plateforme
        self.platform = (x, y)

    # Procédure pour le dessin du joueur
    def draw(self, surface):
        if self.jumping:
            self.jump(surface)
        else:
            keys = pygame.key.get_pressed()

            # Joeur fait un jump à gauche ou droite
            if keys[pygame.K_SPACE]:
                self.flip = keys[pygame.K_LEFT]
                self.jumping = True

            # Joueur va à droite ou droite en marchant
            elif keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                self.walk(surface, keys[pygame.K_LEFT])

            else:
                self.sprites['run'].draw(surface, self.x, self.y, self.flip)

    # Le joueur marche
    def walk(self, surface, flip):

        self.flip = flip

        if flip:
            self.x -= self.velocity
        else:
            self.x += self.velocity

        self.sprites['run'].draw(surface, self.x, self.y, self.flip)

    # Le joeur saute
    def jump(self, surface):

        self.y += self.arcJump[self.arcJumpIndex]
        self.arcJumpIndex += 1

        self.x = self.x - self.velocity if self.flip else self.x + self.velocity

        if self.arcJumpIndex >= len(self.arcJump) - 1:
            self.arcJumpIndex = len(self.arcJump) - 1

        if self.y > self.platform[1]:
            self.y = self.platform[1]
            self.jumping = False
            self.arcJumpIndex = 0

        self.sprites['run'].draw(surface, self.x, self.y, self.flip)

