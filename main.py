import pygame
from utilitaries import *
from colors import COLORS
from player import Player
from ennemy import *
from game import Game
from  maps import *

# Audio
file = 'Audio/1.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

def main(screen: pygame.display) -> None:

    player = Player(WIDTH_CENTER, 0)

    minotaur = Minotaur(0, (NB_HEIGTH_CELL -2)*HEIGHT_CELL, 0, 5 * WIDTH_CELL)
    minotaur2 = Minotaur(7 * WIDTH_CELL, (NB_HEIGTH_CELL -1)*HEIGHT_CELL, 7 * WIDTH_CELL, 7 * WIDTH_CELL + 3 * WIDTH_CELL)

    enemies = []
    enemies.append(minotaur)
    enemies.append(minotaur2)

    game = Game(etage1, player, enemies)
    clock = pygame.time.Clock()
    while RUNNING:
        events()

        game.display(screen)


        pygame.display.update()
        screen.fill(COLORS['black'])
        
        clock.tick(FPS)




if __name__ == '__main__':

    screen = init()
    main(screen)

