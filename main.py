import pygame
from utilitaries import *
from colors import COLORS
# from sprite import Sprite
from player import Player
# from ennemy import Ennemy
# from bouton import Bouton

import pygame

file = 'Audio/1.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

def main(screen: pygame.display) -> None:

    player = Player(300, 300)
    # ennemy = Ennemy(300,300)
    # button = Button(300,300)
    while RUNNING:
        events()
        # ennemy.draw(screen)
        player.draw(screen)
        # button.draw(screen)

        pygame.display.update()
        screen.fill(COLORS['white'])
        
        pygame.time.Clock().tick(FPS)


if __name__ == '__main__':

    screen = init()
    main(screen)
