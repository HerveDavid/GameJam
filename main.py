import pygame
from utilitaries import *
from colors import COLORS
from player import Player
from plateforme import *
from game import Game

# Audio
file = 'Audio/1.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

# Map


etage1 = [ 'SS' for i in range(NB_WIDTH_CELL)]
etage1 = [ etage1 for i in range(NB_HEIGTH_CELL)]


def main(screen: pygame.display) -> None:

    player = Player(300, 200)
    # p1 = Platform(0, 0, 'M')
    # p2 = Platform(420, 300, 'MC')
    # p3 = Platform(250, 400, 'M')

    # plateformes = Platforms()
    # plateformes.append(p1)
    # plateformes.append(p2)
    # plateformes.append(p3)

    g = Game(etage1, player)

    while RUNNING:
        events()

        # plateformes.draw(screen, player)

        g.display(screen)

        pygame.display.update()
        screen.fill(COLORS['white'])
        
        pygame.time.Clock().tick(FPS)


if __name__ == '__main__':

    screen = init()
    main(screen)
