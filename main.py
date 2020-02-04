import pygame
from utilitaries import *
from colors import COLORS
from player import Player
from ennemy import Ennemy
from game import Game
from  maps import *

def main(screen: pygame.display) -> None:

    player = Player(300, 300)
    game = Game(etage1, player)
    while RUNNING:
        events()
        # ennemy.draw(screen)
        # player.draw(screen)
        game.display(screen)
        pygame.display.update()
        screen.fill(COLORS['white'])
        
        pygame.time.Clock().tick(FPS)


if __name__ == '__main__':

    screen = init()
    main(screen)
