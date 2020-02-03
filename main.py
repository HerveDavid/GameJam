import pygame
from utilitaries import *
from colors import COLORS
from sprite import Sprite


def main(screen: pygame.display) -> None:

    p = Sprite('Assets/RobocopWalk.png', 8, 1, 5)
    x, y = 0, 0
    while RUNNING:
        events()
        p.draw(screen, WIDTH_CENTER, HEIGHT_CENTER, 4)


        pygame.display.update()
        screen.fill(COLORS['white'])
        
        pygame.time.Clock().tick(FPS)


if __name__ == '__main__':

    screen = init()
    main(screen)
