import pygame
from utilitaries import *
from colors import COLORS
from player import Player

# Procedure pour le lancer le jeu
def game(screen: pygame.display) -> None:

    player = Player(300, 100)

    while RUNNING:
        events()

        player.draw(screen)

        pygame.display.update()
        screen.fill(COLORS['white'])

        pygame.time.Clock().tick(FPS)


if __name__ == '__main__':
    screen = init()
    game(screen)
