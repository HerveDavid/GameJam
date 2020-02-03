import pygame
from utilitaries import *
from colors import COLORS
from sprite import Sprite
from player import Player


def main(screen: pygame.display) -> None:

    player = Player(100, 100)
    while RUNNING:
        events()
        player.draw(screen)

        pygame.display.update()
        screen.fill(COLORS['white'])
        
        pygame.time.Clock().tick(FPS)


if __name__ == '__main__':

    screen = init()
    main(screen)
