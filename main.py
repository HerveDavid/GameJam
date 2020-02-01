from sprite import Sprite
import pygame

pygame.init()

SIZE = WIDTH, HEIGHT = 1040, 720
BACKGROUND_COLOR = pygame.Color('black')
FPS = 60

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


def main():
    player = Sprite('assert/player/idle')
    all_sprites = pygame.sprite.Group(player)  # Creates a sprite group and adds 'player' to it.

    running = True
    while running:

        dt = clock.tick(FPS) / 500  # Amount of seconds between each loop.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        all_sprites.update(dt)  # Calls the 'update' method on all sprites in the list (currently just the player).

        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()