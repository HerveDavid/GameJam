try:
    # Mes modules
    from sprite import Sprite
    from player import Player
    from outils import *

    # Pygame
    import pygame
    from pygame.locals import *
    succes, echecs = pygame.init()
    print("{0} successes and {1} failures".format(succes, echecs))

except ImportError as err:
    print("Echec importation: {0}").format(err)

BACKGROUND_COLOR = pygame.Color('black')
FPS = 60

fenetre = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


def main():
    player = Player("test", fenetre)
    # player.add(Sprite('assert/player/dead'))
    running = True
    while running:

        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            player.bouger(event)

        player.update(dt)

        pygame.display.update()


if __name__ == '__main__':
    main()
