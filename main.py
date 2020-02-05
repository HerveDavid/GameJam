import pygame
from utilitaries import *
from colors import COLORS
from player import Player
from ennemy import *
from game import Game
from  maps import *

def main(screen: pygame.display) -> None:

    player = Player(WIDTH_CENTER, 0)

    minotaur = Minotaur(0, (NB_HEIGTH_CELL -2)*HEIGHT_CELL, 0, 5 * WIDTH_CELL)
    minotaur2 = Minotaur(7 * WIDTH_CELL, (NB_HEIGTH_CELL -1)*HEIGHT_CELL, 7 * WIDTH_CELL, 7 * WIDTH_CELL + 3 * WIDTH_CELL)

    enemies = []
    # enemies.append(minotaur)
    # enemies.append(minotaur2)

    game = Game(etage1, fond1, player, enemies)
    clock = pygame.time.Clock()
    game.initMixer()

    sound_channel_player = pygame.mixer.Channel(0)
    sound_channel_ennemy = pygame.mixer.Channel(1)
    sound_channel_ambient = pygame.mixer.Channel(2)

    channels = []
    channels.append(sound_channel_player)
    channels.append(sound_channel_ennemy)
    channels.append(sound_channel_ambient)

    sound_player_jump = pygame.mixer.Sound("Audio/Fx/jump1.ogg")

    sound_flute = pygame.mixer.Sound("Audio/Fx/flute.ogg")
    sound_step = pygame.mixer.Sound("Audio/Fx/step.ogg")

    sound_minotaur1 = pygame.mixer.Sound("Audio/Fx/minotaur1.wav")
    sound_minotaur2 = pygame.mixer.Sound("Audio/Fx/minotaur2.wav")

    sounds_minotaur = []
    sounds_minotaur.append(sound_minotaur1)
    sounds_minotaur.append(sound_minotaur2)

    sound_blow = pygame.mixer.Sound("Audio/Fx/blow.wav")

    sounds_ambient = []
    sounds_ambient.append(sound_blow)

    while RUNNING:
        events()

        game.display(screen)
        game.playMixerEnnemy(channels[1], sounds_minotaur)
        game.playMixerPlayer(channels[0], sound_player_jump, sound_flute, sound_step)
        game.playMixerAmbiant(channels[2], sound_blow)
        pygame.display.update()
        screen.fill(COLORS['black'])
        
        clock.tick(FPS)

if __name__ == '__main__':

    screen = init()
    main(screen)

