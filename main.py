import pygame
from utilitaries import *
from colors import COLORS
from player import Player
from plateforme import *
from game import Game
from maps import *

# Audio
file = 'Audio/1.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

def main(screen: pygame.display) -> None:
    # bg = pygame.image.load('Assets/Textures/JoJo.png')
    player = Player(300, 200)

    g = Game(etage1, player)

    while RUNNING:
        # screen.blit(bg, (0, 0))
        events()

        # plateformes.draw(screen, player)

        g.display(screen)

        pygame.display.update()
        screen.fill(COLORS['white'])
        
        pygame.time.Clock().tick(FPS)


if __name__ == '__main__':

    screen = init()
    main(screen)
