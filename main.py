import pygame
from utilitaries import *
from colors import COLORS
from player import Player
from plateforme import *



def main(screen: pygame.display) -> None:

    player = Player(300, 200)
    p1 = Platform(300, 300, 100)
    p2 = Platform(420, 300, 100)
    p3 = Platform(250, 400, 100)

    plateformes = Platforms()
    plateformes.append(p1)
    plateformes.append(p2)
    plateformes.append(p3)

    while RUNNING:
        events()

        plateformes.draw(screen, player)
        # player.draw(screen)

        pygame.display.update()
        screen.fill(COLORS['white'])
        
        pygame.time.Clock().tick(FPS)


if __name__ == '__main__':

    screen = init()
    main(screen)
