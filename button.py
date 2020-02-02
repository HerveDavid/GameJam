# Chargement des modules
try:
    import pygame
    from outils import *
except ImportError as err:
    print("Echec importation: {0}").format(err)

# Classe pour un bouton
class Button():

    def __init__(self, x, y, width, height, texte):

        # Largeur et longueur
        self.size = self.width, self.height = int(width), int(height)

        # Position
        self.position = self.x, self.y = int(x), int(y)

        # Couleur
        self.color = [255, 0, 0]

        # Couleur Hover
        self.colorHover = [0, 0, 255]

        # Color Buffer
        self.colorBuffer = self.color

        # Texte
        self.texte = texte

    # Dessine
    def draw(self, fenetre):

        pygame.draw.rect(fenetre, self.color, pygame.Rect(self.x, self.y, self.width, self.height))


        myfont = pygame.font.SysFont('Comic Sans MS', int((self.width + self.height) * 0.2) )
        textsurface = myfont.render(self.texte, True, (0, 0, 0))
        fenetre.blit(textsurface, (self.x, self.y))

        return  self.hoover() and pygame.mouse.get_pressed()[0]

    def hoover(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if int(mouse_x) in [i for i in range(self.x, self.x + self.width)] \
                and int(mouse_y)in [i for i in range(self.y, self.y + self.height)]:
            self.color = self.colorHover
            return 1
        else:
            self.color = self.colorBuffer
            return 0
