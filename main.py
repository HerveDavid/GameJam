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
    world = pygame.Surface((1000,1000)) # Create Map Surface
    world.fill([255, 0, 0])
    player = Player("test", world)
    running = True
    camera_pos = (192,192) # Create Camara Starting Position
    while running:

        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            player.bouger(event)

        camera_pos = player.move(camera_pos)

        fenetre.fill([255, 255, 255])
        world.fill([255, 0, 0])

        player.update(dt, world)

        fenetre.blit(world,camera_pos)
        pygame.display.update()


if __name__ == '__main__':
    main()
