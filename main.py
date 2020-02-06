import pygame
from utilitaries import *
from colors import COLORS
from player import Player
from ennemy import *
from game import Game
from  maps import *
import pygame.freetype
from  changementSalles import *
from tkinter import *

pygame.font.init()
pygame.init()

white = pygame.color.Color('#ffffff')
red = pygame.color.Color('#ff0000')
black = pygame.color.Color('#000000')

font = pygame.font.Font(None, 50)
text = font.render('A Bout De Souffle', True, white)
text_play = font.render('Jouer', True, white)
text_instructions = font.render('Commandes', True, white)
text_credits = font.render('Credits', True, white)
text_back = font.render('Retour', True, white)

bg = pygame.image.load("Assets/Background/main_bg.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
babel = pygame.image.load("Assets/Background/babel.png")
#babel = pygame.transform.scale(babel, (WIDTH/2))

marge = 40
button_width = 240
button_height = 80

# Menu principal
def start_menu(screen):

    start = True
    while start:
        screen.blit(bg, (0, 0))
        screen.blit(babel, ((0.5*WIDTH)-(0.5*babel.get_width()),(0.5*HEIGHT)-(0.5*babel.get_height())))

        action = None
        pos = pygame.mouse.get_pos()
        colour = red

        if pos[0] >= WIDTH/2 - button_width/2 and pos[0] <= WIDTH/2 + button_width/2 and pos[1] >= HEIGHT/2 + 30 and pos[1] <= HEIGHT/2 + 30 + button_height:
            colour = white
            action = "start"

        pygame.draw.rect(screen, colour, (WIDTH / 2 - button_width / 2, HEIGHT / 2 + 30, button_width, button_height))

        colour = red
        if pos[0] >= WIDTH - (button_width + marge) and pos[0] <= WIDTH - marge and pos[1] >= HEIGHT - (button_height + marge) and pos[1] <= HEIGHT - marge:
            colour = white
            action = "credits"

        pygame.draw.rect(screen, colour, (WIDTH - (button_width + marge), HEIGHT - (button_height + marge), button_width, button_height))

        colour = red
        if pos[0] >= marge and pos[0] <= marge + button_width and pos[1] >= HEIGHT - (button_height + marge) and pos[1] <= HEIGHT - marge:
            colour = white
            action = "instructions"

        pygame.draw.rect(screen, colour, (marge, HEIGHT - (button_height + marge), button_width, button_height))

        screen.blit(text, (WIDTH/2 - text.get_rect().width/2, 100))
        screen.blit(text_play, (WIDTH / 2 - text_play.get_rect().width / 2, HEIGHT/2 + 50))
        screen.blit(text_instructions, (marge + 15, HEIGHT - (marge + 60)))
        screen.blit(text_credits, (WIDTH - (marge + (button_width - 50)), HEIGHT - (marge + 60)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if action is not None:
                    return action

def display_credits(screen):

    text_credits_content = font.render('Voici les crédits :', True, white)

    while True:
        action = None
        pos = pygame.mouse.get_pos()
        screen.fill(black)

        colour = red
        if pos[0] >= WIDTH - (button_width + marge) and pos[0] <= WIDTH - marge and pos[1] >= HEIGHT - (button_height + marge) and pos[1] <= HEIGHT - marge:
            colour = white
            action = "back"

        pygame.draw.rect(screen, colour, (WIDTH - (button_width + marge), HEIGHT - (button_height + marge), button_width, button_height))

        screen.blit(text_credits_content, (marge, marge))
        screen.blit(text_back, (WIDTH - (marge + (button_width - 50)),HEIGHT - (marge + 60)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if action is not None:
                    return action


def display_instructions(screen):

    text_instructions_content = font.render('Voici les commandes :', True, white)

    while True:
        action = None
        pos = pygame.mouse.get_pos()
        screen.fill(black)

        colour = red
        if pos[0] >= WIDTH - (button_width + marge) and pos[0] <= WIDTH - marge and pos[1] >= HEIGHT - (button_height + marge) and pos[1] <= HEIGHT - marge:
            colour = white
            action = "back"

        pygame.draw.rect(screen, colour, (WIDTH - (button_width + marge), HEIGHT - (button_height + marge), button_width, button_height))

        screen.blit(text_instructions_content, (marge, marge))
        screen.blit(text_back, (WIDTH - (marge + (button_width - 50)),HEIGHT - (marge + 60)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if action is not None:
                    return action




def main(screen: pygame.display) -> None:

    #--------------------------------------------------------------------------------
    salles = {
        1: Game(map=etage1, fond=fond1, objets=(), player=Player(0, 0), enemies=enemies1),
        2: Game(map=etage2, fond=fond2, objets=(), player=Player(0, 0), enemies=enemies2),
        3: Game(map=etage3, fond=fond3, objets=(), player=Player(0, 0), enemies=enemies3),
        4: Game(map=etage4, fond=fond4, objets=(), player=Player(0, 0), enemies=enemies4)
    }
    index = 1
    game = salles[index]
    #--------------------------------------------------------------------------------
    clock = pygame.time.Clock()

    #Sound
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
    running = TRUE
    while running:
        events()
        #------------------------------------------
        if game.display(screen):
            index += 1
            if index > len(salles):
                print("fin du jeu")
            else:
              game = salles[index]

        #------------------------------------------
        game.playMixerEnnemy(channels[1], sounds_minotaur)
        game.playMixerPlayer(channels[0], sound_player_jump, sound_flute, sound_step)
        game.playMixerAmbiant(channels[2], sound_blow)
        pygame.display.update()
        screen.fill((35, 118, 211))
        
        clock.tick(FPS)

if __name__ == '__main__':

    screen = init()
    menu = True

    while True:
        if menu:
            ans = start_menu(screen)
            if ans == "start":
                menu = False
                main(screen)
            elif ans == "credits":
                menu = False
                ans2 = display_credits(screen)
                if ans2 == "back":
                    menu = True
            elif ans == "instructions":
                menu = False
                ans3 = display_instructions(screen)
                if ans3 == "back":
                    menu = True

