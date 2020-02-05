import pygame
from utilitaries import *
from colors import COLORS
from player import Player
from ennemy import *
from game import Game
from  maps import *
import pygame.freetype
from tkinter import *

pygame.font.init()
pygame.init()

white = pygame.color.Color('#ffffff')
red = pygame.color.Color('#ff0000')
black = pygame.color.Color('#000000')

font = pygame.font.Font(None, 60)
text = font.render('A Bout De Souffle', True, white)

def start_menu(screen):

    start = True
    while start:

        action = None
        pos = pygame.mouse.get_pos()
        button_width = 240
        button_height = 80
        colour = red

        screen.blit(text, (WIDTH/2 - text.get_rect().width/2, 200))

        if pos[0] >= WIDTH/2 - button_width/2 and pos[0] <= WIDTH/2 + button_width/2 and pos[1] >= HEIGHT/2 + 30 and pos[1] <= HEIGHT/2 + 30 + button_height:
            colour = white
            action = "start"

        pygame.draw.rect(screen, colour, (WIDTH / 2 - button_width / 2, HEIGHT / 2 + 30, button_width, button_height))
        pygame.display.flip()

        colour = red
        if pos[0] >= WIDTH/2 - button_width/2 and pos[0] <= WIDTH/2 + button_width/2 and pos[1] >= HEIGHT/2 + 180 and pos[1] <= HEIGHT/2 + 180 + button_height:
            colour = white
            action = "credits"

        pygame.draw.rect(screen, colour, (WIDTH / 2 - button_width / 2, HEIGHT / 2 + 180, button_width, button_height))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if action is not None:
                    return action


def main(screen: pygame.display) -> None:

    player = Player(WIDTH_CENTER, 0)

    game = Game(etage2, (), player, enemies2)
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
        screen.fill((35, 118, 211))
        
        clock.tick(FPS)

if __name__ == '__main__':

    screen = init()
    ans = start_menu(screen)
    if ans == "start":
        main(screen)
    elif ans == "credits":
        display_credits(screen)

